"""Phone screenshots for references/phone.md: one 390x844 frame per section (scroll) or slide (flip), plus sheet.jpg.
Usage: python phone_shots.py URL OUTDIR [--mode scroll|flip] [--dark] [--w 390 --h 844]"""
import argparse, pathlib, subprocess
from playwright.sync_api import sync_playwright
ap = argparse.ArgumentParser(); ap.add_argument('url'); ap.add_argument('out'); ap.add_argument('--mode', default='scroll')
ap.add_argument('--dark', action='store_true'); ap.add_argument('--w', type=int, default=390); ap.add_argument('--h', type=int, default=844)
a = ap.parse_args(); out = pathlib.Path(a.out); out.mkdir(parents=True, exist_ok=True)
for f in out.glob('*.png'): f.unlink()
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width': a.w, 'height': a.h}, device_scale_factor=2, is_mobile=True, has_touch=True,
                    color_scheme='dark' if a.dark else 'light')
    errs = []; pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' else None); pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(a.url); pg.wait_for_timeout(1500)
    if a.mode == 'scroll':
        tops = pg.evaluate("[...document.querySelectorAll('main > section')].map(s => s.offsetTop)")
        for i, t in enumerate(tops):
            pg.evaluate(f"window.scrollTo(0,{t})"); pg.wait_for_timeout(2600)
            pg.screenshot(path=str(out / f'{i:02d}.png'))
    else:
        n = pg.evaluate("document.querySelectorAll('[class*=deck] > .slide').length")
        for i in range(n):
            pg.evaluate(f"window.__go && window.__go({i})"); pg.wait_for_timeout(1800)
            pg.screenshot(path=str(out / f'{i:02d}.png'))
    over = pg.evaluate("document.documentElement.scrollWidth > innerWidth")
    words = pg.evaluate("document.body.innerText.split(/\s+/).filter(Boolean).length")
    print('errors:', errs or 'none', '| horizontal overflow:', over, '| words:', words)
    b.close()
shots = sorted(out.glob('[0-9][0-9].png'))
cols = min(6, len(shots))
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-pattern_type', 'sequence', '-i', str(out / '%02d.png'), '-vf',
                f'scale=300:-1,tile={cols}x{(len(shots)+cols-1)//cols}:padding=6:color=gray', '-frames:v', '1', str(out / 'sheet.jpg')], check=True)
print('sheet:', out / 'sheet.jpg', len(shots), 'frames')
