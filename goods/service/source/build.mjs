// usage: node build.mjs <name> <w_mm> <h_mm>  -> <name>_raw.pdf (served from localhost:8803 so the fonts load)
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const [name, w, h] = process.argv.slice(2);
const b = await chromium.launch(); const p = await b.newPage();
await p.goto(`http://localhost:8803/${name}.html`, { waitUntil: 'networkidle' });
await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(500);
await p.pdf({ path: `${name}_raw.pdf`, width: `${w}mm`, height: `${h}mm`, printBackground: true, preferCSSPageSize: true });
await b.close();
