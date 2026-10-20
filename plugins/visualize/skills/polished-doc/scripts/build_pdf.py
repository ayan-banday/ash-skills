#!/usr/bin/env python3
"""Render a Clear Documents HTML file to a paged PDF with a footer.

Usage:
  python build_pdf.py doc.html doc.pdf
  python build_pdf.py doc.html doc.pdf --seed 9 --footer "Onboarding plan · draft"
  python build_pdf.py doc.html doc.pdf --size Letter
  python build_pdf.py doc.html doc.pdf --seed 9 --harmony analogous --hue 210 --save-html final.html

What it does, in order:
  1. --seed N: runs palette.py and swaps the CSS between /* PALETTE START */ and
     /* PALETTE END */ for that palette. Without --seed the file's own palette is kept.
  2. Runs keepnext.py in memory, so no heading is stranded at a page bottom.
  3. Prints with headless Chromium (Playwright), backgrounds on, footer with page numbers.
Then run check_pages.py on the PDF.

Needs: pip install playwright && python -m playwright install chromium
(falls back to an installed Microsoft Edge if Chromium is missing).
"""
import argparse
import asyncio
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import keepnext  # noqa: E402

FOOTER = ('<div style="width:100%;font-family:Segoe UI,Arial,sans-serif;font-size:7.5pt;color:#59636a;'
          'padding:0 17mm;display:flex;justify-content:space-between">'
          '<span>{text}</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>')


def apply_palette(html, seed, hue=None, harmony=None):
    cmd = [sys.executable, str(HERE / "palette.py"), "--seed", str(seed), "--format", "css"]
    if hue is not None:
        cmd += ["--hue", str(hue)]
    if harmony:
        cmd += ["--harmony", harmony]
    out = subprocess.run(cmd, capture_output=True, text=True, check=True).stdout
    body = re.search(r":root\s*\{(.*?)\}", out, re.S)
    if not body:
        sys.exit("palette.py gave no :root block")
    lines = "\n".join("  " + l.strip() for l in body.group(1).strip().splitlines())
    block = re.compile(r"/\* PALETTE START \*/.*?/\* PALETTE END \*/", re.S)
    if not block.search(html):
        print("warning: no /* PALETTE START */ ... /* PALETTE END */ block, palette not applied")
        return html
    return block.sub(lambda _: f"/* PALETTE START */\n:root{{\n{lines}\n}}\n/* PALETTE END */", html, count=1)


def keep_headings(html):
    if 'data-keepnext="1"' in html:
        return html
    html = keepnext.caption_tables(html)
    html = keepnext.small_tables_keep(html)
    html = keepnext.part_heads(html)
    html = keepnext.wrap_groups(html, r'(?m)^  <div class="grp[" ]', 1)
    html = keepnext.wrap_groups(html, r'(?m)^  <h3\b', 1)
    return html.replace("<body>", '<body data-keepnext="1">', 1)


async def render(src, dst, footer, size):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        try:
            browser = await p.chromium.launch()
        except Exception:
            browser = await p.chromium.launch(channel="msedge")
        page = await browser.new_page()
        await page.goto(Path(src).resolve().as_uri(), wait_until="networkidle")
        await page.evaluate("document.fonts.ready")
        await page.wait_for_timeout(500)
        await page.pdf(path=dst, format=size, print_background=True, display_header_footer=True,
                       header_template="<span></span>", footer_template=FOOTER.format(text=footer),
                       margin={"top": "16mm", "bottom": "18mm", "left": "17mm", "right": "17mm"})
        await browser.close()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("html")
    ap.add_argument("pdf")
    ap.add_argument("--seed", type=int)
    ap.add_argument("--hue", type=float, help="fix the base hue (0-360), with --seed")
    ap.add_argument("--harmony", help="fix the harmony type, with --seed")
    ap.add_argument("--save-html", help="also write the palette-applied HTML here (the final HTML deliverable)")
    ap.add_argument("--footer", default="")
    ap.add_argument("--size", default="A4", choices=["A4", "Letter"])
    a = ap.parse_args()

    html = Path(a.html).read_text(encoding="utf8")
    if a.seed is not None:
        html = apply_palette(html, a.seed, a.hue, a.harmony)
    if a.save_html:
        Path(a.save_html).write_text(html, encoding="utf8")
        print("wrote", a.save_html)
    html = keep_headings(html)
    # write next to the source so relative image paths still resolve
    fd, tmp = tempfile.mkstemp(suffix=".html", dir=str(Path(a.html).resolve().parent))
    os.close(fd)
    try:
        Path(tmp).write_text(html, encoding="utf8")
        asyncio.run(render(tmp, a.pdf, a.footer, a.size))
    finally:
        os.remove(tmp)
    try:
        import pypdfium2 as pdfium
        print(f"wrote {a.pdf}: {len(pdfium.PdfDocument(a.pdf))} pages")
    except ImportError:
        print(f"wrote {a.pdf}")
    print("next: python check_pages.py", a.pdf, "--allow 1 --sheets <folder>")


if __name__ == "__main__":
    main()
