#!/usr/bin/env python3
"""Check a book's tutor: stations, config and pasted code (references/tutor.md).

    python scripts/check_tutor.py "<book.html>"

FAIL lines must be fixed; WARN lines are worth a look. The config must be JSON:
window.TUTOR = { ... };  (no comments, double quotes).
"""
import json
import re
import sys


def main(path):
    html = open(path, encoding="utf-8").read()
    fails, warns = [], []
    m = re.search(r"window\.TUTOR\s*=\s*", html)
    if not m:
        print("FAIL no window.TUTOR config found")
        return 1
    try:
        cfg, _ = json.JSONDecoder().raw_decode(html[m.end():])
    except json.JSONDecodeError as e:
        print(f"FAIL window.TUTOR is not valid JSON: {e}")
        return 1
    book, st, ideas = cfg.get("BOOK", {}), cfg.get("STATIONS", {}), cfg.get("IDEAS", {})
    for k in ("id", "title", "field", "outcome", "work", "short"):
        if not book.get(k):
            fails.append(f"BOOK.{k} is missing")
    if not cfg.get("ASH"):
        fails.append("ASH is missing")
    on_page = re.findall(r'<button class="stn[^"]*"[^>]*data-s="([^"]+)"', html)
    if len(on_page) != len(set(on_page)):
        fails.append("a station id appears twice on the page")
    for s in on_page:
        if s not in st:
            fails.append(f"station {s} is on the page but not in STATIONS")
    for s in st:
        if s not in on_page:
            fails.append(f"station {s} is in STATIONS but not on the page")
    if list(st) != [s for s in on_page if s in st]:
        warns.append("STATIONS are not in reading order")
    by_ch = {}
    for s, v in st.items():
        by_ch.setdefault(v.get("chapter", "?"), []).append(s)
        for k in ("chapter", "name", "q"):
            if not v.get(k):
                fails.append(f"station {s} has no {k}")
        sug = v.get("sug") or []
        if not 2 <= len(sug) <= 3:
            fails.append(f"station {s} has {len(sug)} suggested questions (needs 2 or 3)")
        if len(v.get("q", "").split()) > 16:
            warns.append(f"station {s}: the question is long ({len(v['q'].split())} words)")
    for ch, ids in by_ch.items():
        if ch.lower().startswith("chapter"):
            if not 3 <= len(ids) <= 6:
                fails.append(f"{ch} has {len(ids)} stations (needs 3 to 6)")
        elif len(ids) > 1:
            warns.append(f"{ch} has {len(ids)} stations (parts take one at most)")
        if ch not in ideas:
            fails.append(f"IDEAS has no entry for {ch}")
        elif ch.lower().startswith("chapter") and not 6 <= len(ideas[ch]) <= 12:
            warns.append(f"IDEAS for {ch} has {len(ideas[ch])} ideas (aim for 6 to 12)")
    for ch, m_ in ideas.items():
        for name, words in m_.items():
            short = [w for w in words if len(w.strip()) <= 4 and not w.startswith(" ")]
            if short:
                warns.append(f"IDEAS {ch} / {name}: short words {short} match inside other words; start them with a space")
    ex = cfg.get("EXAMPLE")
    if ex and ex.get("station") not in st:
        fails.append("EXAMPLE.station is not a station")
    notes_on, gaps_on = cfg.get("NOTES", True) is not False, bool(cfg.get("GAPS"))
    need = [('id="desk"', "the desk (assets/tutor.html)"), ('id="trail"', "the rail (assets/tutor.html)"),
            ('id="aidot"', "the selection dot (assets/tutor.html)"), ("function countIdeas", "the tutor script (assets/tutor.html)"),
            ('id="dpick"', "the model and thinking dots (an old assets/tutor.html with dropdowns? paste the current one)"),
            (".rail{", "the tutor CSS (assets/tutor.css)"), (".drow{", "the dots' CSS (paste the current assets/tutor.css)")]
    if notes_on:
        need.append(('id="notesbtn"', 'the "My notes" button in the top bar'))
    if gaps_on:
        need.append(('id="gapdot"', "the gap symbol (paste the current assets/tutor.html)"))
        if not notes_on:
            need.append(('id="gapsbtn"', 'the "Gaps" button in the top bar'))
    for needle, what in need:
        if needle not in html:
            fails.append(f"missing {what}")
    if not notes_on and 'id="notesbtn"' in html:
        fails.append('NOTES is false but the top bar still has the "My notes" button: use the "Gaps" button')
    if 'id="dmodel"' in html or 'id="dgap"' in html:
        fails.append("old tutor code (Model dropdowns or the Mark as a gap button): paste the current assets/tutor.html and tutor.css")
    if cfg.get("SCOPE") not in (None, "book", "chapter"):
        fails.append('SCOPE is "chapter" or left out')
    if html.find("window.TUTOR") > html.find("function countIdeas") > -1:
        fails.append("window.TUTOR must come before the tutor script")
    for f in fails:
        print("FAIL", f)
    for w in warns:
        print("WARN", w)
    print(f"{len(st)} stations in {len(by_ch)} parts and chapters: " + ", ".join(f"{c} {len(i)}" for c, i in by_ch.items()))
    print("PASS" if not fails else f"FAIL ({len(fails)})")
    return 1 if fails else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
