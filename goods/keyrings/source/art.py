# Artwork for the keyring set, in mm (SVG y-down). Each entry: artboard size, hole, art markup.
# Palette shared with the carrot file: orange #f5821f, green #2f6b3a, dark #2a2318, cheek #ffc799, cream border #fdf8ee.

DARK = '#2a2318'

def face(cx, cy, eye_dx=2.4, eye_r=1.6):
    return f'''
  <circle cx="{cx-eye_dx}" cy="{cy}" r="{eye_r}" fill="{DARK}"/><circle cx="{cx+eye_dx}" cy="{cy}" r="{eye_r}" fill="{DARK}"/>
  <circle cx="{cx-eye_dx+0.5}" cy="{cy-0.55}" r="0.5" fill="#fff"/><circle cx="{cx+eye_dx+0.5}" cy="{cy-0.55}" r="0.5" fill="#fff"/>
  <ellipse cx="{cx-4.4}" cy="{cy+2.6}" rx="1.5" ry="1" fill="#ffc799"/><ellipse cx="{cx+4.4}" cy="{cy+2.6}" rx="1.5" ry="1" fill="#ffc799"/>
  <path d="M{cx-1.8} {cy+3.1} C{cx-0.7} {cy+4.3} {cx+0.7} {cy+4.3} {cx+1.8} {cy+3.1}" fill="none" stroke="{DARK}" stroke-width="0.8" stroke-linecap="round"/>'''

# ---------------- 허수아비: 밀짚모자 + 삼베 얼굴 + 초록 셔츠(주황 덧댄 천) + 막대 ----------------
def straw_fan(x, y, flip):
    s = -1 if flip else 1
    pts = [(0, -2.6), (-3.4, -3.2), (-3.9, -1.2), (-4.2, 0.6), (-3.6, 2.6), (0, 2.4)]
    d = 'M' + ' L'.join(f'{x + s*px:.2f} {y + py:.2f}' for px, py in pts) + ' Z'
    lines = ' '.join(f'M{x:.2f} {y + oy:.2f} L{x + s*lx:.2f} {y + ly:.2f}' for oy, lx, ly in ((-1.6, -3.2, -2.6), (-0.4, -3.8, -0.7), (0.8, -3.7, 1.4), (1.8, -3.0, 2.4)))
    return f'<path d="{d}" fill="#f2c14e"/><path d="{lines}" fill="none" stroke="#c9922b" stroke-width="0.35" stroke-linecap="round"/>'

SCARECROW = dict(
    w=48, h=58, hole=(24, 7.6, 1.7),
    art=f'''
<g transform="translate(1 1.6)">
  <!-- 막대 (팔 막대와 기둥) -->
  <rect x="3.2" y="31" width="39.6" height="2.2" rx="1.1" fill="#9b6a3c"/>
  <rect x="22" y="44" width="2" height="9.6" rx="0.6" fill="#9b6a3c"/>
  <path d="M22.4 46 v6.6 M23.6 45.4 v7" stroke="#7d5330" stroke-width="0.3" fill="none"/>
  <!-- 손목 밀짚 -->
  {straw_fan(6.4, 32.1, False)}
  {straw_fan(39.6, 32.1, True)}
  <!-- 셔츠 -->
  <path d="M8 29.6 H38 Q39.6 29.6 39.6 31.2 V34 Q39.6 35.6 38 35.6 H29.6 V44.6 L16.4 44.6 V35.6 H8 Q6.4 35.6 6.4 34 V31.2 Q6.4 29.6 8 29.6 Z" fill="#2f6b3a"/>
  <path d="M10 32.6 H15.6 M30.4 32.6 H36" stroke="#4d8a57" stroke-width="0.5" stroke-linecap="round"/>
  <rect x="24.4" y="37.2" width="3.8" height="3.8" rx="0.4" fill="#f5821f" transform="rotate(-6 26.3 39.1)"/>
  <path d="M24.9 37.9 l.6 .6 M27.2 37.6 l.6 .6 M25.2 40.2 l.6 .6 M27.5 39.9 l.6 .6" stroke="#fdf8ee" stroke-width="0.35" stroke-linecap="round" transform="rotate(-6 26.3 39.1)"/>
  <circle cx="20" cy="38" r="0.7" fill="#fdf8ee"/><circle cx="20" cy="41.4" r="0.7" fill="#fdf8ee"/>
  <!-- 셔츠 아래 밀짚 -->
  <path d="M16.6 44.2 L17.4 47.6 L18.9 45.2 L20.3 48.2 L21.6 45.2 L24.6 45.2 L25.8 48.2 L27.2 45.2 L28.6 47.6 L29.4 44.2 Z" fill="#f2c14e"/>
  <!-- 목 밀짚 -->
  <path d="M19.6 29.9 L20.6 27.6 L21.8 29.4 L23 27.2 L24.2 29.4 L25.4 27.6 L26.4 29.9 Z" fill="#f2c14e"/>
  <!-- 얼굴 (삼베 자루) -->
  <circle cx="23" cy="21.6" r="6.6" fill="#ecd3a2"/>
  <path d="M17.4 18.4 h1.1 M28.1 24.4 h1 M18.2 26 h.9 M27.4 17.2 h.9" stroke="#c9a874" stroke-width="0.35" stroke-linecap="round"/>
  {face(23, 21.4)}
  <path d="M16.6 23.4 l-.9 .3 M16.5 21.4 l-1 0 M29.4 23.4 l.9 .3 M29.5 21.4 l1 0" stroke="#b08a5a" stroke-width="0.35" stroke-linecap="round"/>
  <!-- 모자 밑 밀짚 머리 -->
  <path d="M16.8 16.6 L15.2 20.2 L17.4 19 L17.6 21.2 L18.8 17 Z M29.2 16.6 L30.8 20.2 L28.6 19 L28.4 21.2 L27.2 17 Z" fill="#f2c14e"/>
  <!-- 밀짚모자 -->
  <path d="M16.6 15.2 C16.6 7.6 19.2 3.2 23 3.2 C26.8 3.2 29.4 7.6 29.4 15.2 Z" fill="#e3b04b"/>
  <path d="M19 13.6 C19 8.4 20.6 5.2 23 4.6" fill="none" stroke="#f2cc72" stroke-width="0.6" stroke-linecap="round"/>
  <rect x="16.7" y="11.6" width="12.6" height="2.6" fill="#2f6b3a"/>
  <ellipse cx="23" cy="15.4" rx="12" ry="2.4" fill="#e3b04b"/>
  <path d="M12.6 15.6 Q23 18.4 33.4 15.6" fill="none" stroke="#c99536" stroke-width="0.45" stroke-linecap="round"/>
  <path d="M28.6 11.8 l2.4 -1.4 l.2 1.6 Z" fill="#f5821f"/>
</g>''')

# ---------------- 문어 씨! (아크릴 키링, 머리 위 고리 탭) ----------------
OCTOPUS = dict(
    w=48, h=50, hole=(24, 8.03, 1.7),
    art='''
<g transform="translate(1 4.2) scale(0.383)">
  <circle cx="60" cy="10" r="9" fill="#c4532d"/>
  <ellipse cx="60" cy="48" rx="34" ry="32" fill="#c4532d"/>
  <path d="M34 70 C28 92 18 98 12 92 M48 76 C46 98 38 110 30 106 M72 76 C74 98 82 110 90 106 M86 70 C92 92 102 98 108 92" fill="none" stroke="#c4532d" stroke-width="10" stroke-linecap="round"/>
  <ellipse cx="46" cy="31" rx="11" ry="6" transform="rotate(-28.6 46 31)" fill="#ffffff" fill-opacity="0.2"/>
  <circle cx="47" cy="48" r="7" fill="#ffffff"/><circle cx="73" cy="48" r="7" fill="#ffffff"/>
  <circle cx="48" cy="49" r="3.8" fill="#1f2a1f"/><circle cx="74" cy="49" r="3.8" fill="#1f2a1f"/>
  <circle cx="49.6" cy="47.4" r="1.3" fill="#ffffff"/><circle cx="75.6" cy="47.4" r="1.3" fill="#ffffff"/>
  <ellipse cx="37" cy="58" rx="5" ry="3" fill="#ffb0a0" fill-opacity="0.75"/><ellipse cx="83" cy="58" rx="5" ry="3" fill="#ffb0a0" fill-opacity="0.75"/>
  <path d="M53 61 Q60 67 67 61" fill="none" stroke="#1f2a1f" stroke-width="2.6" stroke-linecap="round"/>
</g>''')

# ---------------- 당근 (보내 주신 오프린트미 파일 그대로, PDF 좌표를 SVG로 뒤집음) ----------------
CARROT_OUT = 'M2 38 C0 44 1 50 5 52 C7 53 9 51 10 48 L10 52 C10 54.5 12 56 15 56 C18 56 20 54.5 20 52 L20 48 C21 51 23 53 25 52 C29 50 30 44 28 38 C25 26 19 10 16 2 C15.6 0.6 14.4 0.6 14 2 C11 10 5 26 2 38 Z'
CARROT_LEAF = 'M2 39 C0 44 1 50 5 52 C7 53 9 51 10 48 L10 52 C10 54.5 12 56 15 56 C18 56 20 54.5 20 52 L20 48 C21 51 23 53 25 52 C29 50 30 44 28 39 Z'
CARROT = dict(
    w=30, h=56, hole=(15, 6, 1.7), outline_pdf=CARROT_OUT,
    art=f'''
<g transform="translate(0 56) scale(1 -1)">
  <path d="{CARROT_OUT}" fill="rgb(245,130,31)"/>
  <path d="{CARROT_LEAF}" fill="rgb(47,107,58)"/>
  <path d="M5 33 L9 32.2 M21 33 L25 32.2 M8 14 L12 13.2 M18 17 L22 16.2" stroke="rgb(206,95,16)" stroke-width="0.6" stroke-linecap="round"/>
  <circle cx="11.3" cy="28" r="1.9" fill="rgb(42,35,24)"/><circle cx="18.7" cy="28" r="1.9" fill="rgb(42,35,24)"/>
  <circle cx="11.9" cy="28.7" r="0.6" fill="#fff"/><circle cx="19.3" cy="28.7" r="0.6" fill="#fff"/>
  <ellipse cx="7.2" cy="24.5" rx="1.8" ry="1.2" fill="rgb(255,199,153)"/><ellipse cx="22.8" cy="24.5" rx="1.8" ry="1.2" fill="rgb(255,199,153)"/>
  <path d="M13 24.6 C14.2 23.2 15.8 23.2 17 24.6" fill="none" stroke="rgb(42,35,24)" stroke-width="0.8" stroke-linecap="round"/>
</g>''')
