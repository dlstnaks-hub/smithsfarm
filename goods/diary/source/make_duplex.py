# home duplex test print: the A4 one-sheet layout (cover left, inner page right) on both sides of one sheet
import sys
from pypdf import PdfReader, PdfWriter
src, out = sys.argv[1], sys.argv[2]
w=PdfWriter()
for _ in range(2): w.add_page(PdfReader(src).pages[0])
w.add_metadata({'/Title':'스씨네 그림일기 A5 양면 시험 인쇄 (A4 한 장 양면)'})
w.write(out)
