// one transparent 600dpi PNG per pick page
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'fs';
const names = fs.readFileSync('picks_names.txt', 'utf8').trim().split('\n').map(l => l.split('\t')[0]);
const px = Math.round(100 / 25.4 * 600);
const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: px, height: px } });
await p.goto('http://localhost:8803/picks.html', { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready);
await p.addStyleTag({ content: `.page{width:${px}px!important;height:${px}px!important} svg.sheet{width:${px}px!important;height:${px}px!important}` });
await p.waitForTimeout(400);
const pages = await p.$$('.page');
for (let i = 0; i < pages.length; i++) await pages[i].screenshot({ path: `pick_${names[i]}.png`, omitBackground: true });
await b.close();
