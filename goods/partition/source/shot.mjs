import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage({viewport:{width:1587,height:1123}, deviceScaleFactor:2});
await p.goto('http://localhost:8810/part/drawing.html', { waitUntil: 'networkidle' });
await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(800);
await p.pdf({ path: 'drawing.pdf', width: '420mm', height: '297mm', printBackground: true });
await p.screenshot({ path: 'drawing.png', clip:{x:0,y:0,width:1587,height:1123} });
await b.close();
