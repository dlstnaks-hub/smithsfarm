# Vector back of the name card for Illustrator: cream background and divider as shapes, text and icons as traced
# outline paths (ink.json), the three keyring characters as one embedded image with a soft mask.
import json, sys, zlib
from PIL import Image, ImageChops
mm = 72 / 25.4; W, H = 94*mm, 54*mm
def pt(x, y): return f'{x*mm:.3f} {(54-y)*mm:.3f}'
px = 90 / 1020                        # back_clean.png pixel -> mm
BG = (243, 239, 228)
ops = [f'{BG[0]/255:.4f} {BG[1]/255:.4f} {BG[2]/255:.4f} rg 0 0 {W:.3f} {H:.3f} re f']
# divider line
ops.append(f'{193/255:.4f} {191/255:.4f} {179/255:.4f} rg {2*mm+72*px*mm:.3f} {(54-2-312*px)*mm:.3f} {(947-72)*px*mm:.3f} {2.5*px*mm:.3f} re f')
# characters image
ch = Image.open('back-000.jpg').convert('RGB').crop((683, 165, 951, 275))
diff = ImageChops.difference(ch, Image.new('RGB', ch.size, BG)).convert('L')
alpha = diff.point(lambda v: min(255, v*255//28))
cx, cy, cw, chh = 2+66*px, 2+149*px, 348*px, 143*px
ops.append(f'q {cw*mm:.3f} 0 0 {chh*mm:.3f} {cx*mm:.3f} {(54-cy-chh)*mm:.3f} cm /Im1 Do Q')
# text + icons
ops.append(f'{0x26/255:.4f} {0x2a/255:.4f} {0x1f/255:.4f} rg')
for start, segs in json.load(open('ink.json')):
    ops.append(pt(*start) + ' m')
    for s in segs:
        ops.append((pt(*s[1]) + ' l ' + pt(*s[2]) + ' l') if s[0] == 'L' else (' '.join(pt(*p) for p in s[1:]) + ' c'))
    ops.append('h')
ops.append('f*')
content = zlib.compress(('\n'.join(ops) + '\n').encode())
rgb = zlib.compress(ch.tobytes()); am = zlib.compress(alpha.tobytes())
w, h = ch.size
objs = [
 b'<< /Type /Catalog /Pages 2 0 R >>',
 b'<< /Type /Pages /Kids [3 0 R] /Count 1 >>',
 f'<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {W:.3f} {H:.3f}] /TrimBox [{2*mm:.3f} {2*mm:.3f} {W-2*mm:.3f} {H-2*mm:.3f}] /BleedBox [0 0 {W:.3f} {H:.3f}] /Contents 4 0 R /Resources << /XObject << /Im1 6 0 R >> >> >>'.encode(),
 (f'<< /Length {len(content)} /Filter /FlateDecode >>', content),
 b'<< /Title (SmithsFarm namecard back 94x54mm, trim 90x50mm) /Producer (smithsfarm goods) >>',
 (f'<< /Type /XObject /Subtype /Image /Width {w} /Height {h} /ColorSpace /DeviceRGB /BitsPerComponent 8 /SMask 7 0 R /Interpolate true /Length {len(rgb)} /Filter /FlateDecode >>', rgb),
 (f'<< /Type /XObject /Subtype /Image /Width {w} /Height {h} /ColorSpace /DeviceGray /BitsPerComponent 8 /Interpolate true /Length {len(am)} /Filter /FlateDecode >>', am),
]
out = bytearray(b'%PDF-1.6\n%\xe2\xe3\xcf\xd3\n'); offs = []
for i, o in enumerate(objs, 1):
    offs.append(len(out))
    if isinstance(o, tuple): out += f'{i} 0 obj\n{o[0]}\nstream\n'.encode() + o[1] + b'\nendstream\nendobj\n'
    else: out += f'{i} 0 obj\n'.encode() + o + b'\nendobj\n'
x = len(out)
out += f'xref\n0 {len(objs)+1}\n0000000000 65535 f \n'.encode() + ''.join(f'{o:010d} 00000 n \n' for o in offs).encode()
out += f'trailer\n<< /Size {len(objs)+1} /Root 1 0 R /Info 5 0 R >>\nstartxref\n{x}\n%%EOF\n'.encode()
for p in sys.argv[1:]: open(p, 'wb').write(out)
