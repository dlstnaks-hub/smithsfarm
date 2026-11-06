import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage({viewport:{width:1800,height:780}});
await p.goto('http://localhost:8810/part/compare.html', { waitUntil: 'networkidle' });
await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(800);
await p.screenshot({ path: 'compare.png', fullPage: true });
await b.close();
