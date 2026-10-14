# Stamp card 90x50mm (+2mm bleed = 94x54): front logo + characters, back 6 stamp slots with rewards at 3 and 6.
from common import *
W, H = 94, 54
front = (
    logo(7.5, 8.5, 31)
    + f'<text x="7.5" y="35.2" class="k" font-size="6.6" fill="{DARK}" letter-spacing="0.2">스탬프 카드</text>'
    + f'<text x="7.8" y="40.6" class="r" font-weight="700" font-size="2.9" fill="{GREEN}" letter-spacing="0.9">STAMP CARD</text>'
    + char('scarecrow', 45.2, 19.5, 21) + char('carrot', 61.2, 17.6, 23) + char('octopus', 70.4, 22.5, 17.2)
    + f'<line x1="7.5" y1="46.6" x2="86.5" y2="46.6" stroke="#cfc8b6" stroke-width="0.25"/>'
    + f'<text x="7.5" y="45.2" class="n" font-size="2.6" fill="#6b6658">이름</text>'
    + f'<text x="86.5" y="45.2" text-anchor="end" class="n" font-size="2.3" fill="#6b6658">해운대 동백역 · 스미스씨네 농장</text>'
)
order = ['carrot', 'octopus', 'scarecrow', 'carrot', 'octopus', 'scarecrow']
slots = ''
for i, nm in enumerate(order):
    cx, cy = 14.6 + (i % 3) * 13.4, 20.6 + (i // 3) * 14.2
    reward = i in (2, 5)
    slots += f'<circle cx="{cx}" cy="{cy}" r="5.3" fill="#ffffff" stroke="{ORANGE if reward else "#cfc8b6"}" stroke-width="{0.7 if reward else 0.35}"/>'
    h = 7.0 if nm != 'octopus' else 5.8
    slots += char(nm, cx - char_w(nm, h)/2, cy - h/2, h, opacity=0.16)
    slots += f'<text x="{cx}" y="{cy+7.9}" text-anchor="middle" class="r" font-weight="700" font-size="2.0" fill="{ORANGE if reward else "#9b9483"}">{i+1}</text>'
back = (
    f'<text x="8.7" y="11.6" class="k" font-size="4.4" fill="{DARK}">도장을 모아 주세요!</text>'
    + slots
    + f'<rect x="54" y="15.6" width="33" height="29.6" rx="2.4" fill="{CREAM}"/>'
    + f'<text x="57" y="22.4" class="b" font-size="2.9" fill="{ORANGE}">도장 3개</text>'
    + f'<text x="57" y="26.6" class="n" font-size="2.6" fill="{DARK}">음료 1잔 서비스</text>'
    + f'<line x1="57" y1="30" x2="84" y2="30" stroke="#d9d1bd" stroke-width="0.25"/>'
    + f'<text x="57" y="35.2" class="b" font-size="2.9" fill="{ORANGE}">도장 6개</text>'
    + f'<text x="57" y="39.4" class="n" font-size="2.6" fill="{DARK}">키링 1개 선물</text>'
    + f'<text x="57" y="42.8" class="n" font-size="2.1" fill="#6b6658">당근 · 문어 · 허수아비 중 하나</text>'
    + f'<text x="8.7" y="49.0" class="n" font-size="2.1" fill="#8a8473">방문 1회 · 1테이블에 도장 1개를 찍어 드려요</text>'
)
open('stamp.html', 'w').write(doc(W, H, [page(W, H, front, CREAM), page(W, H, back, '#ffffff')]))
