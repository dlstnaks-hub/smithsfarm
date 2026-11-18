import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const [src, out, w, h, scale] = process.argv.slice(2);
const b = await chromium.launch(); const p = await b.newPage({viewport:{width:+w,height:+h}, deviceScaleFactor:+(scale||1)});
await p.goto(`http://localhost:8810/bill/${src}`, { waitUntil: 'networkidle' });
await p.evaluate(() => document.fonts && document.fonts.ready); await p.waitForTimeout(300);
await p.screenshot({ path: out, omitBackground: true });
await b.close();
