# Sizes for the 90mm tier (shop prices by width + height of the cut line).
# The artwork is scaled; the 3.4mm ring hole and the 1.2mm cream border keep their real size.
import art
SCALE = {'scarecrow': 0.9162, 'octopus': 1.0}
def get(name):
    k = dict(getattr(art, name.upper()))
    s = SCALE[name]
    if s != 1.0:
        k['art'] = f'<g transform="scale({s})">{k["art"]}</g>'
        k['w'], k['h'] = k['w']*s, k['h']*s
        hx, hy, hr = k['hole']; k['hole'] = (hx*s, hy*s, hr)
    return k
