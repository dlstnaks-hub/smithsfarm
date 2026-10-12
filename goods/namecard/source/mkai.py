# Vector front of the name card: traced logo as editable paths, written as a plain PDF (Illustrator opens it as .ai)
import re, sys, zlib
svg = open('front.svg').read()
d = re.search(r' d="([^"]+)"', svg).group(1)
col = re.search(r'fill="(#[0-9a-f]{6})" fill-rule', svg).group(1)
r, g, b = (int(col[i:i+2], 16) / 255 for i in (1, 3, 5))
mm = 72 / 25.4; H = 54
def pt(x, y): return f'{float(x)*mm:.3f} {(H-float(y))*mm:.3f}'
ops = []
for tok in re.findall(r'[MLCZ][^MLCZ]*', d):
    c, nums = tok[0], tok[1:].split()
    if c == 'M': ops.append(pt(*nums[:2]) + ' m')
    elif c == 'L': ops.append(pt(*nums[:2]) + ' l')
    elif c == 'C': ops.append(' '.join(pt(nums[i], nums[i+1]) for i in (0, 2, 4)) + ' c')
    else: ops.append('h')
W, Hp = 94*mm, 54*mm
content = f'1 1 1 rg 0 0 {W:.3f} {Hp:.3f} re f\n{r:.4f} {g:.4f} {b:.4f} rg\n' + '\n'.join(ops) + '\nf*\n'
data = zlib.compress(content.encode())
objs = [
 '<< /Type /Catalog /Pages 2 0 R >>',
 '<< /Type /Pages /Kids [3 0 R] /Count 1 >>',
 f'<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {W:.3f} {Hp:.3f}] /TrimBox [{2*mm:.3f} {2*mm:.3f} {W-2*mm:.3f} {Hp-2*mm:.3f}] /BleedBox [0 0 {W:.3f} {Hp:.3f}] /Contents 4 0 R /Resources << >> >>',
 None,
 '<< /Title (SmithsFarm namecard front 94x54mm, trim 90x50mm) /Producer (smithsfarm goods) >>',
]
out = bytearray(b'%PDF-1.6\n%\xe2\xe3\xcf\xd3\n'); offs = []
for i, o in enumerate(objs, 1):
    offs.append(len(out))
    if o is None:
        out += f'{i} 0 obj\n<< /Length {len(data)} /Filter /FlateDecode >>\nstream\n'.encode() + data + b'\nendstream\nendobj\n'
    else:
        out += f'{i} 0 obj\n{o}\nendobj\n'.encode()
x = len(out)
out += f'xref\n0 {len(objs)+1}\n0000000000 65535 f \n'.encode() + ''.join(f'{o:010d} 00000 n \n' for o in offs).encode()
out += f'trailer\n<< /Size {len(objs)+1} /Root 1 0 R /Info 5 0 R >>\nstartxref\n{x}\n%%EOF\n'.encode()
for p in sys.argv[1:]: open(p, 'wb').write(out)
