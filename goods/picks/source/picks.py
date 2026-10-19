# Celebration spring picks: keyring characters + a pastel word with dark outline (style of the elephant "축하해" pick).
# Writes picks.html, one 100x100mm transparent page per pick; picks_post.py adds the black border and the cut line.
from common import *
PAST = ['#a6d47e', '#f5a660', '#ec8fac', '#b49be0', '#7fc4e6']
def word(text, y, size, start=0):
    spans = ''.join(f'<tspan fill="{PAST[(start+i) % len(PAST)]}">{ch}</tspan>' if ch != ' ' else ' ' for i, ch in enumerate(text))
    return (f'<text x="50" y="{y}" text-anchor="middle" class="k" font-size="{size}" letter-spacing="-0.6" '
            f'stroke="{DARK}" stroke-width="{size*0.13:.2f}" stroke-linejoin="round" paint-order="stroke">{spans}</text>')
def centred(name, h, y, dx=0):
    return char(name, 50 - char_w(name, h)/2 + dx, y, h)
PICKS = {
    'chukhahae':   ('축하해',     centred('octopus', 46, 13) + word('축하해', 82, 27, 0)),
    'saengil':     ('생일 축하해', centred('carrot', 50, 13) + word('생일 축하해', 80, 19.5, 1)),
    'gomawoyo':    ('고마워요',    centred('scarecrow', 52, 10) + word('고마워요', 82, 24, 2)),
    'saranghae':   ('사랑해',     char('carrot', 24, 11, 50) + char('octopus', 46, 23, 36) + word('사랑해', 82, 27, 2)),
}
pages = [f'<div class="page"><svg class="sheet" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">{body}</svg></div>\n' for _, body in PICKS.values()]
html = HEAD.format(w=100, h=100).replace('</style>', 'html,body{background:transparent}</style>') + ''.join(pages) + '</body></html>'
open('picks.html', 'w').write(html)
open('picks_names.txt', 'w').write('\n'.join(f'{k}\t{v[0]}' for k, v in PICKS.items()))
