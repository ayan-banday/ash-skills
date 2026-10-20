"""Turn a page into a standalone HTML file that any static host serves as is.

Claude artifact pages ship without <!doctype>, <html>, <head> or <body>: the artifact
viewer adds them. This adds the same skeleton (charset, viewport, the small reset) and a
plain tab icon. A page that already starts with <!doctype html> is copied unchanged.

Usage: python wrap_page.py SOURCE.html OUT.html
"""
import argparse
import pathlib

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath d='M0 15 6 4l3 5 2-3 5 9z' fill='%232b2722'/%3E%3C/svg%3E">
<style>
:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
body{margin:0;font:14px/1.4 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
img{max-width:100%}
[hidden]{display:none!important}
</style>
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source")
    ap.add_argument("out")
    a = ap.parse_args()
    src = pathlib.Path(a.source).read_text(encoding="utf-8")
    out = pathlib.Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    if src.lstrip()[:15].lower().startswith("<!doctype html"):
        out.write_text(src, encoding="utf-8")
        print(f"already standalone, copied to {out}")
    else:
        out.write_text(HEAD + src + "\n", encoding="utf-8")
        print(f"wrapped, wrote {out}")


if __name__ == "__main__":
    main()
