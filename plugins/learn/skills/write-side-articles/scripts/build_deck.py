"""Build one side article as its own swipe deck, and check it against the deck rules. Plain Python, no AI.

    python scripts/build_deck.py <article>.html --out <deck>.html [--avoid 191,54]

<article>.html is the article: its palette block, its meta, its cards (shape: references/article-format.md).
The script puts them into assets/deck-template.html (the engine Ash approved on 2026-11-05, prototype v14),
then checks every rule code can check (Fuji ticket 39). It prints each failure with its card and exits 1;
the deck is written only when nothing fails. --avoid takes the combination numbers of earlier decks.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
TEMPLATE = HERE / "assets" / "deck-template.html"

# The card order (ticket 39, big question 1). "world" takes one or two cards.
ORDER = ["question", "promise", "wrong", "instead", "why", "concept", "concept", "team", "world", "world?",
         "changes", "far", "limit", "answer", "other"]
DEFAULT_BLUES = {"#0000ff", "#007aff", "#0a84ff", "#1a73e8", "#2563eb", "#3b82f6", "#0066cc"}
OLD_PICTURES = re.compile(r"\b(park|lawn|boat|lagoon|worn path)\b", re.I)  # the culture prototype's drawings
BACKREF = re.compile(r"\b(the same (draft|example|one|story|person)|as (we|you) saw|from earlier|(see|as) above|"
                     r"the last card|(previous|next|earlier|first) card|like before|remember the)\b", re.I)
HOWTO = re.compile(r"\b(tap|swipe|click|scroll)\b", re.I)
HEDGE = re.compile(r"\b(no speech|no poster|not just|simply put|in other words|basically|it's worth|note that)\b", re.I)
MAX_WORDS = 30          # "No paragraphs": one block of text never runs longer than this
PART_NAME_MAX = 9       # one word that fits a quarter of a 390px trail


def text_of(html: str) -> str:
    html = re.sub(r"<(title|details|svg)\b.*?</\1>", " ", html, flags=re.S | re.I)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html)).strip()


def words(s: str) -> int:
    return len(s.split())


class Blocks(HTMLParser):
    """Collects the text of every <p>, <li>, <b class=quote>, keyline line and stop line, to catch paragraphs."""
    TAGS = {"p", "li"}

    def __init__(self):
        super().__init__()
        self.stack, self.out = [], []

    def handle_starttag(self, tag, attrs):
        if tag in self.TAGS:
            self.stack.append([])

    def handle_endtag(self, tag):
        if tag in self.TAGS and self.stack:
            self.out.append(" ".join("".join(self.stack.pop()).split()))

    def handle_data(self, data):
        if self.stack:
            self.stack[-1].append(data)


def split_article(src: str) -> tuple[str, dict, list[dict], str]:
    m = re.search(r'<style id="tokens">(.*?)</style>', src, re.S)
    if not m:
        raise SystemExit('article: no <style id="tokens"> block (paste palette.py output into it)')
    tokens = m[1].strip()
    j = re.search(r'<script type="application/json" id="article">(.*?)</script>', src, re.S)
    if not j:
        raise SystemExit('article: no <script type="application/json" id="article"> block')
    meta = json.loads(j[1])
    cards = [{"part": int(c[0]), "kind": c[1], "html": c[2]} for c in
             re.findall(r'<template class="card" data-part="(\d)" data-kind="([a-z]+)">(.*?)</template>', src, re.S)]
    rest = src.replace(m[0], "").strip()
    return tokens, meta, cards, rest


def hexes(tokens: str) -> dict[str, str]:
    vals = dict(re.findall(r"--([a-z0-9-]+):\s*([^;]+);", tokens))
    out = {}
    for k, v in vals.items():
        seen = 0
        while v.startswith("var(--") and seen < 5:
            v = vals.get(v[6:-1], v)
            seen += 1
        out[k] = v.strip().lower()
    return out


def check(tokens: str, meta: dict, cards: list[dict], avoid: set[int]) -> list[str]:
    bad = []
    add = lambda where, msg: bad.append(f"{where}: {msg}")  # noqa: E731

    # the look: a new combination, the island from it but not the accent, four part colours
    combo = re.search(r"No\. (\d+)", tokens)
    if not combo:
        add("tokens", "no 'No. N' palette comment from match-ash-design's palette.py")
    elif int(combo[1]) in avoid:
        add("tokens", f"combination No. {combo[1]} was used by an earlier deck; run palette.py with a new seed")
    if "place dark" not in tokens:
        add("tokens", "not a place-dark palette (decks are dark only)")
    hx = hexes(tokens)
    island = hx.get("island")
    if not island:
        add("tokens", "no --island colour")
    elif island == hx.get("acc"):
        add("tokens", "--island is the accent; take another colour of the combination (a --b token)")
    elif island in DEFAULT_BLUES:
        add("tokens", "--island is a default blue")

    # the meta
    for k in ("id", "title", "question", "world", "expert", "reader"):
        if not str(meta.get(k, "")).strip():
            add("meta", f"missing {k}")
    if not str(meta.get("question", "")).endswith("?"):
        add("meta", "the question doesn't end with '?'")
    parts = meta.get("parts") or []
    if len(parts) != 4:
        add("meta", f"{len(parts)} parts; the trail has exactly 4")
    for p in parts:
        n = str(p.get("name", ""))
        if " " in n.strip() or len(n) > PART_NAME_MAX:
            add("meta", f"part name '{n}' must be one word of at most {PART_NAME_MAX} letters, to fit at 390px")
        if len(str(p.get("long", ""))) > 26:
            add("meta", f"part long name '{p.get('long')}' is over 26 characters")
    if len({str(p.get("c")) for p in parts}) != len(parts):
        add("meta", "two parts share a colour")
    if re.search(r"haiku", json.dumps(meta.get("written_by", "")), re.I):
        add("meta", "copy written by Haiku; write it in the build session on the strongest model")

    # the card order
    kinds = [c["kind"] for c in cards]
    pat = "^" + "".join(f"({k[:-1]},)?" if k.endswith("?") else f"{k}," for k in ORDER) + "$"
    if not re.match(pat, "".join(k + "," for k in kinds)):
        add("order", f"cards are {kinds}; want {[k for k in ORDER]} ('world?' is an optional second world card)")
    if [c["part"] for c in cards] != sorted(c["part"] for c in cards) or {c["part"] for c in cards} != {0, 1, 2, 3}:
        add("order", "parts must run 0, 1, 2, 3 in order, each with at least one card")

    names = set()
    for i, c in enumerate(cards, 1):
        h, where = c["html"], f"card {i} ({c['kind']})"
        heads = re.findall(r"<h[12]\b[^>]*>(.*?)</h[12]>", h, re.S)
        if len(heads) != 1:
            add(where, f"{len(heads)} headings; one per card")
        elif c["kind"] != "question" and not text_of(heads[0]).endswith("?"):
            add(where, f"heading '{text_of(heads[0])}' isn't a plain question")
        if c["kind"] == "question" and "@@QUESTION@@" not in h:
            add(where, "the first card's heading must be @@QUESTION@@")
        body = text_of(re.sub(r"<h[12]\b.*?</h[12]>", " ", h, flags=re.S))
        if re.search(r"<table\b", h, re.I):
            add(where, "a table; show the real moment instead")
        if re.search(r"<(s|del|strike)\b|line-through", h, re.I):
            add(where, "a cross-out; show before and now side by side")
        for b in (lambda p: (p.feed(h), p.out)[1])(Blocks()):
            if words(b) > MAX_WORDS:
                add(where, f"a {words(b)}-word block (max {MAX_WORDS}): '{b[:60]}…'; break it into short stacked lines")
        for rx, msg in ((BACKREF, "points back to another card; every card stands alone"),
                        (HOWTO, "a how-to line; Ash knows how the deck works"),
                        (HEDGE, "a hedging line; cut it")):
            m = rx.search(body)
            if m:
                add(where, f"'{m[0]}' {msg}")
        if h.count('class="mark"') > 1:
            add(where, "more than one highlighter line")
        if h.count('class="keyline"') > 1:
            add(where, "more than one box")
        names |= {text_of(n).lower() for n in re.findall(r'class="name"[^>]*>(.*?)</', h, re.S)}
        svgs = re.findall(r"<svg\b.*?</svg>", h, re.S)
        for s in svgs:
            t = re.search(r"<title[^>]*>(.*?)</title>", s, re.S)
            if not t:
                add(where, "a drawing with no <title>")
            elif OLD_PICTURES.search(t[1]):
                add(where, f"'{OLD_PICTURES.search(t[1])[0]}' is the culture prototype's picture; draw from this article's world")
            if re.search(r"#[0-9a-f]{3,6}\b", s, re.I):
                add(where, "a drawing with a literal colour; use the s-/k- classes")
        if svgs:
            first_text = re.search(r'<(p|div) class="(line|big|lead|seq)', h)
            if first_text and first_text.start() < h.index("<svg"):
                add(where, "words before the picture; picture first, words after")
        if c["kind"] in ("instead", "why", "far") and not svgs:
            add(where, "no drawing; this card shows its idea as a picture")
        if c["kind"] == "question" and words(body) > 45:
            add(where, f"where you are runs {words(body)} words; two short lines")
        if c["kind"] == "far" and not re.search(r'class="eyebrow">\s*Far away', h):
            add(where, "the far-transfer eyebrow starts 'Far away'")
        if c["kind"] == "concept" and kinds.index("concept") == i - 2 and 'class="name"' not in h:
            add(where, "the second concept card ends on the concept's name")
        if c["kind"] == "concept" and kinds.index("concept") == i - 1 and not re.search(r'class="places', h):
            add(where, "the first concept card shows the parts big and numbered (ol.places)")
        if c["kind"] == "team" and 'class="ba' not in h:
            add(where, "the team card shows before and now side by side (div.ba)")
        if c["kind"] == "answer":
            if 'class="st"' not in h:
                add(where, "the answer comes in steps (div.st)")
            if 'class="mark"' not in h:
                add(where, "the answer ends on one marked line")
            if "<details" not in h:
                add(where, "no folded Sources")
        if c["kind"] == "other":
            qs = re.findall(r'<button class="q" data-q="([^"]+)">(.*?)</button>', h, re.S)
            if len(qs) != 3:
                add(where, f"{len(qs)} other questions; three")
            for dq, label in qs:
                if dq.strip() != text_of(label) or not dq.strip().endswith("?"):
                    add(where, f"other question '{dq[:50]}' must match its label and end with '?'")
    if len(names) > 2:
        add("deck", f"{len(names)} named concepts {sorted(names)}; at most the big concept and the far-transfer name")
    return bad


def build(article: Path, out: Path, avoid: set[int]) -> list[str]:
    src = article.read_text(encoding="utf-8")
    tokens, meta, cards, rest = split_article(src)
    bad = check(tokens, meta, cards, avoid)
    if not bad:
        page = TEMPLATE.read_text(encoding="utf-8")
        title = re.sub(r"[<>&]", "", str(meta["title"]))
        page = page.replace("@@TITLE@@", title).replace("@@TOKENS@@", tokens).replace("@@ARTICLE@@", rest)
        out.write_text(page, encoding="utf-8")
    return bad


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("article", type=Path)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--avoid", default="", help="combination numbers earlier decks used, comma-separated")
    a = ap.parse_args()
    avoid = {int(x) for x in re.findall(r"\d+", a.avoid)}
    bad = build(a.article, a.out, avoid)
    if bad:
        print("\n".join(bad))
        sys.exit(1)
    print(f"built {a.out}")


if __name__ == "__main__":
    main()
