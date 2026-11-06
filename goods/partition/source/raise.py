# Size-up to the ordered W4300 x H2300: the current oatmeal screen is H1800, so the top goes up 500mm,
# and the front run gets ~290mm more at its right end (front 2150 + joint 430 + left 1720 = 4300).
# Only partition fabric is used as source, so the booth, table, chairs and lamp stay in front.
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
src=Image.open('mock_one.jpg').convert('RGB'); A=np.array(src).astype(np.float32); H,W,_=A.shape
def greenmask(a):
    r,g,b=a[...,0],a[...,1],a[...,2]; return (g>r+15)&(g>b+15)
green=greenmask(A)
def top(x):                            # straight top edges of the current screen
    if x<735: return 690-(x-240)*4/480
    return 687-(x-780)*37/840 if x>=780 else 686
def scale(x):                          # px per mm (front run: 430mm panel = 205px)
    if x<735: return 0.35
    if x>784: return 0.478
    return 0.35+(x-735)/49*(0.478-0.35)
def fabric(a,x,y0,n):                  # n rows of partition fabric from column x, starting at y0, skipping anything not green
    col=a[:,x]; ok=np.nonzero(greenmask(a[:,x][None])[0][y0:])[0]+y0
    ok=ok[:max(n,1)*3]
    if len(ok)==0: return None
    return col[ok[np.arange(n)%len(ok)]]
out=A.copy(); CAP=10
for x in range(232,1677):
    yt=int(round(top(x))); d=int(round(500*scale(x)))
    if not green[yt+CAP:yt+40,x].any(): continue
    M=180 if x<735 else 260
    G=np.nonzero(green[yt+CAP:,x])[0][:M]+yt+CAP        # fabric rows only (booth, table, chairs are skipped and kept)
    T=np.concatenate([np.arange(yt-d+CAP,yt+CAP),G[G>=yt+CAP]])
    T=np.unique(T)
    srcrows=G[np.round(np.linspace(0,len(G)-1,len(T))).astype(int)]
    col=A[:,x].copy()
    out[T,x]=col[srcrows]
    out[yt-d:yt-d+CAP,x]=A[yt:yt+CAP,x]                 # top edge moves up
    # remove the old top edge line that is now inside the panel
# right end: ~290mm more panel; built from the row-by-row fabric profile of the last panel
ext=int(290*0.478); x0=1650
og=greenmask(out)
prof=np.zeros((H,3),np.float32); last=None
for y in range(H):
    xs=np.nonzero(og[y,1380:1640])[0]
    if len(xs)>20: last=np.median(out[y,1380+xs],axis=0)
    if last is not None: prof[y]=last
ty=int(round(top(1640)))-int(round(500*0.478))
for i in range(1677+ext-x0):
    out[ty+CAP:,x0+i]=prof[ty+CAP:]*(0.97+0.03*np.cos(i/9.0))
    out[ty:ty+CAP,x0+i]=out[ty:ty+CAP,1600]
x0=1677
img=Image.fromarray(np.clip(out,0,255).astype(np.uint8))
dr=ImageDraw.Draw(img)
ty=int(round(top(1676)))-239
dr.line([(x0-1,ty),(x0-1,H)],fill=(32,48,33),width=2)            # hinge seam at the old end
dr.line([(x0+ext-2,ty+1),(x0+ext-2,H)],fill=(36,54,37),width=3)  # new end edge
# pendant lamp and cord stay in front
r,g,b=A[...,0],A[...,1],A[...,2]
lamp=((r>140)&(g>120)&(r-b>60)); lamp[:440,:]=False; lamp[620:,:]=False; lamp[:, :860]=False; lamp[:,1050:]=False
cord=(r+g+b<200); cord[:, :945]=False; cord[:, 968:]=False; cord[:380,:]=False; cord[480:,:]=False
mk=Image.fromarray(((lamp|cord)*255).astype(np.uint8)).filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.GaussianBlur(1))
img=Image.composite(src,img,mk)
img.save('mock_big.jpg',quality=93)
