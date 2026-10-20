#!/usr/bin/env python3
"""Screenshot sweep for a scroll-told page: frames in scroll order at laptop and tablet sizes, plus checks.

Usage: python sweep.py page.html --out shots/ [--sizes laptop,tablet,ipad,mini,phone] [--live] [--step 0.9] [--max 40]

Writes:
  final-<size>-NN.png   every finished state (?final=1), one frame per --step viewport heights
  live-laptop-NN.png    with --live: real animation at 1280x800, scrolling slowly and waiting at each stop
  phone.png             390x844: must show only the "open on your laptop" gate
Prints: console errors, horizontal overflow (elements past the right edge), class names reused across sections,
and the hero check (does anything from the second section show in the first screen).
Run with plain python (python -I hides Playwright).
"""
import argparse, pathlib
from playwright.sync_api import sync_playwright

SIZES = {'laptop': (1280, 800), 'tablet': (1024, 768), 'ipad': (768, 1024), 'mini': (744, 1133), 'phone': (390, 844)}
COLLIDE = r'''() => { const single = new Set();
  for (const ss of document.styleSheets) { let rules; try { rules = ss.cssRules } catch (e) { continue }
    const walk = rs => { for (const r of rs) { if (r.cssRules && !r.selectorText) walk(r.cssRules);
      else if (r.selectorText) r.selectorText.split(',').forEach(s => { const m = s.trim().match(/^\.([\w-]+)(?:::?[\w-]+(?:\([^)]*\))?)*$/); if (m) single.add(m[1]); }); } };
    walk(rules); }
  const shared = new Set(['band','wrap','lede','label','hand','chip','chips','rv','in','ln','thin','hid','cl','guide','red','cyan','svg-label','svg-hand','btn','badge','js','phone','gate','band-head','paper','card','dark','t1','t2','t3','part','lit']);
  const out = {}; single.forEach(c => { if (shared.has(c) || /^c-/.test(c)) return;
    const ctx = new Set([...document.getElementsByClassName(c)].map(e => (e.closest('section,header,footer,.gate') || {}).id || '?'));
    if (ctx.size > 1) out[c] = [...ctx]; }); return out; }'''
OVER = r'''() => { const W = document.documentElement.clientWidth;
  return [...document.querySelectorAll('main *')].filter(e => { const r = e.getBoundingClientRect(); return r.width && r.right > W + 1 && getComputedStyle(e).position !== 'fixed'; })
   .slice(0, 8).map(e => (e.closest('section') || {}).id + ' ' + e.tagName.toLowerCase() + '.' + String(e.className && e.className.baseVal !== undefined ? e.className.baseVal : e.className).split(' ')[0]); }'''
HERO = r'''() => { const top = [...document.querySelectorAll('section')].filter(s => !s.parentElement.closest('section'))
    .map(s => ({ s, r: s.getBoundingClientRect() })).filter(o => o.r.height > 0).sort((a, b) => a.r.top - b.r.top);
  if (top.length < 2) return 'only one section';
  const first = top.find(o => o.r.top <= 1 && o.r.bottom > 1) || top[0];
  const next = top.find(o => o.r.top >= first.r.bottom - 1);
  if (!next) return 'ok'; const t = next.r.top;
  return t < innerHeight - 1 ? `next section shows ${Math.round(innerHeight - t)}px into the first screen` : 'ok'; }'''


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('html'); ap.add_argument('--out', default='shots')
    ap.add_argument('--sizes', default='laptop,tablet,ipad,phone'); ap.add_argument('--live', action='store_true')
    ap.add_argument('--step', type=float, default=0.9); ap.add_argument('--max', type=int, default=40)
    a = ap.parse_args()
    out = pathlib.Path(a.out); out.mkdir(parents=True, exist_ok=True)
    base = pathlib.Path(a.html).resolve().as_uri()
    with sync_playwright() as p:
        b = p.chromium.launch()
        for name in a.sizes.split(','):
            w, h = SIZES[name]
            ctx = b.new_context(viewport={'width': w, 'height': h}, has_touch=(name == 'phone'), is_mobile=(name == 'phone'))
            pg = ctx.new_page(); errs = []
            pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' else None)
            pg.on('pageerror', lambda e: errs.append(str(e)))
            if name == 'phone':
                pg.goto(base); pg.wait_for_timeout(600); pg.screenshot(path=str(out / 'phone.png'))
                gate = pg.evaluate("() => { const g = document.querySelector('.gate'); return g && getComputedStyle(g).display !== 'none' }")
                print(f'phone 390x844: gate {"shown" if gate else "NOT SHOWN"}; console errors: {errs or "none"}')
                ctx.close(); continue
            pg.goto(base + '?final=1'); pg.wait_for_timeout(900)
            H = pg.evaluate('document.documentElement.scrollHeight'); y = 0; n = 0
            while y < H and n < a.max:
                pg.evaluate(f'scrollTo(0,{y})'); pg.wait_for_timeout(250)
                pg.screenshot(path=str(out / f'final-{name}-{n:02d}.png')); n += 1; y += int(h * a.step)
            print(f'{name} {w}x{h}: {n} frames, page {H}px; overflow: {pg.evaluate(OVER) or "none"}; console errors: {errs or "none"}')
            if name == 'laptop':
                pg.evaluate('scrollTo(0,0)'); print('hero check:', pg.evaluate(HERO))
                print('classes used in more than one section (fine for one shared component, a bug if two different things share a name):', pg.evaluate(COLLIDE) or 'none')
            ctx.close()
        if a.live:
            ctx = b.new_context(viewport={'width': 1280, 'height': 800}); pg = ctx.new_page()
            pg.goto(base); pg.wait_for_timeout(3800)
            H = pg.evaluate('document.documentElement.scrollHeight'); y = 0; n = 0
            while y < H and n < a.max:
                pg.mouse.wheel(0, 0 if n == 0 else int(800 * a.step)); pg.wait_for_timeout(1600)
                pg.screenshot(path=str(out / f'live-laptop-{n:02d}.png')); n += 1; y += int(800 * a.step)
            print(f'live laptop: {n} frames')
            ctx.close()
        b.close()


if __name__ == '__main__':
    main()
