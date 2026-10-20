"""Open a static page in headless Chromium the way a visitor would, and report problems.

Serves the page's folder over local http, loads the page at laptop (1366x800) and phone
(390x844) widths, waits for the animations, saves a screenshot of each, and lists console
errors and failed requests, and notes a page wider than the screen. Exit 0 when there are no errors.

Usage: python check_page.py PATH/TO/index.html [--out DIR] [--wait MS]
"""
import argparse
import asyncio
import functools
import glob
import http.server
import pathlib
import threading


class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def serve(root):
    handler = functools.partial(Quiet, directory=str(root))
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


async def run(page_path, out, wait):
    from playwright.async_api import async_playwright

    root = page_path.parent
    srv = serve(root)
    url = f"http://127.0.0.1:{srv.server_address[1]}/{page_path.name}"
    exe = glob.glob("/opt/pw-browsers/chromium-*/chrome-linux*/chrome")
    problems = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path=exe[0]) if exe else await p.chromium.launch()
        for name, vp in (("laptop", (1366, 800)), ("phone", (390, 844))):
            pg = await browser.new_page(viewport={"width": vp[0], "height": vp[1]})
            pg.on("console", lambda m, n=name: problems.append(f"{n}: console {m.text}") if m.type == "error" else None)
            pg.on("pageerror", lambda e, n=name: problems.append(f"{n}: script error {e}"))
            pg.on("requestfailed", lambda r, n=name: problems.append(f"{n}: failed {r.url}"))
            await pg.goto(url, wait_until="networkidle")
            await pg.wait_for_timeout(wait)
            shot = out / f"{name}.png"
            await pg.screenshot(path=str(shot))
            if await pg.evaluate("document.documentElement.scrollWidth > innerWidth + 1"):
                print(f"{name}: note, the page is wider than the screen (expected for a horizontal page, a bug otherwise)")
            print(f"{name}: title '{await pg.title()}', screenshot {shot}")
            await pg.close()
        await browser.close()
    srv.shutdown()
    return problems


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("page")
    ap.add_argument("--out", default="shots")
    ap.add_argument("--wait", type=int, default=4000)
    a = ap.parse_args()
    out = pathlib.Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    problems = asyncio.run(run(pathlib.Path(a.page).resolve(), out, a.wait))
    for line in problems:
        print(line)
    print("PASS" if not problems else f"FAIL ({len(problems)} problems)")
    raise SystemExit(0 if not problems else 1)


if __name__ == "__main__":
    main()
