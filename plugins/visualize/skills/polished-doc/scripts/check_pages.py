#!/usr/bin/env python3
"""Flag PDF pages that waste space: short pages and big blank gaps.

Usage:
  python check_pages.py doc.pdf                 # report only
  python check_pages.py doc.pdf --sheets out/   # also write two-page PNG sheets to look at
  python check_pages.py doc.pdf --allow 1       # exempt page 1, only when it is a cover page

A page is SHORT when its content ends above --min-fill of the usable height (default 0.75).
A page has a GAP when a blank band inside its content is taller than --max-gap of the
usable height (default 0.22). The last page may be short, but under --min-last
(default 0.25) it is a STRAGGLER: a few lines spilled over and should be pulled back.
Needs pypdfium2 and Pillow (pip install pypdfium2 pillow).
"""
import argparse
import os
import sys

try:
    import pypdfium2 as pdfium
    from PIL import Image
except ImportError:
    sys.exit("Install the checker's dependencies: pip install pypdfium2 pillow")


def rows_with_ink(img, left, right, top, bottom, thresh=242):
    g = img.convert("L")
    w, _ = g.size
    px = g.load()
    ink = []
    for y in range(top, bottom):
        hit = False
        for x in range(left, right, 2):
            if px[x, y] < thresh:
                hit = True
                break
        ink.append(hit)
    return ink


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("--min-fill", type=float, default=0.75)
    ap.add_argument("--max-gap", type=float, default=0.22)
    ap.add_argument("--min-last", type=float, default=0.25, help="smallest fill allowed on the last page")
    ap.add_argument("--allow", type=int, nargs="*", default=[], help="1-based pages exempt from the checks (a cover, a deliberate closing page)")
    ap.add_argument("--sheets", help="folder for two-page PNG sheets")
    ap.add_argument("--margin-top", type=float, default=0.06, help="share of page height above content")
    ap.add_argument("--margin-bottom", type=float, default=0.08, help="share of page height for footer zone")
    a = ap.parse_args()

    doc = pdfium.PdfDocument(a.pdf)
    n = len(doc)
    imgs, problems = [], []
    for i in range(n):
        img = doc[i].render(scale=0.6).to_pil().convert("RGB")
        imgs.append(img)
        w, h = img.size
        top, bottom = int(h * a.margin_top), int(h * (1 - a.margin_bottom))
        ink = rows_with_ink(img, int(w * 0.05), int(w * 0.95), top, bottom)
        usable = bottom - top
        last = max((k for k, v in enumerate(ink) if v), default=0)
        fill = last / usable
        gap = run = 0
        for v in ink[: last + 1]:
            run = 0 if v else run + 1
            gap = max(gap, run)
        page = i + 1
        notes = []
        if fill < a.min_fill and page != n and page not in a.allow:
            notes.append(f"SHORT: content ends at {fill:.0%} of the page")
        if page == n and n > 1 and fill < a.min_last:
            notes.append(f"STRAGGLER: the last page holds only {fill:.0%}; pull it back or add to it")
        if gap / usable > a.max_gap and page not in a.allow:
            notes.append(f"GAP: blank band of {gap / usable:.0%} inside the content")
        status = "; ".join(notes) if notes else "ok"
        print(f"page {page:>3}: fill {fill:4.0%}  biggest gap {gap / usable:4.0%}  {status}")
        if notes:
            problems.append(page)

    if a.sheets:
        os.makedirs(a.sheets, exist_ok=True)
        for k in range(0, n, 2):
            pair = imgs[k:k + 2]
            sheet = Image.new("RGB", (sum(p.width for p in pair) + 10 * (len(pair) - 1), pair[0].height), "#888")
            x = 0
            for p in pair:
                sheet.paste(p, (x, 0))
                x += p.width + 10
            sheet.save(os.path.join(a.sheets, f"pages-{k + 1:02d}-{k + len(pair):02d}.png"))
        print(f"sheets written to {a.sheets}")

    print(f"{len(problems)} page(s) to fix: {problems}" if problems else "all pages pass")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
