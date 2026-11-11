#!/usr/bin/env python3
"""Colour any page from one numbered combination in Wada Sanzo's Dictionary of Color Combinations.

    python scripts/palette.py --place dark --seed "Breaking Into Growth"   same seed, same combination
    python scripts/palette.py --place dark --combo 273                     one combination by its number
    python scripts/palette.py --place pitch --seed random                  a new one each run
    python scripts/palette.py --place dark --preset 2                      an approved preset (1, 2 or 3)
    python scripts/palette.py --place dark --combo 273 --key band          force a key-line style (dark only)
    python scripts/palette.py --place light --combo 273 --format json      tokens plus the book's colours
    python scripts/palette.py --place dark --count 6 --sheet sheet.html    six candidates to look at
    python scripts/palette.py --place dark --near "Espresso and Sand"      only combinations like one favourite
    python scripts/palette.py --place dark --format study --seed "Title"   the study-page tokens (BBA, Shasta)
    python scripts/palette.py --place dark --format study --no-red --seed "Title"   the same, never red-led
    python scripts/palette.py --format study --chapters 4 --seed "Title"   one palette per chapter tab, none red
    python scripts/palette.py --place dark --any                           ignore the favourites lean
    python scripts/palette.py --list                                       how many combinations fit each place
    python scripts/palette.py --test                                       every combination, every place, the presets

Places:
  dark   Ash's own pages: study pages, books, the week page, his tools. Near-black ground with no blue or
         green tint; every colour of the book allowed as pastels and accents (Ash, Nov 3 2026), except
         a yellow p1 (p1 is the marker band).
  light  pages for others: briefs, slides, posts, Udyaan, anything else. Warm paper from the lightest colour.
  pitch  pitches for outsiders: the same warm light paper as light. Green is fine anywhere it fits (Ash, Nov 11 2026).
  print  printed documents: light, quieter paper and fills.

Prints a :root{...} block with 12 tokens (--bg --bg2 --bg3 --tx --mu --ln --p1 --p2 --p3 --acc --acc2 --on
--onacc) plus --b1..--b4, the combination's colours exactly as printed (big shapes only, never behind text).
On dark it also prints the key-line CSS. combo_hues(n) gives other scripts (brief-page) the book's hues.

Favourites lean (Ash, Nov 3 2026): on dark, a seeded pick lands about 75% of the time on a combination
that reimagines one of the palettes Ash already liked (Shasta's four and the three presets); the
rest of the book shares the other 25%. --near keeps only one favourite's look; --any turns the lean off.

--format study prints the token names Ash's study pages use (BBA pages and Shasta study pages):
--bg --surface --line --text --muted --head --bold --hl --hl-text --bullet --link, the picture board
--paper (dark) with --ink (labels and strokes on it), --on (dark text inside any soft fill), and one
colour per meaning in pictures: --sand/--sand-f (plan, yes), --loss/--loss-f (problem), --memory/
--memory-f (memory, notes), --grey (done, past, no).
Data: assets/wada-colors.json (MIT, see assets/LICENSE-wada-colors). Pure standard library.
"""
import argparse
import collections
import html
import json
import math
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "assets", "wada-colors.json")
PLACES = ["dark", "light", "pitch", "print"]
KEYS = ["block", "band", "underline"]

# ---------- OKLCH <-> sRGB ----------

def _lin_to_srgb(x):
    return 12.92 * x if x <= 0.0031308 else 1.055 * x ** (1 / 2.4) - 0.055

def _srgb_to_lin(x):
    return x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4

def _oklch_rgb(L, C, h):
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

def px(L, C, h):
    """OKLCH to hex, lowering chroma until the colour fits in sRGB."""
    L = min(0.999, max(0.0, L))
    while C > 0:
        rgb = _oklch_rgb(L, C, h % 360)
        if rgb:
            return "#" + "".join(f"{round(v * 255):02X}" for v in rgb)
        C -= 0.003
    rgb = _oklch_rgb(L, 0, 0)
    return "#" + "".join(f"{round(v * 255):02X}" for v in rgb)

def oklch(hx):
    r, g, b = (_srgb_to_lin(int(hx[i:i + 2], 16) / 255) for i in (1, 3, 5))
    l = (0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b) ** (1 / 3)
    m = (0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b) ** (1 / 3)
    s = (0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b) ** (1 / 3)
    L = 0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s
    a = 1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s
    bb = 0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s
    return L, math.hypot(a, bb), math.degrees(math.atan2(bb, a)) % 360

def luminance(hx):
    r, g, b = (_srgb_to_lin(int(hx[i:i + 2], 16) / 255) for i in (1, 3, 5))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def contrast(a, b):
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)

def rgba(hx, a):
    return f"rgba({int(hx[1:3], 16)},{int(hx[3:5], 16)},{int(hx[5:7], 16)},{a})"

# ---------- The book ----------

def load():
    combos = collections.defaultdict(list)
    for c in json.load(open(DATA, encoding="utf-8")):
        for n in c["combinations"]:
            combos[n].append({"name": c["name"], "hex": c["hex"].upper(), "o": oklch(c["hex"])})
    return dict(sorted(combos.items()))

BOOK = load()

def coloured(c):
    return c["o"][1] >= 0.03

def is_cool(o):  # green or blue
    return o[1] >= 0.03 and 100 <= o[2] <= 268

def is_yellow(o):
    return o[1] > 0.035 and 85 <= o[2] < 110

def ground_ok(hx):
    """A dark ground is near-black with no blue or green tint."""
    L, C, h = oklch(hx)
    return C <= 0.004 or not (90 <= h <= 300)

def combo_hues(n):
    """The book's colours for combination n, strongest first: [(name, hex, L, C, h), ...]."""
    cols = sorted(BOOK[n], key=lambda c: -c["o"][1])
    return [(c["name"], c["hex"]) + tuple(c["o"]) for c in cols]

# ---------- Tokens per place ----------

def _lift(hx, ground, need, step):
    L, C, h = oklch(hx)
    out = hx
    for _ in range(80):
        if contrast(out, ground) >= need:
            break
        L += step
        out = px(L, C, h)
    return out

def _pair_accents(notes, ground, need, step):
    by = sorted(notes, key=lambda c: -c["o"][1])
    a = by[0]
    far = [c for c in by[1:] if abs((c["o"][2] - a["o"][2] + 180) % 360 - 180) > 25]
    a2 = far[0] if far else (by[1] if len(by) > 1 else a)
    return _lift(a["hex"], ground, need, step), _lift(a2["hex"], ground, need, step)

def dark(cols):
    notes = [c for c in cols if coloured(c)]
    if not notes:
        return None
    grounds = [c for c in notes if not (90 <= c["o"][2] <= 300)]
    if grounds:
        gh, gc = min(grounds, key=lambda c: c["o"][0])["o"][2], 1
    else:
        gh, gc = 0, 0
    p = dict(bg=px(.185, .011 * gc, gh), bg2=px(.215, .017 * gc, gh), bg3=px(.245, .021 * gc, gh),
             tx=px(.93, .008 * gc, gh), mu=px(.73, .012 * gc, gh))
    acc, acc2 = _pair_accents(notes, p["bg"], 3.2, .01)
    past = []
    for c in sorted(notes, key=lambda c: (is_yellow(c["o"]), -c["o"][0])):  # a yellow never leads (p1 is the marker)
        L, C, h = c["o"]
        hx = c["hex"] if (C <= .085 and contrast(p["bg"], c["hex"]) >= 7) else px(max(L, .82), min(C, .085), h)
        if hx not in past:
            past.append(hx)
    if grounds:
        d = min(grounds, key=lambda c: c["o"][0])
        past.append(px(.80, min(d["o"][1], .05), gh))
    while len(past) < 3:
        L, C, h = oklch(past[-1])
        past.append(px(.87, C * .5, h + 8))
    p.update(p1=past[0], p2=past[1], p3=past[2], acc=acc, acc2=acc2)
    p.update(ln=rgba(p["tx"], .12), on=p["bg"],
             onacc=p["bg"] if contrast(p["bg"], acc) >= contrast(p["tx"], acc) else p["tx"])
    return p

def light(cols, muted=False):
    notes = [c for c in cols if coloured(c)]
    if not notes:
        return None
    paper = max(cols, key=lambda c: c["o"][0])
    pc = .012
    pc *= .6 if muted else 1
    ph = paper["o"][2]
    ink = min(notes, key=lambda c: c["o"][0])["o"][2]
    p = dict(bg=px(.968, pc, ph), bg2=px(.938, pc * 1.3, ph), bg3=px(.905, pc * 1.6, ph),
             tx=px(.24, .03, ink), mu=px(.47, .025, ink))
    cm = .045 if muted else .075
    past = []
    for c in sorted(notes, key=lambda c: -c["o"][1]):
        hx = px(.86, min(c["o"][1], cm), c["o"][2])
        if hx not in past:
            past.append(hx)
    while len(past) < 3:
        L, C, h = oklch(past[-1])
        past.append(px(.90, C * .5, h + 10))
    acc, acc2 = _pair_accents(notes, p["bg"], 3.2, -.01)
    p.update(p1=past[0], p2=past[1], p3=past[2], acc=acc, acc2=acc2)
    p.update(ln=rgba(p["tx"], .14), on=p["tx"],
             onacc=p["bg"] if contrast(p["bg"], acc) >= contrast(p["tx"], acc) else p["tx"])
    return p

def tokens(n, place):
    cols = BOOK[n]
    p = {"dark": lambda: dark(cols), "light": lambda: light(cols),
         "pitch": lambda: light(cols), "print": lambda: light(cols, muted=True)}[place]()
    if p:
        p.update({f"b{i + 1}": cols[i % len(cols)]["hex"] for i in range(4)})
    return p

def checks(p, place):
    """Every contrast and colour rule. Returns failures (empty = pass)."""
    bad = []
    if place == "dark":
        for k in ("bg", "bg2", "bg3"):
            if not ground_ok(p[k]):
                bad.append(f"{k} {p[k]} has blue or green in it")
            need = 10.5 if k == "bg3" else 12
            if contrast(p["tx"], p[k]) < need:
                bad.append(f"tx on {k} {contrast(p['tx'], p[k]):.1f}:1 < {need}")
        if is_yellow(oklch(p["p1"])):
            bad.append(f"p1 {p['p1']} is yellow")
    else:
        if contrast(p["tx"], p["bg"]) < 7:
            bad.append(f"tx on bg {contrast(p['tx'], p['bg']):.1f}:1 < 7")
    if contrast(p["mu"], p["bg2"]) < 4.5:
        bad.append(f"mu on bg2 {contrast(p['mu'], p['bg2']):.1f}:1 < 4.5")
    for k in ("p1", "p2", "p3"):
        if contrast(p["on"], p[k]) < 7:
            bad.append(f"on on {k} {contrast(p['on'], p[k]):.1f}:1 < 7")
    for k in ("acc", "acc2"):
        if contrast(p[k], p["bg"]) < 3:
            bad.append(f"{k} on bg {contrast(p[k], p['bg']):.1f}:1 < 3")
    return bad

def fits(place):
    return [n for n in BOOK if (t := tokens(n, place)) and not checks(t, place)]

# ---------- Favourites: the palettes Ash already liked (lead colour, second colour, what it fits) ----------

FAVOURITES = {
    "Espresso and Sand": ("#E4D2B4", "#CE9D95", "money, habits and slow, steady building"),
    "Charcoal Rose": ("#F0C9CD", "#BCA880", "people, writing and communication"),
    "Ink and Clay": ("#EFCCBC", "#C79CB3", "tools, systems and how things work"),
    "Night Plum": ("#EEC9D6", "#C8A285", "creative work, design and ideas"),
    "Graphite and chalk": ("#EBC3CE", "#E58A6F", "study books"),
    "Ink and clay": ("#E2B6A4", "#D2603F", "study books"),
    "Charcoal and rose": ("#F0C4D2", "#C8668A", "study books"),
}
FAV_SHARE = 0.75

def _hd(a, b):
    d = abs(a - b) % 360
    return min(d, 360 - d)

def like(n):
    """The favourites a combination reimagines on dark: its lead pastel near theirs, a second colour near their second."""
    t = tokens(n, "dark")
    if not t:
        return []
    h1 = oklch(t["p1"])[2]
    others = [oklch(t[k])[2] for k in ("p2", "p3", "acc") if oklch(t[k])[1] > .02]
    out = []
    for name, (lead, second, _) in FAVOURITES.items():
        if _hd(h1, oklch(lead)[2]) <= 20 and others and min(_hd(o, oklch(second)[2]) for o in others) <= 30:
            out.append(name)
    return out

def _fav_name(q):
    hits = [k for k in FAVOURITES if k.lower() == q.lower()] or [k for k in FAVOURITES if k.lower().startswith(q.lower())]
    if len(hits) != 1:
        sys.exit(f"--near takes one of: {', '.join(FAVOURITES)}")
    return hits[0]

def red_led(n, place="dark"):
    """A combination whose lead pastel or accent is red, salmon or pink (Ash, Nov 4 2026: "use the different colour palettes apart from red")."""
    t = tokens(n, place)
    return any(oklch(t[k])[1] > .03 and (oklch(t[k])[2] >= 345 or oklch(t[k])[2] <= 55) for k in ("p1", "acc"))

def pool(place, near=None, lean=True, study=False, no_red=False):
    """Candidate combinations and their weights for a place."""
    ns = fits(place)
    if no_red:
        ns = [n for n in ns if not red_led(n, place)]
    if study:
        ns = [n for n in ns if not study_checks(study_tokens(tokens(n, place)))]
    if near:
        ns = [n for n in ns if near in like(n)]
        return ns, [1.0] * len(ns)
    if place != "dark" or not lean:
        return ns, [1.0] * len(ns)
    fav = {n for n in ns if like(n)}
    if not fav or len(fav) == len(ns):
        return ns, [1.0] * len(ns)
    wf, wo = FAV_SHARE / len(fav), (1 - FAV_SHARE) / (len(ns) - len(fav))
    return ns, [wf if n in fav else wo for n in ns]

def choose(seed, place, count=1, near=None, lean=True, study=False, no_red=False):
    ns, ws = pool(place, near, lean, study, no_red)
    if not ns:
        sys.exit("no combination fits these options")
    rng, picked = random.Random(seed), []
    while ns and len(picked) < count:
        i = rng.choices(range(len(ns)), weights=ws)[0]
        picked.append(ns.pop(i)); ws.pop(i)
    return picked

def chapters(seed, count, lean=True):
    """One combination per chapter of a tabbed book: none red-led, no yellow accent, lead pastels at least 45 degrees apart."""
    ns, ws = pool("dark", lean=lean, study=True, no_red=True)
    rng, picked = random.Random(seed), []
    while ns and len(picked) < count:
        i = rng.choices(range(len(ns)), weights=ws)[0]
        n = ns.pop(i); ws.pop(i)
        t = tokens(n, "dark")
        if is_yellow(oklch(t["acc"])) or is_yellow(oklch(t["acc2"])):  # a lemon kicker or loss colour across a whole chapter
            continue
        h = oklch(t["p1"])[2]
        if all(_hd(h, oklch(tokens(m, "dark")["p1"])[2]) >= 45 for m in picked):
            picked.append(n)
    if len(picked) < count:
        sys.exit(f"only {len(picked)} chapter palettes fit; ask for fewer chapters")
    return picked

# ---------- Study-page tokens (BBA and Shasta study pages) ----------

def study_tokens(p):
    L, C, gh = oklch(p["bg"])
    gc = 1 if C > 0.004 else 0
    def text_on_bg(hx, need=4.5):
        return _lift(hx, p["bg"], need, .01)
    h1, h3 = oklch(p["p1"])[2], oklch(p["p3"])[2]
    reds = sorted((p["acc"], p["acc2"]), key=lambda x: _hd(oklch(x)[2], 25))
    loss = text_on_bg(reds[0])
    lh = oklch(loss)[2]
    return {
        "bg": p["bg"], "surface": p["bg2"], "line": px(.33, .012 * gc, gh),
        "text": p["tx"], "muted": p["mu"], "head": px(.97, .006 * gc, gh),
        "bold": p["p1"], "hl": px(.32, .04, h1), "hl-text": p["tx"],
        "bullet": text_on_bg(p["acc"]), "link": p["p2"],
        "paper": p["bg3"], "ink": p["tx"], "on": p["bg"],
        "sand": p["p1"], "sand-f": px(.88, oklch(p["p1"])[1] * .6, h1),
        "loss": loss, "loss-f": px(.85, min(oklch(loss)[1], .06), lh),
        "memory": p["p3"], "memory-f": px(.88, oklch(p["p3"])[1] * .6, h3),
        "grey": px(.80, .008 * gc, gh),
    }

def study_checks(t):
    bad = []
    need = [("text", "bg", 7), ("muted", "bg", 4.5), ("muted", "surface", 4.5), ("head", "bg", 7),
            ("bold", "bg", 4.5), ("bullet", "bg", 4.5), ("link", "bg", 4.5), ("hl-text", "hl", 4.5),
            ("ink", "paper", 7), ("loss", "bg", 4.5), ("loss", "paper", 3), ("memory", "paper", 3),
            ("sand", "paper", 3)]
    need += [("on", k, 7) for k in ("sand", "sand-f", "loss-f", "memory", "memory-f", "grey")]
    for a, b, r in need:
        if contrast(t[a], t[b]) < r:
            bad.append(f"{a} on {b} {contrast(t[a], t[b]):.1f}:1 < {r}")
    return bad

def study_css(label, t):
    keys = list(t)
    rows = ["  " + " ".join(f"--{k}:{t[k]};" for k in keys[i:i + 5]) for i in range(0, len(keys), 5)]
    return "\n".join([f"/* Palette: {label} · study page, dark (match-ash-design scripts/palette.py --format study) */",
                      ":root{", *rows, "  color-scheme:dark;", "}"])

# ---------- Approved presets (dark, Nov 2 2026) ----------

PRESETS = {
    1: ("Graphite and chalk", "block",
        dict(bg="#1C1B1A", bg2="#252321", bg3="#2E2B29", tx="#E9E5E0", mu="#A49D96",
             p1="#EBC3CE", p2="#C9D5E4", p3="#EDCFB6", acc="#E58A6F", acc2="#C8668A")),
    2: ("Ink and clay", "band",
        dict(bg="#171615", bg2="#211F1D", bg3="#2B2826", tx="#EDE6DF", mu="#A89F96",
             p1="#E2B6A4", p2="#D9A8B5", p3="#D8CAB7", acc="#D2603F", acc2="#C8668A")),
    3: ("Charcoal and rose", "underline",
        dict(bg="#1E1D1F", bg2="#28262A", bg3="#322F34", tx="#ECE8EA", mu="#A69FA5",
             p1="#F0C4D2", p2="#E3CBD8", p3="#D9C3CF", acc="#C8668A", acc2="#E58A6F")),
}

def preset(i):
    name, key, p = PRESETS[i]
    p = dict(p)
    p.update(ln=rgba(p["tx"], .12), on=p["bg"], onacc=p["bg"],
             b1=p["p1"], b2=p["p2"], b3=p["p3"], b4=p["acc"])
    return name, key, p

# ---------- Output ----------

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

ORDER = ["bg", "bg2", "bg3", "tx", "mu", "ln", "p1", "p2", "p3", "acc", "acc2", "on", "onacc", "b1", "b2", "b3", "b4"]

def css(label, place, p, key=None):
    scheme = "dark" if place == "dark" else "light"
    lines = [f"/* Palette: {label} · place {place}{' · key line: ' + key if key else ''} (match-ash-design scripts/palette.py) */",
             ":root{",
             f"  --bg:{p['bg']}; --bg2:{p['bg2']}; --bg3:{p['bg3']};",
             f"  --tx:{p['tx']}; --mu:{p['mu']}; --ln:{p['ln']};",
             f"  --p1:{p['p1']}; --p2:{p['p2']}; --p3:{p['p3']}; --acc:{p['acc']}; --acc2:{p['acc2']};",
             f"  --on:{p['on']}; --onacc:{p['onacc']};",
             f"  --b1:{p['b1']}; --b2:{p['b2']}; --b3:{p['b3']}; --b4:{p['b4']}; /* as printed: big shapes only */",
             f"  color-scheme:{scheme};", "}"]
    if key:
        lines.append(key_css(key, p))
    return "\n".join(lines)

def label_of(n):
    fav = like(n)
    return f"No. {n}, " + " + ".join(c["name"] for c in BOOK[n]) + (f" · like {', '.join(fav)}" if fav else "")

def pick_seed(seed, place):
    return choose(seed, place)[0]

def sheet(items, place):
    cards = []
    for n, p in items:
        dots = "".join(f'<i style="background:{c["hex"]}"></i>' for c in BOOK[n])
        cards.append(f"""<section style="background:{p['bg']};color:{p['tx']};border:1px solid {p['ln']}">
<div class="dots">{dots}</div><b>{html.escape(label_of(n))}</b>
<h2>Does knowing my style save more grilling?</h2>
<p style="color:{p['mu']}">Muted text on the page.</p>
<div class="card" style="background:{p['bg2']}"><span class="pill" style="background:{p['p1']};color:{p['on']}">Holds</span>
<span class="pill" style="background:{p['p2']};color:{p['on']}">p2</span><span class="pill" style="background:{p['p3']};color:{p['on']}">p3</span>
<span class="pill" style="background:{p['acc']};color:{p['onacc']}">accent</span><span class="pill" style="background:{p['acc2']};color:{p['onacc']}">accent 2</span></div></section>""")
    return ("""<!doctype html><meta charset="utf-8"><title>Palette sheet</title><style>
body{margin:0;padding:20px;background:#777;font:15px system-ui,sans-serif;display:grid;grid-template-columns:repeat(auto-fill,minmax(360px,1fr));gap:16px}
section{padding:16px;border-radius:6px}h2{font-size:19px;margin:10px 0 4px}.dots{display:flex;gap:3px;margin-bottom:6px}.dots i{width:22px;height:22px;border-radius:2px}
.card{padding:10px;border-radius:4px;display:flex;flex-wrap:wrap;gap:6px}.pill{padding:4px 10px;border-radius:3px;font-weight:700}</style>""" + "".join(cards))

def selftest():
    fails = 0
    for place in PLACES:
        fit = fits(place)
        print(f"{place:6} {len(fit):3} of {len(BOOK)} combinations fit")
        if len(fit) < 200:
            print(f"FAIL {place}: fewer than 200 combinations fit"); fails += 1
    ns, ws = pool("dark")
    share = sum(w for n, w in zip(ns, ws) if like(n))
    print(f"favourites: {sum(1 for n in ns if like(n))} combinations look like one, picked {share:.0%} of the time on dark")
    for fav in FAVOURITES:
        print(f"  {fav:20} {len(pool('dark', near=fav)[0]):3}")
    st = pool("dark", study=True)[0]
    print(f"study  {len(st):3} of {len(BOOK)} combinations fit study pages")
    if len(st) < 150:
        print("FAIL study: fewer than 150 fit"); fails += 1
    for i in PRESETS:
        name, key, p = preset(i)
        bad = checks(p, "dark")
        print(("FAIL " if bad else "ok   ") + f"preset {i} {name}" + (" " + "; ".join(bad) if bad else ""))
        fails += bool(bad)
    for seed in ("Breaking Into Growth", "test-1", "test-2"):
        for place in PLACES:
            n = pick_seed(seed, place)
            bad = checks(tokens(n, place), place)
            fails += bool(bad)
            if bad:
                print(f"FAIL seed {seed} {place}: {bad}")
    print("PASS" if not fails else f"FAIL ({fails})")
    return 1 if fails else 0

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--place", choices=PLACES, default="dark")
    ap.add_argument("--seed", default="random")
    ap.add_argument("--combo", type=int)
    ap.add_argument("--preset", type=int, choices=[1, 2, 3])
    ap.add_argument("--key", choices=KEYS)
    ap.add_argument("--format", choices=["css", "json", "study"], default="css")
    ap.add_argument("--near", help="only combinations that look like one favourite: " + ", ".join(FAVOURITES))
    ap.add_argument("--any", action="store_true", help="every fitting combination equally likely")
    ap.add_argument("--count", type=int, default=1)
    ap.add_argument("--no-red", action="store_true", help="skip combinations led by red, salmon or pink")
    ap.add_argument("--chapters", type=int, metavar="N",
                    help="with --format study: one palette per chapter of a tabbed book, as [data-chapter=\"chK\"] blocks (never red)")
    ap.add_argument("--sheet", metavar="PATH")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--test", action="store_true")
    a = ap.parse_args()
    if a.test:
        return selftest()
    if a.list:
        for place in PLACES:
            print(f"{place:6} {len(fits(place)):3} of {len(BOOK)}")
        print(f"study  {len(pool('dark', study=True)[0]):3} of {len(BOOK)}")
        for fav in FAVOURITES:
            print(f"  like {fav:20} {len(pool('dark', near=fav)[0]):3}")
        return 0
    study = a.format == "study"
    if study and a.place != "dark":
        sys.exit("--format study is for dark study pages: use --place dark")
    if a.preset:
        if a.place != "dark":
            sys.exit("presets are dark only")
        name, key, p = preset(a.preset)
        print(css(name, "dark", p, a.key or key))
        return 0
    seed = random.random() if a.seed == "random" else a.seed
    if a.chapters:
        if not study:
            sys.exit("--chapters needs --format study")
        # Each block colours its tab (data-chapter="chK") and, while that tab is open, the whole page and
        # the tutor (:root[data-on="chK"]), so the rail, the desk and the background follow the chapter.
        for k, n in enumerate(chapters(seed, a.chapters, not a.any), 1):
            p = tokens(n, "dark")
            t = study_tokens(p)
            tut = {key: p[key] for key in ("bg2", "bg3", "tx", "mu", "ln", "p1", "p2", "p3", "acc", "acc2", "onacc")}
            body = study_css(label_of(n), t).replace(":root{", f'[data-chapter="ch{k}"],:root[data-on="ch{k}"]{{')
            body = body.replace("  color-scheme:dark;\n", "  " + " ".join(f"--{key}:{v};" for key, v in tut.items()) + "\n")
            print(body.replace("study page, dark", f"chapter {k}, dark"))
        return 0
    if a.combo:
        if a.combo not in BOOK:
            sys.exit(f"no combination {a.combo}; the book has 1 to {max(BOOK)}")
        ns = [a.combo]
    else:
        ns = choose(seed, a.place, a.count, _fav_name(a.near) if a.near else None, not a.any, study, a.no_red)
    items = []
    for n in ns:
        p = tokens(n, a.place)
        bad = checks(p, a.place) if p else ["no usable colours"]
        if bad:
            sys.exit(f"{label_of(n)} fails for {a.place}: {'; '.join(bad)}. Pick another combination.")
        items.append((n, p))
    if a.sheet:
        with open(a.sheet, "w", encoding="utf-8") as f:
            f.write(sheet(items, a.place))
        print("wrote", a.sheet, "with", ", ".join(f"No. {n}" for n, _ in items))
        return 0
    for n, p in items:
        if study:
            t = study_tokens(p)
            bad = study_checks(t)
            if bad:
                sys.exit(f"{label_of(n)} fails for study pages: {'; '.join(bad)}. Pick another combination.")
            print(study_css(label_of(n), t))
            continue
        if a.format == "json":
            print(json.dumps({"combo": n, "book": [{"name": c["name"], "hex": c["hex"]} for c in BOOK[n]],
                              "place": a.place, "like": like(n), "tokens": p}, indent=1))
        else:
            key = (a.key or random.Random(f"{seed}-{n}-key").choice(KEYS)) if a.place == "dark" else None
            print(css(label_of(n), a.place, p, key))
    return 0

if __name__ == "__main__":
    sys.exit(main())
