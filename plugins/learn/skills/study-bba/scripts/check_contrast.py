#!/usr/bin/env python3
"""Check that every rule in a study page's CSS that sets both a text colour and a background
can be read: contrast of at least 4.5 to 1 (the plain-text accessibility minimum).

    python scripts/check_contrast.py <page.html>

Why: the tutor's model picker once took its text from the dark panel (--text) and its box
from the light paper blocks (--paper), so its words were pale on pale (Ash, Nov 3 2026).
Reads the hex colours in :root, resolves var(--x), and checks each rule with both a
`color` and a `background`. FAIL lines must be fixed.
"""
import re
import sys


def lum(hexc):
    h = hexc.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    rgb = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    lin = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in rgb]
    return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]


def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def main(path):
    html = open(path, encoding="utf-8").read()
    css = "\n".join(re.findall(r"<style[^>]*>(.*?)</style>", html, re.S))
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    root = re.search(r":root\s*\{(.*?)\}", css, re.S)
    tokens = dict(re.findall(r"(--[\w-]+)\s*:\s*(#[0-9a-fA-F]{3,6})\b", root.group(1))) if root else {}

    def resolve(v):
        v = v.strip()
        m = re.match(r"var\((--[\w-]+)", v)
        if m:
            return tokens.get(m.group(1))
        m = re.match(r"#[0-9a-fA-F]{3,6}\b", v)
        return m.group(0) if m else None

    fails, checked = [], 0
    for sel, body in re.findall(r"([^{}@]+)\{([^{}]*)\}", css):
        sel = sel.strip()
        if sel.startswith(":root"):
            continue
        fg = re.search(r"(?:^|;)\s*color\s*:\s*([^;]+)", body)
        bg = re.search(r"background(?:-color)?\s*:\s*([^;]+)", body)
        if not (fg and bg):
            continue
        f, b = resolve(fg.group(1)), resolve(bg.group(1))
        if not (f and b):
            continue
        checked += 1
        r = ratio(f, b)
        if r < 4.5:
            fails.append(f"{sel}: text {fg.group(1).strip()} on {bg.group(1).strip()} is {r:.1f}:1 (needs 4.5:1)")
    print(f"checked {checked} rule(s) with both a text colour and a background")
    for f in fails:
        print("FAIL ", f)
    if not fails:
        print("PASS: every coloured box can be read")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
