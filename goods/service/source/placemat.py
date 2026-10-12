# Kids placemat A3 landscape: colouring scene, maze (carrot -> scarecrow), find-the-octopus count.
import random
from common import *
W, H = 420, 297
rnd = random.Random(7)
S = ''
# header
S += logo(16, 12, 52)
S += f'<text x="80" y="31" class="k" font-size="15" fill="{DARK}">꼬마 손님 놀이판</text>'
S += f'<text x="81" y="40" class="r" font-weight="700" font-size="5" fill="{GREEN}" letter-spacing="2.4">PLAY &amp; COLOR</text>'
for i, lab in enumerate(('이름', '나이')):
    x = 268 + i * 82
    S += f'<text x="{x}" y="33" class="b" font-size="6" fill="{DARK}">{lab}</text><line x1="{x+15}" y1="34.5" x2="{x+(70 if i==0 else 52)}" y2="34.5" stroke="{DARK}" stroke-width="0.6"/>'
S += f'<text x="{268+82+56}" y="33" class="b" font-size="6" fill="{DARK}">살</text>' if False else ''
# panel helper
def panel(x, y, w, h, title, sub):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="#ffffff" stroke="{GREEN}" stroke-width="1.4"/>'
            f'<rect x="{x+8}" y="{y-6}" width="{len(title)*6.6+14}" height="12" rx="6" fill="{GREEN}"/>'
            f'<text x="{x+15}" y="{y+2.2}" class="b" font-size="6.2" fill="#ffffff">{title}</text>'
            f'<text x="{x+w-8}" y="{y+11}" text-anchor="end" class="n" font-size="4.4" fill="#6b6658">{sub}</text>')
# colouring scene
px, py, pw, ph = 16, 56, 214, 226
S += panel(px, py, pw, ph, '색칠해 보세요', '당근 · 문어 · 허수아비를 예쁘게 칠해 줘요')
S += f'<g fill="none" stroke="{DARK}" stroke-width="1.1" stroke-linecap="round">'
S += '<circle cx="196" cy="92" r="13" fill="#ffffff"/>' + ''.join(
    f'<line x1="{196+17*c:.1f}" y1="{92+17*s:.1f}" x2="{196+23*c:.1f}" y2="{92+23*s:.1f}"/>'
    for c, s in [(1,0),(.71,.71),(0,1),(-.71,.71),(-1,0),(-.71,-.71),(0,-1),(.71,-.71)])
def cloud(x, y, k):
    return f'<path transform="translate({x} {y}) scale({k})" fill="#ffffff" d="M0 10 a7 7 0 0 1 8 -9 a10 10 0 0 1 18 -1 a8 8 0 0 1 14 6 a6 6 0 0 1 -2 12 h-34 a6 6 0 0 1 -4 -8 Z"/>'
S += cloud(40, 80, 1.1) + cloud(118, 74, 0.8)
S += '<path d="M24 236 Q70 226 120 234 T222 230"/><path d="M24 252 Q80 244 130 252 T222 246" stroke-width="0.7"/>'
S += '</g>'
S += char('scarecrow', 28, 138, 112, line=True) + char('carrot', 112, 128, 120, line=True) + char('octopus', 150, 168, 78, line=True)
for x in (36, 98, 196):
    S += char('carrot', x, 252, 22, line=True)
# maze
mx, my, mw, mh = 244, 56, 160, 112
S += panel(mx, my, mw, mh, '미로 찾기', '당근이 허수아비 친구를 만나러 가요')
C, R, cs = 12, 7, 11.2
ox, oy = mx + (mw - C*cs)/2 + 2, my + 18
seen = {(0, 0)}; stack = [(0, 0)]; opened = set()
while stack:
    c, r = stack[-1]
    nb = [(c+dc, r+dr) for dc, dr in ((1,0),(-1,0),(0,1),(0,-1)) if 0 <= c+dc < C and 0 <= r+dr < R and (c+dc, r+dr) not in seen]
    if not nb: stack.pop(); continue
    n = rnd.choice(nb); opened.add(frozenset([(c, r), n])); seen.add(n); stack.append(n)
walls = []
for r in range(R):
    for c in range(C):
        x, y = ox + c*cs, oy + r*cs
        if r == 0: walls.append((x, y, x+cs, y))
        if c == 0 and r != 0: walls.append((x, y, x, y+cs))
        if c == C-1 and r != R-1: walls.append((x+cs, y, x+cs, y+cs))
        if r == R-1: walls.append((x, y+cs, x+cs, y+cs))
        if c < C-1 and frozenset([(c, r), (c+1, r)]) not in opened: walls.append((x+cs, y, x+cs, y+cs))
        if r < R-1 and frozenset([(c, r), (c, r+1)]) not in opened: walls.append((x, y+cs, x+cs, y+cs))
S += f'<g stroke="{DARK}" stroke-width="1" stroke-linecap="round">' + ''.join(f'<line x1="{a:.2f}" y1="{b:.2f}" x2="{c:.2f}" y2="{d:.2f}"/>' for a, b, c, d in walls) + '</g>'
S += char('carrot', ox - 9, oy - 1, 13) + char('scarecrow', ox + C*cs + 0.6, oy + (R-1)*cs - 2.5, 14)
S += f'<text x="{ox-5}" y="{oy+18}" text-anchor="middle" class="b" font-size="3.4" fill="{ORANGE}">출발</text>'
S += f'<text x="{ox+C*cs+7}" y="{oy+(R-1)*cs-4}" text-anchor="middle" class="b" font-size="3.4" fill="{GREEN}">도착</text>'
# find the octopus
fx, fy, fw, fh = 244, 182, 160, 100
S += panel(fx, fy, fw, fh, '숨은 문어 찾기', '문어는 모두 몇 마리일까요?')
cols, rows = 9, 4
cells = ['octopus'] * 9 + ['carrot'] * 14 + ['scarecrow'] * 13
rnd.shuffle(cells)
gx, gy, gw, gh = fx + 9, fy + 17, (fw - 18) / cols, (fh - 30) / rows
for i, nm in enumerate(cells):
    c, r = i % cols, i // cols
    h = {'octopus': 11, 'carrot': 14, 'scarecrow': 14}[nm] * rnd.uniform(0.85, 1.0)
    x = gx + c*gw + gw/2 - char_w(nm, h)/2 + rnd.uniform(-1.5, 1.5); y = gy + r*gh + gh/2 - h/2 + rnd.uniform(-1.2, 1.2)
    S += char(nm, x, y, h, line=True)
S += f'<text x="{fx+12}" y="{fy+fh-5}" class="b" font-size="5" fill="{DARK}">정답:</text><rect x="{fx+27}" y="{fy+fh-11}" width="16" height="8.5" rx="2" fill="none" stroke="{DARK}" stroke-width="0.5"/><text x="{fx+45}" y="{fy+fh-5}" class="b" font-size="5" fill="{DARK}">마리</text>'
S += f'<text transform="translate({fx+fw-9} {fy+fh-8}) rotate(180)" class="n" font-size="3" fill="#9b9483">정답 9마리</text>'
S += f'<text x="{W/2}" y="{H-6}" text-anchor="middle" class="n" font-size="4" fill="#8a8473">해운대 동백역 · 스미스씨네 농장 · 다 그린 그림은 직원에게 보여 주세요!</text>'
open('placemat.html', 'w').write(doc(W, H, [page(W, H, S, '#ffffff')]))
