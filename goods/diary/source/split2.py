s=open('diary_print.html').read()
head=s[:s.index('<body>')+len('<body>')]
body=s[s.index('<body>')+len('<body>'):s.index('</body>')]
parts=body.split('<div class="page">')
cover_pages=['<div class="page">'+parts[1].rsplit('</div>',1)[0]+'</div>']
inner='<div class="page">'+parts[2]
inner=inner.replace('#fdfaf2','#ffffff')
keep=lambda t: t.replace('fill="#ffffff" stroke="#','fill="#fff" stroke="#').replace('<g stroke="#ffffff" stroke-width="8">','<g stroke="#fff" stroke-width="8">').replace('<rect x="-6" y="-6" width="200" height="275" fill="#ffffff"/>','<rect x="-6" y="-6" width="200" height="275" fill="#fff"/>')
maps={'preview':{'#7d776c':'#7f7f7f','#cfc9bd':'#d1d1d1','#2a2418':'#231f20','#4a4336':'#474445','#b9b2a2':'#a7a5a6','#2f6b3a':'#2f6b3a','#8fb79a':'#97b59d'},
 'plate1_black':{'#7d776c':'#737373','#cfc9bd':'#cccccc','#2a2418':'#000000','#4a4336':'#333333','#b9b2a2':'#a6a6a6','#2f6b3a':'none','#8fb79a':'none'},
 'plate2_green':{'#7d776c':'none','#cfc9bd':'none','#2a2418':'none','#4a4336':'none','#b9b2a2':'none','#2f6b3a':'#000000','#8fb79a':'#808080'}}
for name,m in maps.items():
    t=keep(inner)
    for a,b in m.items(): t=t.replace('"'+a+'"','"@@'+b+'"')
    open(f'inner_{name}.html','w').write(head+t.replace('@@','')+'\n</body></html>')
open('cover_4c.html','w').write(head+'\n'.join(cover_pages)+'\n</body></html>')
