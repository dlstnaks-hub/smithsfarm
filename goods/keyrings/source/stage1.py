# write plain art SVGs (transparent background) for silhouette tracing
import art, sized
PX = 10
for name, k in (('scarecrow', sized.get('scarecrow')), ('octopus', sized.get('octopus'))):
    w, h = k['w'], k['h']
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{round(w*PX)}" height="{round(h*PX)}" viewBox="0 0 {w} {h}">{k["art"]}</svg>'
    open(f'{name}_art.svg', 'w').write(svg)
