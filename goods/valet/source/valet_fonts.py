# Sheet comparing title fonts on the valet poster: only "스미스씨네 농장" changes; each card also shows the title enlarged.
import re
src = open('valet.py').read()
ns = {}; exec("Y = '#f2c230'; BG = '#1b1b1b'; FR = '#111111'\n" + src[src.index('def art():'):src.index('for name, w, h, bleed')], ns)
base = ns['art']()
TITLE = r'<text x="210" y="74"[^>]*>스미스씨네 농장</text>'
D = 'fonts/dl/'
OPTS = [  # label, family, weight, size, letter-spacing, css, note
    ('주아 (Jua)', 'Jua', 400, 42, 1, D+'fontsource-jua-5.3.0/package/index.css', '둥글고 통통해요. 키즈 프렌들리 느낌이 가장 강해요'),
    ('도현 (Do Hyeon)', 'Do Hyeon', 400, 46, 1, D+'fontsource-do-hyeon-5.3.0/package/index.css', '간판 같은 단정한 고딕이에요. 멀리서도 잘 읽혀요'),
    ('고운바탕 (Gowun Batang)', 'Gowun Batang', 700, 40, 2, 'fonts/batang/package/700.css', '따뜻한 명조체예요. 이탈리안 레스토랑다운 고급스러움'),
    ('개구 (Gaegu)', 'Gaegu', 700, 48, -3, D+'fontsource-gaegu-5.3.0/package/700.css', '손글씨 느낌이에요. 농장·그림일기 감성과 잘 맞아요'),
    ('해바라기 (Sunflower)', 'Sunflower', 700, 42, 1, D+'fontsource-sunflower-5.3.1/package/700.css', '얇고 동글한 고딕이에요. 깔끔하고 세련된 느낌'),
    ('검은고딕 (Black Han Sans)', 'Black Han Sans', 400, 42, 1, D+'fontsource-black-han-sans-5.3.0/package/index.css', '아주 굵고 묵직해요. 발렛파킹 글자와 무게를 맞춘 느낌'),
    ('동글 (Dongle)', 'Dongle', 700, 64, 0, D+'fontsource-dongle-5.3.0/package/700.css', '말랑하고 동글동글해요. 캐릭터 굿즈와 잘 어울려요'),
    ('연성 (Yeon Sung)', 'Yeon Sung', 400, 44, 0, D+'fontsource-yeon-sung-5.3.0/package/index.css', '붓으로 쓴 듯 부드러워요. 정겨운 시골 농장 느낌'),
    ('송명 (Song Myung)', 'Song Myung', 400, 42, 2, D+'fontsource-song-myung-5.3.1/package/index.css', '단단한 옛 명조예요. 클래식하고 신뢰감 있어요'),
    ('나눔손글씨 펜 (Nanum Pen)', 'Nanum Pen Script', 400, 56, 0, D+'fontsource-nanum-pen-script-5.3.0/package/index.css', '펜으로 쓴 손글씨예요. 직접 쓴 메모처럼 친근해요'),
]
css = [o[5] for o in OPTS] + ['fonts/noto/package/korean-900.css', 'fonts/noto/package/korean-700.css', 'fonts/noto/package/korean-500.css', 'fonts/noto/package/latin-500.css', 'fonts/noto/package/latin-700.css']
cards = ''
for i, (label, fam, wt, size, ls, _, note) in enumerate(OPTS, 1):
    t = f'<text x="210" y="76" text-anchor="middle" font-family="{fam}" font-weight="{wt}" font-size="{size}" fill="#ffffff" letter-spacing="{ls}">스미스씨네 농장</text>'
    a = re.sub(TITLE, t, base).replace('class="k"', 'font-family="Noto Sans KR" font-weight="900"')
    z = f'<svg class="z" viewBox="40 22 340 76"><rect x="0" y="0" width="420" height="120" fill="#1b1b1b"/>{t}</svg>'
    cards += f'<div class="c"><svg viewBox="0 0 420 594">{a}</svg>{z}<b>{i}. {label}</b><p>{note}</p></div>'
html = ('<!doctype html><html lang="ko"><head><meta charset="utf-8">' + ''.join(f'<link rel="stylesheet" href="{c}">' for c in css) + '''<style>
body{margin:0;background:#ece8de;font-family:'Noto Sans KR';width:1800px;color:#2a2418}
h1{font-weight:900;font-size:40px;margin:40px 40px 8px} .s{margin:0 40px 28px;color:#6b6658;font-size:20px}
.g{display:grid;grid-template-columns:repeat(5,1fr);gap:40px 24px;padding:0 40px 48px}
.c svg{width:100%;display:block;box-shadow:0 6px 18px rgba(0,0,0,.18)} .c svg.z{margin-top:14px;box-shadow:none;border-radius:6px}
b{display:block;font-size:22px;margin-top:16px} p{margin:6px 0 0;font-size:16px;color:#5b5648;line-height:1.4}
</style></head><body><h1>상단 "스미스씨네 농장" 폰트 시안 10가지</h1><p class="s">나머지(발렛파킹·안내 문구)는 그대로 두고 맨 위 이름만 바꿨어요</p><div class="g">''' + cards + '</div></body></html>')
open('valet_fonts.html', 'w').write(html)
