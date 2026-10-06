import { chromium } from 'playwright';
const b = await chromium.launch(); const p = await b.newPage();
for (const n of ['cover_4c','inner_preview','inner_plate1_black','inner_plate2_green']) {
  await p.goto('http://localhost:8800/'+n+'.html', { waitUntil:'networkidle' });
  await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(500);
  await p.pdf({ path:'raw_'+n+'.pdf', width:'154mm', height:'216mm', printBackground:true, preferCSSPageSize:true });
}
await b.close();
