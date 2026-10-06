# Sizes for the 130mm tier (shop prices by width + height of the cut line).
# The artwork is scaled; the 3.4mm ring hole and the 1.2mm cream border keep their real size.
import art
SCALE = {'scarecrow': 1.3547, 'octopus': 1.498, 'carrot': 1.506}
def get(name):
    k = dict(getattr(art, name.upper()))
    s = SCALE[name]
    k['scale'] = s
    if s != 1.0:
        k['art'] = f'<g transform="scale({s})">{k["art"]}</g>'
        k['w'], k['h'] = round(k['w']*s, 2), round(k['h']*s, 2)
        hx, hy, hr = k['hole']; k['hole'] = (hx*s, hy*s, hr)
    return k
