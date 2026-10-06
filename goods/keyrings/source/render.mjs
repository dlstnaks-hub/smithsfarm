import { chromium } from 'playwright';
import fs from 'fs';
const [mode, ...names] = process.argv.slice(2);
const b = await chromium.launch(); const p = await b.newPage();
for (const n of names) {
  const svg = fs.readFileSync(n + (mode==='png' ? '_art.svg' : '_print.svg'), 'utf8');
  if (mode === 'png') {
    const w = +svg.match(/width="([\d.]+)"/)[1], h = +svg.match(/height="([\d.]+)"/)[1];
    await p.setViewportSize({ width: Math.ceil(w), height: Math.ceil(h) });
    await p.setContent('<html><body style="margin:0;background:transparent">' + svg + '</body></html>');
    await p.screenshot({ path: n + '_alpha.png', omitBackground: true, clip: { x:0, y:0, width:w, height:h } });
  } else {
    const w = svg.match(/data-w="([\d.]+)"/)[1], h = svg.match(/data-h="([\d.]+)"/)[1];
    await p.setContent('<html><head><style>@page{size:'+w+'mm '+h+'mm;margin:0} html,body{margin:0} svg{display:block}</style></head><body>' + svg + '</body></html>');
    await p.pdf({ path: n + '_print.pdf', width: w+'mm', height: h+'mm', printBackground: true, preferCSSPageSize: true });
  }
}
await b.close();
