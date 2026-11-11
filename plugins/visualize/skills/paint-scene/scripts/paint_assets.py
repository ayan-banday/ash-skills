#!/usr/bin/env python3
"""Repaint the kit's bloom masks and tiles with p5.brush (headless Chromium via Playwright).

    python scripts/paint_assets.py              repaint every mask and tile into assets/
    python scripts/paint_assets.py --sheet x.png  also save a contact sheet of every mask

Run it only when a mask is added or changed in scripts/painter.html (a Commission saving a new part).
Pages never run p5.brush: they use the saved PNGs through kit.py. Needs internet for the p5.brush CDN.
"""
import argparse, base64, time
from pathlib import Path
from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
ASSETS = HERE.parent / "assets"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sheet", help="save a contact sheet PNG of every mask here")
    a = ap.parse_args()
    t0 = time.time()
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        pg.goto((HERE / "painter.html").as_uri())
        pg.wait_for_function("window.ready===true", timeout=60000)
        out = pg.evaluate("window.run()")
        for rel, url in out.items():
            f = ASSETS / rel
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_bytes(base64.b64decode(url.split(",", 1)[1]))
            print(f"{rel}  {f.stat().st_size // 1024} KB")
        if a.sheet:
            masks = [k for k in out if k.startswith("masks/")]
            cells = "".join(
                f'<figure><div style="-webkit-mask:url({out[k]}) center/contain no-repeat;mask:url({out[k]}) center/contain no-repeat"></div>'
                f"<figcaption>{Path(k).stem}</figcaption></figure>" for k in masks)
            pg.set_viewport_size({"width": 1400, "height": 900})
            pg.set_content("<style>body{margin:0;background:#141613;font:13px monospace;color:#bbb;display:grid;"
                           "grid-template-columns:repeat(6,1fr);gap:8px;padding:12px}figure{margin:0}"
                           "div{aspect-ratio:1;background:#e9a39b;outline:1px solid #333}</style>" + cells)
            pg.screenshot(path=a.sheet, full_page=True)
            print("sheet:", a.sheet)
        b.close()
    print(f"done in {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
