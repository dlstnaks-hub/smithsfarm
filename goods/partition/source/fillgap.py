# One-piece folding version: close the gap between the two runs with a panel of the same fabric, hinge seams at both sides.
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
im=Image.open('mock.jpg').convert('RGB'); a=np.array(im).astype(np.float32)
x0,x1,y0,y1=735,784,686,900
w=x1-x0
L=a[y0:y1, x0-w-2:x0-2]            # strip of the left run next to the gap
R=a[y0:y1, x1+4:x1+4+w]            # strip of the front run next to the gap
t=np.linspace(0,1,w)[None,:,None]
fill=L*(1-t)+R*t
fill*=0.93                          # the joining panel sits a little in shadow
out=a.copy(); out[y0:y1,x0:x1]=fill
img=Image.fromarray(np.clip(out,0,255).astype(np.uint8))
d=ImageDraw.Draw(img)
for x in (x0,x1-1):
    d.line([(x,y0),(x,y1)],fill=(30,44,31),width=2)            # hinge seams
d.line([(x0,y0),(x1,y0)],fill=(52,78,52),width=1)              # top edge
# booth back stays in front: re-paste the original booth below its top edge
src=Image.open('mock.jpg').convert('RGB')
m=Image.new('L',img.size,0); ImageDraw.Draw(m).polygon([(700,897),(740,894),(805,888),(810,888),(810,1000),(700,1000)],fill=255)
img=Image.composite(src,img,m)
img.save('mock_one.jpg',quality=93)
img.crop((600,620,900,960)).resize((600,680)).save('gapz2.png')
