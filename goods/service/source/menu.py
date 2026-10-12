# Large-print menu (A4) for older guests + a request card they can point at instead of asking.
import re
from common import *
W, H = 210, 297
src = open('/home/user/smithsfarm/goods/diary/source/diary_print.html', encoding='utf-8').read()
inner = src.split('<!-- 오늘 먹은 메뉴 -->')[1]
i0 = inner.index('<g transform="translate(-2 0)" fill="none"')
depth, j = 0, i0
for m in re.finditer(r'<g\b|</g>', inner[i0:]):
    depth += 1 if m.group(0) == '<g' else -1
    if depth == 0: j = i0 + m.end(); break
ICONS = inner[i0:j]
def icon(k, x, y, s):          # k: 0 뇨끼 1 피자 2 돌문어 3 단호박 4 파스타
    cx = 97 + 17*k
    return f'<svg x="{x}" y="{y}" width="{s}" height="{s}" viewBox="{cx-5.7} 34.8 11.4 11.4">{ICONS}</svg>'

def header(title, sub):
    return (logo(16, 14, 44) + f'<text x="194" y="27" text-anchor="end" class="k" font-size="12" fill="{DARK}">{title}</text>'
            + f'<text x="194" y="37" text-anchor="end" class="n" font-size="5.2" fill="#5b5648">{sub}</text>'
            + f'<line x1="16" y1="46" x2="194" y2="46" stroke="{GREEN}" stroke-width="1.2"/>')

p1 = header('큰 글씨 메뉴판', '천천히 보시고 편하게 골라 주세요')
for k, name in enumerate(['뇨끼', '피자', '돌문어', '단호박', '파스타']):
    y = 54 + k * 41
    p1 += f'<rect x="16" y="{y}" width="178" height="36" rx="5" fill="{CREAM}"/>'
    p1 += f'<circle cx="37" cy="{y+18}" r="15" fill="#ffffff"/>' + icon(k, 22, y+3, 30)
    p1 += f'<text x="60" y="{y+22.5}" class="k" font-size="12" fill="{DARK}">{name}</text>'
    p1 += f'<line x1="122" y1="{y+24}" x2="176" y2="{y+24}" stroke="#b9b09a" stroke-width="0.6"/><text x="186" y="{y+23.5}" text-anchor="end" class="b" font-size="7" fill="{DARK}">원</text>'
p1 += f'<rect x="16" y="262" width="178" height="21" rx="5" fill="{GREEN}"/>'
p1 += f'<text x="105" y="275.6" text-anchor="middle" class="b" font-size="6.4" fill="#ffffff">주문이 어려우시면 언제든 직원을 불러 주세요</text>'

asks = ['덜 짜게', '덜 맵게', '부드럽게 익혀서', '작게 잘라서', '나눠 담아서', '앞접시 더', '따뜻한 물', '숟가락 · 포크', '아이 의자', '천천히 내 주세요']
p2 = header('이렇게 해 주세요', '원하시는 곳에 표시해서 직원에게 보여 주세요')
for i, a in enumerate(asks):
    x, y = 16 + (i % 2) * 91, 56 + (i // 2) * 30
    p2 += f'<rect x="{x}" y="{y}" width="87" height="25" rx="5" fill="{CREAM}"/>'
    p2 += f'<rect x="{x+6}" y="{y+5.5}" width="14" height="14" rx="2.5" fill="#ffffff" stroke="{DARK}" stroke-width="0.9"/>'
    p2 += f'<text x="{x+26}" y="{y+16.4}" class="b" font-size="{8 if len(a) < 7 else 7}" fill="{DARK}">{a}</text>'
p2 += f'<text x="16" y="219" class="b" font-size="6.4" fill="{DARK}">더 필요하신 것</text>'
for k in range(3):
    p2 += f'<line x1="16" y1="{232+k*13}" x2="194" y2="{232+k*13}" stroke="#b9b09a" stroke-width="0.6"/>'
p2 += char('carrot', 158, 205, 18) + char('octopus', 172, 210, 13.4)
p2 += f'<rect x="16" y="268" width="178" height="15" rx="5" fill="{GREEN}"/>'
p2 += f'<text x="105" y="278" text-anchor="middle" class="b" font-size="5.6" fill="#ffffff">말씀하시기 편하신 대로 해 주셔도 돼요. 천천히 도와 드릴게요</text>'
open('menu.html', 'w').write(doc(W, H, [page(W, H, p1), page(W, H, p2)]))
