# Black outline border + cut line for each pick, then an ohprint-style PDF (print image + magenta cut path).
import sys, zlib, io
from PIL import Image, ImageFilter, ImageDraw, ImageChops
import numpy as np, potrace
DPI = 600; PX = 25.4 / DPI; BORDER_MM = 2.4; MARGIN = 2.0
DARK = (42, 36, 24)
names = [l.split('\t') for l in open('picks_names.txt').read().strip().split('\n')]
for key, label in names:
    art = Image.open(f'pick_{key}.png').convert('RGBA')
    a = art.split()[3].point(lambda v: 255 if v > 60 else 0)
    r = BORDER_MM / PX
    m = a.filter(ImageFilter.GaussianBlur(r / 2)).point(lambda v: 255 if v > 6 else 0)        # dilate ~ r
    ImageDraw.floodfill(m, (0, 0), 128)                                                       # fill holes
    m = m.point(lambda v: 0 if v == 128 else 255)
    m = m.filter(ImageFilter.GaussianBlur(10)).point(lambda v: 255 if v > 128 else 0)         # smooth the cut shape
    x0, y0, x1, y1 = m.getbbox(); pad = round(MARGIN / PX)
    box = (x0 - pad, y0 - pad, x1 + pad, y1 + pad)
    m, art = m.crop(box), art.crop(box)
    out = Image.new('RGBA', m.size, (0, 0, 0, 0)); out.paste(Image.new('RGBA', m.size, DARK + (255,)), (0, 0), m)
    out.alpha_composite(art)
    out.save(f'pickout_{key}.png', dpi=(DPI, DPI))
    # cut line
    path = potrace.Bitmap(np.array(m) < 128).trace(turdsize=50, alphamax=1.0, opticurve=True, opttolerance=0.2)
    W, H = m.width * PX, m.height * PX
    mm = 72 / 25.4
    def pt(p): return f'{p.x*PX*mm:.3f} {(H - p.y*PX)*mm:.3f}'
    ops = []
    for c in path:
        ops.append(pt(c.start_point) + ' m')
        for sg in c.segments:
            ops.append(f'{pt(sg.c)} l {pt(sg.end_point)} l' if sg.is_corner else f'{pt(sg.c1)} {pt(sg.c2)} {pt(sg.end_point)} c')
        ops.append('h')
    cut = ' '.join(ops)
    rgb = out.convert('RGB'); alpha = out.split()[3]
    content = (f'q {W*mm:.3f} 0 0 {H*mm:.3f} 0 0 cm /Im1 Do Q\n'
               f'/OC /ocC BDC 1 0 1 RG 0.142 w {cut} S EMC\n').encode()
    content = f'/OC /ocP BDC\n'.encode() + content.replace(b'/OC /ocC', b'EMC\n/OC /ocC', 1)
    cs, rs, as_ = zlib.compress(content), zlib.compress(rgb.tobytes()), zlib.compress(alpha.tobytes())
    objs = [
        b'<< /Type /Catalog /Pages 2 0 R /OCProperties << /OCGs [8 0 R 9 0 R] /D << /Order [8 0 R 9 0 R] /ON [8 0 R 9 0 R] >> >> >>',
        b'<< /Type /Pages /Kids [3 0 R] /Count 1 >>',
        f'<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {W*mm:.3f} {H*mm:.3f}] /TrimBox [0 0 {W*mm:.3f} {H*mm:.3f}] /Contents 4 0 R /Resources << /XObject << /Im1 6 0 R >> /Properties << /ocP 8 0 R /ocC 9 0 R >> >> >>'.encode(),
        (f'<< /Length {len(cs)} /Filter /FlateDecode >>', cs),
        f'<< /Title (SmithsFarm pick - {key} {W:.1f}x{H:.1f}mm) >>'.encode(),
        (f'<< /Type /XObject /Subtype /Image /Width {rgb.width} /Height {rgb.height} /ColorSpace /DeviceRGB /BitsPerComponent 8 /SMask 7 0 R /Length {len(rs)} /Filter /FlateDecode >>', rs),
        (f'<< /Type /XObject /Subtype /Image /Width {rgb.width} /Height {rgb.height} /ColorSpace /DeviceGray /BitsPerComponent 8 /Length {len(as_)} /Filter /FlateDecode >>', as_),
        b'<< /Type /OCG /Name (print) >>',
        b'<< /Type /OCG /Name (cutline) >>',
    ]
    buf = bytearray(b'%PDF-1.6\n%\xe2\xe3\xcf\xd3\n'); offs = []
    for i, o in enumerate(objs, 1):
        offs.append(len(buf))
        if isinstance(o, tuple): buf += f'{i} 0 obj\n{o[0]}\nstream\n'.encode() + o[1] + b'\nendstream\nendobj\n'
        else: buf += f'{i} 0 obj\n'.encode() + o + b'\nendobj\n'
    x = len(buf)
    buf += f'xref\n0 {len(objs)+1}\n0000000000 65535 f \n'.encode() + ''.join(f'{o:010d} 00000 n \n' for o in offs).encode()
    buf += f'trailer\n<< /Size {len(objs)+1} /Root 1 0 R /Info 5 0 R >>\nstartxref\n{x}\n%%EOF\n'.encode()
    open(f'pick_{key}.pdf', 'wb').write(buf)
    print(key, label, f'{W:.1f} x {H:.1f} mm', len(path), 'curves')
