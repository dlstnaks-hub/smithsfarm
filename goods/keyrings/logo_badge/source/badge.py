# Put a small orange SMITH's FARM badge (icon + wordmark, white) on each keyring's chest, in the print layer only.
import re
d = re.search(r' d="([^"]+)"', open('../svc/logo_src.svg').read()).group(1)
MAIN = ' '.join(s for s in re.findall(r'M[^M]*', d) if min(float(v) for v in re.findall(r'-?\d+\.?\d*', s)[1::2]) < 35)
LB = (27.0, 16.4, 40.0, 17.9)                          # logo box without the subtitle
def badge(cx, cy, w, stroke):
    h = w * 0.62; lw = w * 0.82; lh = lw * LB[3] / LB[2]
    return (f'<g><rect x="{cx-w/2:.3f}" y="{cy-h/2:.3f}" width="{w:.3f}" height="{h:.3f}" rx="{h*0.2:.3f}" fill="#ed6d00" stroke="#fdf8ee" stroke-width="{stroke}"/>'
            f'<svg x="{cx-lw/2:.3f}" y="{cy-lh/2:.3f}" width="{lw:.3f}" height="{lh:.3f}" viewBox="{LB[0]} {LB[1]} {LB[2]} {LB[3]}"><path fill="#ffffff" fill-rule="evenodd" d="{MAIN}"/></svg></g>')
SPOT = {   # (transform matching the art group, badge centre and width in art units, border width)
    'scarecrow': ('translate(-3.000 -5.200) scale(1.3547) translate(1 1.6)', 23.0, 39.6, 11.6, 0.45),
    'carrot':    ('scale(1.506)', 15.0, 39.6, 9.6, 0.45),
    'octopus':   ('translate(-4.200 -5.500) scale(1.498) translate(1 4.2) scale(0.383)', 60.0, 80.5, 30.0, 1.2),
}
for n, (tf, cx, cy, w, sw) in SPOT.items():
    p = f'{n}_print.svg'; s = open(p).read()
    i = s.rindex('</svg>')
    open(p, 'w').write(s[:i] + f'<g transform="{tf}">{badge(cx, cy, w, sw)}</g>' + s[i:])
