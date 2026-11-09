import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
await p.goto('http://localhost:8810/wc/wc.html', { waitUntil: 'networkidle' });
await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(800);
await p.pdf({ path: 'wc.pdf', width: '210mm', height: '297mm', printBackground: true, preferCSSPageSize: true });
await b.close();
