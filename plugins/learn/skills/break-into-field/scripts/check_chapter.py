"""Mechanical check on a markdown chapter, before the critic reads it.

Usage: python check_chapter.py <chapter.md | book.html>

An HTML file is stripped to markdown-like text first (headings to #, list items to -,
blockquotes to >), and only the chapter sections (id starting with "ch") are checked.

FAIL: an em dash; "not X, but Y" or "not just / not only"; a block quote (quotes don't
      teach; keep them in the research file); a date like 1970 or a bracketed timestamp;
      a heading from the cut list (What you'll learn, First principles, Mental models,
      Judge a build, Words you now own, Glossary, Key takeaways, Common mistakes,
      Practice, Check yourself); a bullet over 2 sentences; a flat list over 3 items;
      a chapter that doesn't open with "Where you are now" or close with "The answer".
WARN: hedges; a bold opener under 4 words (often a slogan); a heading ending with a
      colon-free label of one word.
It reads patterns, not meaning. The critic covers the rest (references/critic.md).
"""
import re
import sys

CUT = ["what you'll learn", "first principles", "mental models", "judge a build",
       "words you now own", "glossary", "key takeaways", "common mistakes", "practice",
       "check yourself", "the fix, part by part"]
HEDGES = re.compile(r"\b(probably|might|maybe|perhaps|likely|arguably|somewhat)\b", re.I)


def html_to_text(html):
    """Keep only sections whose id starts with ch; turn headings, items and quotes into markdown marks."""
    secs = re.findall(r'<section[^>]*id="ch[^"]*"[^>]*>(.*?)</section>', html, re.S)
    html = "\n".join(secs) if secs else html
    html = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", html, flags=re.S)
    html = re.sub(r"<h([1-6])[^>]*>", lambda m: "\n" + "#" * int(m.group(1)) + " ", html)
    html = re.sub(r"</h[1-6]>", "\n", html)
    html = re.sub(r"<li[^>]*>", "\n- ", html)
    html = re.sub(r"<blockquote[^>]*>", "\n> ", html)
    html = re.sub(r"<(strong|b)>", "**", html)
    html = re.sub(r"</(strong|b)>", "**", html)
    html = re.sub(r"</(p|div|ol|ul|table|tr)>", "\n", html)
    html = re.sub(r"<[^>]+>", "", html)
    html = re.sub(r"&nbsp;", " ", html)
    return html


def main(path):
    text = open(path, encoding="utf-8").read()
    if path.lower().endswith((".html", ".htm")):
        text = html_to_text(text)
    lines = text.splitlines()
    fails, warns = [], []
    heads = [l.strip("# ").strip() for l in lines if l.startswith("#")]
    if "—" in text:
        fails.append("em dash found; use a comma, a full stop or brackets")
    if re.search(r"\bnot (just|only)\b", text, re.I) or re.search(r"\bnot\s+\w+(\s+\w+){0,4},\s*but\b", text, re.I):
        fails.append('"not X, but Y" found; state the point positively')
    for i, l in enumerate(lines, 1):
        s = l.strip()
        if s.startswith(">"):
            fails.append(f"line {i}: block quote; quotes stay in the research file")
        if re.search(r"\b(19|20)\d\d\b", s) and not s.startswith("#"):
            fails.append(f"line {i}: a date; cut the history")
        if re.search(r"\[\d{1,2}:\d\d\]", s):
            fails.append(f"line {i}: timestamp")
        if re.match(r"^[-*] ", s):
            body = re.sub(r"\*\*", "", s[2:])
            n = len(re.findall(r"[.!?](\s|$)", body))
            if n > 2:
                fails.append(f"line {i}: bullet of {n} sentences (max 2)")
            m = re.match(r"^\*\*([^*]+)\*\*", s[2:])
            if m and len(m.group(1).split()) < 4:
                warns.append(f"line {i}: short bold opener '{m.group(1)}'; a slogan?")
        if HEDGES.search(s):
            warns.append(f"line {i}: hedge word")
    for h in heads:
        if h.lower().rstrip("?") in CUT:
            fails.append(f'heading "{h}" is on the cut list')
    # flat lists over 3 items
    run = 0
    for i, l in enumerate(lines, 1):
        if re.match(r"^[-*] ", l):
            run += 1
            if run == 4:
                fails.append(f"line {i}: flat list of 4+ items; group under bold labels")
        elif l.strip() and not l.startswith("  "):
            run = 0
    if heads and "where you are now" not in heads[0].lower() and (len(heads) < 2 or "where you are now" not in heads[1].lower()):
        fails.append('the chapter must open with "Where you are now"')
    if heads and "the answer" not in heads[-1].lower():
        fails.append('the chapter must close with "The answer"')
    for w in warns:
        print("warn ", w)
    for f in fails:
        print("FAIL ", f)
    if not fails:
        print("PASS: no mechanical breaks")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
