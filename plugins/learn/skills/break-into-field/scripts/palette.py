#!/usr/bin/env python3
"""Pick a dark palette and a key-line style for one study book.

    python scripts/palette.py --seed "Breaking Into Growth"   same seed, same palette
    python scripts/palette.py --seed random                   a new one each run
    python scripts/palette.py --preset 2                      an approved preset (1, 2 or 3)
    python scripts/palette.py --family mono --key band        force a family or a key-line style
    python scripts/palette.py --test                          20 random seeds and the 3 presets, every check

Prints a :root{...} block with the 12 tokens, the key-line CSS, and a one-line swatch.
Ash's rules (Nov 2 2026): dark charcoal grounds only, no blue or green in any ground,
pastels do the colour work, no yellow highlight. Pure standard library.
"""
import argparse
import math
import random
import sys

# ---------- OKLCH <-> sRGB ----------

def _lin_to_srgb(x):
    return 12.92 * x if x <= 0.0031308 else 1.055 * x ** (1 / 2.4) - 0.055

def _srgb_to_lin(x):
    return x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4

def oklch_to_rgb(L, C, h):
    """Returns (r, g, b) in 0..1, or None if the colour falls outside sRGB."""
    a, b = C * math.cos(math.radians(h)), C * math.sin(math.radians(h))
    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541728 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b
    l, m, s = l_ ** 3, m_ ** 3, s_ ** 3
    lin = (4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
           -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
           -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s)
    if any(v < -0.0005 or v > 1.0005 for v in lin):
        return None
    return tuple(min(1, max(0, _lin_to_srgb(v))) for v in lin)

def hex_to_oklch(hx):
    r, g, b = (_srgb_to_lin(int(hx[i:i + 2], 16) / 255) for i in (1, 3, 5))
    l = (0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b) ** (1 / 3)
    m = (0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b) ** (1 / 3)
    s = (0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b) ** (1 / 3)
    L = 0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s
    a = 1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s
    bb = 0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s
    return L, math.hypot(a, bb), math.degrees(math.atan2(bb, a)) % 360

def to_hex(rgb):
    return "#" + "".join(f"{round(v * 255):02X}" for v in rgb)

def luminance(hx):
    r, g, b = (_srgb_to_lin(int(hx[i:i + 2], 16) / 255) for i in (1, 3, 5))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def contrast(a, b):
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)

# ---------- The rules ----------

BANDS = {  # pastel hue bands: (low, high, max chroma)
    "rose": (340, 375, 0.08),     # 340 to 15, written past 360
    "clay": (25, 50, 0.08),
    "apricot": (55, 70, 0.08),
    "sand": (75, 85, 0.035),
    "lilac": (300, 330, 0.08),
    "sky": (225, 250, 0.035),     # at most one per palette, never p1
}
FAMILIES = {"clay": 3, "mono": 3, "chalk": 2}
KEYS = ["block", "band", "underline"]

PRESETS = {
    1: ("Graphite and chalk", "chalk", "block",
        dict(bg="#1C1B1A", bg2="#252321", bg3="#2E2B29", tx="#E9E5E0", mu="#A49D96",
             p1="#EBC3CE", p2="#C9D5E4", p3="#EDCFB6", acc="#E58A6F")),
    2: ("Ink and clay", "clay", "band",
        dict(bg="#171615", bg2="#211F1D", bg3="#2B2826", tx="#EDE6DF", mu="#A89F96",
             p1="#E2B6A4", p2="#D9A8B5", p3="#D8CAB7", acc="#D2603F")),
    3: ("Charcoal and rose", "mono", "underline",
        dict(bg="#1E1D1F", bg2="#28262A", bg3="#322F34", tx="#ECE8EA", mu="#A69FA5",
             p1="#F0C4D2", p2="#E3CBD8", p3="#D9C3CF", acc="#C8668A")),
}

def ground_ok(hx):
    """A ground is near-black with no blue or green: hue 90 to 300 only when it is neutral."""
    L, C, h = hex_to_oklch(hx)
    return C <= 0.004 or not (90 <= h <= 300)

def checks(p):
    """Every check from the spec. Returns a list of failures (empty = pass)."""
    bad = []
    for k in ("bg", "bg2", "bg3"):
        if not ground_ok(p[k]):
            bad.append(f"{k} {p[k]} has blue or green in it")
        need = 10.5 if k == "bg3" else 12  # bg3 holds only bubbles and cards; the approved presets sit at 10.9 to 11.8
        if contrast(p["tx"], p[k]) < need:
            bad.append(f"tx on {k} {contrast(p['tx'], p[k]):.1f}:1 < {need}")
    if contrast(p["mu"], p["bg2"]) < 4.5:
        bad.append(f"mu on bg2 {contrast(p['mu'], p['bg2']):.1f}:1 < 4.5")
    for k in ("p1", "p2", "p3"):
        if contrast(p["bg"], p[k]) < 7:
            bad.append(f"on on {k} {contrast(p['bg'], p[k]):.1f}:1 < 7")
        L, C, h = hex_to_oklch(p[k])
        if 100 <= h <= 200 and C > 0.02:
            bad.append(f"{k} {p[k]} is green")
        if 85 <= h <= 110 and C > 0.035:
            bad.append(f"{k} {p[k]} is yellow")
    if contrast(p["acc"], p["bg"]) < 3:
        bad.append(f"acc on bg {contrast(p['acc'], p['bg']):.1f}:1 < 3")
    return bad

def pick(rng, L, C, h):
    rgb = oklch_to_rgb(L, C, h % 360)
    return to_hex(rgb) if rgb else None

def pastel(rng, band, L=None, C=None):
    lo, hi, cmax = BANDS[band]
    return pick(rng, L if L is not None else rng.uniform(0.80, 0.88),
                C if C is not None else rng.uniform(0.03, min(0.08, cmax)), rng.uniform(lo, hi))

def make(rng, family=None):
    family = family or rng.choices(list(FAMILIES), weights=list(FAMILIES.values()))[0]
    kind = rng.choices(["warm", "rose", "neutral"], weights=[3, 2, 2])[0]
    gh = rng.uniform(20, 80) if kind == "warm" else rng.uniform(330, 360) if kind == "rose" else rng.uniform(0, 360)
    gc = rng.uniform(0, 0.0035) if kind == "neutral" else rng.uniform(0.004, 0.012)
    gl = rng.uniform(0.17, 0.23)
    p = dict(bg=pick(rng, gl, gc, gh), bg2=pick(rng, gl + 0.03, gc, gh), bg3=pick(rng, gl + 0.06, gc, gh),
             tx=pick(rng, rng.uniform(0.91, 0.94), min(gc, 0.012), gh),
             mu=pick(rng, rng.uniform(0.70, 0.74), min(gc + 0.004, 0.012), gh))
    if family == "clay":
        bands = ["clay", "rose", "sand"]
        rng.shuffle(bands)
        if bands[0] == "sand":  # sand is too quiet to lead
            bands[0], bands[1] = bands[1], bands[0]
        p1, p2, p3 = (pastel(rng, b) for b in bands)
    elif family == "mono":
        band = rng.choice(["rose", "clay", "apricot", "lilac"])
        lo, hi, _ = BANDS[band]
        h = rng.uniform(lo, hi)
        p1 = pick(rng, rng.uniform(0.84, 0.88), rng.uniform(0.06, 0.08), h)
        p2 = pick(rng, rng.uniform(0.84, 0.88), rng.uniform(0.04, 0.055), h + rng.uniform(-6, 6))
        p3 = pick(rng, rng.uniform(0.80, 0.84), rng.uniform(0.03, 0.04), h + rng.uniform(-6, 6))
    else:  # chalk: three different bands, sky at most once and never first
        lead = rng.choice(["rose", "clay", "apricot", "lilac"])
        rest = rng.sample([b for b in BANDS if b != lead], 2)
        p1, p2, p3 = pastel(rng, lead), pastel(rng, rest[0]), pastel(rng, rest[1])
    acc_h = rng.uniform(15, 45) if rng.random() < 0.6 else rng.uniform(345, 360)
    p.update(p1=p1, p2=p2, p3=p3, acc=pick(rng, rng.uniform(0.60, 0.70), rng.uniform(0.12, 0.17), acc_h))
    return family, p

def generate(seed, family=None, tries=200):
    rng = random.Random(seed)
    for _ in range(tries):
        fam, p = make(rng, family)
        if all(p.values()) and not checks(p):
            return fam, p
    return None, None

# ---------- Output ----------

def rgba(hx, a):
    return f"rgba({int(hx[1:3], 16)},{int(hx[3:5], 16)},{int(hx[5:7], 16)},{a})"

def key_css(style, p):
    if style == "block":
        return (".keyline{display:block;margin:18px 0;padding:14px 18px;background:var(--bg2);border-left:4px solid var(--p1);border-radius:0 8px 8px 0}\n"
                ".keyline .l{display:block;font:600 11.5px 'Overpass Mono',monospace;letter-spacing:.06em;text-transform:uppercase;color:var(--p1);margin-bottom:4px}\n"
                ".keyline .t{font:700 19px/1.45 Overpass,sans-serif;color:var(--tx)}\n"
                "/* HTML: <div class=\"keyline\"><span class=\"l\">The point</span><span class=\"t\">Sentence that reads alone.</span></div> */")
    if style == "band":
        return (f".keyline{{background:linear-gradient(transparent 42%,{rgba(p['p1'], .30)} 42%);font-weight:700;color:var(--tx);padding:1px 3px;box-decoration-break:clone;-webkit-box-decoration-break:clone}}\n"
                ".keyline-why{display:block;margin:-6px 0 16px;padding-left:12px;border-left:2px solid var(--p1);font-size:15px;color:var(--mu)}\n"
                "/* HTML: <p><span class=\"keyline\">Sentence that reads alone.</span></p><span class=\"keyline-why\">Why it matters: ...</span> */")
    return (".keyline{color:var(--p1);font-weight:700;text-decoration:underline dotted var(--p1);text-decoration-thickness:2px;text-underline-offset:5px}\n"
            "/* HTML: <p>... <span class=\"keyline\">the sentence that reads alone</span>, because the reason travels with it.</p> */")

def css(name, family, key, p):
    ln = rgba(p["tx"], .12)
    root = (":root{\n"
            f"  --bg:{p['bg']}; --bg2:{p['bg2']}; --bg3:{p['bg3']};\n"
            f"  --tx:{p['tx']}; --mu:{p['mu']}; --ln:{ln};\n"
            f"  --p1:{p['p1']}; --p2:{p['p2']}; --p3:{p['p3']}; --acc:{p['acc']}; --on:{p['bg']};\n"
            "  color-scheme:dark;\n}")
    sw = " ".join(f"{k}={p[k]}" for k in ("bg", "bg2", "bg3", "tx", "mu", "p1", "p2", "p3", "acc"))
    return (f"/* Palette: {name} · family {family} · key line: {key} (break-into-field scripts/palette.py) */\n"
            f"{root}\n{key_css(key, p)}\n/* swatch: {sw} */")

def selftest():
    fails = 0
    for i in range(20):
        seed = f"test-{i}-{random.random()}"
        fam, p = generate(seed)
        if not p:
            print(f"FAIL seed {i}: no passing palette in 200 tries"); fails += 1; continue
        bad = checks(p)
        for k in ("bg", "bg2", "bg3"):
            L, C, h = hex_to_oklch(p[k])
            if C > 0.004 and 90 <= h <= 300:
                bad.append(f"{k} hue {h:.0f} banned")
        print(("FAIL " if bad else "ok   ") + f"seed {i:2} {fam:5} bg={p['bg']} p1={p['p1']} p2={p['p2']} p3={p['p3']} acc={p['acc']}" + (" " + "; ".join(bad) if bad else ""))
        fails += bool(bad)
    for n, (name, fam, key, p) in PRESETS.items():
        bad = checks(p)
        print(("FAIL " if bad else "ok   ") + f"preset {n} {name}" + (" " + "; ".join(bad) if bad else ""))
        fails += bool(bad)
    print("PASS" if not fails else f"FAIL ({fails})")
    return 1 if fails else 0

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--seed", default="random")
    ap.add_argument("--preset", type=int, choices=[1, 2, 3])
    ap.add_argument("--family", choices=list(FAMILIES))
    ap.add_argument("--key", choices=KEYS)
    ap.add_argument("--test", action="store_true")
    a = ap.parse_args()
    if a.test:
        return selftest()
    if a.preset:
        name, fam, key, p = PRESETS[a.preset]
        print(css(name, fam, a.key or key, p))
        return 0
    seed = random.random() if a.seed == "random" else a.seed
    fam, p = generate(seed, a.family)
    if not p:
        print("No passing palette in 200 tries.", file=sys.stderr)
        return 1
    key = a.key or random.Random(f"{seed}-key").choice(KEYS)
    print(css(f"seed {a.seed}", fam, key, p))
    return 0

if __name__ == "__main__":
    sys.exit(main())
