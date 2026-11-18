# Illustrator-ready .ai (PDF-compatible) of the 3D bill holder, same A4 page and positions as the original .ai.
# Layers: 1 입체 일러스트 (600dpi image, transparent background), 2 로고 SMITH's FARM (brand wordmark, vector, white outline),
#         3 도무송 칼선 (vector die-cut, as in the original) + caption.
import re, sys, zlib
from PIL import Image
svg = open('src_ids.svg').read()
P = {m.group(1): m.group(0) for m in re.finditer(r'<path id="(p\d+)"[^>]*/>', svg)}
PW, PH = 595.276, 841.89
def ops(d):
    o = []
    for tok in re.findall(r'[MLCZ][^MLCZ]*', d):
        c, n = tok[0], tok[1:].split()
        o.append({'M': lambda: f'{n[0]} {n[1]} m', 'L': lambda: f'{n[0]} {n[1]} l',
                  'C': lambda: ' '.join(n[:6]) + ' c', 'Z': lambda: 'h'}[c]())
    return '\n'.join(o)
d = lambda k: re.search(r' d="([^"]+)"', P[k]).group(1)
FLIP = f'1 0 0 -1 0 {PW*0+PH} cm'
TEXT = [f'p{i}' for i in range(14, 29)]; CAP = [f'p{i}' for i in range(29, 36)]
WS, WTX, WTY = open('word_tf.txt').read().split()
text_paths = ops(open('word.d').read())
cut_m = re.search(r'transform="matrix\(([^)]*)\)"', P['p0']).group(1).replace(',', ' ')
im = Image.open('art_3d_word_img_600.png').convert('RGBA')
rgb = zlib.compress(im.convert('RGB').tobytes(), 9); alpha = zlib.compress(im.getchannel('A').tobytes(), 9)
iw, ih = im.size
X0, Y0, AW, AH = 40, 146, 250, 494
content = (
 '/OC /L1 BDC\n'
 f'q {AW} 0 0 {AH} {X0} {PH-Y0-AH:.3f} cm /Art Do Q\nEMC\n'
 '/OC /L2 BDC\n'
 f'q {FLIP}\nq {WS} 0 0 {WS} {WTX} {WTY} cm\n0.0784 0.0471 0.0392 RG {1.1/float(WS):.4f} w 1 j 0.0784 0.0471 0.0392 rg\n{text_paths}\nB*\n'
 f'1 0.98 0.949 rg\n{text_paths}\nf*\nQ\nQ\nEMC\n'
 '/OC /L3 BDC\n'
 f'q {FLIP}\nq {cut_m} cm\n0.0196 0.0039 0.0078 RG 1 w 0 J 0 j\n{ops(d("p0"))}\nS\nQ\n'
 '0.1373 0.098 0.0863 rg\n' + '\n'.join(ops(d(k)) for k in CAP) + '\nf\nQ\nEMC\n')
data = zlib.compress(content.encode())
L = [('입체 일러스트', 9), ('로고 SMITH\'s FARM', 10), ('도무송 칼선', 11)]
def pdfstr(s): return '<FEFF' + s.encode('utf-16-be').hex().upper() + '>'
objs = {
 1: '<< /Type /Catalog /Pages 2 0 R /OCProperties << /OCGs [9 0 R 10 0 R 11 0 R] /D << /Order [9 0 R 10 0 R 11 0 R] /ON [9 0 R 10 0 R 11 0 R] >> >> >>',
 2: '<< /Type /Pages /Kids [3 0 R] /Count 1 >>',
 3: f'<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {PW} {PH}] /TrimBox [0 0 {PW} {PH}] /Contents 4 0 R '
    '/Resources << /XObject << /Art 5 0 R >> /Properties << /L1 9 0 R /L2 10 0 R /L3 11 0 R >> >> /Group << /S /Transparency /CS /DeviceRGB >> >>',
 4: ('stream', data, ''),
 5: ('stream', rgb, f'/Type /XObject /Subtype /Image /Width {iw} /Height {ih} /ColorSpace /DeviceRGB /BitsPerComponent 8 /SMask 6 0 R /Interpolate true'),
 6: ('stream', alpha, f'/Type /XObject /Subtype /Image /Width {iw} /Height {ih} /ColorSpace /DeviceGray /BitsPerComponent 8'),
 7: f'<< /Title {pdfstr("스미스팜 빌지 도무송 - A 입체적")} /Creator (smithsfarm goods) /Producer (smithsfarm goods) >>',
 9: f'<< /Type /OCG /Name {pdfstr(L[0][0])} >>', 10: f'<< /Type /OCG /Name {pdfstr(L[1][0])} >>', 11: f'<< /Type /OCG /Name {pdfstr(L[2][0])} >>',
}
out = bytearray(b'%PDF-1.6\n%\xe2\xe3\xcf\xd3\n'); offs = {}
for i in sorted(objs):
    offs[i] = len(out); o = objs[i]
    if isinstance(o, tuple):
        _, s, extra = o
        out += f'{i} 0 obj\n<< {extra} /Length {len(s)} /Filter /FlateDecode >>\nstream\n'.encode() + s + b'\nendstream\nendobj\n'
    else:
        out += f'{i} 0 obj\n{o}\nendobj\n'.encode()
n = max(objs) + 1; x = len(out)
out += f'xref\n0 {n}\n0000000000 65535 f \n'.encode()
out += ''.join((f'{offs[i]:010d} 00000 n \n' if i in offs else '0000000000 65535 f \n') for i in range(1, n)).encode()
out += f'trailer\n<< /Size {n} /Root 1 0 R /Info 7 0 R >>\nstartxref\n{x}\n%%EOF\n'.encode()
for p in sys.argv[1:]: open(p, 'wb').write(out)
