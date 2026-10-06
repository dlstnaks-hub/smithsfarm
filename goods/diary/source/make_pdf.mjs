import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await b.newPage();
await p.goto('http://localhost:8800/diary_print.html', { waitUntil: 'networkidle' });
await p.evaluate(() => document.fonts.ready);
await p.waitForTimeout(800);
await p.pdf({ path: 'raw.pdf', width: '154mm', height: '216mm', printBackground: true, preferCSSPageSize: true });
await b.close();
