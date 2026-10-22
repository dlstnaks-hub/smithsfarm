# Draw a dashed fold guide down the middle of page 1 (the cover side) of an A4 landscape fold sheet.
# usage: add_foldline.py <in.pdf> <out.pdf>
import sys
from pypdf import PdfReader, PdfWriter
from pypdf.generic import DecodedStreamObject, ArrayObject, NameObject
mm = 72 / 25.4
r = PdfReader(sys.argv[1]); w = PdfWriter(clone_from=r)
pg = w.pages[0]; b = pg.mediabox
x = float(b.left) + float(b.width) / 2
ops = f'q 0.62 0.6 0.56 RG {0.35*mm:.3f} w [{2.2*mm:.3f} {1.6*mm:.3f}] 0 d {x:.3f} {float(b.bottom):.3f} m {x:.3f} {float(b.top):.3f} l S Q\n'
st = DecodedStreamObject(); st.set_data(ops.encode())
c = pg['/Contents']
arr = ArrayObject(c.get_object() if isinstance(c.get_object(), ArrayObject) else [c])
arr.append(w._add_object(st)); pg[NameObject('/Contents')] = arr
w.write(sys.argv[2])
