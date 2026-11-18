# Swap only the serif "SMITH's FARM" for the brand wordmark (from the logo), fitted to the same box and centre.
import re, json, make3
d = re.search(r' d="([^"]+)"', open('logo_src.svg').read()).group(1)
def nums(s): return [float(v) for v in re.findall(r'-?[\d.]+', s)]
def bbox(ss):
    n = [v for s in ss for v in nums(s)]; return min(n[0::2]), min(n[1::2]), max(n[0::2]), max(n[1::2])
subs = re.findall(r'M[^M]*', d)
word = [s for s in subs if 27 <= bbox([s])[1] and bbox([s])[3] < 35.5]          # SMITH's FARM row only
WD = ' '.join(word); wx0, wy0, wx1, wy1 = bbox(word)
BB = {r[0]: r[1:] for r in json.load(open('bbox.json'))}
T = [f'p{i}' for i in range(14, 29)]
ox0 = min(BB[k][0] for k in T); oy0 = min(BB[k][1] for k in T)
ox1 = max(BB[k][0] + BB[k][2] for k in T); oy1 = max(BB[k][1] + BB[k][3] for k in T)
s = min((ox1 - ox0) / (wx1 - wx0), (oy1 - oy0) / (wy1 - wy0) * 1.0)
s = (ox1 - ox0) / (wx1 - wx0)                     # same width as the old wordmark
cx, cy = (ox0 + ox1) / 2, (oy0 + oy1) / 2
tx, ty = cx - (wx0 + wx1) / 2 * s, cy - (wy0 + wy1) / 2 * s
print('old', [round(v, 1) for v in (ox0, oy0, ox1 - ox0, oy1 - oy0)], 'new h', round((wy1 - wy0) * s, 1))
open('word.d', 'w').write(WD); open('word_tf.txt', 'w').write(f'{s} {tx} {ty}')
TF = f'matrix({s:.5f} 0 0 {s:.5f} {tx:.4f} {ty:.4f})'
w = lambda extra: f'<path d="{WD}" fill-rule="evenodd" transform="{TF}" {extra}/>'
defs, body, _ = make3.v3d()
vb = f'{make3.X0} {make3.Y0} {make3.X1-make3.X0} {make3.Y1-make3.Y0}'
head = f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="{vb}" width="250" height="494"><defs>{make3.defs_common()}{defs}</defs>{body}'
shadow = f'<g clip-path="url(#U)"><g fill="#000" opacity=".35" filter="url(#soft2)" transform="translate(1.2 1.6)">{w("")}</g></g>'
letters = w('fill="#fff" stroke="#fff" stroke-width="1.6" stroke-linejoin="round"') + w('fill="#140c0a"')
open('art_3d_word_img.svg', 'w').write(head + shadow + '</svg>')
open('art_3d_word.svg', 'w').write(head + shadow + letters + '</svg>')
