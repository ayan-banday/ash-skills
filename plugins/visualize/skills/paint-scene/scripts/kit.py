#!/usr/bin/env python3
"""Turn a page that uses the paint-scene kit into one self-contained file, export its scenes as PNG, or screenshot it.

    python scripts/kit.py bundle page.html out.html          inline ink.css / ink.js and only the masks and tiles the page uses
    python scripts/kit.py bundle page.html out.html --all    inline every mask and tile (the gallery)
    python scripts/kit.py png out.html --dir pngs            every <canvas> scene as a PNG, for Figma and slides
    python scripts/kit.py shot out.html shot.png --width 390 a screenshot to check (full page)
    python scripts/kit.py list                               every mask, tile and part by name

How a page asks for the kit: <link rel="stylesheet" href="ink.css"> and <script src="ink.js"></script> (any path
ending in those names). bundle finds what the page uses: data-bloom="round", data-hatch="slant", class ink-grain,
and in scene settings name:"round", tile:"cross", land:{...} (default mask ground), hatch:{...} (default tile slant).
Needs Playwright for png and shot (pip install playwright; playwright install chromium).
"""
import argparse, base64, re, sys, time
from pathlib import Path

KIT = Path(__file__).resolve().parent.parent / "assets"


def data_uri(p):
    return "data:image/png;base64," + base64.b64encode(p.read_bytes()).decode()


def masks():
    return {p.stem.replace("bloom-", ""): p for p in sorted((KIT / "masks").glob("bloom-*.png"))}


def tiles():
    return {p.stem: p for p in sorted((KIT / "tiles").glob("*.png"))}


def used(html, everything):
    """Masks for CSS (data-bloom), masks for scenes (JS), tiles. --all puts every mask in the CSS."""
    m, t = masks(), tiles()
    jm = set(re.findall(r'''name\s*:\s*["']([\w-]+)["']''', html)) & set(m)
    if re.search(r"\bland\s*:\s*\{", html) and not re.search(r"\bland\s*:\s*\{[^}]*name", html):
        jm.add("ground")
    if everything:
        return set(m), jm, set(t)
    um = set(re.findall(r'data-bloom="([\w-]+)"', html))
    ut = {"hatch-" + h for h in re.findall(r'data-hatch="([\w-]+)"', html)}
    ut |= {"hatch-" + h for h in re.findall(r'''tile\s*:\s*["']([\w-]+)["']''', html)}
    if re.search(r"\bhatch\s*:\s*\{", html) and not re.search(r"\bhatch\s*:\s*\{[^}]*tile", html):
        ut.add("hatch-slant")
    if "ink-grain" in html or re.search(r'src="[^"]*ink\.js"', html):
        ut.add("grain")
    bad = (um - set(m)) | (ut - set(t))
    if bad:
        sys.exit(f"unknown asset(s): {', '.join(sorted(bad))}. Run: python scripts/kit.py list")
    return um, jm, ut


def bundle(src, out, everything):
    t0 = time.time()
    html = Path(src).read_text(encoding="utf8")
    um, jm, ut = used(html, everything)
    m, t = masks(), tiles()
    css_vars = "".join(f'[data-bloom="{n}"]{{--bloom:url({data_uri(m[n])})}}\n' for n in sorted(um))
    css_vars += "".join(f'[data-hatch="{n[6:]}"]{{--hatch:url({data_uri(t[n])})}}\n' for n in sorted(ut) if n.startswith("hatch-"))
    if "grain" in ut:
        css_vars += f":root{{--ink-grain:url({data_uri(t['grain'])})}}\n"
    css = (KIT / "ink.css").read_text(encoding="utf8")
    js_assets = "Ink.maskNames=%s;Ink.assets={masks:{%s},tiles:{%s}};" % (
        "[" + ",".join(f'"{n}"' for n in m) + "]",
        ",".join(f'"{n}":"{data_uri(m[n])}"' for n in sorted(jm)),
        ",".join(f'"{n}":"{data_uri(t[n])}"' for n in sorted(ut)))
    js = (KIT / "ink.js").read_text(encoding="utf8")
    link = re.compile(r'<link[^>]+href="[^"]*ink\.css"[^>]*>')
    script = re.compile(r'<script[^>]+src="[^"]*ink\.js"[^>]*>\s*</script>')
    if not link.search(html) and not script.search(html):
        sys.exit('no <link href="ink.css"> or <script src="ink.js"> in the page')
    html = link.sub(lambda _: "<style>/* paint-scene ink.css */\n" + css + "\n" + css_vars + "</style>", html)
    # a page with scenes but no ink.css still needs nothing from the CSS; masks reach JS through Ink.assets
    html = script.sub(lambda _: "<script>/* paint-scene ink.js */\n" + js + "\n" + js_assets + "</script>", html)
    Path(out).write_text(html, encoding="utf8")
    kb = Path(out).stat().st_size // 1024
    print(f"{out}: {kb} KB, masks {sorted(um | jm) or '-'}, tiles {sorted(ut) or '-'} ({time.time() - t0:.1f}s)")


def browser(page_path, width, height, fn):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": width, "height": height}, device_scale_factor=1)
        pg.goto(Path(page_path).resolve().as_uri())
        pg.wait_for_load_state("networkidle")
        pg.evaluate("async()=>{if(document.fonts)await document.fonts.ready;await Promise.all((window.Ink&&window.Ink.pending)||[]);}")
        fn(pg)
        b.close()


def png(page, outdir):
    t0 = time.time()
    Path(outdir).mkdir(parents=True, exist_ok=True)

    def go(pg):
        res = pg.evaluate("()=>[...document.querySelectorAll('canvas')].map((c,i)=>[c.id||('scene-'+(i+1)),c.toDataURL('image/png'),c.dataset.inkWarn||''])")
        for name, url, warn in res:
            f = Path(outdir) / f"{name}.png"
            f.write_bytes(base64.b64decode(url.split(",", 1)[1]))
            print(f"{f}" + (f"   WARN {warn}" if warn else ""))
    browser(page, 1280, 900, go)
    print(f"done in {time.time() - t0:.1f}s")


def shot(page, out, width, height):
    t0 = time.time()

    def go(pg):
        warns = pg.evaluate("()=>[...document.querySelectorAll('canvas')].map(c=>c.dataset.inkWarn||'').filter(Boolean)")
        sw = pg.evaluate("()=>document.documentElement.scrollWidth")
        pg.screenshot(path=out, full_page=True)
        print(f"{out}  scrollWidth {sw} (viewport {width})" + ("   SIDEWAYS SCROLL" if sw > width else ""))
        for w in warns:
            print("WARN", w)
    browser(page, width, height, go)
    print(f"done in {time.time() - t0:.1f}s")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("bundle"); b.add_argument("src"); b.add_argument("out"); b.add_argument("--all", action="store_true")
    p = sub.add_parser("png"); p.add_argument("page"); p.add_argument("--dir", default="pngs")
    s = sub.add_parser("shot"); s.add_argument("page"); s.add_argument("out"); s.add_argument("--width", type=int, default=1280); s.add_argument("--height", type=int, default=900)
    sub.add_parser("list")
    a = ap.parse_args()
    if a.cmd == "bundle":
        bundle(a.src, a.out, a.all)
    elif a.cmd == "png":
        png(a.page, a.dir)
    elif a.cmd == "shot":
        shot(a.page, a.out, a.width, a.height)
    else:
        print("masks:", ", ".join(masks()))
        print("tiles:", ", ".join(tiles()))
        js = (KIT / "ink.js").read_text(encoding="utf8")
        names = re.findall(r'^ "([\w-]+)":\{k:"(figure|prop)"', js, re.M)
        print("figures:", ", ".join(n for n, k in names if k == "figure"))
        print("props:", ", ".join(n for n, k in names if k == "prop"))


if __name__ == "__main__":
    main()
