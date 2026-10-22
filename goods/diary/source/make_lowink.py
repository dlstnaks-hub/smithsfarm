# Ink-saving version of the diary: cover keeps its coloured text but everything else becomes white line art to colour in;
# the inner page loses its cream background. usage: make_lowink.py <diary_print.html> <out.html>
import re, sys
src = open(sys.argv[1], encoding='utf-8').read()
cover, rest = src.split('<!-- 2쪽: 속지 -->')
D = '#2a2418'
# background, spine
cover = cover.replace('<rect x="-6" y="-6" width="200" height="275" fill="#d8c095"/>', '<rect x="-6" y="-6" width="200" height="275" fill="#ffffff"/>')
cover = cover.replace('<rect x="-6" y="-6" width="17" height="275" fill="#c6a973"/>', '')
cover = cover.replace('<rect x="11" y="-6" width="0.4" height="275" fill="#b69660"/>', '')
# arch window and hills: outline only
cover = cover.replace('fill="#fdf8ee" stroke="#2f6b3a" stroke-width="3.2"', f'fill="#ffffff" stroke="{D}" stroke-width="1.3"')
cover = cover.replace('fill="#4f8a5b"/>', f'fill="#ffffff" stroke="{D}" stroke-width="0.8"/>')
cover = re.sub(r'<path d="M40 196[^>]*opacity="0.55"/>', '<path d="M40 199 C58 195 72 200 90 197 C108 194 124 200 156 196" fill="none" stroke="#2a2418" stroke-width="0.6"/>', cover)
# octopus: legs as hollow tubes, head/hat/cheeks outlined, small dark pupils kept
legs = re.search(r'<g fill="none" stroke="#b5482a" stroke-width="10" stroke-linecap="round">(.*?)</g>', cover, re.S)
cover = cover.replace(legs.group(0), f'<g fill="none" stroke-linecap="round"><g stroke="{D}" stroke-width="12.4">{legs.group(1)}</g><g stroke="#ffffff" stroke-width="9.6">{legs.group(1)}</g></g>')
cover = cover.replace('fill="url(#head)"/>', f'fill="#ffffff" stroke="{D}" stroke-width="1.4"/>')
cover = cover.replace('Q46 21 33 28 Z" fill="#2f6b3a"/>', f'Q46 21 33 28 Z" fill="#ffffff" stroke="{D}" stroke-width="1.4" stroke-linejoin="round"/>')
cover = cover.replace('r="2.6" fill="#24532d"/>', f'r="2.6" fill="#ffffff" stroke="{D}" stroke-width="1.2"/>')
for cx in ('47', '73'):
    cover = cover.replace(f'<circle cx="{cx}" cy="48" r="6.4" fill="#ffffff"/>', f'<circle cx="{cx}" cy="48" r="6.4" fill="#ffffff" stroke="{D}" stroke-width="1.2"/>')
cover = cover.replace('fill="#f2a08a" opacity="0.8"/>', f'fill="none" stroke="{D}" stroke-width="0.8" stroke-dasharray="1.6 1.2"/>')
# bottom band: green bar becomes a green rule, the text keeps the green colour
cover = cover.replace('<rect x="-6" y="232" width="200" height="37" fill="#2f6b3a"/>', '<line x1="40" y1="236" x2="156" y2="236" stroke="#2f6b3a" stroke-width="0.8"/>')
cover = cover.replace('font-size="6" fill="#ffffff" letter-spacing="0.2">해운대', 'font-size="6" fill="#2f6b3a" letter-spacing="0.2">해운대')
# inner page: white paper
rest = rest.replace('fill="#fdfaf2"/>', 'fill="#ffffff"/>', 1)
open(sys.argv[2], 'w', encoding='utf-8').write(cover + '<!-- 2쪽: 속지 -->' + rest)
