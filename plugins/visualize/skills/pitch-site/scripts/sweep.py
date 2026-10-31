#!/usr/bin/env python3
"""Screenshot sweep for a scroll-told page: frames in scroll order at laptop and tablet sizes, plus checks.

Usage: python sweep.py page.html --out shots/ [--sizes laptop,tablet,ipad,mini,phone] [--live] [--step 0.9] [--max 40]

Writes:
  final-<size>-NN.png   every finished state (?final=1), one frame per --step viewport heights
  live-laptop-NN.png    with --live: real animation at 1280x800, scrolling slowly and waiting at each stop
  phone.png             390x844: must show only the "open on your laptop" gate
Prints: console errors, horizontal overflow (elements past the right edge), class names reused across sections,
the hero check (does anything from the second section show in the first screen), and per laptop screen: more than
80 words, text painted under a line, shape or box, more than one marker, and marker plus accent over 8% of the screen.
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
# One screen, measured (after Hallmark's gates 58, 73 and 23): words on screen, text painted under something else,
# markers on screen, and the share of the screen painted in the marker or an accent.
SCREEN = r'''() => { const H = innerHeight, W = innerWidth, root = getComputedStyle(document.documentElement);
  const rgb = c => (c.match(/[\d.]+/g) || []).map(Number);
  const probe = v => { if (!root.getPropertyValue(v).trim()) return null; const d = document.createElement('i');
    d.style.color = `var(${v})`; document.body.appendChild(d); const c = rgb(getComputedStyle(d).color); d.remove(); return c; };
  const acc = ['--marker', '--accent-1', '--accent-2'].map(v => [v, probe(v)]).filter(a => a[1]);
  const near = (c, a) => c.length >= 3 && (c.length < 4 || c[3] > .5) && Math.abs(c[0]-a[0]) + Math.abs(c[1]-a[1]) + Math.abs(c[2]-a[2]) < 30;
  const SHAPES = new Set(['path','line','polyline','polygon','circle','ellipse','rect','image','use','IMG','VIDEO','CANVAS']);
  const pinned = e => { for (let n = e, i = 0; n && i < 8; n = n.parentElement, i++) { const p = getComputedStyle(n).position; if (p === 'fixed' || p === 'sticky') return true; } return false; };
  const opaque = e => { const s = getComputedStyle(e); return SHAPES.has(e.tagName) || s.backgroundImage !== 'none' || (rgb(s.backgroundColor)[3] ?? 1) > .5
    || [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim()); };
  let words = 0; const covered = new Set();
  const tw = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  for (let t; (t = tw.nextNode());) { const own = t.parentElement, txt = t.textContent.trim();
    if (!txt || !own || own.closest('script,style,noscript,.gate') || !own.checkVisibility({ opacityProperty: true, visibilityProperty: true })) continue;
    const r = document.createRange(); r.selectNodeContents(t); const lines = [...r.getClientRects()].filter(q => q.width > 2 && q.bottom > 0 && q.top < H);
    if (!lines.length) continue;
    const b = r.getBoundingClientRect(); if (b.top + b.height / 2 > 0 && b.top + b.height / 2 < H) words += txt.split(/\s+/).length;
    for (const q of lines) { if (q.top < 0 || q.bottom > H) continue;
      for (const f of [.2, .5, .8]) { const hit = document.elementFromPoint(q.left + q.width * f, q.top + q.height / 2);
        if (!hit || hit === own || own.contains(hit) || hit.contains(own) || pinned(hit) || !opaque(hit)) continue;
        covered.add(`"${txt.slice(0, 30)}" under ${hit.tagName.toLowerCase()}${hit.id ? '#' + hit.id : ''} in #${(own.closest('section') || {}).id || '?'}`); break; } } }
  const marks = [...document.querySelectorAll('mark')].filter(m => { const q = m.getBoundingClientRect(); return q.width && q.bottom > 0 && q.top < H; }).length;
  const area = {}; let n = 0;
  for (let x = W / 64; x < W; x += W / 32) for (let y = H / 40; y < H; y += H / 20) { n++; const e = document.elementFromPoint(x, y); if (!e) continue;
    const s = getComputedStyle(e), paint = [rgb(s.backgroundColor)]; if (e instanceof SVGElement) paint.push(rgb(s.fill));
    for (const [v, a] of acc) if ((v === '--marker' && e.tagName === 'MARK') || paint.some(c => near(c, a))) { area[v] = (area[v] || 0) + 1; break; } }
  const accent = Object.fromEntries(Object.entries(area).map(([v, k]) => [v, Math.round(100 * k / n)]));
  return { words, covered: [...covered], marks, accent }; }'''
WORDS, ACCENT = 80, 8  # per laptop screen: about 80 words, accent and marker together on at most 8% of it


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
            H = pg.evaluate('document.documentElement.scrollHeight'); y = 0; n = 0; screens = []
            while y < H and n < a.max:
                pg.evaluate(f'scrollTo(0,{y})'); pg.wait_for_timeout(250)
                pg.screenshot(path=str(out / f'final-{name}-{n:02d}.png'))
                if name == 'laptop': screens.append(pg.evaluate(SCREEN))
                n += 1; y += int(h * a.step)
            print(f'{name} {w}x{h}: {n} frames, page {H}px; overflow: {pg.evaluate(OVER) or "none"}; console errors: {errs or "none"}')
            if name == 'laptop':
                pg.evaluate('scrollTo(0,0)'); print('hero check:', pg.evaluate(HERO))
                print('classes used in more than one section (fine for one shared component, a bug if two different things share a name):', pg.evaluate(COLLIDE) or 'none')
                tag = lambda i: f'final-laptop-{i:02d}'
                wordy = [f'{tag(i)} ({s["words"]})' for i, s in enumerate(screens) if s['words'] > WORDS]
                print(f'screens over {WORDS} words (one idea per screen; cut words or split the screen):', ', '.join(wordy) or 'none')
                cov = sorted({c for s in screens for c in s['covered']})
                print('text painted under something (move it or give it a paper halo):', '; '.join(cov[:12]) or 'none')
                many = [f'{tag(i)} ({s["marks"]})' for i, s in enumerate(screens) if s['marks'] > 1]
                print('screens with more than one marker (one per screen):', ', '.join(many) or 'none')
                loud = [f'{tag(i)} ({", ".join(f"{k} {v}%" for k, v in s["accent"].items())})' for i, s in enumerate(screens) if sum(s['accent'].values()) > ACCENT]
                print(f'screens over {ACCENT}% marker and accent (colour stops meaning anything):', ', '.join(loud) or 'none')
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
