#!/usr/bin/env python3
"""Screenshot each section of an HTML file on its own with headless Chrome, or probe horizontal overflow.

Usage:
  python shots.py page.html --outdir shots            # every <section> and .part divider, 1280px and 500px
  python shots.py page.html --outdir shots --ids s-funnel s-meera
  python shots.py page.html --outdir shots --theme dark|light
  python shots.py page.html --overflow 400            # prints scroll width and elements past the edge

Why isolate sections: anchor-jump screenshots come out blank in headless Chrome because of smooth
scrolling and the sticky nav, so this hides every other top-level element with injected CSS.
Headless Chrome cannot go narrower than about 500px, so the 400px check uses an iframe probe.
Run from a SHORT path on Windows (paths over 260 characters break Chrome).
"""
import argparse
import glob
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/usr/bin/google-chrome", "/usr/bin/chromium", "/usr/bin/chromium-browser",
]


def find_chrome():
    for c in CANDIDATES:
        if os.path.exists(c):
            return c
    sys.exit("No Chrome or Edge found. Install one, or screenshot manually.")


def run_chrome(chrome, args, timeout=120):
    return subprocess.run([chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars"] + args,
                          capture_output=True, text=True, timeout=timeout)


def section_ids(html):
    ids = re.findall(r'<(?:section|div)\b[^>]*\bid="([^"]+)"[^>]*>', html)
    keep = []
    for m in re.finditer(r'<(section|div)\b([^>]*)>', html):
        attrs = m.group(2)
        idm = re.search(r'\bid="([^"]+)"', attrs)
        if not idm:
            continue
        cls = re.search(r'\bclass="([^"]*)"', attrs)
        classes = cls.group(1).split() if cls else []
        if m.group(1) == "section" or "part" in classes:
            keep.append(idm.group(1))
    return keep or ids


def shots(page, outdir, ids, theme):
    chrome = find_chrome()
    html = open(page, encoding="utf-8").read()
    ids = ids or section_ids(html)
    os.makedirs(outdir, exist_ok=True)
    tmp = tempfile.mkdtemp(prefix="shots_")
    theme_attr = ""
    if theme:
        html = html.replace("<html", '<html data-theme="%s"' % theme, 1)
    for sid in ids:
        css = ("<style>html{scroll-behavior:auto!important} body>*{display:none!important} "
               "body>#%s{display:block!important}</style></head>" % sid)
        page_tmp = os.path.join(tmp, sid + ".html")
        with open(page_tmp, "w", encoding="utf-8") as f:
            f.write(html.replace("</head>", css, 1))
        for label, width, height in (("desk", 1280, 1700), ("narrow", 500, 2600)):
            out = os.path.abspath(os.path.join(outdir, "%s-%s.png" % (sid, label)))
            run_chrome(chrome, ["--window-size=%d,%d" % (width, height), "--virtual-time-budget=6000",
                                "--screenshot=" + out, Path(page_tmp).resolve().as_uri()])
            print("wrote", out if os.path.exists(out) else "FAILED " + out)


PROBE = """<!doctype html><body><iframe id="f" src="%s" style="width:%dpx;height:900px;border:0"></iframe>
<pre id="r">waiting</pre><script>
document.getElementById('f').onload=function(){setTimeout(function(){
 var d=document.getElementById('f').contentDocument,w=d.defaultView.innerWidth,out=[];
 out.push('inner='+w+' scrollW='+d.documentElement.scrollWidth+' bodyScrollW='+d.body.scrollWidth);
 var bad=[];d.querySelectorAll('body *').forEach(function(el){var r=el.getBoundingClientRect();
  if(r.right>w+1&&!el.closest('.scroll')&&!el.closest('nav')&&!el.closest('svg')&&el.tagName!=='SCRIPT'){
   bad.push(el.tagName+'.'+(typeof el.className==='string'?el.className:'')+' right='+Math.round(r.right));}});
 out.push('overflowing: '+(bad.slice(0,25).join(' | ')||'none'));
 document.getElementById('r').textContent=out.join('\\n');},2500)};
</script></body>"""


def overflow(page, width):
    chrome = find_chrome()
    tmp = tempfile.mkdtemp(prefix="probe_")
    probe = os.path.join(tmp, "probe.html")
    copy = os.path.join(tmp, "page.html")
    with open(page, encoding="utf-8") as src, open(copy, "w", encoding="utf-8") as dst:
        dst.write(src.read())
    with open(probe, "w", encoding="utf-8") as f:
        f.write(PROBE % ("page.html", width))
    res = run_chrome(chrome, ["--allow-file-access-from-files", "--virtual-time-budget=8000", "--dump-dom",
                              Path(probe).resolve().as_uri()])
    m = re.search(r'<pre id="r">(.*?)</pre>', res.stdout, flags=re.S)
    print(m.group(1) if m else "probe failed")
    sw = re.search(r"scrollW=(\d+)", res.stdout)
    if sw and int(sw.group(1)) > width:
        print("OVERFLOW: page is wider than %dpx" % width)
        return 1
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("page")
    ap.add_argument("--outdir", default="shots")
    ap.add_argument("--ids", nargs="*")
    ap.add_argument("--theme", choices=["light", "dark"])
    ap.add_argument("--overflow", type=int, metavar="WIDTH")
    a = ap.parse_args()
    if a.overflow:
        sys.exit(overflow(a.page, a.overflow))
    shots(a.page, a.outdir, a.ids, a.theme)


if __name__ == "__main__":
    main()
