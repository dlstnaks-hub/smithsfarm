# home duplex test print: A4 landscape, side 1 = two covers, side 2 = two inner pages; cut down the middle
import sys
from pypdf import PdfReader, PdfWriter, Transformation, PageObject
from pypdf.generic import RectangleObject
mm=72/25.4
src, out = sys.argv[1], sys.argv[2]
w=PdfWriter()
for i in range(2):
    sheet=PageObject.create_blank_page(width=297*mm, height=210*mm)
    for x in (0.25, 148.75):
        pg=PdfReader(src).pages[i]; t=pg.trimbox
        pg.mediabox=RectangleObject([t.left,t.bottom,t.right,t.top]); pg.cropbox=pg.mediabox
        sheet.merge_transformed_page(pg, Transformation().translate(x*mm-float(t.left), -float(t.bottom)), expand=False)
    w.add_page(sheet)
w.add_metadata({'/Title':'스씨네 그림일기 A5 양면 시험 인쇄 (A4 한 장에 2부)'})
w.write(out)
