# White SMITH's FARM logo printed on the front-right panel of the C option (#EF6C00), following the fabric shading.
from PIL import Image
import numpy as np
base=Image.open('mock_EF6C00.jpg').convert('RGB'); A=np.array(base).astype(np.float32)
src=Image.open('/home/user/smithsfarm/goods/logo/스미스팜_로고_흰색.png').convert('RGB')   # white logo on orange: blue channel = logo coverage
mask=src.split()[2]
logo=Image.new('RGBA',src.size,(255,255,255,0)); logo.putalpha(mask)
logo=logo.crop(mask.point(lambda v:255 if v>40 else 0).getbbox())
LW=240; lh=round(logo.height*LW/logo.width)
logo=logo.resize((LW,lh),Image.LANCZOS)
cx,cy=1510,640
x0,y0=cx-LW//2,cy-lh//2
al=np.array(logo.split()[3]).astype(np.float32)[...,None]/255*0.96
reg=A[y0:y0+lh,x0:x0+LW]
L=reg.mean(-1,keepdims=True); k=np.clip(L/np.median(L),0.8,1.1)
white=np.array([246,242,236],np.float32)*k
A[y0:y0+lh,x0:x0+LW]=reg*(1-al)+white*al
Image.fromarray(np.clip(A,0,255).astype(np.uint8)).save('mock_C_logo.jpg',quality=93)
print(x0,y0,LW,lh)
