#!/usr/bin/env python3
"""Swap in the page palette, inline libraries, run the copy scan, and syntax-check the page script.

Usage:
  python build.py --template template.html --out final.html [--seed N [--hue H] [--harmony NAME]]
                  [--libs libs_dir] [--artifact artifact.html]

--seed replaces everything between /* PALETTE START */ and /* PALETTE END */ in the template
with the light and dark theme from palette.py (the template itself is updated too, so the
source keeps the palette it was built with).
Library markers, each inside its own <script> tag: /*__D3__*/ /*__GSAP__*/ /*__ST__*/.
A page with no markers needs no --libs.
--artifact PATH also writes a copy ready for the Artifact tool: no doctype, <html>, <head> or <body>
wrapper (the artifact host adds its own) and a claude:viewport-fit-sides meta beside the <title>.
Run from a SHORT path on Windows (paths over 260 characters break Python and Chrome).
"""
import argparse
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
MARKERS = (("D3", "d3.min.js"), ("GSAP", "gsap.min.js"), ("ST", "ScrollTrigger.min.js"))
PAL = re.compile(r"(/\* PALETTE START \*/)(.*?)(/\* PALETTE END \*/)", re.S)
FIT_META = '<meta name="claude:viewport-fit-sides" content="cover">'


def artifact_copy(html):
    """The same page without its own document wrapper, as the Artifact tool expects."""
    art = re.sub(r"<!doctype html>\s*", "", html, flags=re.I)
    art = re.sub(r"</?(html|head|body)\b[^>]*>\s*", "", art, flags=re.I)
    art = re.sub(r'<meta charset="utf-8">\s*', "", art, flags=re.I)
    art = re.sub(r'<meta name="viewport"[^>]*>\s*', "", art, flags=re.I)
    if "claude:viewport-fit-sides" not in art:
        art = art.replace("</title>", "</title>\n" + FIT_META, 1)
    return art.lstrip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--template", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--libs")
    ap.add_argument("--seed", type=int)
    ap.add_argument("--hue", type=float)
    ap.add_argument("--harmony")
    ap.add_argument("--artifact", metavar="PATH")
    a = ap.parse_args()

    tpl = open(a.template, encoding="utf-8").read()

    if a.seed is not None:
        import palette
        if not PAL.search(tpl):
            sys.exit("template has no /* PALETTE START */ ... /* PALETTE END */ block")
        p = palette.generate(a.seed, a.harmony, a.hue)
        if "failed" in p:
            sys.exit("palette seed %d fails contrast: %s. Pick another seed." % (a.seed, p["failed"]))
        tpl = PAL.sub(lambda m: m.group(1) + "\n" + palette.css_block(p) + "\n" + m.group(3), tpl)
        with open(a.template, "w", encoding="utf-8") as f:
            f.write(tpl)
        print("palette: seed %d, %s, brand hue %s" % (a.seed, p["harmony"], p["hues"]["brand"]))

    out = tpl
    for key, fname in MARKERS:
        marker = "/*__%s__*/" % key
        if marker not in out:
            continue
        if not a.libs:
            sys.exit("template uses %s; pass --libs (run fetch_libs.py first)" % marker)
        lib_path = os.path.join(a.libs, fname)
        if not os.path.exists(lib_path):
            sys.exit("missing %s. Run fetch_libs.py first." % lib_path)
        lib = open(lib_path, encoding="utf-8").read().replace("</script", "<\\/script")
        out = out.replace(marker, lib)
    with open(a.out, "w", encoding="utf-8") as f:
        f.write(out)
    print("wrote", a.out, "(%d KB)" % (len(out) // 1024))
    if a.artifact:
        with open(a.artifact, "w", encoding="utf-8") as f:
            f.write(artifact_copy(out))
        print("wrote", a.artifact, "(artifact copy)")

    # copy scan on the template (no library source)
    rc = subprocess.call([sys.executable, os.path.join(HERE, "scan_copy.py"), a.template])

    # syntax check of the last inline script
    if shutil.which("node"):
        scripts = re.findall(r"<script>(.*?)</script>", out, flags=re.S)
        if scripts:
            tmp = a.out + ".lastscript.js"
            with open(tmp, "w", encoding="utf-8") as f:
                f.write(scripts[-1])
            ok = subprocess.call(["node", "--check", tmp]) == 0
            os.remove(tmp)
            print("page script syntax:", "ok" if ok else "ERROR")
            if not ok:
                rc = 1
    else:
        print("node not found, skipped syntax check")
    sys.exit(rc)


if __name__ == "__main__":
    main()
