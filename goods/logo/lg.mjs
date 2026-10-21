import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'fs';
const L = '/home/user/smithsfarm/goods/logo/';
const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 2000, height: 1050 } });
for (const n of ['주황', '흰색', '검정']) {
  const s = fs.readFileSync(L + `스미스팜_로고_${n}.svg`, 'utf8').replace(/width="[^"]*mm" height="[^"]*mm"/, 'width="2000" height="1050"');
  await p.setContent('<html><body style="margin:0;background:transparent">' + s + '</body></html>');
  await p.screenshot({ path: L + `스미스팜_로고_${n}.png`, omitBackground: true, clip: { x: 0, y: 0, width: 2000, height: 1050 } });
}
await b.close();
