# Illustrated sheet of quick (1-2 min) complimentary dishes, flat style matching the store prints. Output: dishes.html
PLATE = '<ellipse cx="60" cy="47" rx="50" ry="22" fill="#ddd6c6"/><ellipse cx="60" cy="44" rx="50" ry="22" fill="#ffffff"/><ellipse cx="60" cy="44" rx="40" ry="16" fill="none" stroke="#efe9dc" stroke-width="1.2"/>'
SMALL = '<ellipse cx="60" cy="58" rx="40" ry="10" fill="#ddd6c6"/><ellipse cx="60" cy="56" rx="40" ry="10" fill="#ffffff"/>'
def crackle(x, y, w):
    return f'<path d="M{x} {y} l{w*.25} -1.4 l{w*.2} 1.6 l{w*.25} -1.2 l{w*.2} 1.1" fill="none" stroke="#7a3d0e" stroke-width="0.6" stroke-linecap="round" opacity="0.6"/>'
MINT = lambda x, y: f'<path d="M{x} {y} q3 -5 7 -3 q-2 5 -7 3 Z M{x} {y} q-1 -6 3 -8 q2 5 -3 8 Z" fill="#4f8a3c"/>'
D = {}
D['banana'] = PLATE + ''.join(
    f'<g transform="rotate({r} 60 44)"><path d="M24 {y} C34 {y-9} 86 {y-9} 96 {y} C86 {y+6} 34 {y+6} 24 {y} Z" fill="#f6e3a1"/>'
    f'<path d="M27 {y-1} C38 {y-8} 82 {y-8} 93 {y-1} C82 {y+2} 38 {y+2} 27 {y-1} Z" fill="#d98a2b"/>'
    f'<path d="M34 {y-3} C46 {y-7} 74 {y-7} 86 {y-3}" stroke="#f3b45a" stroke-width="1.6" fill="none" stroke-linecap="round"/>{crackle(40, y-2.4, 36)}</g>'
    for r, y in ((-4, 40), (4, 50))) + MINT(88, 30)
D['pumpkin'] = SMALL + '<ellipse cx="60" cy="44" rx="27" ry="13" fill="#ffffff"/><rect x="33" y="30" width="54" height="16" fill="#ffffff"/><ellipse cx="60" cy="30" rx="27" ry="10" fill="#f3f0ea"/>' \
    '<ellipse cx="60" cy="30" rx="23" ry="8" fill="#c9701d"/><ellipse cx="56" cy="28.5" rx="12" ry="3.5" fill="#e7943a"/>' \
    '<circle cx="66" cy="31" r="1.4" fill="#8a4512"/><circle cx="52" cy="32" r="1" fill="#8a4512"/>' + crackle(48, 29, 22) + \
    '<path d="M33 34 v10 M87 34 v10" stroke="#e6e0d3" stroke-width="1"/>' + \
    '<path d="M92 48 q4 -6 10 -3 q-3 7 -10 3 Z" fill="#4f7d3a"/><path d="M96 44 q1 -4 4 -5" stroke="#7a5230" stroke-width="1.4" fill="none" stroke-linecap="round"/>'
D['fig'] = PLATE + ''.join(
    f'<g transform="translate({x} {y})"><ellipse cx="0" cy="0" rx="13" ry="10" fill="#6b2f4d"/><ellipse cx="0" cy="-1" rx="10.5" ry="7.6" fill="#e58a8a"/>'
    f'<ellipse cx="0" cy="-1" rx="6" ry="4.4" fill="#c4473a"/><ellipse cx="-1" cy="-3" rx="7" ry="2.4" fill="#c06a1c" opacity="0.75"/>'
    + ''.join(f'<circle cx="{dx}" cy="{dy}" r="0.6" fill="#f6dfa6"/>' for dx, dy in ((-2, 0), (1.5, -1), (0, 1.5), (2.5, 1), (-3, -1.5))) + '</g>'
    for x, y in ((44, 42), (70, 47))) + '<path d="M78 34 q6 -5 12 -1 q4 5 -2 8 q-7 3 -11 -1 q-3 -3 1 -6 Z" fill="#fbf8f1" stroke="#e8e2d4" stroke-width="0.7"/>' \
    '<path d="M36 34 C48 30 60 52 82 40" stroke="#e8b84a" stroke-width="1.4" fill="none" stroke-linecap="round"/>' + MINT(30, 52)
D['tiramisu'] = SMALL + '<path d="M44 14 h32 l-3 44 h-26 Z" fill="#f6f1e6" opacity="0.6" stroke="#d9d2c3" stroke-width="0.8"/>' \
    '<path d="M45.6 34 h28.8 l-0.9 13 h-27 Z" fill="#8a5a36"/><path d="M45 24 h30 l-0.6 10 h-28.8 Z" fill="#fbf3dd"/>' \
    '<path d="M46.4 47 h27.2 l-0.8 10 h-25.6 Z" fill="#fbf3dd"/><path d="M45.6 34 h28.8" stroke="#5e3a22" stroke-width="1"/>' \
    '<path d="M44.8 22 q15 -4 30.4 0 v3 h-30.4 Z" fill="#6b3f22"/>' + ''.join(f'<circle cx="{48+i*3.1}" cy="{21.6+(i%2)*0.6}" r="0.5" fill="#4a2a16"/>' for i in range(9)) + \
    '<rect x="80" y="20" width="3" height="34" rx="1.5" fill="#c9c4b8" transform="rotate(14 81 37)"/><ellipse cx="85" cy="19" rx="3.4" ry="5" fill="#d9d4c8" transform="rotate(14 85 19)"/>'
D['pannacotta'] = SMALL + '<path d="M38 54 C38 30 46 22 60 22 C74 22 82 30 82 54 Z" fill="#fbf7ee"/><path d="M42 50 C42 32 48 26 56 25" stroke="#ffffff" stroke-width="2.4" fill="none" stroke-linecap="round"/>' \
    '<path d="M44 30 C48 22 72 22 76 30 C76 36 74 33 72 38 C70 42 69 34 66 36 C63 38 63 44 60 41 C57 38 57 34 54 37 C51 40 50 35 48 37 C46 39 44 34 44 30 Z" fill="#c4304a"/>' \
    + ''.join(f'<circle cx="{x}" cy="{y}" r="3" fill="#8e1f3a"/><circle cx="{x-0.8}" cy="{y-0.9}" r="0.8" fill="#e46a7f"/>' for x, y in ((54, 23), (63, 21.5), (59, 26))) + MINT(66, 22)
D['affogato'] = SMALL + '<path d="M40 26 h40 l-4 30 h-32 Z" fill="#f6f1e6" opacity="0.7" stroke="#d9d2c3" stroke-width="0.8"/>' \
    '<path d="M41.5 40 h37 l-2.3 16 h-32.4 Z" fill="#6b3f22"/><ellipse cx="60" cy="40" rx="18.5" ry="3" fill="#8a5a36"/>' \
    '<path d="M46 40 C44 28 52 22 60 22 C68 22 76 28 74 40 Z" fill="#fbf3dd"/><path d="M50 30 q4 -6 10 -6" stroke="#ffffff" stroke-width="2" fill="none" stroke-linecap="round"/>' \
    '<path d="M64 24 C66 30 63 34 66 40" stroke="#6b3f22" stroke-width="2.4" fill="none" stroke-linecap="round"/>' \
    '<path d="M84 10 h12 l-1 12 h-10 Z" fill="#ffffff" stroke="#c9c4b8" stroke-width="0.8" transform="rotate(-35 90 16)"/><path d="M82 18 q-10 2 -16 8" stroke="#6b3f22" stroke-width="2" fill="none" stroke-linecap="round"/>'
D['focaccia'] = PLATE + '<g transform="rotate(-6 46 42)"><rect x="24" y="28" width="42" height="28" rx="6" fill="#c98b3c"/><rect x="25" y="27" width="40" height="26" rx="5" fill="#e9b85c"/>' \
    + ''.join(f'<ellipse cx="{x}" cy="{y}" rx="2" ry="1.4" fill="#c98b3c"/>' for x, y in ((32, 33), (44, 32), (56, 34), (36, 43), (50, 42), (60, 46), (30, 48))) + \
    '<path d="M38 36 l4 -3 M40 37 l4 -1 M52 39 l3 -4 M54 40 l4 -2" stroke="#4f7d3a" stroke-width="1" stroke-linecap="round"/><circle cx="46" cy="47" r="1" fill="#fff"/><circle cx="33" cy="39" r="0.9" fill="#fff"/></g>' \
    '<ellipse cx="84" cy="46" rx="13" ry="7" fill="#e6e0d3"/><ellipse cx="84" cy="44.5" rx="13" ry="6.5" fill="#ffffff"/><ellipse cx="84" cy="44.5" rx="10" ry="4.6" fill="#c9b03a"/>' \
    '<ellipse cx="85" cy="44.5" rx="3.2" ry="1.6" fill="#4a2a16"/><ellipse cx="81" cy="43.4" rx="2.5" ry="0.8" fill="#e8d36a"/>'
D['bruschetta'] = PLATE + ''.join(
    f'<g transform="rotate({r} {x} 42)"><path d="M{x-17} 42 C{x-17} 33 {x+17} 33 {x+17} 42 C{x+17} 50 {x-17} 50 {x-17} 42 Z" fill="#c98b3c"/>'
    f'<path d="M{x-15} 41.5 C{x-15} 35 {x+15} 35 {x+15} 41.5 C{x+15} 47 {x-15} 47 {x-15} 41.5 Z" fill="#f0cf8a"/>'
    + ''.join(f'<rect x="{x+dx}" y="{37+dy}" width="4.2" height="3.6" rx="0.9" fill="#d23b2e" transform="rotate({dx*7} {x+dx} {37+dy})"/>' for dx, dy in ((-11, 2), (-6, 0), (-1, 3), (4, 0.5), (8, 3), (-8, 5), (1, 6), (6, 5.6)))
    + f'<path d="M{x-3} 39 q3 -4 7 -2 q-3 4 -7 2 Z" fill="#3f7d34"/></g>' for x, r in ((42, -8), (78, 6)))
D['skewer'] = PLATE + '<rect x="18" y="42.6" width="80" height="1.6" rx="0.8" fill="#c8a36a" transform="rotate(-10 60 44)"/>' \
    '<g transform="rotate(-10 60 44)"><path d="M98 43.4 l7 -5 l0 10 Z" fill="#f5821f"/><path d="M104 40 q3 -4 6 -2 M104 43.4 q4 -1 6 1 M104 46.5 q3 3 6 2" stroke="#2f6b3a" stroke-width="1.6" fill="none" stroke-linecap="round"/>' \
    '<ellipse cx="32" cy="43.4" rx="5" ry="6" fill="#f6e7b0" stroke="#e2cd84" stroke-width="0.8"/><circle cx="32" cy="43.4" r="1.4" fill="#e2cd84"/>' \
    '<path d="M42 37 C50 36 52 44 47 50 C44 53 40 50 39 46 C38 42 38 38 42 37 Z" fill="#e0353e"/><path d="M41 37 q2 -3 5 -1" stroke="#3f7d34" stroke-width="1.6" fill="none"/>' \
    + ''.join(f'<circle cx="{x}" cy="{44+dy}" r="0.45" fill="#ffe9a8"/>' for x, dy in ((43, 2), (45, -2), (46, 3), (42, -1))) + \
    '<circle cx="58" cy="43.4" r="6" fill="#86b84a"/><circle cx="56" cy="41.5" r="1.6" fill="#b6dc7a"/>' \
    '<circle cx="71" cy="43.4" r="6" fill="#6b2f6b"/><circle cx="69" cy="41.5" r="1.6" fill="#a065a0"/>' \
    '<ellipse cx="84" cy="43.4" rx="5" ry="6" fill="#f6e7b0" stroke="#e2cd84" stroke-width="0.8"/><circle cx="84" cy="43.4" r="1.4" fill="#e2cd84"/></g>'
D['babycappu'] = '<ellipse cx="60" cy="48" rx="40" ry="17" fill="#ddd6c6"/><ellipse cx="60" cy="46" rx="40" ry="17" fill="#ffffff"/>' \
    '<path d="M92 38 q12 0 10 8 q-2 6 -12 4" fill="none" stroke="#f1ece2" stroke-width="4"/>' \
    '<ellipse cx="60" cy="40" rx="30" ry="15" fill="#f1ece2"/><ellipse cx="60" cy="39" rx="26" ry="12.6" fill="#d9b48c"/><ellipse cx="60" cy="39" rx="23" ry="11" fill="#fbf6ec"/>' \
    '<g fill="none" stroke="#8a5a36" stroke-width="1.3" stroke-linecap="round"><ellipse cx="60" cy="36" rx="8" ry="5.4"/><path d="M54 40 q-2 4 -5 3 M58 41 q-1 4 -3 5 M62 41 q1 4 3 5 M66 40 q2 4 5 3"/></g>' \
    '<circle cx="57.4" cy="35.6" r="0.9" fill="#8a5a36"/><circle cx="62.6" cy="35.6" r="0.9" fill="#8a5a36"/><path d="M58.6 38 q1.4 1 2.8 0" stroke="#8a5a36" stroke-width="0.7" fill="none"/>'
ITEMS = [
    ('banana', '바나나 브륄레', '30초', '지금 주력 메뉴 · 반 갈라 설탕 뿌리고 토치', True),
    ('pumpkin', '단호박 브륄레', '1분', '단호박 퓌레를 미리 종지에 · 설탕 + 토치', False),
    ('fig', '구운 무화과 & 리코타', '1분', '반 갈라 토치로 굽고 리코타·꿀 · 여름엔 복숭아', False),
    ('tiramisu', '미니 티라미수 컵', '30초', '전날 소주잔 컵에 만들어 두고 코코아만', False),
    ('pannacotta', '파나코타 한 스푼', '30초', '미리 굳혀 두고 베리 소스만 올리기', False),
    ('affogato', '미니 아포가토', '1분', '아이스크림 + 에스프레소 · 아이는 초코 시럽', False),
    ('focaccia', '포카치아 & 올리브오일', '1분', '피자 반죽으로 구워 두고 데우기 · 식전 서비스', False),
    ('bruschetta', '브루스케타 한 입', '1분', '토마토·바질 미리 썰어 두고 바게트에 올리기', False),
    ('skewer', '꼬마 과일 꼬치', '1분', '바나나·딸기·포도 + 당근 모양 픽 · 아이 전용', False),
    ('babycappu', '아기 카푸치노', '1분', '우유 거품 위에 코코아로 문어 얼굴 · 아이 전용', False),
]
cards = ''
for key, name, t, how, star in ITEMS:
    badge = '<span class="star">대표 메뉴</span>' if star else ''
    cards += f'''<div class="card{' main' if star else ''}"><svg viewBox="0 0 120 70">{D[key]}</svg>
<div class="t"><b>{name}</b>{badge}<span class="time">⏱ {t}</span></div><p>{how}</p></div>'''
html = f'''<!doctype html><html lang="ko"><head><meta charset="utf-8">
<link rel="stylesheet" href="fonts/noto/package/korean-400.css"><link rel="stylesheet" href="fonts/noto/package/korean-700.css"><link rel="stylesheet" href="fonts/noto/package/korean-900.css">
<link rel="stylesheet" href="fonts/noto/package/latin-400.css"><link rel="stylesheet" href="fonts/noto/package/latin-700.css">
<style>
body{{margin:0;background:#f3efe4;font-family:'Noto Sans KR',sans-serif;color:#2a2418;width:1080px}}
h1{{font-weight:900;font-size:46px;margin:0}} .sub{{color:#6b6658;font-size:22px;margin:8px 0 0}}
header{{padding:48px 48px 28px}}
.grid{{display:grid;grid-template-columns:1fr 1fr;gap:22px;padding:0 48px 48px}}
.card{{background:#fff;border-radius:22px;padding:14px 22px 22px;box-shadow:0 4px 14px rgba(60,50,30,.08)}}
.card.main{{outline:3px solid #f5821f}}
.card svg{{width:100%;display:block;background:#faf7f0;border-radius:14px}}
.t{{display:flex;align-items:center;gap:10px;margin-top:14px}} .t b{{font-size:27px;font-weight:900}}
.time{{margin-left:auto;background:#2f6b3a;color:#fff;border-radius:99px;padding:3px 13px;font-size:19px;font-weight:700;white-space:nowrap}}
.star{{background:#f5821f;color:#fff;border-radius:99px;padding:2px 10px;font-size:16px;font-weight:700}}
p{{margin:8px 0 0;font-size:19px;color:#5b5648;line-height:1.45}}
</style></head><body><header><h1>1~2분 서비스 메뉴 아이디어</h1><p class="sub">스미스씨네 농장 · 미리 준비해 두고 주문이 들어오면 굽거나 담기만 해요</p></header>
<div class="grid">{cards}</div></body></html>'''
open('dishes.html', 'w').write(html)
