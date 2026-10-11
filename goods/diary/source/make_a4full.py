# home test print: each A5 page enlarged to fill a whole A4 portrait sheet (A5 -> A4 keeps the same ratio)
# usage: make_a4full.py <A5 print pdf with 3mm bleed> <out pdf> <page indexes, e.g. 1 or 0,1>
import sys
from pypdf import PdfReader, PdfWriter, Transformation, PageObject
from pypdf.generic import RectangleObject
mm=72/25.4; W,H=210*mm,297*mm
src,out,idx=sys.argv[1],sys.argv[2],[int(i) for i in sys.argv[3].split(',')]
w=PdfWriter()
for i in idx:
    pg=PdfReader(src).pages[i]; b=pg.bleedbox
    bw,bh=float(b.width),float(b.height); k=max(W/bw,H/bh)   # bleed covers the sheet, trim area sits inside it
    sheet=PageObject.create_blank_page(width=W,height=H)
    tx=(W-bw*k)/2-float(b.left)*k; ty=(H-bh*k)/2-float(b.bottom)*k
    sheet.merge_transformed_page(pg, Transformation().scale(k,k).translate(tx,ty), expand=False)
    w.add_page(sheet)
w.write(out)
