# A4 door signs (men / women) in the style of the A3 RESTROOM sign: cream paper, thin tan frame,
# Fraunces + Noto Sans KR, green for men, brick orange for women, a farmer character in the corner.
CREAM, LINE, INK = '#faf6ec', '#d8cdb2', '#2b241c'
GREEN, ORANGE = '#5b6b45', '#b8623f'
HAT, HAT2, SKIN, WOOD, SHOE = '#e2c48f', '#d6b67c', '#eeba8e', '#8a6a4a', '#3c3226'

def picto(kind, c):
    if kind == 'men':
        return f'''<circle cx="105" cy="62" r="14" fill="{c}"/>
<rect x="82" y="82" width="46" height="50" rx="9" fill="{c}"/>
<rect x="67.5" y="84" width="11" height="46" rx="5.5" fill="{c}"/>
<rect x="131.5" y="84" width="11" height="46" rx="5.5" fill="{c}"/>
<rect x="84.5" y="124" width="18.5" height="36" rx="5.5" fill="{c}"/>
<rect x="107" y="124" width="18.5" height="36" rx="5.5" fill="{c}"/>'''
    return f'''<circle cx="105" cy="62" r="14" fill="{c}"/>
<path d="M91 82 H119 L137 134 H73 Z" fill="{c}" stroke="{c}" stroke-width="7" stroke-linejoin="round"/>
<rect x="72" y="84" width="9" height="34" rx="4.5" fill="{c}" transform="rotate(14 76 86)"/>
<rect x="129" y="84" width="9" height="34" rx="4.5" fill="{c}" transform="rotate(-14 134 86)"/>
<rect x="90" y="128" width="11" height="32" rx="4" fill="{c}"/>
<rect x="109" y="128" width="11" height="32" rx="4" fill="{c}"/>'''

def farmer_man():
    return f'''<g fill="none" stroke="{WOOD}" stroke-width="3.2" stroke-linecap="round">
  <path d="M82 112 V20"/><path d="M71 20 H93"/><path d="M73 20 V7"/><path d="M78.5 20 V5"/><path d="M85.5 20 V5"/><path d="M91 20 V7"/></g>
<ellipse cx="45" cy="31" rx="30" ry="7" fill="{HAT2}"/>
<path d="M30 31 Q30 11 45 11 Q60 11 60 31 Z" fill="{HAT}"/>
<circle cx="45" cy="46" r="16" fill="{SKIN}"/>
<path d="M37 44 q3 3 6 0 M47 44 q3 3 6 0" fill="none" stroke="{SHOE}" stroke-width="1.8" stroke-linecap="round"/>
<path d="M38 51 q7 6 14 0" fill="none" stroke="{SHOE}" stroke-width="2" stroke-linecap="round"/>
<rect x="31" y="102" width="12" height="24" rx="4" fill="{GREEN}"/><rect x="47" y="102" width="12" height="24" rx="4" fill="{GREEN}"/>
<ellipse cx="37" cy="128" rx="9" ry="5" fill="{SHOE}"/><ellipse cx="53" cy="128" rx="9" ry="5" fill="{SHOE}"/>
<rect x="27" y="62" width="36" height="46" rx="10" fill="{GREEN}"/>
<rect x="40" y="76" width="10" height="10" rx="2" fill="none" stroke="#46552f" stroke-width="1.8"/><circle cx="45" cy="71" r="1.6" fill="#46552f"/>
<path d="M25 70 Q16 82 20 95" fill="none" stroke="{SKIN}" stroke-width="8" stroke-linecap="round"/>
<path d="M64 70 Q74 66 80 64" fill="none" stroke="{SKIN}" stroke-width="7" stroke-linecap="round"/>
<circle cx="25" cy="68" r="8.5" fill="{ORANGE}"/><circle cx="65" cy="68" r="8.5" fill="{ORANGE}"/>
<circle cx="13" cy="93" r="5" fill="#c0432e"/><circle cx="20" cy="90" r="5" fill="#d9a33a"/><circle cx="27" cy="93" r="5" fill="#6b8a45"/>
<rect x="5" y="95" width="30" height="5" rx="2" fill="#6f5338"/>
<path d="M7 100 H33 L29 118 H11 Z" fill="{WOOD}"/>'''

def farmer_woman():
    return f'''<path d="M27 46 Q26 74 34 82 L56 82 Q64 74 63 46 Z" fill="#5a3d2b"/>
<circle cx="45" cy="46" r="16" fill="{SKIN}"/>
<ellipse cx="45" cy="31" rx="30" ry="7" fill="{HAT2}"/>
<path d="M30 31 Q30 11 45 11 Q60 11 60 31 Z" fill="{HAT}"/>
<path d="M30.5 27 H59.5 V31 H30.5 Z" fill="{ORANGE}"/>
<path d="M58 29 l9 -4 l-1 8 Z" fill="{ORANGE}"/>
<path d="M37 45 q3 3 6 0 M47 45 q3 3 6 0" fill="none" stroke="{SHOE}" stroke-width="1.8" stroke-linecap="round"/>
<circle cx="35" cy="51" r="3" fill="#e99a86" opacity="0.8"/><circle cx="55" cy="51" r="3" fill="#e99a86" opacity="0.8"/>
<path d="M39 52 q6 5 12 0" fill="none" stroke="{SHOE}" stroke-width="2" stroke-linecap="round"/>
<rect x="35" y="104" width="8" height="20" rx="3" fill="{SKIN}"/><rect x="47" y="104" width="8" height="20" rx="3" fill="{SKIN}"/>
<ellipse cx="38" cy="127" rx="8" ry="4.6" fill="{SHOE}"/><ellipse cx="52" cy="127" rx="8" ry="4.6" fill="{SHOE}"/>
<path d="M32 62 H58 L68 108 H22 Z" fill="{ORANGE}" stroke="{ORANGE}" stroke-width="5" stroke-linejoin="round"/>
<path d="M37 72 H53 L57 104 H33 Z" fill="#f3e6cc"/><path d="M40 86 H50" stroke="#d8c6a2" stroke-width="1.6"/>
<path d="M64 70 Q76 74 76 88" fill="none" stroke="{SKIN}" stroke-width="7" stroke-linecap="round"/>
<path d="M26 70 Q16 80 20 93" fill="none" stroke="{SKIN}" stroke-width="7" stroke-linecap="round"/>
<circle cx="27" cy="67" r="8" fill="{GREEN}"/><circle cx="63" cy="67" r="8" fill="{GREEN}"/>
<g stroke="#5f7d3a" stroke-width="2.2" stroke-linecap="round"><path d="M10 88 l-3 -7"/><path d="M15 87 l0 -8"/><path d="M27 88 l3 -7"/></g>
<path d="M8 90 l4 -3 l3 12 Z" fill="#e9772f"/><path d="M14 89 l3 -3 l2 13 Z" fill="#e9772f"/><path d="M26 90 l3 0 l-5 12 Z" fill="#e9772f"/>
<rect x="5" y="94" width="30" height="5" rx="2" fill="#6f5338"/>
<path d="M7 99 H33 L29 117 H11 Z" fill="{WOOD}"/>
<circle cx="76" cy="90" r="4.5" fill="{SKIN}"/>'''

def page(kind):
    c = GREEN if kind == 'men' else ORANGE
    ko = '남자 화장실' if kind == 'men' else '여자 화장실'
    en = 'MEN' if kind == 'men' else 'WOMEN'
    who = farmer_man() if kind == 'men' else farmer_woman()
    return f'''<div class="page"><svg viewBox="0 0 210 297" xmlns="http://www.w3.org/2000/svg">
<rect width="210" height="297" fill="{CREAM}"/>
<rect x="10" y="10" width="190" height="277" fill="none" stroke="{LINE}" stroke-width="0.6"/>
<text x="105" y="27" text-anchor="middle" class="fr" font-size="5.2" letter-spacing="1.2" fill="{INK}">SMITH's FARM <tspan class="ko" font-weight="500" font-size="4.6" letter-spacing="0.3" fill="#6b6457"> · 스미스씨네농장</tspan></text>
<line x1="80" y1="33" x2="130" y2="33" stroke="{LINE}" stroke-width="0.5"/>
<g transform="translate(0 4)">{picto(kind, c)}</g>
<text x="105" y="201" text-anchor="middle" class="ko" font-weight="800" font-size="27" fill="{c}" letter-spacing="1">{ko}</text>
<text x="{108 if kind == 'men' else 107}" y="227" text-anchor="middle" class="fr" font-size="{23 if kind == 'men' else 17}" letter-spacing="{6 if kind == 'men' else 4}" fill="{INK}">{en}</text>
<line x1="24" y1="240" x2="128" y2="240" stroke="{LINE}" stroke-width="0.5"/>
<text x="24" y="254" class="ko" font-weight="700" font-size="5.4" fill="{INK}">깨끗하게 사용해 주세요</text>
<text x="24" y="262" class="fri" font-size="4.2" fill="{c}">Please keep it clean, thank you!</text>
<text x="24" y="275" class="ko" font-weight="500" font-size="3.6" fill="#8a8273">휴지는 휴지통에 · 물은 꼭 내려 주세요</text>
<g transform="translate(142 236) scale(0.36)">{who}</g>
</svg></div>
'''

HEAD = '''<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>Smith's Farm Restroom Door Signs A4</title>
<link rel="stylesheet" href="../diary/fonts/fontsource-noto-sans-kr-5.3.0/package/korean-500.css"><link rel="stylesheet" href="../diary/fonts/fontsource-noto-sans-kr-5.3.0/package/korean-700.css">
<link rel="stylesheet" href="../diary/fonts/fontsource-noto-sans-kr-5.3.0/package/korean-800.css"><link rel="stylesheet" href="../diary/fonts/fontsource-noto-sans-kr-5.3.0/package/latin-500.css">
<link rel="stylesheet" href="../diary/fonts/fraunces/package/latin-600.css"><link rel="stylesheet" href="../diary/fonts/fraunces/package/latin-400-italic.css">
<style>@page{size:210mm 297mm;margin:0}html,body{margin:0}.page{width:210mm;height:297mm;overflow:hidden;break-after:page}.page:last-child{break-after:auto}
svg{display:block;width:210mm;height:297mm}.ko{font-family:'Noto Sans KR',sans-serif}.fr{font-family:'Fraunces',serif;font-weight:600}.fri{font-family:'Fraunces',serif;font-style:italic;font-weight:400}</style></head><body>
'''
open('wc.html','w').write(HEAD+page('men')+page('women')+'</body></html>\n')
