import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1170, height: 2532 } });
for (const k of ['jua', 'black']) {
  await p.goto(`http://localhost:8803/valet_phone_${k}.html`, { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready);
  await p.addStyleTag({ content: '.page,svg.sheet{width:1170px!important;height:2532px!important}' }); await p.waitForTimeout(400);
  await p.screenshot({ path: `valet_phone_${k}.png`, clip: { x: 0, y: 0, width: 1170, height: 2532 } });
}
await b.close();
