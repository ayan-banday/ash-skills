#!/usr/bin/env python3
"""Random but harmonious, muted, professional document palettes, built in OKLCH.

Usage:
  python palette.py [--seed N] [--harmony NAME] [--hue DEG] [--count K]
                    [--format json|css] [--sheet PATH]

Harmonies: monochromatic, analogous, complementary, split-complementary, triadic.
With --count K, palettes use seeds N..N+K-1.
"""
from __future__ import annotations

import argparse
import html
import json
import math
import random
import sys

HARMONIES = ["monochromatic", "analogous", "complementary",
             "split-complementary", "triadic"]
ROLE_ORDER = ["bg", "surface", "ink", "muted", "line", "primary", "primary_soft",
              "accent", "accent_soft", "alert", "ok"]

# --------------------------------------------------------------------------
# Colour maths: OKLCH -> OKLab -> linear sRGB -> sRGB hex
# --------------------------------------------------------------------------


def oklab_to_linear(L: float, a: float, b: float):
    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541728 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b
    l, m, s = l_ ** 3, m_ ** 3, s_ ** 3
    return (4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
            -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
            -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s)


def oklch_to_linear(L: float, C: float, h: float):
    hr = math.radians(h)
    return oklab_to_linear(L, C * math.cos(hr), C * math.sin(hr))


def in_gamut(rgb, eps=1e-6):
    return all(-eps <= v <= 1 + eps for v in rgb)


def gamma(v: float) -> float:
    v = min(1.0, max(0.0, v))
    return 12.92 * v if v <= 0.0031308 else 1.055 * v ** (1 / 2.4) - 0.055


def to_hex(L: float, C: float, h: float):
    """OKLCH -> hex, reducing chroma until in sRGB gamut. Returns (hex, C_used)."""
    if not in_gamut(oklch_to_linear(L, C, h)):
        lo, hi = 0.0, C
        for _ in range(30):
            mid = (lo + hi) / 2
            if in_gamut(oklch_to_linear(L, mid, h)):
                lo = mid
            else:
                hi = mid
        C = lo
    rgb = oklch_to_linear(L, C, h)
    r, g, b = (round(gamma(v) * 255) for v in rgb)
    return "#{:02x}{:02x}{:02x}".format(r, g, b), C


def hex_to_rgb(hx: str):
    hx = hx.lstrip("#")
    return tuple(int(hx[i:i + 2], 16) for i in (0, 2, 4))


def rel_luminance(hx: str) -> float:
    def lin(c):
        c /= 255
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (lin(c) for c in hex_to_rgb(hx))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a: str, b: str) -> float:
    la, lb = rel_luminance(a), rel_luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def hue_dist(a: float, b: float) -> float:
    d = abs(a - b) % 360
    return min(d, 360 - d)


# --------------------------------------------------------------------------
# Palette generation
# --------------------------------------------------------------------------

# role -> (L range, C range)
RANGES = {
    "bg":           ((0.975, 0.990), (0.002, 0.008)),
    "surface":      ((0.995, 1.000), (0.000, 0.004)),
    "ink":          ((0.22, 0.28), (0.008, 0.020)),
    "muted":        ((0.45, 0.52), (0.012, 0.025)),
    "line":         ((0.86, 0.90), (0.004, 0.015)),
    "primary":      ((0.42, 0.52), (0.05, 0.11)),
    "primary_soft": ((0.93, 0.96), (0.014, 0.025)),
    "accent":       ((0.55, 0.68), (0.06, 0.12)),
    "accent_soft":  ((0.93, 0.96), (0.018, 0.032)),
    "alert":        ((0.45, 0.52), (0.08, 0.11)),
    "ok":           ((0.45, 0.52), (0.05, 0.08)),
}

# (name, fg role, bg role or literal hex, minimum ratio)
CHECKS = [
    ("ink_on_bg", "ink", "bg", 7.0),
    ("muted_on_bg", "muted", "bg", 4.5),
    ("primary_on_bg", "primary", "bg", 4.5),
    ("white_on_primary", "#ffffff", "primary", 4.5),
    ("ink_on_primary_soft", "ink", "primary_soft", 7.0),
    ("alert_on_bg", "alert", "bg", 4.5),
    ("ok_on_bg", "ok", "bg", 4.5),
    ("accent_on_bg", "accent", "bg", 3.0),
]


def accent_hue(harmony: str, hue: float, rng: random.Random) -> float:
    if harmony == "monochromatic":
        return hue
    if harmony == "analogous":
        return (hue + rng.choice([-30, 30])) % 360
    if harmony == "complementary":
        return (hue + 180) % 360
    if harmony == "split-complementary":
        return (hue + rng.choice([150, 210])) % 360
    if harmony == "triadic":
        return (hue + 120) % 360
    raise ValueError(f"unknown harmony {harmony!r}")


def semantic_hue(base: float, primary: float, rng: random.Random, jitter=5.0,
                 min_gap=25.0) -> float:
    """Hue near `base`; pushed away from primary if within min_gap degrees."""
    h = (base + rng.uniform(-jitter, jitter)) % 360
    if hue_dist(h, primary) < min_gap:
        signed = ((h - primary + 180) % 360) - 180  # -180..180
        side = 1 if signed >= 0 else -1
        h = (primary + side * (min_gap + rng.uniform(2, 8))) % 360
    return h


def generate(seed: int, harmony: str | None = None, hue: float | None = None) -> dict:
    rng = random.Random(seed)
    harmony = harmony or rng.choice(HARMONIES)
    hue = (rng.uniform(0, 360) if hue is None else float(hue)) % 360
    ah = accent_hue(harmony, hue, rng)
    alert_h = semantic_hue(30, hue, rng)
    ok_h = semantic_hue(150, hue, rng)

    hues = {"bg": hue, "surface": hue, "ink": hue, "muted": hue, "line": hue,
            "primary": hue, "primary_soft": hue, "accent": ah,
            "accent_soft": ah, "alert": alert_h, "ok": ok_h}

    spec = {}  # role -> [L, C, hue]
    for role in ROLE_ORDER:
        (l0, l1), (c0, c1) = RANGES[role]
        spec[role] = [round(rng.uniform(l0, l1), 4), round(rng.uniform(c0, c1), 4),
                      hues[role]]

    def build(role):
        return to_hex(*spec[role])[0]

    roles = {r: build(r) for r in ROLE_ORDER}

    def val(x):
        return x if x.startswith("#") else roles[x]

    # Adjust L in small steps (darker) until each foreground role passes.
    for role in ["primary", "ink", "muted", "alert", "ok", "accent"]:
        mine = [c for c in CHECKS if c[1] == role or c[2] == role]
        for _ in range(120):
            roles[role] = build(role)
            if all(contrast(val(f), val(b)) >= m for _, f, b, m in mine):
                break
            spec[role][0] = round(spec[role][0] - 0.005, 4)
        roles[role] = build(role)

    results = {name: round(contrast(val(f), val(b)), 2) for name, f, b, _ in CHECKS}
    failed = [name for name, f, b, m in CHECKS if contrast(val(f), val(b)) < m]
    out = {
        "seed": seed,
        "harmony": harmony,
        "hues": {"primary": round(hue, 1), "accent": round(ah, 1)},
        "roles": roles,
        "contrast": results,
    }
    if failed:
        out["failed"] = failed
    return out


# --------------------------------------------------------------------------
# Output
# --------------------------------------------------------------------------


def css_block(p: dict, selector: str = ":root") -> str:
    lines = [f"{selector} {{"]
    for r in ROLE_ORDER:
        lines.append(f"  --{r.replace('_', '-')}: {p['roles'][r]};")
    lines.append("}")
    return "\n".join(lines)


def sheet_html(palettes: list[dict]) -> str:
    minimum = {n: m for n, _, _, m in CHECKS}
    cards = []
    for p in palettes:
        R = p["roles"]
        e = html.escape
        sw = "".join(
            f'<div class="sw"><div class="chip" style="background:{R[r]}"></div>'
            f'<b>{r}</b><code>{R[r]}</code></div>' for r in ROLE_ORDER)
        rows = "".join(
            f'<tr class="{"ok" if v >= minimum[k] else "bad"}"><td>{k.replace("_", " ")}</td>'
            f'<td>{v:.2f}</td><td>&ge; {minimum[k]:g}</td>'
            f'<td>{"pass" if v >= minimum[k] else "FAIL"}</td></tr>'
            for k, v in p["contrast"].items())
        cards.append(f"""
<section class="card" style="--bg:{R['bg']};--surface:{R['surface']};--ink:{R['ink']};--muted:{R['muted']};--line:{R['line']};--primary:{R['primary']};--primary-soft:{R['primary_soft']};--accent:{R['accent']};--accent-soft:{R['accent_soft']};--alert:{R['alert']};--ok:{R['ok']}">
  <header><span class="seed">seed {p['seed']}</span><span class="harm">{e(p['harmony'])}</span>
  <span class="hues">primary {p['hues']['primary']}&deg; &middot; accent {p['hues']['accent']}&deg;</span></header>
  <div class="swatches">{sw}</div>
  <div class="sample">
    <h2>Quarterly review: findings and next steps</h2>
    <p>Body text sits in the ink colour on the tinted background. <span class="mut">Secondary text uses the muted role.</span>
    Status reads <span class="ok">on track</span> or <span class="alert">needs attention</span>.</p>
    <div class="callout"><strong>Key point.</strong> A soft callout uses the primary-soft fill with a primary rule.</div>
    <div class="callout2"><span class="dot"></span> Accent-soft panel with an accent marker.</div>
  </div>
  <table>{rows}</table>
</section>""")
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Palette sheet</title>
<style>
body{{margin:0;padding:24px;background:#eceae8;font-family:Segoe UI,system-ui,sans-serif;color:#222}}
h1{{font-size:18px;margin:0 0 16px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(420px,1fr));gap:20px}}
.card{{background:var(--bg);color:var(--ink);border:1px solid var(--line);border-radius:8px;padding:16px}}
header{{display:flex;gap:12px;align-items:baseline;flex-wrap:wrap;font-size:13px;margin-bottom:12px}}
.seed{{font-weight:700}} .harm{{color:var(--primary);font-weight:600}} .hues{{color:var(--muted)}}
.swatches{{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;font-size:11px}}
.sw{{display:flex;flex-direction:column;gap:2px}}
.chip{{height:34px;border-radius:4px;border:1px solid var(--line)}}
.sw code{{color:var(--muted);font-size:10.5px}}
.sample{{background:var(--surface);border:1px solid var(--line);border-radius:6px;padding:14px;margin:14px 0}}
.sample h2{{margin:0 0 8px;font-size:17px;color:var(--primary)}}
.sample p{{margin:0 0 10px;font-size:13px;line-height:1.5}}
.mut{{color:var(--muted)}} .ok{{color:var(--ok);font-weight:600}} .alert{{color:var(--alert);font-weight:600}}
.callout{{background:var(--primary-soft);border-left:3px solid var(--primary);padding:8px 10px;font-size:13px;border-radius:0 4px 4px 0}}
.callout2{{background:var(--accent-soft);padding:8px 10px;font-size:13px;margin-top:8px;border-radius:4px}}
.dot{{display:inline-block;width:10px;height:10px;border-radius:50%;background:var(--accent);margin-right:6px}}
table{{width:100%;border-collapse:collapse;font-size:11.5px}}
td{{padding:2px 4px;border-top:1px solid var(--line)}} td:nth-child(n+2){{text-align:right}}
tr.bad td{{color:#b00020;font-weight:700}}
</style></head><body>
<h1>Palette sheet &ndash; {len(palettes)} palettes</h1>
<div class="grid">{''.join(cards)}</div>
</body></html>"""


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--seed", type=int, help="random seed (default: random)")
    ap.add_argument("--harmony", choices=HARMONIES)
    ap.add_argument("--hue", type=float, help="primary hue in degrees (0-360)")
    ap.add_argument("--count", type=int, default=1, help="number of palettes")
    ap.add_argument("--format", choices=["json", "css"], default="json")
    ap.add_argument("--sheet", metavar="PATH", help="write an HTML swatch sheet")
    a = ap.parse_args(argv)

    seed0 = a.seed if a.seed is not None else random.SystemRandom().randrange(1, 10 ** 6)
    palettes = [generate(seed0 + i, a.harmony, a.hue) for i in range(max(1, a.count))]

    if a.sheet:
        with open(a.sheet, "w", encoding="utf-8") as f:
            f.write(sheet_html(palettes))

    if a.format == "json":
        print(json.dumps(palettes[0] if len(palettes) == 1 else palettes, indent=2))
    else:
        if len(palettes) == 1:
            print(css_block(palettes[0]))
        else:
            for p in palettes:
                print(f"/* seed {p['seed']} - {p['harmony']} */")
                print(css_block(p, f".palette-{p['seed']}"))
    bad = [p["seed"] for p in palettes if "failed" in p]
    if bad:
        print(f"warning: contrast checks failed for seeds {bad}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
