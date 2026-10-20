#!/usr/bin/env python3
"""Copy scan for a proposal site: visible HTML text, SVG <text>, and copy-like strings inside scripts.

Usage: python scan.py page.html [--facts facts.md]

Checks: em and en dashes (also as entities), hype and banned words, lead-ins, hedges, negative parallelism,
slot headings, paragraphs over three sentences, one-word sentences, "Get started" style CTAs, and (with --facts)
every number in the copy that does not appear in the facts sheet. Exit code 1 on any hit.
A human still reads for: one wording per need, verbatim quotes, whether the highlights alone tell the story.
"""
import argparse, re, sys

BANNED = ["demystify", "leverage", "journey", "empower", "crucial", "optimize", "unlock", "unleash", "elevate",
          "seamless", "game-changer", "dive in", "landscape", "robust", "holistic", "synergy", "supercharge",
          "streamline", "effortless", "cutting-edge", "next-gen", "world-class", "revolutioni", "reimagin",
          "stewardship", "value chain", "best-in-class", "transformative", "harness", "in today's"]
LEAD_INS = ["Here's", "Here is", "Here are", "Let's dive", "worth noting", "It's worth"]
HEDGES = ["could", "might", "perhaps", "somewhat", "arguably", "tends to", "kind of", "sort of", "in some ways",
          "potentially", "hopefully", "nothing here is fixed"]
NEG = [r"\bnot\b[^.<>]{0,70}\bbut\b", r"\bisn't\b[^.<>]{0,60}\bit's\b", r"\bIt's not\b", r"\bnot just\b",
       r"\baren't\b[^.<>]{0,60}\bthey're\b", r"\bmore than just\b"]
SLOTS = ["overview", "introduction", "the problem", "summary", "why it matters", "next steps",
         "our approach", "why us", "why choose us", "features", "how it works", "about us", "conclusion", "background"]
CTAS = ["get started", "learn more", "let's talk", "get in touch", "contact us", "let's build"]


def strip_tags(s):
    s = re.sub(r"<[^>]+>", " ", s)
    for a, b in [("&amp;", "&"), ("&nbsp;", " "), ("&quot;", '"'), ("&#39;", "'"), ("&rsquo;", "'"), ("&lsquo;", "'")]:
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip()


def copy_text(raw):
    """Return (visible_html_without_code, list of extra copy strings from SVG text and scripts)."""
    extra = [strip_tags(t) for t in re.findall(r"<text\b[^>]*>(.*?)</text>", raw, flags=re.S | re.I)]
    for js in re.findall(r"<script\b[^>]*>(.*?)</script>", raw, flags=re.S | re.I):
        js = re.sub(r"/\*.*?\*/|(?<![:'\"])//[^\n]*", " ", js, flags=re.S)
        for q in re.findall(r"'((?:[^'\\\n]|\\.){12,})'|\"((?:[^\"\\\n]|\\.){12,})\"|`([^`]{12,})`", js):
            s = next(x for x in q if x)
            s = strip_tags(re.sub(r"\$\{[^}]*\}", " ", s))
            if re.search(r"[A-Za-z]{3,} [A-Za-z]{3,} [A-Za-z]{2,}", s) and not re.search(r"[{};=]|^[\w.-]+$|url\(|var\(--", s):
                extra.append(s)
    html = re.sub(r"<(style|script|svg)\b.*?</\1>", " ", raw, flags=re.S | re.I)
    return html, extra


def ctx(text, m, w=45):
    return text[max(0, m.start() - w):m.end() + w]


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("html"); ap.add_argument("--facts")
    a = ap.parse_args()
    raw = open(a.html, encoding="utf-8").read()
    html, extra = copy_text(raw)
    full = strip_tags(html) + " | " + " | ".join(extra)
    hits = []
    for ch, name in [("—", "em dash"), ("–", "en dash")]:
        for m in re.finditer(ch, full):
            hits.append((name, ctx(full, m)))
    for ent in ["&mdash;", "&ndash;", "&#8212;", "&#8211;"]:
        if ent in html:
            hits.append(("dash entity", ent))
    for w in BANNED:
        for m in re.finditer(r"\b" + re.escape(w), full, flags=re.I):
            hits.append(("hype or banned word", ctx(full, m)))
    for w in LEAD_INS:
        for m in re.finditer(r"\b" + re.escape(w) + r"\b", full, flags=re.I):
            hits.append(("lead-in", ctx(full, m)))
    for w in HEDGES:
        for m in re.finditer(r"\b" + re.escape(w) + r"\b", full, flags=re.I):
            hits.append(("hedge", ctx(full, m)))
    for p in NEG:
        for m in re.finditer(p, full, flags=re.I):
            hits.append(("negative parallelism", ctx(full, m)))
    for w in CTAS:
        for m in re.finditer(r"\b" + re.escape(w) + r"\b", full, flags=re.I):
            hits.append(("vague call to action", ctx(full, m)))
    for tag, inner in re.findall(r"<(h[1-3])\b[^>]*>(.*?)</\1>", html, flags=re.S | re.I):
        t = strip_tags(inner)
        if t.lower().strip(" .:") in SLOTS:
            hits.append(("heading names a slot", t))
        if len(t.split()) > 14:
            hits.append(("heading too long (over 14 words)", t))
    for inner in re.findall(r"<p\b[^>]*>(.*?)</p>", html, flags=re.S | re.I):
        t = strip_tags(inner)
        t2 = re.sub(r"\b(Dr|Mr|Mrs|Ms|St|vs|etc|e\.g|i\.e|No|approx)\.", lambda m: m.group(0).replace(".", "․"), t)
        sents = [s for s in re.split(r"(?<=[.!?])\s+", t2) if s]
        if len(sents) > 3:
            hits.append(("paragraph over three sentences", t[:90] + "..."))
        for s in sents:
            if len(re.findall(r"[A-Za-z']+", s)) == 1 and not re.search(r"\d", s):
                hits.append(("one-word sentence", s))
    if a.facts:
        facts = open(a.facts, encoding="utf-8").read()
        fact_nums = set(re.findall(r"\d[\d,.]*", facts))
        norm = lambda n: n.replace(",", "").rstrip(".").lstrip("0") or "0"
        fact_norm = {norm(n) for n in fact_nums}
        for m in re.finditer(r"(?<![\w#-])\d[\d,.]*(?:\s?(?:%|x|crore|cr|lakh|k|m)\b)?", full, flags=re.I):
            n = re.match(r"\d[\d,.]*", m.group(0)).group(0)
            if norm(n) in fact_norm or norm(n) in {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10"}:
                continue
            hits.append(("number not in facts (check)", ctx(full, m, 35)))
    seen = []
    for h in hits:
        if h not in seen:
            seen.append(h)
    if not seen:
        print("copy scan: clean"); return 0
    for kind, c in seen:
        print(f"HIT [{kind}] {c}")
    print(f"copy scan: {len(seen)} hit(s)")
    return 1


if __name__ == "__main__":
    sys.exit(main())
