#!/usr/bin/env python3
"""One palette per page: seeded, muted, contrast-checked, with matching light and dark themes.

Usage:
  python palette.py --seed N [--hue DEG] [--harmony NAME]            # print the theme CSS block
  python palette.py --seed N --count 6 --sheet palettes.html          # preview six candidates
  python palette.py --seed N --format json                            # roles and contrast ratios

--hue fixes the base hue when the subject has a material colour (kraft card is about 65,
terracotta 40, indigo dye 275, chalkboard 160). Without it the seed picks one.
Harmonies: monochromatic, analogous, complementary, split-complementary, triadic.

The CSS block uses this skill's token names (--bg, --surface, --ink, --muted, --line, --soft,
--brand, --brand-ink, --accent, --accent-soft, --alert, --ok, --marker, --tint-1..3) and the
three-state theme shape from references/design-system.md. build.py --seed swaps it into the
template between /* PALETTE START */ and /* PALETTE END */.
Adapted from polished-doc/scripts/palette.py (same OKLCH maths, plus a dark theme).
"""
from __future__ import annotations

import argparse
import json
import math
import random
import sys

HARMONIES = ["monochromatic", "analogous", "complementary", "split-complementary", "triadic"]
ROLES = ["bg", "surface", "ink", "muted", "line", "soft", "brand", "brand_ink", "accent",
         "accent_soft", "alert", "ok", "marker", "tint_1", "tint_2", "tint_3"]

# ---------------------------------------------------------------- colour maths (OKLCH -> sRGB hex)


def _lin(L, C, h):
    a, b = C * math.cos(math.radians(h)), C * math.sin(math.radians(h))
    l_, m_, s_ = L + .3963377774 * a + .2158037573 * b, L - .1055613458 * a - .0638541728 * b, L - .0894841775 * a - 1.2914855480 * b
    l, m, s = l_ ** 3, m_ ** 3, s_ ** 3
    return (4.0767416621 * l - 3.3077115913 * m + .2309699292 * s,
            -1.2684380046 * l + 2.6097574011 * m - .3413193965 * s,
            -.0041960863 * l - .7034186147 * m + 1.7076147010 * s)


def _gamma(v):
    v = min(1.0, max(0.0, v))
    return 12.92 * v if v <= .0031308 else 1.055 * v ** (1 / 2.4) - .055


def to_hex(L, C, h):
    """OKLCH to hex, lowering chroma until the colour fits in sRGB."""
    ok = lambda c: all(-1e-6 <= v <= 1 + 1e-6 for v in _lin(L, c, h))
    if not ok(C):
        lo, hi = 0.0, C
        for _ in range(30):
            mid = (lo + hi) / 2
            lo, hi = (mid, hi) if ok(mid) else (lo, mid)
        C = lo
    return "#" + "".join("%02x" % round(_gamma(v) * 255) for v in _lin(L, C, h))


def _lum(hx):
    def f(c):
        c /= 255
        return c / 12.92 if c <= .04045 else ((c + .055) / 1.055) ** 2.4
    r, g, b = (int(hx[i:i + 2], 16) for i in (1, 3, 5))
    return .2126 * f(r) + .7152 * f(g) + .0722 * f(b)


def contrast(a, b):
    la, lb = _lum(a), _lum(b)
    return (max(la, lb) + .05) / (min(la, lb) + .05)


def hue_dist(a, b):
    d = abs(a - b) % 360
    return min(d, 360 - d)


# ---------------------------------------------------------------- ranges per theme: role -> (L range, C range)

LIGHT = {
    "bg": ((.965, .982), (.006, .014)), "surface": ((.990, .998), (.002, .006)),
    "ink": ((.22, .27), (.012, .022)), "muted": ((.46, .52), (.015, .03)),
    "line": ((.86, .89), (.01, .02)), "soft": ((.93, .95), (.012, .022)),
    "brand": ((.42, .50), (.07, .12)), "accent": ((.58, .68), (.10, .15)),
    "accent_soft": ((.93, .95), (.025, .04)), "alert": ((.46, .52), (.10, .13)),
    "ok": ((.46, .52), (.06, .09)), "marker": ((.88, .91), (.08, .12)),
    "tint_1": ((.90, .93), (.03, .045)), "tint_2": ((.90, .93), (.03, .045)), "tint_3": ((.90, .93), (.03, .045)),
}
DARK = {
    "bg": ((.17, .20), (.008, .016)), "surface": ((.22, .24), (.01, .018)),
    "ink": ((.93, .95), (.006, .012)), "muted": ((.75, .79), (.015, .03)),
    "line": ((.34, .38), (.012, .022)), "soft": ((.25, .27), (.015, .025)),
    "brand": ((.74, .80), (.07, .11)), "accent": ((.78, .84), (.08, .12)),
    "accent_soft": ((.29, .32), (.03, .05)), "alert": ((.70, .75), (.09, .12)),
    "ok": ((.72, .76), (.06, .09)), "marker": ((.40, .44), (.06, .09)),
    "tint_1": ((.29, .32), (.03, .05)), "tint_2": ((.29, .32), (.03, .05)), "tint_3": ((.29, .32), (.03, .05)),
}

# (name, fg, bg, minimum, role that moves if it fails)
CHECKS = [
    ("ink on bg", "ink", "bg", 7.0, "ink"), ("muted on bg", "muted", "bg", 4.5, "muted"),
    ("muted on surface", "muted", "surface", 4.5, "muted"), ("brand on bg", "brand", "bg", 4.5, "brand"),
    ("brand-ink on brand", "brand_ink", "brand", 4.5, "brand"), ("ink on soft", "ink", "soft", 7.0, "soft"),
    ("ink on accent-soft", "ink", "accent_soft", 7.0, "accent_soft"), ("ink on marker", "ink", "marker", 7.0, "marker"),
    ("ink on tint-1", "ink", "tint_1", 7.0, "tint_1"), ("ink on tint-2", "ink", "tint_2", 7.0, "tint_2"),
    ("ink on tint-3", "ink", "tint_3", 7.0, "tint_3"), ("alert on bg", "alert", "bg", 4.5, "alert"),
    ("ok on bg", "ok", "bg", 4.5, "ok"), ("accent on bg (shapes)", "accent", "bg", 3.0, "accent"),
]


def accent_hue(harmony, hue, rng):
    return {"monochromatic": hue, "analogous": hue + rng.choice([-35, 35]), "complementary": hue + 180,
            "split-complementary": hue + rng.choice([150, 210]), "triadic": hue + 120}[harmony] % 360


def away(base, avoid, rng, gap=40.0):
    """A hue near base, pushed at least gap degrees away from every hue in avoid."""
    h = (base + rng.uniform(-6, 6)) % 360
    for a in avoid:
        if hue_dist(h, a) < gap:
            side = 1 if ((h - a + 180) % 360) - 180 >= 0 else -1
            h = (a + side * (gap + rng.uniform(2, 8))) % 360
    return h


def theme(rng, ranges, hues, dark):
    spec = {}
    for r in ROLES:
        if r == "brand_ink":
            continue
        (l0, l1), (c0, c1) = ranges[r]
        spec[r] = [rng.uniform(l0, l1), rng.uniform(c0, c1), hues[r]]
    col = {r: to_hex(*spec[r]) for r in spec}
    col["brand_ink"] = col["bg"] if dark else "#ffffff"
    # A failing check moves its role's lightness: text roles away from the background,
    # fill roles (soft, marker, tints) away from the ink. Two passes settle knock-on effects.
    for _ in range(2):
        for name, fg, bg, need, mover in CHECKS:
            for _ in range(160):
                if contrast(col[fg], col[bg]) >= need:
                    break
                is_fill = mover in ("soft", "accent_soft", "marker", "tint_1", "tint_2", "tint_3")
                step = .005 if (dark != is_fill) else -.005
                spec[mover][0] = min(.995, max(.05, spec[mover][0] + step))
                col[mover] = to_hex(*spec[mover])
                if dark:
                    col["brand_ink"] = col["bg"]
    ratios = {n: round(contrast(col[f], col[b]), 2) for n, f, b, _, _ in CHECKS}
    failed = [n for n, f, b, need, _ in CHECKS if contrast(col[f], col[b]) < need]
    return col, ratios, failed


def generate(seed, harmony=None, hue=None):
    rng = random.Random(seed)
    harmony = harmony or rng.choice(HARMONIES)
    hue = (rng.uniform(0, 360) if hue is None else float(hue)) % 360
    ah = accent_hue(harmony, hue, rng)
    alert_h, ok_h = away(30, [hue, ah], rng), away(150, [hue, ah], rng)
    third = max([(hue + 120) % 360, (hue + 240) % 360], key=lambda h: hue_dist(h, ah))
    hues = {r: hue for r in ROLES}
    hues.update(accent=ah, accent_soft=ah, marker=ah, alert=alert_h, ok=ok_h,
                tint_1=hue, tint_2=ah, tint_3=third)
    light, lr, lf = theme(random.Random(seed * 7 + 1), LIGHT, hues, False)
    dark, dr, df = theme(random.Random(seed * 7 + 2), DARK, hues, True)
    out = {"seed": seed, "harmony": harmony, "hues": {"brand": round(hue, 1), "accent": round(ah, 1), "third": round(third, 1)},
           "light": light, "dark": dark, "contrast": {"light": lr, "dark": dr}}
    if lf or df:
        out["failed"] = {"light": lf, "dark": df}
    return out


def _decls(col):
    return " ".join("--%s: %s;" % (r.replace("_", "-"), col[r]) for r in ROLES)


def css_block(p):
    note = "/* palette seed %d, %s, brand hue %s, accent hue %s (scripts/palette.py) */" % (
        p["seed"], p["harmony"], p["hues"]["brand"], p["hues"]["accent"])
    light, dark = _decls(p["light"]), _decls(p["dark"])
    return "\n".join([
        note,
        ":root { %s color-scheme: light; }" % light,
        "@media (prefers-color-scheme: dark) { :root:not([data-theme=\"light\"]) { %s color-scheme: dark; } }" % dark,
        ":root[data-theme=\"dark\"] { %s color-scheme: dark; }" % dark,
    ])


def sheet(palettes):
    cards = []
    for p in palettes:
        for mode in ("light", "dark"):
            c = p[mode]
            sw = "".join('<div><i style="background:%s"></i>%s<br><code>%s</code></div>' % (c[r], r, c[r]) for r in ROLES)
            bad = p.get("failed", {}).get(mode, [])
            cards.append(f"""<section style="background:{c['bg']};color:{c['ink']};border:1px solid {c['line']}">
<b>seed {p['seed']} · {p['harmony']} · {mode}</b>{' <span style="color:%s">FAILED: %s</span>' % (c['alert'], ', '.join(bad)) if bad else ''}
<h2 style="color:{c['brand']}">Which plugin holds which skill?</h2>
<p style="color:{c['muted']}">Muted text on the page. <span style="background:{c['marker']};color:{c['ink']};padding:0 4px">Marker on what the reader gets</span>.
<span style="color:{c['alert']}">Alert word</span> and <span style="color:{c['ok']}">ok word</span>.</p>
<p><span style="background:{c['tint_1']};padding:2px 8px">tint 1</span> <span style="background:{c['tint_2']};padding:2px 8px">tint 2</span>
<span style="background:{c['tint_3']};padding:2px 8px">tint 3</span> <span style="background:{c['brand']};color:{c['brand_ink']};padding:2px 8px">brand fill</span>
<svg width="60" height="20"><circle cx="10" cy="10" r="8" fill="{c['accent']}"/><path d="M24 10h30" stroke="{c['ink']}" stroke-width="2"/></svg></p>
<div class="sw">{sw}</div></section>""")
    return """<!doctype html><meta charset="utf-8"><title>Palette sheet</title><style>
body{margin:0;padding:20px;background:#ddd;font:14px Segoe UI,system-ui,sans-serif;display:grid;grid-template-columns:repeat(auto-fill,minmax(440px,1fr));gap:16px}
section{padding:16px;border-radius:6px}h2{font-size:20px;margin:8px 0}.sw{display:grid;grid-template-columns:repeat(8,1fr);gap:6px;font-size:10px}
.sw i{display:block;height:26px;border-radius:3px;border:1px solid rgba(128,128,128,.4)}code{font-size:9.5px}</style>""" + "".join(cards)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--seed", type=int)
    ap.add_argument("--hue", type=float)
    ap.add_argument("--harmony", choices=HARMONIES)
    ap.add_argument("--count", type=int, default=1)
    ap.add_argument("--format", choices=["css", "json"], default="css")
    ap.add_argument("--sheet", metavar="PATH")
    a = ap.parse_args(argv)
    seed0 = a.seed if a.seed is not None else random.SystemRandom().randrange(1, 10 ** 6)
    pals = [generate(seed0 + i, a.harmony, a.hue) for i in range(max(1, a.count))]
    if a.sheet:
        with open(a.sheet, "w", encoding="utf-8") as f:
            f.write(sheet(pals))
        print("wrote", a.sheet)
    if a.format == "json":
        print(json.dumps(pals[0] if len(pals) == 1 else pals, indent=2))
    elif not a.sheet:
        print("\n\n".join(css_block(p) for p in pals))
    bad = [p["seed"] for p in pals if "failed" in p]
    if bad:
        print("warning: contrast failed for seeds %s; pick another seed" % bad, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
