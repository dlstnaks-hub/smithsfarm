import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1800, height: 900 }, deviceScaleFactor: 1.5 });
await p.goto('http://localhost:8803/valet_fonts.html', { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(600);
console.log(await p.evaluate(() => [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family + ' ' + f.weight).filter((v, i, a) => a.indexOf(v) === i).join(', ')));
await p.screenshot({ path: 'valet_fonts.png', fullPage: true }); await b.close();
