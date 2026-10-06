cd "$(dirname "$0")"
python3 -m http.server 8800 >/dev/null 2>&1 & SRV=$!
sleep 1; export NO_PROXY=localhost no_proxy=localhost
node make_pdf.mjs; kill $SRV
python3 - <<'PY'
from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject
mm=72/25.4; W=154*mm; H=216*mm
r=PdfReader('raw.pdf'); w=PdfWriter()
for pg in r.pages:
    top=float(pg.mediabox.height); y0=top-H
    for box in ('mediabox','cropbox','bleedbox','artbox'): setattr(pg,box,RectangleObject([0,y0,W,top]))
    pg.trimbox=RectangleObject([3*mm,y0+3*mm,W-3*mm,top-3*mm]); w.add_page(pg)
w.add_metadata({'/Title':'스씨네 그림일기 A5 (재단 148x210mm, 재단 여백 3mm)'})
w.write('out3/스씨네그림일기_A5_인쇄소용_재단여백3mm.pdf')
# home test print: A4 landscape, A5 cover on the left and A5 inner page on the right; cut down the middle
from pypdf import Transformation, PageObject
r=PdfReader('out3/스씨네그림일기_A5_인쇄소용_재단여백3mm.pdf'); w=PdfWriter()
sheet=PageObject.create_blank_page(width=297*mm, height=210*mm)
for i,pg in enumerate(r.pages[:2]):
    t=pg.trimbox; x=(0.25 if i==0 else 148.75)*mm
    pg.mediabox=RectangleObject([t.left,t.bottom,t.right,t.top]); pg.cropbox=pg.mediabox
    sheet.merge_transformed_page(pg, Transformation().translate(x-float(t.left), -float(t.bottom)), expand=False)
w.add_page(sheet)
w.write('out3/스씨네그림일기_A5_테스트인쇄용_A4한장.pdf')
PY
