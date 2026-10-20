#!/usr/bin/env python3
"""Export each visual in a Clear Documents HTML file as a PNG, for Word or Google Docs.

Usage:
  python figures.py doc.html out_dir
  python figures.py doc.html out_dir --selector "figure, .decide" --width 760 --scale 2

Files are named fig-01.png, fig-02.png, ... in document order, and sizes.txt lists each
file with its pixel size so the Word script can keep the aspect ratio
(width in the docx = 600 px at most; height = width * h / w).
Needs Playwright (see build_pdf.py).
"""
import argparse
import asyncio
from pathlib import Path


async def run(src, out, selector, width, scale):
    from playwright.async_api import async_playwright
    out.mkdir(parents=True, exist_ok=True)
    async with async_playwright() as p:
        try:
            browser = await p.chromium.launch()
        except Exception:
            browser = await p.chromium.launch(channel="msedge")
        page = await browser.new_page(viewport={"width": width, "height": 1000}, device_scale_factor=scale)
        await page.goto(Path(src).resolve().as_uri(), wait_until="networkidle")
        await page.evaluate("document.fonts.ready")
        await page.wait_for_timeout(500)
        lines = []
        for i, el in enumerate(await page.query_selector_all(selector), 1):
            name = f"fig-{i:02d}.png"
            await el.screenshot(path=str(out / name))
            box = await el.bounding_box()
            lines.append(f"{name}\t{int(box['width'])}\t{int(box['height'])}")
        (out / "sizes.txt").write_text("\n".join(lines) + "\n", encoding="utf8")
        await browser.close()
        print(f"wrote {len(lines)} figures to {out}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("html")
    ap.add_argument("out")
    ap.add_argument("--selector", default="figure, .decide")
    ap.add_argument("--width", type=int, default=760)
    ap.add_argument("--scale", type=float, default=2)
    a = ap.parse_args()
    asyncio.run(run(a.html, Path(a.out), a.selector, a.width, a.scale))


if __name__ == "__main__":
    main()
