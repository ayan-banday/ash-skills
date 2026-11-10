// Screenshot every card of a built deck on a 390 by 844 phone, and report what breaks the
// one-card-per-screen rule. The Ask pane needs claude.ai, so check it on the published link. Plain Playwright (pre-installed in cloud sessions; elsewhere `npm i playwright`).
//
//   node scripts/deck_shots.js <deck>.html <outdir>
//
// Prints one line per problem and exits 1 if any: a card taller than the screen (Ash would have to scroll),
// sideways scroll, text under the island, text smaller than 12px, a drawing label cut off at its edge, dead space (content under half the card). Shots: <outdir>/card-NN.png.
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const [deck, out] = process.argv.slice(2);
  if (!deck || !out) { console.error('usage: node deck_shots.js <deck>.html <outdir>'); process.exit(2); }
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 1, hasTouch: true });
  const errors = [];
  page.on('pageerror', e => errors.push('script error: ' + e.message));
  await page.goto('file://' + path.resolve(deck));
  await page.evaluate(() => { try { localStorage.clear(); } catch (e) {} });
  await page.reload();
  await page.waitForTimeout(400);
  const kinds = await page.evaluate(() => [...document.querySelectorAll('template.card')].map(t => t.dataset.kind));
  const n = kinds.length;
  const bad = [...errors];
  for (let i = 0; i < n; i++) {
    await page.waitForTimeout(260);
    const r = await page.evaluate(() => {
      const card = document.querySelector('.card'), dot = card.querySelector('.dot');
      const h = card.querySelector('h1,h2');
      const out = { heading: h ? h.textContent.trim().slice(0, 50) : '(none)' };
      out.tall = document.documentElement.scrollHeight - window.innerHeight;
      out.wide = document.documentElement.scrollWidth - window.innerWidth;
      const d = dot.getBoundingClientRect();
      out.under = [...card.querySelectorAll('p,li,.stop,.ba div,.keyline,.board,.qs,.chips,summary')].filter(el => {
        const b = el.getBoundingClientRect();
        if (el.tagName !== 'SUMMARY' && el.closest('details:not([open])')) return false;  // folded sources take no room
        return b.height && b.bottom > d.top + 2 && b.top < d.bottom && b.right > d.left && b.left < d.right;
      }).length;
      out.tiny = [...card.querySelectorAll('*')].filter(el => el.childNodes.length && [...el.childNodes].some(c => c.nodeType === 3 && c.textContent.trim())
        && el.closest('svg') === null && parseFloat(getComputedStyle(el).fontSize) < 12).length;
      out.svgTiny = [...card.querySelectorAll('svg text')].filter(t => {
        const s = t.closest('svg'), vb = s.viewBox.baseVal, k = s.getBoundingClientRect().width / (vb.width || 1);
        return parseFloat(t.getAttribute('font-size') || 14) * k < 11;
      }).length;
      // dead space: how far down the card, above the island, the content reaches
      const cb = card.getBoundingClientRect(), kids = [...card.children].filter(el => !el.classList.contains('dot'));
      const last = Math.max(...kids.map(el => el.getBoundingClientRect().bottom));
      out.fill = Math.round((last - cb.top) / (cb.height - 64) * 100);
      out.cut = [...card.querySelectorAll('svg text')].filter(t => {
        const vb = t.closest('svg').viewBox.baseVal, b = t.getBBox();
        return b.x < vb.x - 1 || b.y < vb.y - 1 || b.x + b.width > vb.x + vb.width + 1 || b.y + b.height > vb.y + vb.height + 1;
      }).map(t => t.textContent.trim().slice(0, 30));
      return out;
    });
    const tag = `card ${String(i + 1).padStart(2, '0')} "${r.heading}"`;
    if (r.tall > 0) bad.push(`${tag}: ${r.tall}px taller than the phone screen`);
    if (r.wide > 0) bad.push(`${tag}: ${r.wide}px sideways scroll`);
    if (r.under) bad.push(`${tag}: ${r.under} block(s) under the island`);
    if (r.tiny) bad.push(`${tag}: ${r.tiny} text element(s) under 12px`);
    // every card fills at least half, the promise too (Ash, 2026-11-10: the first two cards left the page empty)
    if (r.fill < 50) bad.push(`${tag}: dead space, the content fills ${r.fill}% of the card; draw bigger, use p.big, or cut the card`);
    if (r.cut.length) bad.push(`${tag}: drawing label(s) cut off at the edge: ${r.cut.join(' | ')}`);
    if (r.svgTiny) bad.push(`${tag}: ${r.svgTiny} drawing label(s) under 11px on screen`);
    await page.screenshot({ path: path.join(out, `card-${String(i + 1).padStart(2, '0')}.png`), fullPage: true });
    if (i < n - 1) await page.keyboard.press('ArrowRight');
  }
  bad.push(...errors.filter(e => !bad.includes(e)));
  console.log(bad.length ? bad.join('\n') : `ok: ${n} cards fit a 390 by 844 screen`);
  await browser.close();
  process.exit(bad.length ? 1 : 0);
})();
