#!/usr/bin/env python3
"""Assemble a proposal site: work/starter.html + work/frag-*.html (in name order) -> work/index.html.

Usage:
  python build.py work/                          index.html (publish this) + preview/index.html (doctype-wrapped)
  python build.py work/ --only frag-3 --out test-B.html    starter + matching fragments only, for one builder
  python build.py work/ --motif kit.js,kolam.js  splice motif scripts (from work/ or the skill's assets/motifs/) into /*MOTIF*/

Prints the size, the fragment count, and the number of em or en dashes in the copy (must be 0).
"""
import argparse, pathlib, re

SKILL = pathlib.Path(__file__).resolve().parent.parent
ap = argparse.ArgumentParser(); ap.add_argument('work'); ap.add_argument('--only', nargs='*')
ap.add_argument('--out', default='index.html'); ap.add_argument('--motif', default='')
a = ap.parse_args()
W = pathlib.Path(a.work)
frags = sorted(W.glob('frag-*.html'))
if a.only:
    frags = [f for f in frags if any(f.name.startswith(o) for o in a.only)]
page = (W / 'starter.html').read_text(encoding='utf-8')
left = re.findall(r'\{\{[^}]*\}\}', page)
if left:
    print('WARNING: unfilled starter placeholders:', ', '.join(sorted(set(x[:40] for x in left))))
if a.motif:
    code = []
    for name in a.motif.split(','):
        p = W / name
        if not p.exists():
            p = SKILL / 'assets' / 'motifs' / name
        code.append(p.read_text(encoding='utf-8'))
    page = page.replace('/*MOTIF*/', '\n'.join(code))
page = page.replace('<!--@@SECTIONS-->', '\n'.join(f.read_text(encoding='utf-8') for f in frags))
out = W / a.out
wrapped = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" '
           'content="width=device-width, initial-scale=1, viewport-fit=cover"></head><body>\n' + page + '\n</body></html>')
if a.out == 'index.html':
    out.write_text(page, encoding='utf-8')
    (W / 'preview').mkdir(exist_ok=True); (W / 'preview' / 'index.html').write_text(wrapped, encoding='utf-8')
else:
    out.write_text(wrapped, encoding='utf-8')
copy = re.sub(r'<script.*?</script>|<style.*?</style>', '', '\n'.join(f.read_text(encoding='utf-8') for f in frags), flags=re.S)
dash = len(re.findall('[—–]', copy))
print(f'{out.name}: {len(page):,} bytes, {len(frags)} fragments, em/en dashes in copy: {dash}')
