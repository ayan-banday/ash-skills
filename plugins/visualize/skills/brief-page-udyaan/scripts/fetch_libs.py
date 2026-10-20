#!/usr/bin/env python3
"""Download the pinned libraries used by brief-page-udyaan into one folder.

Usage: python fetch_libs.py <dest_dir>

Use a short destination path on Windows (paths over 260 characters break Python and Chrome).
"""
import os
import sys
import urllib.request

LIBS = {
    "d3.min.js": "https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js",
    "gsap.min.js": "https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js",
    "ScrollTrigger.min.js": "https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js",
}


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    dest = sys.argv[1]
    os.makedirs(dest, exist_ok=True)
    for name, url in LIBS.items():
        path = os.path.join(dest, name)
        if os.path.exists(path) and os.path.getsize(path) > 10000:
            print("have", name)
            continue
        with urllib.request.urlopen(url, timeout=60) as r:
            data = r.read()
        with open(path, "wb") as f:
            f.write(data)
        print("fetched", name, len(data), "bytes")


if __name__ == "__main__":
    main()
