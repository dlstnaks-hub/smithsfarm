# Phone-screen version of the valet poster (1170x2532, iPhone ratio): same pieces, spread over the taller canvas.
from common import HEAD
Y = '#f2c230'; BG = '#1b1b1b'; FR = '#111111'
W, H = 420, 909
FONTS = {
    'jua':   ('Jua', 400, 46, 'fonts/dl/fontsource-jua-5.3.0/package/index.css'),
    'black': ('Black Han Sans', 400, 46, 'fonts/dl/fontsource-black-han-sans-5.3.0/package/index.css'),
}
for key, (fam, wt, size, css) in FONTS.items():
    art = f'''<rect width="{W}" height="{H}" fill="{FR}"/><rect x="12" y="12" width="{W-24}" height="{H-24}" fill="{BG}"/>
<text x="210" y="175" text-anchor="middle" font-family="{fam}" font-weight="{wt}" font-size="{size}" fill="#ffffff" letter-spacing="1">스미스씨네 농장</text>
<g transform="translate(-42 150) scale(1.2)"><path d="M210 312 L148 232 A74 74 0 1 1 272 232 Z" fill="{Y}"/><circle cx="210" cy="190" r="54" fill="{BG}"/>
<text x="210" y="216" text-anchor="middle" font-family="Noto Sans KR" font-weight="700" font-size="74" fill="{Y}">P</text></g>
<text x="210" y="660" text-anchor="middle" font-family="Noto Sans KR" font-weight="900" font-size="74" fill="#ffffff" letter-spacing="-1">발렛파킹</text>
<text x="210" y="704" text-anchor="middle" font-family="Noto Sans KR" font-weight="500" font-size="22" fill="#ffffff">Valet Parking</text>
<rect x="70" y="764" width="3" height="72" fill="#ffffff"/>
<text x="86" y="790" font-family="Noto Sans KR" font-weight="500" font-size="23" fill="#ffffff">무료주차 (발렛비 3000원)</text>
<text x="86" y="826" font-family="Noto Sans KR" font-weight="500" font-size="23" fill="#ffffff">입차 / 출차 도와드립니다</text>'''
    html = HEAD.format(w=W, h=H).replace('<style>', f'<link rel="stylesheet" href="{css}"><style>') + \
        f'<div class="page"><svg class="sheet" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}">{art}</svg></div></body></html>'
    open(f'valet_phone_{key}.html', 'w').write(html)
