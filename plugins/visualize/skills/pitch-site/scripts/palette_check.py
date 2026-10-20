#!/usr/bin/env python3
"""Contrast check for a direction's tokens (WCAG 2.x). Reads the :root token block of a starter or page.

Usage: python palette_check.py work/starter.html
Checks every text pair the pages use: ink and muted on paper, card and each tint; paper on ground and ground-2;
ink on marker; accents on paper. Body text needs 4.5:1; large text and lines 3:1. Also flags any green hue
(OKLCH-ish hue 100 to 210 with real chroma), which Ash does not want. Exit 1 on a failure.
"""
import re, sys, colorsys


def hexrgb(h):
    h = h.strip().lstrip('#')
    if len(h) == 3: h = ''.join(c * 2 for c in h)
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def lum(rgb):
    f = lambda c: c / 12.92 if c <= .04045 else ((c + .055) / 1.055) ** 2.4
    r, g, b = map(f, rgb); return .2126 * r + .7152 * g + .0722 * b


def ratio(a, b):
    la, lb = sorted([lum(hexrgb(a)), lum(hexrgb(b))], reverse=True); return (la + .05) / (lb + .05)


def main():
    src = open(sys.argv[1], encoding='utf-8').read()
    root = re.search(r':root\s*\{(.*?)\}', src, re.S).group(1)
    tok = dict(re.findall(r'--([\w-]+)\s*:\s*(#[0-9A-Fa-f]{3,6})', root))
    # per-band overrides such as .band.t1{--muted:#57534E}
    over = {}
    for sel, body in re.findall(r'(\.band\.[\w.,\s]+)\{([^}]*)\}', src):
        for k, v in re.findall(r'--([\w-]+)\s*:\s*(#[0-9A-Fa-f]{3,6})', body):
            for s in sel.split(','):
                over.setdefault(s.strip().split('.')[-1], {})[k] = v
    bands = {'paper': 'paper', 'card': 'card', 't1': 'tint-1', 't2': 'tint-2', 't3': 'tint-3'}
    fails = 0
    def check(fg, bg, need, label):
        nonlocal fails
        if fg not in tok and not fg.startswith('#'): return
        if bg not in tok and not bg.startswith('#'): return
        f = tok.get(fg, fg); b = tok.get(bg, bg); r = ratio(f, b)
        ok = r >= need; fails += not ok
        print(f"{'ok  ' if ok else 'FAIL'} {r:5.2f}:1 (need {need}) {label}")
    for band, bg in bands.items():
        for fg, need in [('ink', 4.5), ('muted', 4.5), ('red', 4.5)]:
            col = over.get(band, {}).get(fg, tok.get(fg))
            if col: check(col, bg, need, f'{fg} on {band} band')
    for bg in ['ground', 'ground-2']:
        check('paper', bg, 4.5, f'paper on {bg}')
        check('marker', bg, 3, f'marker on {bg} (lines, pills)')
    check('ink', 'marker', 4.5, 'ink on marker (highlighted text)')
    for k, v in tok.items():
        r, g, b = hexrgb(v); h, l, s = colorsys.rgb_to_hls(r, g, b)
        if 100 / 360 <= h <= 175 / 360 and s > .12 and .08 < l < .95:
            print(f'FAIL green-ish token --{k}: {v} (Ash does not want green)'); fails += 1
    print('palette: clean' if not fails else f'palette: {fails} failure(s)')
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main())
