# Set exact page boxes (Chrome rounds the page size up a little); optional bleed in mm becomes the TrimBox inset.
import sys
from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject
src, out, w, h, bleed, title = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]), sys.argv[6]
mm = 72/25.4; W, H, B = w*mm, h*mm, bleed*mm
wr = PdfWriter()
for pg in PdfReader(src).pages:
    top = float(pg.mediabox.top); box = RectangleObject([0, top-H, W, top])
    for k in ('mediabox', 'cropbox', 'bleedbox', 'artbox'): setattr(pg, k, box)
    pg.trimbox = RectangleObject([B, top-H+B, W-B, top-B]); wr.add_page(pg)
wr.add_metadata({'/Title': title}); wr.write(out)
