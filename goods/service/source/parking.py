# Parking guide card 90x50mm (+2mm bleed): front simple map of the two side passages, back logo + address.
from common import *
W, H = 94, 54
def sign(x, y):   # yellow "출차주의" warning sign
    return (f'<path d="M{x} {y-3.4} L{x+3.4} {y+2.4} L{x-3.4} {y+2.4} Z" fill="#f6c343" stroke="{DARK}" stroke-width="0.35" stroke-linejoin="round"/>'
            f'<text x="{x}" y="{y+1.7}" text-anchor="middle" class="k" font-size="3.4" fill="{DARK}">!</text>'
            f'<text x="{x}" y="{y+5.6}" text-anchor="middle" class="b" font-size="2" fill="{DARK}">출차주의</text>')
def arrow(x, y1, y2):
    return (f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2+1.6}" stroke="{ORANGE}" stroke-width="1" stroke-dasharray="1.6 1.1"/>'
            f'<path d="M{x-1.8} {y2+2} L{x} {y2-0.4} L{x+1.8} {y2+2} Z" fill="{ORANGE}"/>')
front = (
    f'<text x="7" y="11.6" class="k" font-size="5.2" fill="{DARK}">주차 안내</text>'
    + f'<circle cx="34.6" cy="9.7" r="2.9" fill="{GREEN}"/><text x="34.6" y="11.1" text-anchor="middle" class="k" font-size="3.8" fill="#ffffff">P</text>'
    + f'<text x="7" y="17" class="n" font-size="2.5" fill="#4a463e">건물 양 옆 <tspan class="b" fill="{DARK}">‘출차주의’ 표지판</tspan> 통로로 들어오세요</text>'
    # road
    + f'<rect x="0" y="38" width="94" height="7" fill="#d9d4c7"/>'
    + f'<line x1="0" y1="41.5" x2="94" y2="41.5" stroke="#ffffff" stroke-width="0.5" stroke-dasharray="3 2"/>'
    + f'<text x="88" y="43.9" text-anchor="end" class="n" font-size="2" fill="#6b6658">도로</text>'
    # side passages
    + f'<rect x="21" y="21.5" width="9" height="16.5" fill="#ece6d8"/><rect x="64" y="21.5" width="9" height="16.5" fill="#ece6d8"/>'
    + arrow(25.5, 37.2, 24.4) + arrow(68.5, 37.2, 24.4)
    + sign(16.4, 27.6) + sign(77.6, 27.6)
    # building
    + f'<rect x="31.5" y="20.4" width="31" height="17.6" rx="1.4" fill="#ffffff" stroke="{GREEN}" stroke-width="0.6"/>'
    + logo(37.2, 22.4, 19.6)
    + f'<text x="47" y="35.9" text-anchor="middle" class="b" font-size="2.2" fill="{DARK}">스미스씨네 농장 건물</text>'
    + f'<text x="47" y="48.6" text-anchor="middle" class="n" font-size="2.1" fill="#4a463e">나오는 차가 있으니 천천히 들어와 주세요 · 부산 해운대구 우동 957-51</text>'
)
back = (
    logo(26, 12.5, 42)
    + f'<text x="47" y="44" text-anchor="middle" class="n" font-size="2.6" fill="#4a463e">010-2901-5663 · @smiths.farm</text>'
)
open('parking.html', 'w').write(doc(W, H, [page(W, H, front, CREAM), page(W, H, back, '#ffffff')]))
