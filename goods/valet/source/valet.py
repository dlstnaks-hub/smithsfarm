# Valet parking poster (A-series portrait). Drawn on a 420x594 grid (A2 in mm); A1 is the same drawing scaled.
# Writes valet_<name>.html for each size; bleed (mm) extends the black background past the trim.
from common import HEAD
Y = '#f2c230'; BG = '#1b1b1b'; FR = '#111111'
def art():
    return f'''
<rect x="-10" y="-10" width="440" height="614" fill="{FR}"/>
<rect x="12" y="12" width="396" height="570" fill="{BG}"/>
<text x="210" y="74" text-anchor="middle" class="k" font-size="38" fill="#ffffff" letter-spacing="1">스미스씨네 농장</text>
<path d="M210 312 L148 232 A74 74 0 1 1 272 232 Z" fill="{Y}"/>
<circle cx="210" cy="190" r="54" fill="{BG}"/>
<text x="210" y="216" text-anchor="middle" font-family="Noto Sans KR, sans-serif" font-weight="700" font-size="74" fill="{Y}">P</text>
<text x="210" y="398" text-anchor="middle" class="k" font-size="72" fill="#ffffff" letter-spacing="-1">발렛파킹</text>
<text x="210" y="438" text-anchor="middle" font-family="Noto Sans KR, sans-serif" font-weight="500" font-size="21" fill="#ffffff">Free Valet Parking</text>
<rect x="70" y="466" width="3" height="66" fill="#ffffff"/>
<text x="86" y="490" font-family="Noto Sans KR, sans-serif" font-weight="500" font-size="22" fill="#ffffff">무료주차 (발렛비 3000원)</text>
<text x="86" y="524" font-family="Noto Sans KR, sans-serif" font-weight="500" font-size="22" fill="#ffffff">입차 / 출차 도와드립니다</text>'''
for name, w, h, bleed in (('A2', 420, 594, 0), ('A1', 594, 841, 0), ('A2_bleed', 420, 594, 3), ('A1_bleed', 594, 841, 3)):
    W, H = w + 2*bleed, h + 2*bleed
    k = w / 420
    body = f'<div class="page"><svg class="sheet" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" fill="{FR}"/><g transform="translate({bleed} {bleed}) scale({k:.6f})">{art()}</g></svg></div>'
    open(f'valet_{name}.html', 'w').write(HEAD.format(w=W, h=H) + body + '</body></html>')
    print(name, W, H)
