"""Mechanical check on a study book (HTML) or one chapter (markdown), before the critic reads it.

Usage: python check_chapter.py <book.html | chapter.md>

Chapters are the <section> elements whose id is ch1, ch2, ... Each is checked on its own.
The paragraph rule is checked across the whole book (every part, every answer block).

FAIL, the paragraph rule (writing-rules.md, "Short paragraphs, one idea each"):
      a paragraph over 3 sentences or 60 words; a paragraph of 2+ sentences that doesn't
      open with a bold lead-in; a bullet over 2 sentences or 40 words.
FAIL, in each chapter: an em dash; "not X, but Y" or "not just / not only"; a block quote;
      a date like 1970 or a bracketed timestamp; a heading from the cut list; a generic
      skeleton heading that should be problem-specific; a flat list over 3 items; a map ID
      (A1, B2...) instead of the problem's plain name; a chapter that doesn't open with
      "Where you are now", doesn't close with "The answer", or whose answer lacks the bold
      line "What this unlocks next".
WARN: hedges; a bold opener under 4 words (often a slogan); a basic term (dashboard,
      database, script...) whose first use carries no plain meaning beside it.
It reads patterns, not meaning. The critic covers the rest (references/critic.md).
"""
import re
import sys

CUT = ["what you'll learn", "first principles", "mental models", "judge a build",
       "words you now own", "glossary", "key takeaways", "common mistakes", "practice",
       "check yourself", "the fix, part by part"]
GENERIC = ["how the people who build this think", "why someone had to invent the answer"]
HEDGES = re.compile(r"\b(probably|might|maybe|perhaps|likely|arguably|somewhat)\b", re.I)
# Basic terms Ash met unexplained in v2. The first use needs its plain meaning beside it.
BASIC = ["dashboard", "database", "language model", "script", "chunking", "API", "schema",
         "query", "agent", "server", "embeddings", "index", "rubric", "prompt", "token",
         "webhook", "information architecture", "design system", "component", "batch"]
EXPLAINED = re.compile(r"\(|\bcalled\b|\bmeans\b|\bis an?\b|\bwhich\b|, an? |: ", re.I)
MAX_SENT, MAX_WORDS, MAX_BULLET_SENT, MAX_BULLET_WORDS = 3, 60, 2, 40


def strip_tags(s):
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\s+", " ", s.replace("&nbsp;", " ").replace("&amp;", "&")).strip()


def sentences(text):
    text = re.sub(r"\b(e\.g|i\.e|etc|vs)\.", r"\1", text)
    return [s for s in re.split(r"(?<=[.!?])[\"'”’)\]]*\s+(?=[A-Z0-9\"“'(])", text) if s.strip()]


def clean(html):
    html = re.sub(r"<(script|style|svg|nav|footer)[^>]*>.*?</\1>", "", html, flags=re.S)
    return re.sub(r"<!--.*?-->", "", html, flags=re.S)


def blocks_from_html(html):
    """Yield (kind, inner_html) for every paragraph and list item."""
    for m in re.finditer(r"<p\b[^>]*>(.*?)</p>", html, re.S):
        yield "p", m.group(1)
    for m in re.finditer(r"<li\b[^>]*>(.*?)</li>", html, re.S):
        yield "li", re.sub(r"<(ul|ol)\b.*", "", m.group(1), flags=re.S)


def blocks_from_md(text):
    para = []
    bold = lambda s: re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    for line in text.splitlines() + [""]:
        s = line.strip()
        if re.match(r"^([-*]|\d+\.) ", s):
            yield "li", bold(re.sub(r"^([-*]|\d+\.) ", "", s))
            continue
        if not s or s.startswith(("#", ">", "|", "```")):
            if para:
                yield "p", bold(" ".join(para))
            para = []
            continue
        para.append(s)


def check_blocks(blocks, label, fails, warns):
    for kind, inner in blocks:
        text = strip_tags(inner)
        if not text:
            continue
        n, w = len(sentences(text)), len(text.split())
        short = text[:60] + ("..." if len(text) > 60 else "")
        if kind == "p":
            if n > MAX_SENT or w > MAX_WORDS:
                fails.append(f'{label}: paragraph of {n} sentences, {w} words (max {MAX_SENT}, {MAX_WORDS}); split it: "{short}"')
            if n >= 2 and not re.match(r"\s*(<em>[^<]*</em>\s*)?<(strong|b)\b", inner):
                fails.append(f'{label}: paragraph of {n} sentences with no bold lead-in: "{short}"')
        elif n > MAX_BULLET_SENT or w > MAX_BULLET_WORDS:
            fails.append(f'{label}: bullet of {n} sentences, {w} words (max {MAX_BULLET_SENT}, {MAX_BULLET_WORDS}): "{short}"')
        m = re.match(r"\s*<(strong|b)>([^<]+)</\1>", inner)
        # A short bold label ending in a colon ("Week 3:", "To keep it:") is a label, not a slogan.
        if m and kind == "li" and len(m.group(2).split()) < 4 and not m.group(2).strip().endswith(":"):
            warns.append(f"{label}: short bold opener '{m.group(2).strip()}'; a slogan?")


def chapter_text(html):
    """Headings to #, list items to -, quotes to >, everything else plain, one block per line."""
    html = re.sub(r"<h([1-6])[^>]*>", lambda m: "\n" + "#" * int(m.group(1)) + " ", html)
    html = re.sub(r"</h[1-6]>", "\n", html)
    html = re.sub(r"<li[^>]*>", "\n- ", html)
    html = re.sub(r"<blockquote[^>]*>", "\n> ", html)
    html = re.sub(r"</(p|div|ol|ul|table|tr)>", "\n", html)
    return re.sub(r"<[^>]+>", "", html).replace("&nbsp;", " ")


def check_chapter(name, text, fails, warns):
    lines = text.splitlines()
    heads = [l.strip("# ").strip() for l in lines if l.startswith("#")]
    if "—" in text:
        fails.append(f"{name}: em dash found; use a comma, a full stop or brackets")
    if re.search(r"\bnot (just|only)\b", text, re.I) or re.search(r"\bnot\s+\w+(\s+\w+){0,4},\s*but\b", text, re.I):
        fails.append(f'{name}: "not X, but Y" found; state the point positively')
    for i, l in enumerate(lines, 1):
        s = l.strip()
        if s.startswith(">"):
            fails.append(f"{name} line {i}: block quote; quotes stay in the research file")
        if re.search(r"\b(19|20)\d\d\b", s) and not s.startswith("#"):
            fails.append(f"{name} line {i}: a date; cut the history")
        if re.search(r"\[\d{1,2}:\d\d\]", s):
            fails.append(f"{name} line {i}: timestamp")
        m = re.search(r"\b[A-D][1-4]\b", s)
        if m:
            fails.append(f"{name} line {i}: map ID {m.group(0)}; use the problem's plain name")
        if HEDGES.search(s):
            warns.append(f"{name} line {i}: hedge word")
    for h in heads:
        if h.lower().rstrip("?") in CUT:
            fails.append(f'{name}: heading "{h}" is on the cut list')
        if h.lower().rstrip("?") in GENERIC:
            fails.append(f'{name}: heading "{h}" is the generic skeleton wording; make it about this problem')
    run = 0
    for i, l in enumerate(lines, 1):
        if re.match(r"^[-*] ", l):
            run += 1
            if run == 4:
                fails.append(f"{name} line {i}: flat list of 4+ items; group under bold labels")
        elif l.strip():
            run = 0
    if heads and "where you are now" not in " ".join(heads[:2]).lower():
        fails.append(f'{name}: the chapter must open with "Where you are now"')
    if heads and "the answer" not in heads[-1].lower():
        fails.append(f'{name}: the chapter must close with "The answer"')
    if "What this unlocks next" not in text.split("The answer")[-1]:
        fails.append(f'{name}: the answer must end with the bold line "What this unlocks next"')
    plain = re.sub(r"\s+", " ", text)
    for term in BASIC:
        m = re.search(r"\b" + re.escape(term) + r"s?\b", plain, re.I)
        if not m:
            continue
        start = max(plain.rfind(". ", 0, m.start()), plain.rfind("# ", 0, m.start())) + 1
        end = plain.find(". ", m.end())
        sent = plain[start:end if end > 0 else None]
        if not EXPLAINED.search(sent):
            warns.append(f'{name}: "{term}" first used without its plain meaning: "{sent.strip()[:80]}"')


def main(path):
    raw = open(path, encoding="utf-8").read()
    fails, warns = [], []
    if path.lower().endswith((".html", ".htm")):
        body = clean(raw)
        check_blocks(blocks_from_html(body), "book", fails, warns)
        chapters = re.findall(r'<section[^>]*id="(ch\d+)"[^>]*>(.*?)</section>', body, re.S)
        for name, html in chapters:
            check_chapter(name, chapter_text(html), fails, warns)
        print(f"checked {len(chapters)} chapter(s) and every paragraph in the book")
    else:
        check_blocks(blocks_from_md(raw), "chapter", fails, warns)
        check_chapter("chapter", raw, fails, warns)
    for w in warns:
        print("warn ", w)
    for f in fails:
        print("FAIL ", f)
    if not fails:
        print("PASS: no mechanical breaks")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
