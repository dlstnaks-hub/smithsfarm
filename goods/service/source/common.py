# Shared pieces for the store service prints: fonts, palette, logo, the three keyring characters (colour and line art).
import re
from art import CARROT, SCARECROW, OCTOPUS

ORANGE, GREEN, DARK, CREAM, LOGO = '#f5821f', '#2f6b3a', '#2a2418', '#f3efe4', '#ed7409'

HEAD = '''<!doctype html><html lang="ko"><head><meta charset="utf-8">
<link rel="stylesheet" href="fonts/noto/package/korean-400.css"><link rel="stylesheet" href="fonts/noto/package/latin-400.css">
<link rel="stylesheet" href="fonts/noto/package/korean-700.css"><link rel="stylesheet" href="fonts/noto/package/latin-700.css">
<link rel="stylesheet" href="fonts/noto/package/korean-900.css">
<link rel="stylesheet" href="fonts/dodum/package/index.css">
<link rel="stylesheet" href="fonts/quick/package/500.css"><link rel="stylesheet" href="fonts/quick/package/700.css">
<style>
@page {{ size: {w}mm {h}mm; margin: 0 }}
html, body {{ margin: 0; padding: 0 }}
.page {{ width: {w}mm; height: {h}mm; overflow: hidden; page-break-after: always; break-after: page }}
.page:last-child {{ page-break-after: auto; break-after: auto }}
svg.sheet {{ display: block; width: {w}mm; height: {h}mm }}
.r {{ font-family: 'Quicksand', 'Gowun Dodum', sans-serif }}
.b {{ font-family: 'Noto Sans KR', sans-serif; font-weight: 700 }}
.k {{ font-family: 'Noto Sans KR', sans-serif; font-weight: 900 }}
.n {{ font-family: 'Noto Sans KR', sans-serif; font-weight: 400 }}
</style></head><body>
'''

def page(w, h, body, bg='#ffffff'):
    return f'<div class="page"><svg class="sheet" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}"><rect width="{w}" height="{h}" fill="{bg}"/>{body}</svg></div>\n'

def doc(w, h, pages):
    return HEAD.format(w=w, h=h) + ''.join(pages) + '</body></html>\n'

# ---- logo: traced vector path of the card front (mm coords on the 94x54 card), cropped to its own box
_logo = open('logo_src.svg').read()
LOGO_D = re.search(r' d="([^"]+)"', _logo).group(1)
LOGO_BOX = (27.10, 16.51, 39.81, 20.98)          # x, y, w, h of the logo inside the traced card
def logo(x, y, w, color=LOGO):
    bx, by, bw, bh = LOGO_BOX
    h = w * bh / bw
    return f'<svg x="{x}" y="{y}" width="{w}" height="{h:.3f}" viewBox="{bx} {by} {bw} {bh}"><path fill="{color}" fill-rule="evenodd" d="{LOGO_D}"/></svg>'
def logo_h(w): return w * LOGO_BOX[3] / LOGO_BOX[2]

# ---- characters (colour), each with its own art box
OCT_ART = OCTOPUS['art'].replace('<circle cx="60" cy="10" r="9" fill="#c4532d"/>', '')
CHARS = {
    # name: (art markup, viewBox of the drawing itself)
    'carrot':    (CARROT['art'], (0, 0, 30, 56)),
    'octopus':   (OCT_ART, (3.6, 10.2, 40.8, 38.2)),
    'scarecrow': (SCARECROW['art'], (3.0, 4.6, 42.0, 50.8)),
}
def char(name, x, y, h, line=False, opacity=1):
    art, (bx, by, bw, bh) = CHARS[name]
    if line: art = LINE[name]
    w = h * bw / bh
    op = f' opacity="{opacity}"' if opacity != 1 else ''
    return f'<svg x="{x:.3f}" y="{y:.3f}" width="{w:.3f}" height="{h:.3f}" viewBox="{bx} {by} {bw} {bh}"{op}>{art}</svg>'
def char_w(name, h):
    bx, by, bw, bh = CHARS[name][1]; return h * bw / bh

# ---- line art for colouring: every coloured fill becomes white with a dark outline
DARKS = {'#2a2418', 'rgb(42,35,24)', '#1f2a1f', DARK}
def _lineart(markup, sw):
    def fix(m):
        tag = m.group(0)
        if 'fill-opacity' in tag or re.search(r'fill="(#ffc799|#ffb0a0|rgb\(255,199,153\))"', tag):
            return ''                                   # highlights and cheeks
        f = re.search(r'fill="([^"]+)"', tag)
        fill = f.group(1) if f else None
        if fill in (None, 'none'):
            return re.sub(r'stroke="[^"]+"', f'stroke="{DARK}"', tag)
        if fill in DARKS or fill in ('#fff', '#ffffff', '#fdf8ee'):
            return tag
        tag = tag.replace(f'fill="{fill}"', 'fill="#ffffff"')
        tag = re.sub(r' stroke(-width)?="[^"]+"', '', tag)
        return tag.replace('/>', f' stroke="{DARK}" stroke-width="{sw}" stroke-linejoin="round"/>', 1)
    return re.sub(r'<(path|circle|ellipse|rect)\b[^>]*/>', fix, markup)

OCT_LINE = '''<g transform="translate(1 4.2) scale(0.383)">
  <g fill="none" stroke-linecap="round">
    <g stroke="#2a2418" stroke-width="13"><path d="M34 70 C28 92 18 98 12 92"/><path d="M48 76 C46 98 38 110 30 106"/><path d="M72 76 C74 98 82 110 90 106"/><path d="M86 70 C92 92 102 98 108 92"/></g>
    <g stroke="#ffffff" stroke-width="8"><path d="M34 70 C28 92 18 98 12 92"/><path d="M48 76 C46 98 38 110 30 106"/><path d="M72 76 C74 98 82 110 90 106"/><path d="M86 70 C92 92 102 98 108 92"/></g>
  </g>
  <ellipse cx="60" cy="48" rx="34" ry="32" fill="#ffffff" stroke="#2a2418" stroke-width="2.6"/>
  <circle cx="48" cy="48" r="5" fill="none" stroke="#2a2418" stroke-width="2.4"/><circle cx="72" cy="48" r="5" fill="none" stroke="#2a2418" stroke-width="2.4"/>
  <path d="M53 60 Q60 66 67 60" fill="none" stroke="#2a2418" stroke-width="2.4" stroke-linecap="round"/>
</g>'''
LINE = {
    'carrot': _lineart(CARROT['art'], 0.7),
    'scarecrow': _lineart(SCARECROW['art'], 0.45),
    'octopus': OCT_LINE,
}
