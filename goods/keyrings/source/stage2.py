# trace a cut line ~1.2mm outside the artwork, then write print SVGs and data for the 3D page
import json, math
from PIL import Image, ImageFilter
import art
PX = 10; MARGIN = 1.2

def trace(mask, W, H):
    px = mask.load()
    on = lambda x, y: 0 <= x < W and 0 <= y < H and px[x, y] > 127
    D = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
    idx = {d:i for i,d in enumerate(D)}
    start = next((x, y) for y in range(H) for x in range(W) if on(x, y))
    cx, cy = start; bx, by = cx-1, cy; pts = []
    for _ in range(200000):
        pts.append((cx, cy))
        bi = idx[(bx-cx, by-cy)]
        for k in range(1, 9):
            d = (bi+k) % 8; nx, ny = cx+D[d][0], cy+D[d][1]
            if on(nx, ny):
                pd = (bi+k-1) % 8; bx, by = cx+D[pd][0], cy+D[pd][1]; cx, cy = nx, ny; break
        if (cx, cy) == start: break
    return pts

def smooth(pts, w=4):
    n = len(pts)
    return [(sum(pts[(i+j)%n][0] for j in range(-w,w+1))/(2*w+1), sum(pts[(i+j)%n][1] for j in range(-w,w+1))/(2*w+1)) for i in range(n)]

def dp(pts, eps):
    if len(pts) < 3: return pts
    (x1,y1),(x2,y2) = pts[0], pts[-1]; L = math.hypot(x2-x1, y2-y1) or 1e-9
    dmax, imax = 0, 0
    for i in range(1, len(pts)-1):
        x0,y0 = pts[i]; d = abs((y2-y1)*x0 - (x2-x1)*y0 + x2*y1 - y2*x1)/L
        if d > dmax: dmax, imax = d, i
    if dmax > eps: return dp(pts[:imax+1], eps)[:-1] + dp(pts[imax:], eps)
    return [pts[0], pts[-1]]

out = {}
for name, k in (('scarecrow', art.SCARECROW), ('octopus', art.OCTOPUS)):
    a = Image.open(f'{name}_alpha.png').getchannel('A').point(lambda v: 255 if v > 20 else 0)
    r = int(MARGIN*PX)
    m = a.filter(ImageFilter.MaxFilter(2*r+1))
    W, H = m.size
    pts = smooth(trace(m, W, H), 5)
    n = len(pts); h2 = n//2
    pts = dp(pts[:h2+1], 0.35)[:-1] + dp(pts[h2:] + [pts[0]], 0.35)[:-1]
    poly = [(round(x/PX, 3), round(y/PX, 3)) for x, y in pts]
    d = 'M' + ' L'.join(f'{x} {y}' for x, y in poly) + ' Z'
    k['outline_svg'] = d; k['poly'] = poly
    print(name, len(poly), 'points')
# carrot outline is the original vector path (already in PDF y-up coordinates)
for name, k in (('scarecrow', art.SCARECROW), ('octopus', art.OCTOPUS), ('carrot', art.CARROT)):
    w, h = k['w'], k['h']
    border = f'<path d="{k["outline_svg"]}" fill="#fdf8ee"/>' if 'outline_svg' in k else ''
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" data-w="{w}" data-h="{h}" width="{w}mm" height="{h}mm" viewBox="0 0 {w} {h}">{border}{k["art"]}</svg>'
    open(f'{name}_print.svg', 'w').write(svg)
    out[name] = dict(w=w, h=h, hole=k['hole'], poly=k.get('poly'), svg=svg)
json.dump(out, open('keyrings.json', 'w'))
