# Home test print: one A5 page per A4 sheet, colour running 5mm past the A5 cut line,
# tiny grey corner ticks sit outside the colour so they fall away when trimmed.
import re
s=open('diary_print.html').read()
head=s[:s.index('<body>')]
head=re.sub(r'@page \{[^}]*\}','@page { size: 210mm 297mm; margin: 0 }',head)
head=re.sub(r'\.page \{ width: [^;]*; height: [^;]*;','.page { width: 210mm; height: 297mm;',head)
head=re.sub(r'svg \{ display: block; width: [^}]*\}','svg.sheet { display: block; width: 210mm; height: 297mm }',head)
inners=re.findall(r'<svg viewBox="[^"]*" xmlns="http://www.w3.org/2000/svg">(.*?)</svg>',s,re.S)
s5=148/182; vbw=158/s5; vbh=220/s5
vb=f'{94-vbw/2:.3f} {131.5-vbh/2:.3f} {vbw:.3f} {vbh:.3f}'
x0,y0=26,38.5            # 158x220 art centred on A4
tx0,ty0,tx1,ty1=31,43.5,179,253.5   # A5 cut line
def ticks():
    L=[]
    for x in (tx0,tx1):
        for y,d in ((ty0,-1),(ty1,1)): L.append(f'<line x1="{x}" y1="{y+d*6}" x2="{x}" y2="{y+d*11}"/>')
    for y in (ty0,ty1):
        for x,d in ((tx0,-1),(tx1,1)): L.append(f'<line x1="{x+d*6}" y1="{y}" x2="{x+d*11}" y2="{y}"/>')
    return '<g stroke="#9a9a9a" stroke-width="0.2">'+''.join(L)+'</g>'
pages=''.join(f'<div class="page"><svg class="sheet" viewBox="0 0 210 297" xmlns="http://www.w3.org/2000/svg">{ticks()}<svg x="{x0}" y="{y0}" width="158" height="220" viewBox="{vb}" overflow="hidden">{c}</svg></svg></div>' for c in inners)
open('test_a5.html','w').write(head+'<body>'+pages+'</body></html>')
print(len(inners), vb)
