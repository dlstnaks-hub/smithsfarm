import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage();
for (const n of ['3d','abs','real']) {
  await p.goto(`http://localhost:8810/bill/page_${n}.html`, { waitUntil: 'networkidle' }); await p.waitForTimeout(500);
  await p.pdf({ path: `page_${n}.pdf`, width: '210mm', height: '297mm', printBackground: true });
}
await b.close();
