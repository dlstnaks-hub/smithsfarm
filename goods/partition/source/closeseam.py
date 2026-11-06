# Close the light leaking through the seam between panels 3 and 4: the one-piece partition has a sewn/hinged joint there.
from PIL import Image
import numpy as np
a=np.array(Image.open('mock_one.jpg')).astype(np.float32)
for y in range(660,1512):
    row=a[y]
    seg=row[1160:1182]
    leak=(seg[:,2]-seg[:,0]>10)|(seg.sum(1)>row[1150:1158].sum(1).mean()*1.12)
    if not leak.any(): continue
    ref=(row[1150:1158].mean(0)+row[1184:1192].mean(0))/2
    for i in np.nonzero(leak)[0]:
        a[y,1160+i]=ref
    a[y,1168:1172]=ref*0.62           # thin dark joint line instead of a gap
Image.fromarray(np.clip(a,0,255).astype(np.uint8)).save('mock_one.jpg',quality=93)
