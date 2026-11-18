# Mock-up: lay a freshly printed die-cut card (new art + white border) over the front card in the photo,
# using the fitted warp; the bag front and the clothespin stay in front, light follows the photo.
import sys, json, numpy as np, cv2
name = sys.argv[1]; out_name = sys.argv[2] if len(sys.argv) > 2 else f'comp_{name}.jpg'
x0, y0, x1, y1 = json.load(open('region.json')); mx, my = np.load('map.npy')
photo = cv2.imread('photo.jpg').astype(np.float32); reg = photo[y0:y1, x0:x1].copy()
art = cv2.imread(f'../art4_{name}.png', cv2.IMREAD_UNCHANGED).astype(np.float32)
orig = cv2.imread('../art4_orig.png', cv2.IMREAD_UNCHANGED).astype(np.float32)
PAD = 40                                             # art px of room around the art box for the border
def pad(a): return cv2.copyMakeBorder(a, PAD, PAD, PAD, PAD, cv2.BORDER_CONSTANT, value=(0, 0, 0, 0))
art, orig = pad(art), pad(orig)
a = art[..., 3] / 255
k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * 26 + 1, 2 * 26 + 1))   # ~6.5pt white border (die-cut offset)
card = cv2.dilate((a > .5).astype(np.uint8), k).astype(np.float32)
card = cv2.GaussianBlur(card, (0, 0), 1.0)
paper = np.full(art.shape[:2] + (3,), (236, 241, 244), np.float32)  # BGR off-white
rgb = art[..., :3] * a[..., None] + paper * (1 - a[..., None])
edge = cv2.GaussianBlur(card, (0, 0), 3) - card                   # thin darker paper edge
rgb = np.clip(rgb + edge[..., None] * 60, 0, 255)
lay = np.dstack([rgb, card * 255])
mxp, myp = mx + PAD, my + PAD
W = lambda img: cv2.remap(img, mxp, myp, cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=0)
L = W(lay); O = W(orig)
ca = L[..., 3] / 255
# light: photo brightness relative to the printed original, smoothed; outside the old print use the border brightness
lum = lambda im: cv2.cvtColor(np.clip(im, 0, 255).astype(np.uint8), cv2.COLOR_BGR2GRAY).astype(np.float32) + 8
m = (O[..., 3] > 200).astype(np.float32)
num = cv2.GaussianBlur(lum(reg) * m, (0, 0), 25); den = cv2.GaussianBlur(lum(O[..., :3]) * m, (0, 0), 25); ws = cv2.GaussianBlur(m, (0, 0), 25)
ratio = np.where(ws > .02, (num + 1e-3) / (den + 1e-3), np.nan)
fill = np.nanmedian(ratio); ratio = np.nan_to_num(ratio, nan=fill)
ratio = np.clip(cv2.GaussianBlur(ratio, (0, 0), 15), 0.45, 1.5)[..., None]
lit = np.clip(L[..., :3] * ratio, 0, 255)
lit = cv2.GaussianBlur(lit, (0, 0), 0.6)
# soft shadow of the new card on what is behind it
sh = cv2.GaussianBlur(cv2.warpAffine(ca, np.float32([[1, 0, 5], [0, 1, 7]]), (ca.shape[1], ca.shape[0])), (0, 0), 7) * .38
base = reg * (1 - sh[..., None] * (1 - ca[..., None]))
comp = base * (1 - ca[..., None]) + lit * ca[..., None]
# occluders from the photo
yy = np.arange(y1 - y0)[:, None]; xx = np.arange(x1 - x0)[None, :]
rimx = np.float32([0, 190, 290, 390, 490, 590, 670, 770, 820, 970])
rimy = np.float32([840, 835, 825, 802, 770, 745, 730, 722, 725, 735])
bag = (yy > np.interp(xx, rimx, rimy) - 2).astype(np.float32)
pin = np.zeros(ca.shape, np.uint8); cv2.fillPoly(pin, [np.int32([[622, 518], [884, 302], [942, 370], [658, 575]])], 1)
keep = cv2.GaussianBlur(np.maximum(bag, pin), (0, 0), 1.0)[..., None]
comp = reg * keep + comp * (1 - keep)
# a hint of the bag rim's own shadow on the card
rim_sh = np.clip(1 - (yy - (np.interp(xx, rimx, rimy) - 2)) / -14.0, 0, 1) * (yy < np.interp(xx, rimx, rimy)) * ca
comp = comp * (1 - .18 * cv2.GaussianBlur(rim_sh.astype(np.float32), (0, 0), 4)[..., None])
out = photo.copy(); out[y0:y1, x0:x1] = comp
cv2.imwrite(out_name, np.clip(out, 0, 255).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 93])
