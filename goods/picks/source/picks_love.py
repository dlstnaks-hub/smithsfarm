# Blind-date / wedding picks, same style as picks.py. Writes picks.html + picks_names.txt for picks_shot.mjs / picks_post.py.
from common import *
PAST = ['#a6d47e', '#f5a660', '#ec8fac', '#b49be0', '#7fc4e6']
def word(text, y, size, start=0, colors=None):
    cols = colors or PAST
    spans = ''.join(f'<tspan fill="{cols[(start+i) % len(cols)]}">{ch}</tspan>' if ch != ' ' else ' ' for i, ch in enumerate(text))
    return (f'<text x="50" y="{y}" text-anchor="middle" class="k" font-size="{size}" letter-spacing="-0.6" '
            f'stroke="{DARK}" stroke-width="{size*0.13:.2f}" stroke-linejoin="round" paint-order="stroke">{spans}</text>')
def heart(x, y, s, c='#f06a8a'):
    return (f'<path transform="translate({x} {y}) scale({s})" d="M0 3 C-4 -1 -9 2 -6 7 L0 13 L6 7 C9 2 4 -1 0 3 Z" '
            f'fill="{c}" stroke="{DARK}" stroke-width="{1.6/s:.2f}" stroke-linejoin="round" paint-order="stroke"/>')
PINK = ['#ec8fac', '#f5a660', '#f06a8a', '#b49be0']
couple = char('carrot', 22, 11, 50) + char('octopus', 47, 23, 36)
PICKS = {
    'chuk_sogaeting': ('축 소개팅', couple + heart(46, 10, 0.9) + word('축 소개팅', 80, 21, 0, PINK)),
    'dugeun':         ('두근두근', char('octopus', 30, 16, 42) + heart(70, 14, 1.1) + heart(78, 30, 0.7) + word('두근두근', 81, 24, 0, PINK)),
    'chuk_gyeolhon':  ('축 결혼', couple + heart(40, 8, 0.8) + heart(52, 4, 0.6) + word('축 결혼', 81, 26, 0, PINK)),
    'gyeolhon':       ('결혼 축하해', couple + heart(46, 10, 0.9) + word('결혼 축하해', 80, 19.5, 0, PINK)),
    'anniv':          ('축 N주년', couple + heart(46, 10, 0.9) + word('축 N주년', 80, 22, 0, PINK)),
}
pages = [f'<div class="page"><svg class="sheet" xmlns="http://www.w3.org/2000/svg" viewBox="-5 -5 110 110">{body}</svg></div>\n' for _, body in PICKS.values()]
html = HEAD.format(w=110, h=110).replace('</style>', 'html,body{background:transparent}</style>') + ''.join(pages) + '</body></html>'
open('picks.html', 'w').write(html)
open('picks_names.txt', 'w').write('\n'.join(f'{k}\t{v[0]}' for k, v in PICKS.items()) + '\n')
