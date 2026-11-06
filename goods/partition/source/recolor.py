from PIL import Image, ImageDraw, ImageFilter
import numpy as np, colorsys
im=Image.open('room.jpg').convert('RGB'); W,H=im.size
a=np.array(im).astype(np.float32)/255
poly=Image.new('L',(W,H),0); d=ImageDraw.Draw(poly)
d.polygon([(232,688),(738,678),(738,898),(258,984),(240,984)],fill=255)                  # back-left run above the booth
d.polygon([(776,684),(1664,646),(1676,1512),(1180,1512),(1180,1440),(862,1270),(866,1186),(806,1186),(806,886),(776,886)],fill=255)  # front run
d.polygon([(560,1395),(962,1132),(1264,1168),(985,1512),(560,1512)],fill=0)    # table top
m=np.array(poly)>0
r,g,b=a[...,0],a[...,1],a[...,2]
mx=a.max(-1); mn=a.min(-1); sat=(mx-mn)/(mx+1e-6)
warm=(b<r+0.10)&(mx>0.09)
mask=(m&warm).astype(np.uint8)*255
mask=Image.fromarray(mask).filter(ImageFilter.MedianFilter(5)).filter(ImageFilter.GaussianBlur(1.2))
L=0.299*r+0.587*g+0.114*b
ref=np.median(L[m&warm])
C=np.array([71,112,70])/255.0          # RAL 6001 swatch from the sample image
k=(L/ref)[...,None]
k=k**0.65                                # keep folds and shading, slightly softer
new=C*k*0.80
grey=new.mean(-1,keepdims=True); new=np.clip(grey+(new-grey)*0.85,0,1)
out=Image.fromarray((new*255).astype(np.uint8))
res=Image.composite(out,im,mask)
res.save('mock.jpg',quality=93)
Image.fromarray(np.array(mask)).save('mask.png')
print(ref)
