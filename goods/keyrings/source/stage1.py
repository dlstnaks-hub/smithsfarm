# write plain art SVGs (transparent background) for silhouette tracing
import art
PX = 10
for name, k in (('scarecrow', art.SCARECROW), ('octopus', art.OCTOPUS)):
    w, h = k['w'], k['h']
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{w*PX}" height="{h*PX}" viewBox="0 0 {w} {h}">{k["art"]}</svg>'
    open(f'{name}_art.svg', 'w').write(svg)
