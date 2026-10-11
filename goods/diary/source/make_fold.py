# A4 duplex, fold in half: side 1 = two A5 covers side by side, side 2 = one A4 landscape "오늘의 그림" page
import sys
from pypdf import PdfReader, PdfWriter, Transformation, PageObject
from pypdf.generic import RectangleObject
mm=72/25.4
a5, spread, out = sys.argv[1:4]
w=PdfWriter()
sheet=PageObject.create_blank_page(width=297*mm, height=210*mm)
for x in (0.25, 148.75):
    pg=PdfReader(a5).pages[0]; t=pg.trimbox
    pg.mediabox=RectangleObject([t.left,t.bottom,t.right,t.top]); pg.cropbox=pg.mediabox
    sheet.merge_transformed_page(pg, Transformation().translate(x*mm-float(t.left), -float(t.bottom)), expand=False)
w.add_page(sheet)
w.add_page(PdfReader(spread).pages[0])
w.add_metadata({'/Title':'스씨네 그림일기 A4 양면 (표지 2개 / 오늘의 그림 한 면)'})
w.write(out)
