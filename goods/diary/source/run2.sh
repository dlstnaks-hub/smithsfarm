cd "$(dirname "$0")"
python3 -m http.server 8800 >/dev/null 2>&1 & SRV=$!
sleep 1; export NO_PROXY=localhost no_proxy=localhost
python3 split2.py; node make2.mjs; kill $SRV
python3 - <<'PY'
from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject
mm=72/25.4; W=154*mm; H=216*mm
for n,o in {'cover_4c':'1_표지_4도_cover.pdf','inner_preview':'2_속지_2도_미리보기_preview.pdf','inner_plate1_black':'3_속지_1판_먹_K.pdf','inner_plate2_green':'4_속지_2판_별색초록.pdf'}.items():
    r=PdfReader(f'raw_{n}.pdf'); w=PdfWriter()
    for pg in r.pages:
        top=float(pg.mediabox.height); y0=top-H
        for box in ('mediabox','cropbox','bleedbox','artbox'): setattr(pg,box,RectangleObject([0,y0,W,top]))
        pg.trimbox=RectangleObject([3*mm,y0+3*mm,W-3*mm,top-3*mm]); w.add_page(pg)
    w.write('out3/'+o)
PY
for f in out3/3_*.pdf out3/4_*.pdf; do pdftoppm -r 30 -png "$f" "v_$(basename "$f" | cut -c1)"; done
python3 - <<'PY'
from PIL import Image
import base64, io, subprocess
a=Image.open('v_3-1.png'); b=Image.open('v_4-1.png'); c=Image.new('RGB',(a.width*2+10,a.height),'#888'); c.paste(a,(0,0)); c.paste(b,(a.width+10,0)); c.save('plates.png')
subprocess.run(['pdftoppm','-r','150','-png','out3/스씨네그림일기_A5_인쇄소용_재단여백3mm.pdf','tex'],check=True)
out={}
for i in (1,2):
    im=Image.open(f'tex-{i}.png').convert('RGB'); w,h=im.size; bb=round(3/25.4*150)
    im=im.crop((bb,bb,w-bb,h-bb)).resize((1024,1446), Image.LANCZOS)
    buf=io.BytesIO(); im.save(buf,'JPEG',quality=86); out[i]=base64.b64encode(buf.getvalue()).decode()
tex='const COVER_IMG="data:image/jpeg;base64,'+out[1]+'";\nconst PAGE_IMG="data:image/jpeg;base64,'+out[2]+'";\n'
open('tex.js','w').write(tex)
open('book.html','w').write(open('book_src.html').read().replace('/*TEX*/', tex))
PY
