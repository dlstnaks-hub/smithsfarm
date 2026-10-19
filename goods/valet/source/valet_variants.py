# Valet poster with a different title font: writes valet_<font>_<size>.html for A2/A1 (+3mm bleed variants).
import re
from common import HEAD
src = open('valet.py').read()
ns = {}; exec("Y = '#f2c230'; BG = '#1b1b1b'; FR = '#111111'\n" + src[src.index('def art():'):src.index('for name, w, h, bleed')], ns)
base = ns['art']()
TITLE = r'<text x="210" y="74"[^>]*>스미스씨네 농장</text>'
VARIANTS = {
    'jua':   ('Jua', 400, 42, 1, 'fonts/dl/fontsource-jua-5.3.0/package/index.css'),
    'black': ('Black Han Sans', 400, 42, 1, 'fonts/dl/fontsource-black-han-sans-5.3.0/package/index.css'),
}
FR = '#111111'
for key, (fam, wt, size, ls, css) in VARIANTS.items():
    t = f'<text x="210" y="76" text-anchor="middle" font-family="{fam}" font-weight="{wt}" font-size="{size}" fill="#ffffff" letter-spacing="{ls}">스미스씨네 농장</text>'
    art = re.sub(TITLE, t, base)
    for name, w, h, bleed in (('A2', 420, 594, 0), ('A1', 594, 841, 0), ('A2_bleed', 420, 594, 3), ('A1_bleed', 594, 841, 3)):
        W, H = w + 2*bleed, h + 2*bleed
        body = f'<div class="page"><svg class="sheet" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" fill="{FR}"/><g transform="translate({bleed} {bleed}) scale({w/420:.6f})">{art}</g></svg></div>'
        open(f'valet_{key}_{name}.html', 'w').write(HEAD.format(w=W, h=H).replace('<style>', f'<link rel="stylesheet" href="{css}"><style>') + body + '</body></html>')
