// Cloud-session stand-in for render_png.py (added by Ash's ash-skills): uses the Node Playwright
// that cloud containers ship with. Writes <out>.png (light) and <out>-dark.png, square corners.
//   node scripts/render_png.js out.html out.png [scale=2] [selector=.canvas]
const { chromium } = require('playwright');
const path = require('path');
const [,, src, out, scale = '2', sel = '.canvas'] = process.argv;
(async () => {
  const b = await chromium.launch();
  for (const theme of ['light', 'dark']) {
    const p = await b.newPage({ deviceScaleFactor: +scale, viewport: { width: 1600, height: 1200 } });
    await p.goto('file://' + path.resolve(src));
    await p.evaluate(t => { if (t === 'dark') document.documentElement.dataset.theme = 'dark'; }, theme);
    await p.addStyleTag({ content: '.scroller,.canvas{border-radius:0!important}' });
    await p.waitForTimeout(300);
    const file = theme === 'light' ? out : out.replace(/\.png$/, '-dark.png');
    await (await p.$(sel)).screenshot({ path: file });
    console.log(file);
    await p.close();
  }
  await b.close();
})();
