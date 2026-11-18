# 3D bill holder with the official SMITH's FARM logo (white, vector) on the tomato instead of the serif wordmark.
import re, make3
LOGO_D = open('logo_h.d').read()
BX, BY, BW, BH = map(float, open('logo_h.box').read().split())   # horizontal lockup box (mm)
LW = 108.0; LH = LW * BH / BW                      # logo size on the art (pt)
CX, CY = 215.0, 444.0                             # centre on the tomato body
S = LW / BW; TX, TY = CX - LW / 2 - BX * S, CY - LH / 2 - BY * S
TF = f'matrix({S:.5f} 0 0 {S:.5f} {TX:.4f} {TY:.4f})'
logo = lambda fill, extra='': f'<path d="{LOGO_D}" fill-rule="evenodd" fill="{fill}" transform="{TF}" {extra}/>'
defs, body, _ = make3.v3d()
vb = f'{make3.X0} {make3.Y0} {make3.X1-make3.X0} {make3.Y1-make3.Y0}'
head = f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="{vb}" width="250" height="494"><defs>{make3.defs_common()}{defs}</defs>{body}'
shadow = f'<g clip-path="url(#U)"><g opacity=".45" filter="url(#soft2)" transform="translate(.9 1.3)">{logo("#5a0f06")}</g></g>'
open('art_3d_logo_img.svg', 'w').write(head + shadow + '</svg>')               # picture layer (with logo shadow)
open('art_3d_logo.svg', 'w').write(head + shadow + logo('#ffffff') + '</svg>')  # full preview
open('logo_tf.txt', 'w').write(f'{S} {TX} {TY}')
print(LW, round(LH, 2), TF)
