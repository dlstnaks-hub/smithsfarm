import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
await p.goto('http://localhost:8801/diary_spread.html', { waitUntil: 'networkidle' });
await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(800);
await p.pdf({ path: 'spread.pdf', width: '297mm', height: '210mm', printBackground: true, preferCSSPageSize: true });
await b.close();
