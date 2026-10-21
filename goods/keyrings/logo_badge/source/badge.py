# Put the white SMITH's FARM logo (icon + wordmark) on each keyring, in the print layer only: scarecrow chest, carrot leaves, octopus head.
import re
d = re.search(r' d="([^"]+)"', open('../svc/logo_src.svg').read()).group(1)
MAIN = ' '.join(s for s in re.findall(r'M[^M]*', d) if min(float(v) for v in re.findall(r'-?\d+\.?\d*', s)[1::2]) < 35)
LB = (27.0, 16.4, 40.0, 17.9)                          # logo box without the subtitle
def badge(cx, cy, w, _unused=None):
    # white logo (hat icon + SMITH's FARM) straight on the character, no box or border
    h = w * LB[3] / LB[2]
    return (f'<svg x="{cx-w/2:.3f}" y="{cy-h/2:.3f}" width="{w:.3f}" height="{h:.3f}" viewBox="{LB[0]} {LB[1]} {LB[2]} {LB[3]}">'
            f'<path fill="#ffffff" fill-rule="evenodd" d="{MAIN}"/></svg>')
SPOT = {   # (number of leading <g transform> wrappers around the art, logo centre and width in art units, unused)
    'scarecrow': (3, 23.0, 32.95, 11.0, 0),
    'carrot':    (1, 15.0, 12.2, 14.0, 0),
    'octopus':   (3, 70.5, 30.5, 25.0, 0),
}
for n, (tf, cx, cy, w, sw) in SPOT.items():
    p = f'{n}_print.svg'; s = open(p).read()
    tf = ' '.join(re.findall(r'<g transform="([^"]+)"', s)[:tf])   # same wrappers as the art, read from the file
    i = s.rindex('</svg>')
    open(p, 'w').write(s[:i] + f'<g transform="{tf}">{badge(cx, cy, w, sw)}</g>' + s[i:])
