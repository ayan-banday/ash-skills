#!/usr/bin/env python3
"""Check a BBA unit book's shape against Ash's Nov 4 2026 decisions (Fuji ticket 14).

    python scripts/check_book.py <book.html> [--names Asha,Rao]

--names: the teachers named in the source material (step 1 writes them down); any of them anywhere fails.

FAIL lines must be fixed; WARN lines are worth a look. It reads patterns, not meaning: the critic and
references/page-shape.md cover the rest. It checks:
- one book: a cover with concept tags and no summary line, 1+ chapters as tabs (<section data-tab data-chapter>),
  "Questions a founder might still have" last, and the tabs and tutor code pasted;
- no separate class-questions or "beyond class" part, and no sentence about where the material came from;
- never a teacher's name: "Prof. X", "X's class", "X's notes" and the like, in the text or the tutor config;
- each chapter: a founder problem as its h2 (a question), concept tags under it, and big-section headings
  that are problems about the company (a question, no "you", "your", "I", "we");
- the tutor config: NOTES false, GAPS true, SCOPE "chapter", and every chapter's palette block.
"""
import json
import re
import sys

STORY = {"where you are now", "after this chapter, you can", "what this looks like for you", "what usually happens",
         "where the problem lies", "the idea that fixes it", "the answer"}
OPTIONAL = ("how it works", "how you'd build it", "how you'd use it", "how you'd run it", "where else it applies", "when to skip it")
TEACHER = re.compile(r"\b(?:Prof(?:essor)?\.?|Dr\.|Sir|Ma'am|Madam)\s+[A-Z][a-z]+|\b[A-Z][a-z]+'s\s+(?:class|classes|notes|board|questions|course|test|key|lecture|slides|workflow|rule|formula|example|examples|assignment|problem)\b")
NOT_TEACHERS = {"Sensa", "Ash", "Company", "Founder", "Today", "Month", "January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December", "India", "Bengaluru"}
SOURCE_TALK = re.compile(r"beyond class|past what [A-Za-z]+ taught|goes past|from (?:his|her|the) shared notes|in class,? (?:he|she) |"
                         r"class questions|from your notes|your notes (?:give|list|draw|tick|don't)|earlier version of this page", re.I)
PERSON = re.compile(r"\b(you|your|yours|i|me|my|we|our|us)\b", re.I)


def text(s):
    s = re.sub(r"<(script|style|svg)[^>]*>.*?</\1>", "", s, flags=re.S)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s)).replace("&amp;", "&").strip()


def main(path, names=()):
    html = open(path, encoding="utf-8").read()
    fails, warns = [], []
    main_html = (re.search(r"<main>(.*)</main>", html, re.S) or [None, ""])[1]
    if not main_html:
        print("FAIL no <main> holding the book")
        return 1

    # The cover: concept tags linking to chapters, no summary line
    cover = re.search(r'<header class="cover[^"]*"[^>]*>(.*?)</header>', main_html, re.S)
    if not cover:
        fails.append('no cover (<header class="cover part">)')
    else:
        if 'class="lede"' in cover.group(1):
            fails.append("the cover has a summary line (.lede): show only the concept tags")
        if not re.search(r'class="ctags"[^>]*>.*?<a [^>]*href="#ch\d', cover.group(1), re.S):
            fails.append('the cover has no concept tags linking to chapters (<ul class="ctags"> of <a href="#chN">)')

    secs = re.findall(r'<section ([^>]*)>(.*?)</section>', main_html, re.S)
    chapters = [(a, b) for a, b in secs if re.search(r'\bid="ch\d+"', a)]
    if not chapters:
        fails.append('no chapters: each is <section class="part chapter" id="chN" data-chapter="chN" data-tab="...">')
    for a, _ in secs:
        if re.search(r'id="(exam|beyond)"', a) or "beyond" in a:
            fails.append(f"a separate class-questions or beyond-class part ({a.strip()[:60]}): fold strong questions into their sections")
    last = secs[-1][0] if secs else ""
    if not secs or 'id="fq"' not in last:
        fails.append('"Questions a founder might still have" must be the last part (<section class="part endpart" id="fq" ...>)')
    for a, body in secs:
        if 'data-tab="' not in a:
            fails.append(f"a part without a tab name (data-tab): {a.strip()[:60]}")
        if 'data-chapter="' not in a:
            fails.append(f"a part without its palette (data-chapter): {a.strip()[:60]}")

    for a, body in chapters:
        cid = re.search(r'id="(ch\d+)"', a).group(1)
        h2 = re.search(r"<h2[^>]*>(.*?)</h2>", body, re.S)
        if not h2 or not text(h2.group(1)).endswith("?"):
            fails.append(f"{cid}: the chapter heading (h2) is not a founder problem asked as a question")
        elif PERSON.search(text(h2.group(1))):
            fails.append(f"{cid}: the chapter heading talks to the reader; write it about the company: {text(h2.group(1))}")
        if 'class="ctags"' not in body[:3000]:
            fails.append(f"{cid}: no concept tags (<ul class=\"ctags\">) under the heading")
        for h in re.findall(r"<h3[^>]*>(.*?)</h3>", body, re.S):
            t = text(h)
            low = t.lower()
            if low in STORY or low.startswith(OPTIONAL) or low.startswith("why "):
                continue
            if not t.endswith("?"):
                warns.append(f"{cid}: a big-section heading that isn't a problem: {t}")
            elif PERSON.search(t):
                fails.append(f"{cid}: a section heading talks to the reader or the writer; write it about the company: {t}")

    plain = text(main_html)
    cfg_txt = ""
    m = re.search(r"window\.TUTOR\s*=\s*", html)
    if m:
        try:
            cfg, _ = json.JSONDecoder().raw_decode(html[m.end():])
            cfg_txt = json.dumps(cfg, ensure_ascii=False)
            if cfg.get("NOTES") is not False:
                fails.append('the tutor config needs "NOTES": false (BBA books have no notes)')
            if cfg.get("GAPS") is not True:
                fails.append('the tutor config needs "GAPS": true')
            if cfg.get("SCOPE") != "chapter":
                fails.append('the tutor config needs "SCOPE": "chapter" (each ring reads its own chapter)')
        except json.JSONDecodeError as e:
            fails.append(f"window.TUTOR is not valid JSON: {e}")
    else:
        fails.append("no window.TUTOR config")
    for where, t in (("the page", plain), ("the tutor config", cfg_txt), ("the title", text((re.search(r"<title>(.*?)</title>", html) or [None, ""])[1]))):
        for hit in TEACHER.finditer(t):
            name = re.findall(r"[A-Z][a-z]+", hit.group(0))
            if hit.group(0).split()[0].rstrip(".") in ("Prof", "Professor", "Dr", "Sir", "Ma'am", "Madam") or (name and name[0] not in NOT_TEACHERS):
                fails.append(f"a teacher's name in {where}: \"{hit.group(0)}\" (say \"the professor\", or nothing)")
    for n in names:
        for where, t in (("the page", plain), ("the tutor config", cfg_txt)):
            if re.search(rf"\b{re.escape(n)}\b", t):
                fails.append(f'the teacher\'s name "{n}" appears in {where} (say "the professor", or nothing)')
    for hit in sorted(set(h.group(0) for h in SOURCE_TALK.finditer(plain))):
        fails.append(f'the page talks about where its material came from: "{hit}"')

    for needle, what in (('id="tabs"', "the tabs (assets/tabs.html)"), (".tabs{", "the tabs CSS (assets/tabs.css)"),
                         ('id="gapsbtn"', 'the "Gaps" button in the top bar'), ('id="gapdot"', "the current tutor (break-into-field assets/tutor.html)")):
        if needle not in html:
            fails.append(f"missing {what}")
    if 'id="notesbtn"' in html:
        fails.append('a "My notes" button: BBA books have the "Gaps" button only')
    for k in range(1, len(secs) + 1):
        if f'[data-chapter="ch{k}"]' not in html:
            fails.append(f'no palette block for data-chapter="ch{k}" (palette.py --format study --chapters {len(secs)})')
    if html.find('id="tabs"') > html.find("function countIdeas") > -1:
        fails.append("paste assets/tabs.html before the tutor script")

    for f in fails:
        print("FAIL", f)
    for w in warns:
        print("WARN", w)
    print(f"{len(chapters)} chapters, {len(secs)} tabs after the cover")
    print("PASS" if not fails else f"FAIL ({len(fails)})")
    return 1 if fails else 0


if __name__ == "__main__":
    args = sys.argv[1:]
    names = []
    if "--names" in args:
        i = args.index("--names")
        names = [n.strip() for n in args[i + 1].split(",") if n.strip()] if i + 1 < len(args) else []
        args = args[:i] + args[i + 2:]
    if len(args) != 1:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(args[0], names))
