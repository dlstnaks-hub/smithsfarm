import { chromium } from 'playwright';
const b = await chromium.launch(); const p = await b.newPage();
await p.goto('http://localhost:8800/test_a5.html', { waitUntil:'networkidle' });
await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(500);
await p.pdf({ path:'out3/스씨네그림일기_A5_테스트인쇄용.pdf', width:'210mm', height:'297mm', printBackground:true, preferCSSPageSize:true });
await b.close();
