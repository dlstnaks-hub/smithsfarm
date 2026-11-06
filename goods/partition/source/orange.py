# Recolour the finished green mockup to another fabric colour, keeping its shading.
import sys
from PIL import Image
import numpy as np
hexc=sys.argv[1].lstrip('#'); out=sys.argv[2]
C=np.array([int(hexc[i:i+2],16) for i in (0,2,4)],np.float32)
a=np.array(Image.open('mock_big.jpg').convert('RGB')).astype(np.float32)
r,g,b=a[...,0],a[...,1],a[...,2]
ratio=(g-np.maximum(r,b))/np.maximum(g,1)                    # how green a pixel is, independent of how dark
alpha=(np.clip((ratio-0.07)/0.13,0,1)*np.clip((g-14)/10,0,1))[...,None]
L=0.299*r+0.587*g+0.114*b
Lg=0.299*71+0.587*112+0.114*70                               # the green swatch the mockup was made from
k=(L/Lg)[...,None]
new=np.clip(C*k*0.98,0,255)
res=a*(1-alpha)+new*alpha
Image.fromarray(res.astype(np.uint8)).save(out,quality=93)
