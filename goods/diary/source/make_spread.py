# A4 landscape "오늘의 그림" spread: the inner page's header boxes side by side on top, one big drawing frame across the sheet.
# Reads the inner page (2쪽) from diary_print.html and writes diary_spread.html next to the given font folder.
import re, sys
src = open(sys.argv[1], encoding='utf-8').read()
out = sys.argv[2]
inner = src.split('<!-- 2쪽: 속지 -->')[1]
def cut(a, b): return inner.split(a)[1].split(b)[0]
date = cut('<!-- 날짜·날씨 -->', '<!-- 오늘 먹은 메뉴 -->')
menu = cut('<!-- 오늘 먹은 메뉴 -->', '<!-- 오늘의 그림 -->')
octo = cut('<!-- 색칠용 문어 -->', '<!-- 제목 -->')
octo = octo.replace('translate(155 231) scale(0.2)', 'translate(268 184) scale(0.24)')
head = src.split('<body>')[0]
head = re.sub(r'@page \{[^}]*\}', '@page { size: 297mm 210mm; margin: 0 }', head)
head = head.replace('.page { width: 154mm; height: 216mm;', '.page { width: 297mm; height: 210mm;')
head = head.replace('svg { display: block; width: 154mm; height: 216mm }', 'svg { display: block; width: 297mm; height: 210mm }')
head = re.sub(r'<title>.*?</title>', '<title>스씨네 그림일기 — 오늘의 그림 A4 가로 한 면</title>', head)
k = 0.83
svg = f'''<div class="page">
<svg viewBox="0 0 297 210" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="0" width="297" height="210" fill="#fdfaf2"/>
  <!-- 날짜·날씨 (왼쪽 위) -->
  <g transform="translate(12 13.7) scale({k}) translate(-14 -14)">{date}</g>
  <!-- 오늘의 메뉴 (오른쪽 위) -->
  <g transform="translate(152.2 12) scale({k}) translate(-14 -33)">{menu}</g>
  <!-- 제목 -->
  <text x="12" y="40" class="sans" font-weight="700" font-size="5" fill="#2a2418">제목</text>
  <line x1="26" y1="40.8" x2="285" y2="40.8" stroke="#2a2418" stroke-width="0.5"/>
  <!-- 오늘의 그림 (가로 한 면 가득) -->
  <path d="M12 199 V68 Q12 51 37 50.5 Q148.5 47.5 260 50.5 Q285 51 285 68 V199 Z" fill="#ffffff" stroke="#2f6b3a" stroke-width="1.3" stroke-linejoin="round"/>
  <path d="M15.5 196 V69 Q15.5 54 38 53.6 Q148.5 50.7 259 53.6 Q281.5 54 281.5 69 V196 Z" fill="none" stroke="#8fb79a" stroke-width="0.35"/>
  <path d="M146.1 48.3 h4.8 l-.6 3.4 h-3.6 Z" fill="#2f6b3a"/>
  <text x="148.5" y="59.4" text-anchor="middle" class="sans" font-weight="700" font-size="4" fill="#2f6b3a">오늘의 그림</text>
  {octo}
</svg>
</div>'''
open(out, 'w', encoding='utf-8').write(head + '<body>\n' + svg + '\n</body>\n</html>\n')
