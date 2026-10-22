// usage: node shoot.js <html> <outdir> <w> <h> [step] [reduce]
// Browser path: /opt/pw-browsers/chromium is where Chromium lives in a Claude cloud session.
// On a laptop, delete the executablePath option so Playwright uses its own browser.
const { chromium } = require('playwright');
const [,, file, out, W, H, STEP, RED] = process.argv;
(async () => {
  const proxy = process.env.HTTPS_PROXY ? { server: process.env.HTTPS_PROXY } : undefined;
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', proxy, args: ['--ignore-certificate-errors'] });
  const ctx = await b.newContext({ viewport: { width: +W, height: +H }, deviceScaleFactor: 1, isMobile: +W < 700, hasTouch: +W < 700, reducedMotion: RED ? 'reduce' : 'no-preference' });
  const p = await ctx.newPage();
  const errs = []; p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  await p.goto('file://' + file, { waitUntil: 'load' }); await p.waitForTimeout(4500);
  const total = await p.evaluate(() => document.documentElement.scrollHeight);
  const step = +(STEP || H * 0.8); let i = 0;
  for (let y = 0; y < total; y += step) {
    await p.evaluate(y => window.scrollTo(0, y), y); await p.waitForTimeout(1300);
    await p.screenshot({ path: `${out}/${String(i++).padStart(3, '0')}.png` });
  }
  const ow = await p.evaluate(() => [document.documentElement.scrollWidth, innerWidth]);
  console.log(JSON.stringify({ total, shots: i, overflow: ow, errs }));
  await b.close();
})();
