import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'fs';
const b = await chromium.launch(); const p = await b.newPage();
await p.setContent(fs.readFileSync('bg.html','utf8'));
await p.pdf({ path: 'bg.pdf', width: '94mm', height: '54mm', printBackground: true, preferCSSPageSize: true });
await b.close();
