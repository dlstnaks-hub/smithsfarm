# Three restyles of the Smith's Farm bill-holder vegetable bouquet: 3D (입체), abstract (추상), realistic (현실).
# Every effect is clipped to the original shapes, so the silhouette - and the die-cut line - stay exactly as drawn.
import re, json, random, colorsys
src = open('src_ids.svg').read()
P = {m.group(1): m.group(0) for m in re.finditer(r'<path id="(p\d+)"[^>]*/>', src)}
D = {k: re.search(r' d="([^"]+)"', v).group(1) for k, v in P.items()}
def rgb(v):
    nums = [float(x) for x in re.findall(r'([\d.]+)%', re.search(r'fill="rgb\(([^)]*)\)"', v).group(1))]
    return '#%02x%02x%02x' % tuple(round(n * 2.55) for n in nums)
C = {k: rgb(v) for k, v in P.items() if 'fill="rgb' in v}
BB = {k: v[1:] for k, *_ in [[r[0]] for r in []]}
BB = {r[0]: r[1:] for r in json.load(open('bbox.json'))}
ART = [f'p{i}' for i in range(1, 14)]
TEXT = [f'p{i}' for i in range(14, 29)]
CAPTION = [f'p{i}' for i in range(29, 36)]
X0, Y0, X1, Y1 = 40, 146, 290, 640          # art box with a little air

def shade(hexc, f):
    r, g, b = (int(hexc[i:i+2], 16) / 255 for i in (1, 3, 5))
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    l = max(0, min(1, l * f if f < 1 else l + (1 - l) * (f - 1)))
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    return '#%02x%02x%02x' % (round(r * 255), round(g * 255), round(b * 255))

def defs_common():
    o = ''.join(f'<path id="{k}" d="{D[k]}"/>' for k in ART + TEXT)
    o += ''.join(f'<clipPath id="c{k}"><use href="#{k}"/></clipPath>' for k in ART)
    o += '<clipPath id="U">' + ''.join(f'<use href="#{k}"/>' for k in ART) + '</clipPath>'
    return o

def text_layer(style):
    t = ''.join(f'<use href="#{k}"/>' for k in TEXT)
    if style == '3d':
        return (f'<g clip-path="url(#U)"><g fill="#000" opacity=".35" filter="url(#soft2)" transform="translate(1.2 1.6)">{t}</g></g>'
                f'<g fill="#fff" stroke="#fff" stroke-width="1.6" stroke-linejoin="round">{t}</g><g fill="#140c0a">{t}</g>')
    if style == 'abs':
        return f'<g fill="#140c0a" transform="translate(1.1 1.1)">{t}</g><g fill="#f3efe4" stroke="#f3efe4" stroke-width=".3">{t}</g>'
    return f'<g fill="#fff" stroke="#fff" stroke-width="1.2" stroke-linejoin="round" opacity=".9">{t}</g><g fill="#140c0a">{t}</g>'

FILTERS = '''
<filter id="soft2" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="1"/></filter>
<filter id="cast" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="3.2"/></filter>
<filter id="castR" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="4.5"/></filter>
<filter id="puff" x="-5%" y="-5%" width="110%" height="110%" color-interpolation-filters="sRGB">
  <feGaussianBlur in="SourceAlpha" stdDeviation="5.5" result="b"/>
  <feDiffuseLighting in="b" surfaceScale="4.5" diffuseConstant="1.18" lighting-color="#fff" result="d0"><feDistantLight azimuth="225" elevation="52"/></feDiffuseLighting>
  <feGaussianBlur in="d0" stdDeviation="1.2" result="d"/>
  <feSpecularLighting in="b" surfaceScale="4.5" specularConstant=".85" specularExponent="18" lighting-color="#fff" result="s0"><feDistantLight azimuth="225" elevation="52"/></feSpecularLighting>
  <feGaussianBlur in="s0" stdDeviation="1.2" result="s"/>
  <feComposite in="SourceGraphic" in2="d" operator="arithmetic" k1="1" result="lit"/>
  <feComposite in="s" in2="lit" operator="arithmetic" k2=".55" k3="1" result="o"/>
  <feComposite in="o" in2="SourceAlpha" operator="in"/>
</filter>
<filter id="real" x="-5%" y="-5%" width="110%" height="110%" color-interpolation-filters="sRGB">
  <feGaussianBlur in="SourceAlpha" stdDeviation="7" result="b"/>
  <feDiffuseLighting in="b" surfaceScale="3.5" diffuseConstant="1.12" lighting-color="#fff8ec" result="d0"><feDistantLight azimuth="230" elevation="58"/></feDiffuseLighting>
  <feGaussianBlur in="d0" stdDeviation="1.4" result="d"/>
  <feSpecularLighting in="b" surfaceScale="3.5" specularConstant=".6" specularExponent="32" lighting-color="#fff" result="s0"><feDistantLight azimuth="230" elevation="58"/></feSpecularLighting>
  <feGaussianBlur in="s0" stdDeviation="1.4" result="s"/>
  <feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" seed="4" result="n"/>
  <feColorMatrix in="n" type="matrix" values="0 0 0 0 .5  0 0 0 0 .5  0 0 0 0 .5  0 0 0 .9 0" result="ng"/>
  <feComposite in="SourceGraphic" in2="d" operator="arithmetic" k1="1" result="lit"/>
  <feComposite in="s" in2="lit" operator="arithmetic" k2=".4" k3="1" result="o1"/>
  <feBlend in="o1" in2="ng" mode="soft-light" result="o2"/>
  <feComposite in="o2" in2="o1" operator="arithmetic" k2=".55" k3=".45" result="o3"/>
  <feComposite in="o3" in2="SourceAlpha" operator="in"/>
</filter>
<filter id="hl" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="2.2"/></filter>
<filter id="hl2" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="5"/></filter>
'''

def lin(id, c1, c2, x1=0, y1=0, x2=1, y2=1):
    return f'<linearGradient id="{id}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>'
def rad(id, stops, cx=.38, cy=.32, r=.8):
    st = ''.join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in stops)
    return f'<radialGradient id="{id}" cx="{cx}" cy="{cy}" r="{r}">{st}</radialGradient>'

# ------------------------------------------------------------------ 1) 입체 (puffy, layered, cast shadows)
def v3d():
    g = ''.join(lin(f'g{k}', shade(C[k], 1.22), shade(C[k], .78)) for k in ART)
    body = ''
    for k in ART:
        body += f'<g clip-path="url(#U)"><use href="#{k}" fill="#1a0f08" opacity=".32" filter="url(#cast)" transform="translate(3.5 4.5)"/></g>'
        body += f'<g filter="url(#puff)"><use href="#{k}" fill="url(#g{k})"/></g>'
    x, y, w, h = BB['p12']   # tomato gloss
    body += f'<g clip-path="url(#cp12)"><ellipse cx="{x+w*.3}" cy="{y+h*.24}" rx="{w*.14}" ry="{h*.08}" fill="#fff" opacity=".75" filter="url(#hl)" transform="rotate(-20 {x+w*.3} {y+h*.24})"/></g>'
    x, y, w, h = BB['p7']    # eggplant sheen
    body += f'<g clip-path="url(#cp7)"><path d="M{x+w*.32} {y+h*.25} Q{x+w*.22} {y+h*.55} {x+w*.3} {y+h*.85}" stroke="#fff" stroke-width="5" fill="none" opacity=".45" filter="url(#hl)"/></g>'
    return FILTERS + g, body, text_layer('3d')

# ------------------------------------------------------------------ 2) 추상 (graphic blocks, patterns, offset prints)
def vabs():
    pal = {'p1': '#2f6b3a', 'p2': '#c9d96b', 'p3': '#f3efe4', 'p4': '#f3efe4', 'p5': '#3f8f4a', 'p6': '#e6eccd',
           'p7': '#5b3f8c', 'p8': '#c46bb0', 'p9': '#1f4a2a', 'p10': '#9cc15a', 'p11': '#ed7409', 'p12': '#e8402a', 'p13': '#2f6b3a'}
    d = ''
    d += '<pattern id="stripeH" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="2.2" fill="#f3efe4" opacity=".55"/></pattern>'
    d += '<pattern id="dots" width="9" height="9" patternUnits="userSpaceOnUse"><circle cx="4.5" cy="4.5" r="1.7" fill="#ffd2b8" opacity=".75"/></pattern>'
    d += '<pattern id="diag" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(35)"><rect width="1.6" height="7" fill="#e6eccd" opacity=".45"/></pattern>'
    d += '<pattern id="vert" width="6" height="6" patternUnits="userSpaceOnUse"><rect width="1.4" height="6" fill="#1f4a2a" opacity=".35"/></pattern>'
    d += '<pattern id="dotsS" width="6" height="6" patternUnits="userSpaceOnUse"><circle cx="3" cy="3" r="1" fill="#8dbe5a" opacity=".6"/></pattern>'
    PAT = {'p11': 'stripeH', 'p12': 'dots', 'p5': 'diag', 'p1': 'diag', 'p3': 'vert', 'p6': 'dotsS', 'p10': 'diag'}
    body = ''
    for k in ART:
        body += f'<g clip-path="url(#U)"><use href="#{k}" fill="#2a2418" opacity=".22" transform="translate(5 5)"/></g>'
        body += f'<use href="#{k}" fill="{pal[k]}"/>'
        if k in PAT:
            body += f'<g clip-path="url(#c{k})"><rect x="{X0}" y="{Y0}" width="{X1-X0}" height="{Y1-Y0}" fill="url(#{PAT[k]})"/></g>'
        x, y, w, h = BB[k]
        if k == 'p7':    # eggplant: concentric arcs
            body += f'<g clip-path="url(#cp7)" fill="none" stroke="#8a6cc0" stroke-width="2.4" opacity=".8">' + ''.join(
                f'<circle cx="{x+w*.15}" cy="{y+h*1.0}" r="{r}"/>' for r in range(30, 320, 16)) + '</g>'
        if k == 'p12':   # tomato: a big flat half-moon
            body += f'<g clip-path="url(#cp12)"><circle cx="{x+w*.78}" cy="{y+h*.8}" r="{w*.42}" fill="#b8261b" opacity=".85"/></g>'
        if k == 'p11':   # carrot: zig-zag cut
            body += f'<g clip-path="url(#cp11)"><path d="M{x} {y+h*.62} l{w*.25} -{h*.06} l{w*.25} {h*.06} l{w*.25} -{h*.06} l{w*.25} {h*.06} V{y+h} H{x} Z" fill="#c95a00" opacity=".9"/></g>'
        if k == 'p5':    # leaves: half-circle block
            body += f'<g clip-path="url(#cp5)"><circle cx="{x+w*.85}" cy="{y+h*.18}" r="{w*.34}" fill="#2f6b3a" opacity=".85"/></g>'
    return d, body, text_layer('abs')

# ------------------------------------------------------------------ 3) 현실 (natural gradients, texture, veins, gloss)
def vreal():
    R = {
     'p1': lin('rp1', '#5e9c4c', '#2c5a2a', .2, 0, .8, 1), 'p2': lin('rp2', '#cfe08a', '#93ad4a', 0, 0, 0, 1),
     'p3': lin('rp3', '#ffffff', '#e4edd2', 0, 0, 0, 1), 'p4': lin('rp4', '#ffffff', '#eef2e6', 0, 0, 1, 1),
     'p5': rad('rp5', [(0, '#43c05a'), (.6, '#1f9a3c'), (1, '#126b29')], .4, .25, .9),
     'p6': lin('rp6', '#eef5d8', '#c9dca0', 0, 0, 0, 1),
     'p7': rad('rp7', [(0, '#8b6cbf'), (.45, '#5a3b8c'), (1, '#2c1748')], .3, .3, .85),
     'p8': lin('rp8', '#b065b0', '#6c2f74'), 'p9': lin('rp9', '#3f7d45', '#1c4523'),
     'p10': lin('rp10', '#b7d77a', '#6f9a3c', 0, 0, 0, 1),
     'p11': lin('rp11', '#f7a35c', '#d4661f', 0, .5, 1, .5),
     'p12': rad('rp12', [(0, '#ff7a5c'), (.35, '#ee3d22'), (.85, '#b9200f'), (1, '#8c160b')], .35, .3, .8),
     'p13': lin('rp13', '#3cbf5a', '#1a7a32')}
    d = ''.join(R.values())
    body = ''
    rnd = random.Random(7)
    for k in ART:
        body += f'<g clip-path="url(#U)"><use href="#{k}" fill="#1a0f08" opacity=".38" filter="url(#castR)" transform="translate(2.5 4)"/></g>'
        body += f'<g filter="url(#real)"><use href="#{k}" fill="url(#r{k})"/></g>'
        x, y, w, h = BB[k]
        if k == 'p11':   # carrot rings
            rings = ''.join(f'<path d="M{x+w*rnd.uniform(.05,.35)} {y+h*t:.1f} q{w*.18} {rnd.uniform(1.5,3):.1f} {w*rnd.uniform(.3,.5):.1f} 0" />' for t in [i/14 + rnd.uniform(-.02,.02) for i in range(2, 14)])
            body += f'<g clip-path="url(#cp11)" fill="none" stroke="#a9480f" stroke-width="1.1" stroke-linecap="round" opacity=".55">{rings}</g>'
            body += f'<g clip-path="url(#cp11)"><rect x="{x+w*.18}" y="{y}" width="{w*.12}" height="{h}" fill="#fff" opacity=".25" filter="url(#hl)"/></g>'
        if k in ('p1', 'p5', 'p13'):   # leaf veins from the base up
            veins = ''.join(f'<path d="M{x+w*.5} {y+h} Q{x+w*f} {y+h*.5} {x+w*(f*1.1-.05)} {y+h*.05}"/>' for f in (.18, .38, .58, .78, .95))
            body += f'<g clip-path="url(#c{k})" fill="none" stroke="#d9f2c4" stroke-width=".9" opacity=".45">{veins}</g>'
        if k in ('p3', 'p6', 'p10'):   # stalk fibres
            fib = ''.join(f'<line x1="{x+w*f}" y1="{y}" x2="{x+w*(f+rnd.uniform(-.05,.05))}" y2="{y+h}"/>' for f in [i/9 for i in range(1, 9)])
            body += f'<g clip-path="url(#c{k})" stroke="#8fae5c" stroke-width=".6" opacity=".35">{fib}</g>'
        if k == 'p12':   # tomato gloss + lobes
            body += f'<g clip-path="url(#cp12)"><ellipse cx="{x+w*.32}" cy="{y+h*.28}" rx="{w*.16}" ry="{h*.09}" fill="#fff" opacity=".85" filter="url(#hl)" transform="rotate(-25 {x+w*.32} {y+h*.28})"/>'
            body += f'<ellipse cx="{x+w*.42}" cy="{y+h*.36}" rx="{w*.04}" ry="{h*.03}" fill="#fff" opacity=".9" filter="url(#soft2)"/>'
            body += f'<path d="M{x+w*.5} {y+h*.1} Q{x+w*.45} {y+h*.55} {x+w*.5} {y+h*.98} M{x+w*.25} {y+h*.15} Q{x+w*.15} {y+h*.55} {x+w*.3} {y+h*.95}" stroke="#8c160b" stroke-width="2" fill="none" opacity=".35" filter="url(#hl)"/></g>'
        if k == 'p7':    # eggplant gloss
            body += f'<g clip-path="url(#cp7)"><path d="M{x+w*.34} {y+h*.22} Q{x+w*.22} {y+h*.55} {x+w*.32} {y+h*.88}" stroke="#fff" stroke-width="6" fill="none" opacity=".55" filter="url(#hl)"/>'
            body += f'<path d="M{x+w*.4} {y+h*.3} Q{x+w*.32} {y+h*.5} {x+w*.36} {y+h*.7}" stroke="#fff" stroke-width="1.6" fill="none" opacity=".8" filter="url(#soft2)"/></g>'
    return FILTERS + d, body, text_layer('real')

def art_svg(fn, w_px=None):
    defs, body, text = fn()
    vb = f'{X0} {Y0} {X1-X0} {Y1-Y0}'
    size = f'width="{w_px}" height="{round(w_px*(Y1-Y0)/(X1-X0))}"' if w_px else f'width="{X1-X0}" height="{Y1-Y0}"'
    return f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="{vb}" {size}><defs>{defs_common()}{defs}</defs>{body}{text}</svg>'

for name, fn in (('3d', v3d), ('abs', vabs), ('real', vreal)):
    open(f'art_{name}.svg', 'w').write(art_svg(fn))
print(C)
