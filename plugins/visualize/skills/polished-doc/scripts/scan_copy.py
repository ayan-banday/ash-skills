#!/usr/bin/env python3
"""Scan the visible text of an HTML file for copy-rule violations.

Usage: python scan_copy.py file.html

Checks: em and en dashes, banned words, lead-ins, negative parallelism, hedges,
generic headings, frequency claims in headings, paragraphs over three sentences,
one-word sentences, parenthetical side notes. Exit code 1 if anything is found.
Counts that must match a list, and whether the bold alone tells the story, still need a human read.
"""
import re
import sys

BANNED_WORDS = ["demystify", "identify", "leverage", "journey", "empower", "crucial", "optimize", "unlock",
                "elevate", "seamless", "game-changer", "dive in", "landscape", "robust", "holistic", "synergy"]
LEAD_INS = ["Here's", "Here is", "Here are", "Let's dive", "worth noting", "It's worth", "one of two", "a few things", "two things"]
HEDGES = ["might", "perhaps", "somewhat", "arguably", "tends to", "kind of", "sort of", "in some ways", "it could be argued", "could potentially"]
NEG_PARALLEL = [r"\bnot\b[^.<>]{0,70}\bbut\b", r"\bisn't\b[^.<>]{0,60}\bit's\b", r"\bIt's not\b", r"\bisn't\b", r"\baren't\b[^.<>]{0,60}\bthey're\b"]
GENERIC_HEADINGS = ["overview", "introduction", "the problem", "summary", "why it matters", "next steps",
                    "mistakes to avoid", "common mistakes", "background", "conclusion"]
FREQ_WORDS = ["most ", "usually", "often", "always", "never", "everyone", "nobody ever"]


def visible(html):
    html = re.sub(r"<(style|script|svg)\b.*?</\1>", " ", html, flags=re.S | re.I)
    return html


def text_of(fragment):
    t = re.sub(r"<[^>]+>", " ", fragment)
    t = t.replace("&amp;", "&").replace("&nbsp;", " ").replace("&quot;", '"')
    return re.sub(r"\s+", " ", t).strip()


def context(text, m, w=45):
    s = max(0, m.start() - w)
    return text[s:m.end() + w].replace("\n", " ")


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    raw = open(sys.argv[1], encoding="utf-8").read()
    html = visible(raw)
    full = text_of(html)
    hits = []

    if chr(0x2014) in raw:
        hits.append(("em dash", "found in file"))
    if chr(0x2013) in raw:
        hits.append(("en dash", "found in file"))

    for w in BANNED_WORDS:
        for m in re.finditer(r"\b" + re.escape(w), full, flags=re.I):
            hits.append(("banned word", context(full, m)))
    for w in LEAD_INS:
        for m in re.finditer(re.escape(w), full, flags=re.I):
            hits.append(("lead-in", context(full, m)))
    for w in HEDGES:
        for m in re.finditer(r"\b" + re.escape(w) + r"\b", full, flags=re.I):
            hits.append(("hedge", context(full, m)))
    for pat in NEG_PARALLEL:
        for m in re.finditer(pat, full):
            hits.append(("negative parallelism", context(full, m)))
    for m in re.finditer(r"\(([^)]{3,80})\)", full):
        hits.append(("parenthetical aside (check)", context(full, m)))

    for tag, inner in re.findall(r"<(h[1-3])\b[^>]*>(.*?)</\1>", html, flags=re.S | re.I):
        t = text_of(inner)
        low = t.lower()
        if low in GENERIC_HEADINGS:
            hits.append(("heading names a slot", t))
        for fw in FREQ_WORDS:
            if re.search(r"\b" + fw.strip() + r"\b", low) and tag.lower() != "h3":
                hits.append(("frequency claim in heading", t))
                break

    for inner in re.findall(r"<p\b[^>]*>(.*?)</p>", html, flags=re.S | re.I):
        t = text_of(inner)
        t_split = re.sub(r"\b(Dr|Mr|Mrs|Ms|St|vs|etc|e\.g|i\.e|No|approx)\.", lambda m: m.group(0).replace(".", "\u2024"), t)
        sentences = [s for s in re.split(r"(?<=[.!?])\s+", t_split) if s]
        if len(sentences) > 3:
            hits.append(("paragraph over three sentences", t[:90] + "..."))
        for s in sentences:
            words = re.findall(r"[A-Za-z']+", s)
            if len(words) == 1:
                hits.append(("one-word sentence", s))

    if not hits:
        print("copy scan: clean")
        return 0
    seen = set()
    for kind, ctx in hits:
        key = (kind, ctx)
        if key in seen:
            continue
        seen.add(key)
        print("HIT [%s] %s" % (kind, ctx))
    print("copy scan: %d hit(s)" % len(seen))
    return 1


if __name__ == "__main__":
    sys.exit(main())
