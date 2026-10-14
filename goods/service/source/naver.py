# Naver post images from a 94x54 card PDF (2mm bleed): render the trim area straight from the vector PDF at the
# target pixel size, so nothing is up- or down-scaled. usage: naver.py <card.pdf> <out prefix> <workdir>
import subprocess, sys
from PIL import Image, ImageFilter, ImageDraw
pdf, out, work = sys.argv[1:4]
BG = (231, 225, 210, 255)
def card(page, trim_w):
    subprocess.run(['pdftoppm', '-r', f'{trim_w/90*25.4:.3f}', '-f', str(page), '-l', str(page), '-png', '-singlefile', pdf, f'{work}/nv'], check=True)
    im = Image.open(f'{work}/nv.png').convert('RGB'); b = round(2/90*trim_w)
    return im.crop((b, b, b+trim_w, b+round(trim_w*50/90)))
def put(canvas, im, x, y, r=18):
    sh = Image.new('RGBA', canvas.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((x+6, y+14, x+im.width+6, y+im.height+14), r, fill=(60, 50, 30, 70))
    canvas.alpha_composite(sh.filter(ImageFilter.GaussianBlur(18)))
    m = Image.new('L', im.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, im.width-1, im.height-1), r, fill=255)
    canvas.paste(im, (x, y), m)
def stacked(W, H, cw):
    a, b = card(1, cw), card(2, cw); c = Image.new('RGBA', (W, H), BG)
    gap = (H - a.height - b.height) // 3
    put(c, a, (W-cw)//2, gap); put(c, b, (W-cw)//2, gap*2 + a.height)
    return c.convert('RGB')
stacked(1080, 1080, 880).save(f'{out}_1080x1080.png')
stacked(1080, 1350, 960).save(f'{out}_1080x1350.png')
