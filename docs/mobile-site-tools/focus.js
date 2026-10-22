// usage: node focus.js <html> <outdir> <w> <h> [reduce]  -- scroll to key moments, shoot mid-animation and after
// Browser path: /opt/pw-browsers/chromium is where Chromium lives in a Claude cloud session.
// On a laptop, delete the executablePath option so Playwright uses its own browser.
const { chromium } = require('playwright');
const [,, file, out, W, H, RED] = process.argv;
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', proxy: process.env.HTTPS_PROXY ? { server: process.env.HTTPS_PROXY } : undefined });
  const ctx = await b.newContext({ viewport: { width: +W, height: +H }, isMobile: +W < 700, hasTouch: +W < 700, reducedMotion: RED ? 'reduce' : 'no-preference' });
  const p = await ctx.newPage(); const errs = [];
  p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  await p.goto('file://' + file, { waitUntil: 'load' });
  await p.waitForTimeout(900); await p.screenshot({ path: `${out}/a-hero-early.png` });
  await p.waitForTimeout(3500); await p.screenshot({ path: `${out}/a-hero-done.png` });
  const at = async (sel, off, name, waits) => {
    await p.evaluate(([s, o]) => { const e = document.querySelector(s); scrollTo(0, scrollY + e.getBoundingClientRect().top + o); }, [sel, off]);
    for (const [ms, tag] of waits) { await p.waitForTimeout(ms); await p.screenshot({ path: `${out}/${name}-${tag}.png` }); }
  };
  // step down the page in small steps first so scroll-driven pieces see a real scroll
  const total = await p.evaluate(() => document.documentElement.scrollHeight);
  const go = async sel => { const y = await p.evaluate(s => scrollY + document.querySelector(s).getBoundingClientRect().top, sel); for (let cur = await p.evaluate(() => scrollY); cur < y - 400; cur += 300) { await p.evaluate(c => scrollTo(0, c), cur); await p.waitForTimeout(40); } };
  // These selectors are the TVS page's key moments. Swap them for your own page's sections.
  await go('.key'); await at('.key', -300, 'b-key', [[700, 'mid'], [3000, 'done']]);
  await go('.way'); await at('.way', -60, 'c-way', [[900, 'mid'], [4200, 'done']]);
  await go('#map-list'); await at('#map-list', -120, 'd-map', [[2000, 'done']]);
  await go('#orbit-list'); await at('#orbit-list', -330, 'e-orbit', [[1000, 'mid'], [3000, 'done']]);
  await at('#orbit-list', 250, 'e-orbit-scroll', [[900, 'x']]);
  await go('#circle'); await at('#circle', -40, 'f-circle', [[2500, 'x']]);
  await at('#circle', 500, 'f-circle-scroll', [[900, 'x']]);
  await go('#jinto'); await at('#jinto', -300, 'g-end', [[3500, 'x']]);
  const pre = await p.evaluate(() => document.querySelectorAll('.pre').length);
  const ow = await p.evaluate(() => document.documentElement.scrollWidth);
  console.log(JSON.stringify({ total, stuckHidden: pre, scrollWidth: ow, errs }));
  await b.close();
})();
