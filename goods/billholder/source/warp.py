# Warp an art image (rendered at 4px/pt over the art box x40..290, y146..640) onto the photo:
# homography fitted on the control points, plus a smooth thin-plate correction for the bent card.
import sys, json, numpy as np, cv2
from scipy.interpolate import RBFInterpolator
pairs = json.load(open('pairs.json'))
A = np.float64([p[0] for p in pairs]); B = np.float64([p[1] for p in pairs])
Hm, _ = cv2.findHomography(A, B, 0); Hi = np.linalg.inv(Hm)
def h_inv(pts):
    q = np.hstack([pts, np.ones((len(pts), 1))]) @ Hi.T; return q[:, :2] / q[:, 2:]
res = A - h_inv(B)                                   # art-space residual at control points
rbf = RBFInterpolator(B, res, kernel='thin_plate_spline', smoothing=2.0)
photo = cv2.imread('photo.jpg'); H, W = photo.shape[:2]
x0, y0, x1, y1 = 330, 260, 1300, 1120                # region of the front card
ys, xs = np.mgrid[y0:y1, x0:x1]; P = np.column_stack([xs.ravel(), ys.ravel()]).astype(np.float64)
artpt = h_inv(P) + rbf(P)
mx = ((artpt[:, 0] - 40) * 4).reshape(ys.shape).astype(np.float32)
my = ((artpt[:, 1] - 146) * 4).reshape(ys.shape).astype(np.float32)
np.save('map.npy', np.stack([mx, my])); json.dump([x0, y0, x1, y1], open('region.json', 'w'))
art = cv2.imread(sys.argv[1] if len(sys.argv) > 1 else '../art_orig_mask.png', cv2.IMREAD_UNCHANGED)
w = cv2.remap(art, mx, my, cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0, 0))
alpha = w[..., 3] > 128
edge = cv2.Canny(alpha.astype(np.uint8) * 255, 50, 150)
over = photo[y0:y1, x0:x1].copy(); over[edge > 0] = (255, 0, 255)
cv2.imwrite('check.jpg', over)
