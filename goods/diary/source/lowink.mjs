// usage: node lowink.mjs <page html> <out pdf> <w_mm> <h_mm>
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const [page, out, w, h] = process.argv.slice(2);
const b = await chromium.launch(); const p = await b.newPage();
await p.goto(`http://localhost:8800/${page}`, { waitUntil: 'networkidle' });
await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(800);
await p.pdf({ path: out, width: `${w}mm`, height: `${h}mm`, printBackground: true, preferCSSPageSize: true });
await b.close();
