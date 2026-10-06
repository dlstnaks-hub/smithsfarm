# Compose ohprint-style PDFs: same three layers as the carrot file (white / print / cut, magenta 0.05mm)
from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject, DecodedStreamObject, NameObject, DictionaryObject
import json, art
MM = 72/25.4
TEMPLATE = '/root/.claude/uploads/eb5eda96-acad-5762-89cf-9d74948ca0d7/86558b46-ohprint_keyring_03_carrot.pdf'
data = json.load(open('keyrings.json'))

def ring_ops(poly, h, hole):
    o = [f'{x:.3f} {h-y:.3f} {"m" if i==0 else "l"}' for i,(x,y) in enumerate(poly)] + (['h'] if poly else [])
    hx, hy, hr = hole; hy = h - hy; k = 0.5523*hr
    o += [f'{hx+hr:.3f} {hy:.3f} m', f'{hx+hr:.3f} {hy+k:.3f} {hx+k:.3f} {hy+hr:.3f} {hx:.3f} {hy+hr:.3f} c',
          f'{hx-k:.3f} {hy+hr:.3f} {hx-hr:.3f} {hy+k:.3f} {hx-hr:.3f} {hy:.3f} c',
          f'{hx-hr:.3f} {hy-k:.3f} {hx-k:.3f} {hy-hr:.3f} {hx:.3f} {hy-hr:.3f} c',
          f'{hx+k:.3f} {hy-hr:.3f} {hx+hr:.3f} {hy-k:.3f} {hx+hr:.3f} {hy:.3f} c', 'h']
    return ' '.join(o)

import re
def carrot_ops(sc, hole, h):
    # the original carrot outline (PDF y-up) with every coordinate scaled, then the unscaled hole
    toks = re.findall(r'[MCLZ]|-?[\d.]+', art.CARROT_OUT); o = []; cmd = None; nums = []
    def flush():
        if cmd == 'M': o.append(f'{nums[0]*sc:.3f} {nums[1]*sc:.3f} m')
        elif cmd == 'L': o.append(f'{nums[0]*sc:.3f} {nums[1]*sc:.3f} l')
        elif cmd == 'C': o.append(' '.join(f'{v*sc:.3f}' for v in nums) + ' c')
    for t in toks:
        if t in 'MCLZ':
            if cmd: flush()
            cmd, nums = t, []
            if t == 'Z': o.append('h'); cmd = None
        else: nums.append(float(t))
    if cmd: flush()
    ring = ring_ops([], h, hole)
    return ' '.join(o) + ' ' + ring.lstrip(' h')

for name, num in (('carrot', '03'), ('scarecrow', '04'), ('octopus', '05')):
    d = data[name]; w, h = d['w'], d['h']
    path = carrot_ops(d['scale'], d['hole'], h) if name == 'carrot' else ring_ops(d['poly'], h, d['hole'])
    tpl = PdfReader(TEMPLATE); prn = PdfReader(f'{name}_print.pdf').pages[0]
    page = tpl.pages[0]
    top = float(prn.mediabox.height); y0 = top - h*MM
    pc = prn.get_contents().get_data().decode('latin1')
    cx, cy = w/2, h/2
    content = (f'q {MM:.5f} 0 0 {MM:.5f} 0 0 cm\n'
               f'/OC /ocW BDC q 0.99 0 0 0.99 {cx*0.01:.3f} {cy*0.01:.3f} cm 1 1 1 rg {path} f* Q EMC\nQ\n'
               f'/OC /ocP BDC q 1 0 0 1 0 {-y0:.4f} cm {pc} Q EMC\n'
               f'q {MM:.5f} 0 0 {MM:.5f} 0 0 cm\n'
               f'/OC /ocC BDC 0 1 0 0 K 0.1764 w {path} S EMC\nQ\n')
    st = DecodedStreamObject(); st.set_data(content.encode('latin1'))
    w_ = PdfWriter(clone_from=tpl)
    p = w_.pages[0]
    p[NameObject('/Contents')] = w_._add_object(st)
    res = p['/Resources']
    for key, val in prn['/Resources'].items():
        if key == '/ProcSet': continue
        val = val.get_object()
        if key in res and isinstance(val, DictionaryObject):
            for kk, vv in val.items(): res[key].get_object()[kk] = w_._add_object(vv.get_object()) if hasattr(vv, 'get_object') and not isinstance(vv.get_object(), (int, float)) else vv
        else:
            res[NameObject(key)] = val.clone(w_) if hasattr(val, 'clone') else val
    box = RectangleObject([0, 0, w*MM, h*MM])
    for b in ('/MediaBox', '/CropBox', '/BleedBox', '/TrimBox', '/ArtBox'): p[NameObject(b)] = box
    w_.write(f'out/ohprint_keyring_{num}_{name}_130.pdf')
    print(name, w, h)
