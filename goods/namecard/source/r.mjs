import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
await p.goto('http://localhost:8802/back.html', { waitUntil: 'networkidle' });
await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(600);
await p.pdf({ path: 'back.pdf', width: '90mm', height: '50mm', printBackground: true, preferCSSPageSize: true });
await b.close();
