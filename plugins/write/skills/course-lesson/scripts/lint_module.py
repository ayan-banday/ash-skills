#!/usr/bin/env python3
"""Lint a course page or module draft against the course-lesson rules.

Usage: python lint_module.py draft.md [--type page]

Default checks a daily module (Do, week map, tomorrow, fresh examples).
Use --type page for a welcome page or other student-facing page: the module
structure checks are skipped and one bracketed quiet offer is allowed.
Exit code 0 means no findings. Exit code 1 means fix the findings and run again.

The checks are mechanical on purpose. They catch the patterns Ash has flagged
repeatedly, so the writer can spend judgment on clarity instead of hunting for
em dashes. Findings marked REVIEW need a human-style look; the rest are fixes.
"""
import re
import sys
from pathlib import Path

BANNED_HEADINGS = {
    "why start here", "mistakes to avoid", "common mistakes", "key takeaways",
    "overview", "introduction", "summary", "conclusion", "why this matters",
    "what you'll learn", "the problem", "the solution", "faq",
}

LEAD_INS = [
    r"\bhere['’]s\b", r"\bhere (is|are) (what|how|the)\b", r"\blet['’]s dive\b",
    r"\bit['’]s worth noting\b", r"\bnow you try\b", r"\bin this (lesson|module)\b",
    r"\bthe critical mindset shift\b",
]

COUNT_SETUPS = [
    r"\bone of (two|three) things\b", r"\btwo things (can|will|have|happen)",
    r"\bthree things (can|will|have|happen)",
]

FREQ_CLAIMS = [
    r"\balmost (every|all)\b", r"\bnearly (every|all)\b",
    r"\b(most|many|every) (first-time )?(founders|students|beginners|farmers|people|builders|entrepreneurs)\b(?! believe)",
    r"\byou['’]ll probably\b", r"\bevery smart\b",
    r"\b\d+\s?%", r"\bstudies show\b", r"\bresearch shows\b",
]

REUSED_EXAMPLE_WORDS = [
    "vending machine", "banana", "home baker", "fruit pulp", "canteen queue",
    "canteen snack", "pre-order app", "pre-order", "senior sells",
]


def strip_inline(text: str) -> str:
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)  # markdown links
    return text.replace("**", "").replace("`", "")


def sentences(par: str):
    par = re.sub(r"\s+", " ", par.strip())
    return [s for s in re.split(r"(?<=[.!?])\s+", par) if s]


def main(path: str, page: bool = False) -> int:
    raw = Path(path).read_text(encoding="utf-8")
    # Lint the module only. Notes after a "Judgment calls" heading are not page text.
    cut = re.search(r"^#+\s*judgment calls", raw, flags=re.I | re.M)
    if cut:
        raw = raw[:cut.start()]
    lines = raw.splitlines()
    findings = []

    def add(kind, msg, line_no=None, snippet=""):
        loc = f"line {line_no}" if line_no else "draft"
        snip = f' -> "{snippet.strip()[:90]}"' if snippet else ""
        findings.append(f"[{kind}] {loc}: {msg}{snip}")

    # Preamble: draft must start with the title or a heading.
    first = next((l for l in lines if l.strip() and l.strip() != "---"), "")
    if not first.lstrip().startswith("#"):
        add("FIX", "draft starts with chatter instead of the title", None, first)

    in_quote_block = False
    para_buf, para_start = [], 0

    def flush(end_line):
        nonlocal para_buf, para_start
        if not para_buf:
            return
        text = strip_inline(" ".join(para_buf))
        sents = sentences(text)
        limit = 4 if page else 3
        if len(sents) > limit and not text.lstrip().startswith(("-", ">", "|", "1.")):
            add("FIX", f"paragraph has {len(sents)} sentences (max {limit})", para_start, text)
        for s in sents:
            words = re.findall(r"[A-Za-z0-9'’]+", s)
            if len(words) == 1 and s[-1] in ".!?":
                add("FIX", "one-word sentence", para_start, s)
            if len(words) > 32:
                add("REVIEW", f"long sentence ({len(words)} words)", para_start, s)
            if re.match(r"^Not\b", s):
                add("FIX", "sentence starts with 'Not' (fragment or negative parallelism)", para_start, s)
        para_buf = []

    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        plain = strip_inline(stripped)
        low = plain.lower()

        if not stripped:
            flush(i)
            continue

        # Dashes
        if "—" in line or "–" in line:
            add("FIX", "em or en dash", i, line)

        # Headings
        if stripped.startswith("#"):
            flush(i)
            head = re.sub(r"^#+\s*", "", plain).lower()
            head = re.sub(r"\s*\(.*\)\s*$", "", head).strip(" :?")
            if head in BANNED_HEADINGS:
                add("FIX", "heading names a slot instead of the content", i, line)
            for pat in FREQ_CLAIMS:
                if re.search(pat, head):
                    add("FIX", "heading claims how many people do something", i, line)
                    break
            if len(head.split()) < 3 and not head.startswith("day ") and head != "tomorrow":
                add("REVIEW", "very short heading; does it hold the answer?", i, line)
            continue

        # Lead-ins and setups
        for pat in LEAD_INS:
            if re.search(pat, low):
                add("FIX", "lead-in or filler phrase", i, line)
                break
        for pat in COUNT_SETUPS:
            if re.search(pat, low):
                add("FIX", "announces a count instead of saying the thing", i, line)
                break

        # Negative parallelism
        if re.search(r"\bnot\b[^.!?\n]{1,60}[,;:]\s*(but|it['’]s|it is|rather|instead)\b", low) \
           or re.search(r"\b(isn['’]t|aren['’]t|is not|are not|wasn['’]t)\b[^.!?\n]{1,60}[.!]\s*(it['’]s|it is|they['’]re|they are)\b", low) \
           or re.search(r"\bnot (just|only|about)\b[^.!?\n]{1,60}\b(but|it['’]s)\b", low):
            add("FIX", "negative parallelism (not X, but Y)", i, line)
        if re.search(r"\b(are|is|were|was) (patterns|signs?|about|a matter)\b[^.!?\n]{0,50},\s*not\b", low) \
           or re.search(r"\bnot (a|an|the|your|proof|signs?)\b[^.!?\n]{1,40}\bbut\b", low) \
           or re.search(r",\s*not (a|an|the|signs?|proof|because|just|only)\b", low):
            add("FIX", "negative parallelism (', not X' or 'not X but Y')", i, line)
        for idiom in ("move the dial", "game changer", "at the end of the day", "the bottom line",
                      "when it comes to", "in today's", "unlock", "dive in", "journey",
                      "demystify", "leverage", "empower", "crucial", "optimize", "delve", "embark"):
            if idiom in low:
                add("FIX", f"filler idiom '{idiom}'", i, line)
        for jargon in ("red-team", "red team", "stress test", "stress-test", "audit your", "identify", "unit economics"):
            if jargon in low:
                add("REVIEW", f"jargon '{jargon}'; use plain words unless the course already taught it", i, line)
        if re.match(r"^(not|no) [a-z ]{1,30}\.\s*(not|no) ", low):
            add("FIX", "fragment run ('Not X. Not Y.')", i, line)

        # Parenthetical asides (links and short labels are fine)
        for m in re.finditer(r"\(([^()]{20,})\)", plain):
            inner = m.group(1)
            quiet_offer = page and plain.startswith("(") and plain.endswith(")")
            if not inner.lower().startswith(("today", "minutes")) and not re.match(r"^\d", inner) and not quiet_offer:
                add("FIX", "parenthetical aside; make it a sentence or cut it", i, m.group(0))
        if re.search(r"\(made up|\(we['’]ll swap|made-up company", low):
            add("FIX", "'made up' label", i, line)

        # Frequency claims about people
        for pat in FREQ_CLAIMS:
            if re.search(pat, low):
                add("REVIEW", "frequency or statistic claim; only keep if Ash supplied it", i, line)
                break

        # Reused examples
        for w in ([] if page else REUSED_EXAMPLE_WORDS):
            if w in low:
                add("REVIEW", f"example word '{w}' appears in the reference modules; use a fresh example unless this is a one-line callback", i, line)
                break

        # Paragraph accumulation (skip lists, quotes, tables)
        if stripped.startswith(("- ", "* ", ">", "|")) or re.match(r"^\d+\.\s", stripped):
            flush(i)
            continue
        if not para_buf:
            para_start = i
        para_buf.append(stripped)
    flush(len(lines))

    # Opener overuse
    count_believe = len(re.findall(r"most people believe", raw.lower()))
    if count_believe > 1:
        add("FIX", f"'Most people believe' appears {count_believe} times in one module")

    # Structure checks
    needed = {
        "week map": r"your week, day by day",
        "tomorrow": r"^#+\s*tomorrow",
        "a Do section": r"^#+.*\((\d+(\s*to\s*\d+)?) minutes\)",
        "a Short on time line": r"short on time\?",
    }
    for name, pat in ({} if page else needed).items():
        if not re.search(pat, raw, flags=re.I | re.M):
            add("FIX", f"missing {name}")

    # Section order: the Do comes before the week map, and the week map before Tomorrow.
    do_m = re.search(r"^#+.*\((\d+(\s*to\s*\d+)?) minutes\)", raw, flags=re.I | re.M)
    wk_m = re.search(r"^#+\s*your week, day by day", raw, flags=re.I | re.M)
    tm_m = re.search(r"^#+\s*tomorrow", raw, flags=re.I | re.M)
    if do_m and wk_m and do_m.start() > wk_m.start():
        add("FIX", "section order: the Do must come before 'Your week, day by day'")
    if wk_m and tm_m and wk_m.start() > tm_m.start():
        add("FIX", "section order: 'Your week, day by day' must come before 'Tomorrow'")
    if not page and raw.count("(today)") != 1:
        add("FIX", "mark exactly one day '(today)' in the week map")

    # A section that only asks a question and stops
    secs = re.split(r"^#+\s", raw, flags=re.M)
    for sec in secs[1:]:
        title, _, body = sec.partition("\n")
        body = body.strip()
        if body and len(body.split()) < 25 and body.endswith("?"):
            add("REVIEW", "section is only a question with no answer; fold it into the next section", None, title)

    # Bold density
    for i, line in enumerate(lines, 1):
        if line.strip().startswith(("-", "*", ">", "#", "|")):
            continue
        bolds = re.findall(r"\*\*[^*]+\*\*", line)
        if len(bolds) > 3:
            add("REVIEW", f"{len(bolds)} bold phrases in one paragraph (aim for 1-2)", i, line)
        for b in bolds:
            if len(b.split()) > 14:
                add("FIX", "whole sentence is bold; bold the key phrase only", i, b)

    if not findings:
        print("PASS: no findings")
        return 0
    fixes = [f for f in findings if f.startswith("[FIX]")]
    print("\n".join(findings))
    print(f"\n{len(fixes)} to fix, {len(findings) - len(fixes)} to review")
    return 1 if fixes else 0


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    page_mode = "--type" in sys.argv and "page" in sys.argv
    if len(args) < 1 or (page_mode and "page" in args and len(args) < 2):
        print(__doc__)
        sys.exit(2)
    path_arg = next(a for a in args if a != "page")
    sys.exit(main(path_arg, page_mode))
