# Horizontal SMITH's FARM lockup (symbol left, wordmark + tagline right) rebuilt from the stacked traced logo.
import re
d = re.search(r' d="([^"]+)"', open('logo_src.svg').read()).group(1)
subs = re.findall(r'M[^M]*', d)
def nums(s): return [float(v) for v in re.findall(r'-?[\d.]+', s)]
def bbox(ss):
    n = [v for s in ss for v in nums(s)]; return min(n[0::2]), min(n[1::2]), max(n[0::2]), max(n[1::2])
sym = [s for s in subs if bbox([s])[1] < 27]; txt = [s for s in subs if bbox([s])[1] >= 27]
sx0, sy0, sx1, sy1 = bbox(sym); tx0, ty0, tx1, ty1 = bbox(txt)
k = (ty1 - ty0) * 1.12 / (sy1 - sy0)                 # symbol a touch taller than the text block, like the brand lockup
gap = (ty1 - ty0) * 0.42
def move(s, sc, dx, dy):
    out = []; it = iter(nums(s)); cmds = re.findall(r'[MLCZ]', s); parts = re.split(r'[MLCZ]', s)[1:]
    for c, p in zip(cmds, parts):
        v = [float(x) for x in p.split()]
        out.append(c + ' ' + ' '.join(f'{(v[i]*sc+dx) if i % 2 == 0 else (v[i]*sc+dy):.3f}' for i in range(len(v))))
    return ' '.join(out)
sh = (sy1 - sy0) * k; cy = (ty0 + ty1) / 2
sym2 = [move(s, k, tx0 - gap - (sx1 - sx0) * k - sx0 * k, cy - sh / 2 - sy0 * k) for s in sym]
D = ' '.join(sym2 + txt)
X0, Y0, X1, Y1 = bbox(sym2 + txt)
open('logo_h.d', 'w').write(D); open('logo_h.box', 'w').write(f'{X0} {Y0} {X1-X0} {Y1-Y0}')
open('logo_h_check.svg', 'w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{X0-2} {Y0-2} {X1-X0+4} {Y1-Y0+4}" width="700" height="{700*(Y1-Y0+4)/(X1-X0+4):.0f}"><rect x="{X0-2}" y="{Y0-2}" width="100" height="100" fill="#ed6d00"/><path d="{D}" fill="#fff" fill-rule="evenodd"/></svg>')
print(round(X1-X0, 2), round(Y1-Y0, 2))
