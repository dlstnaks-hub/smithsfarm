import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 800 }, deviceScaleFactor: 2 });
await p.goto('http://localhost:8803/dishes.html', { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(400);
await p.screenshot({ path: 'dishes.png', fullPage: true }); await b.close();
