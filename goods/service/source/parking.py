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
STORE = (
    '<rect x="0" y="0" width="100" height="57" rx="2" fill="#f7f4ec" stroke="#cfc8b6" stroke-width="0.8"/>'
    # wall texture dots
    + ''.join(f'<circle cx="{(i*37)%97+1.5}" cy="{(i*23)%53+2}" r="0.45" fill="#e3ddcf"/>' for i in range(70))
    # wall lamp + light
    + '<ellipse cx="73.5" cy="25" rx="7" ry="4.5" fill="#fff3cf" opacity="0.9"/><path d="M71.6 19.6 h3.8 l-0.5 4 h-2.8 Z" fill="#26261f"/>'
    # posters
    + ''.join(f'<rect x="{x}" y="28.5" width="11" height="14.5" fill="#1d1d1b"/><rect x="{x+0.8}" y="29.3" width="9.4" height="12.9" fill="#ffffff"/>'
              f'<rect x="{x+1.6}" y="31.1" width="7.8" height="1.2" fill="#2a2418"/>'
              + char(nm, x + 5.5 - char_w(nm, h)/2, 41.6 - h, h)
              for x, nm, h in ((58.5, 'scarecrow', 8.6), (72, 'carrot', 8.8), (85.5, 'octopus', 7.2)))
    # door frame, glass, handles
    + '<rect x="14" y="21" width="33" height="31" fill="#1d1d1b"/>'
    + '<rect x="17.5" y="24" width="12.6" height="27" fill="#4b5a57"/><rect x="31" y="24" width="12.6" height="27" fill="#4b5a57"/>'
    + '<path d="M18.5 50 L27 25 h3 L21.5 50 Z M32 50 L40.5 25 h2 L34.5 50 Z" fill="#ffffff" opacity="0.13"/>'
    + '<rect x="28.6" y="38" width="0.7" height="4" fill="#c9c4b8"/><rect x="31.8" y="38" width="0.7" height="4" fill="#c9c4b8"/>'
    # step
    + '<rect x="12.5" y="52" width="36" height="3.4" fill="#d8d3c8"/><rect x="15" y="53.2" width="31" height="0.7" fill="#3a3a35"/>'
    # dome awning with ribs, band, scallops
    + '<path d="M9.5 20 C9.5 3.5 51.5 3.5 51.5 20 Z" fill="#1f5c4b"/>'
    + ''.join(f'<path d="M30.5 6.6 Q{30.5+dx*0.55:.1f} 12 {30.5+dx:.1f} 20" fill="none" stroke="#17483a" stroke-width="0.45"/>' for dx in (-17, -11, -5.5, 0, 5.5, 11, 17))
    + '<path d="M8.6 19.6 H52.6 L53 25.2 H8.2 Z" fill="#1f5c4b"/>'
    + ''.join(f'<path d="M{8.2+i*2.9:.1f} 25.2 a1.45 1.45 0 0 0 2.9 0" fill="#1f5c4b" stroke="#ffffff" stroke-width="0.45"/>' for i in range(16))
    + '<text x="30.6" y="23.9" text-anchor="middle" font-family="Noto Sans KR, sans-serif" font-weight="700" font-size="3.6" fill="#ffffff" letter-spacing="0.2">PIZZA &amp; PASTA</text>'
    # name on the wall
    + f'<text x="77.5" y="11.6" text-anchor="middle" font-family="Noto Sans KR, sans-serif" font-weight="700" font-size="5.4" fill="{GREEN}">스미스씨네 농장</text>'
    + '<text x="77.5" y="17" text-anchor="middle" font-family="Quicksand, sans-serif" font-weight="700" font-size="3.2" fill="#8a8473" letter-spacing="0.6">PIZZA &amp; PASTA</text>'
)
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
    # storefront (drawn after the photo: dome awning, black door frame, three posters, wall lamp)
    + f'<g transform="translate(31 19.6) scale(0.32)">{STORE}</g>'
    + f'<text x="47" y="48.6" text-anchor="middle" class="n" font-size="2.1" fill="#4a463e">나오는 차가 있으니 천천히 들어와 주세요 · 부산 해운대구 우동 957-51</text>'
)
back = (
    logo(26, 12.5, 42)
    + f'<text x="47" y="44" text-anchor="middle" class="n" font-size="2.6" fill="#4a463e">010-2901-5663 · @smiths.farm</text>'
)
open('parking.html', 'w').write(doc(W, H, [page(W, H, front, CREAM), page(W, H, back, '#ffffff')]))
