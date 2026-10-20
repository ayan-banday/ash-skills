#!/usr/bin/env python3
"""Wrap every heading with the block that follows it, so print engines cannot strand it.

Chrome's print engine ignores break-after: avoid on headings, so a heading can end a page
with its content on the next. This script wraps, at the top level of each <section>:
  - a part head: eyebrow + h2 + up to two lede paragraphs; with no lede, the first block
    after the h2 (unless it is a table or very long)
  - a .grp group header + the next element
  - an h2 or h3 + the next element
A heading right before a table becomes the table caption instead, so long tables still split by row.
Tables of 8 rows or fewer never split, so no single row is orphaned.
inside <div class="keep"> (which has break-inside: avoid).

Usage: python keepnext.py in.html out.html
"""
import re
import sys

OPEN = re.compile(r"<(div|figure|table|ul|ol|p|h2|h3|section)\b")


def block_end(s, i):
    """Index just past the element that starts at s[i]."""
    m = OPEN.match(s, i)
    if not m:
        raise ValueError("no element at %d: %r" % (i, s[i:i + 40]))
    tag = m.group(1)
    pat = re.compile(r"<(/?)%s\b[^>]*>" % tag)
    depth = 0
    for t in pat.finditer(s, i):
        depth += -1 if t.group(1) else 1
        if depth == 0:
            return t.end()
    raise ValueError("unclosed <%s> at %d" % (tag, i))


def next_start(s, i):
    m = re.compile(r"\s*").match(s, i)
    return m.end()


def wrap_groups(s, starts_pattern, parts_after):
    """Wrap each match of starts_pattern plus `parts_after` following elements."""
    out, pos = [], 0
    for m in re.finditer(starts_pattern, s):
        i = next_start(s, m.start())
        if i < pos:
            continue
        j = block_end(s, i)
        for _ in range(parts_after):
            k = next_start(s, j)
            if not OPEN.match(s, k):
                break
            j = block_end(s, k)
        out.append(s[pos:i])
        out.append('<div class="keep">' + s[i:j] + "</div>")
        pos = j
    out.append(s[pos:])
    return "".join(out)


def small_tables_keep(s, max_rows=8):
    """Tables with few rows stay whole, so no single row is orphaned on the next page."""
    out, pos = [], 0
    for m in re.finditer(r"<table\b[^>]*>", s):
        if m.start() < pos:
            continue
        end = block_end(s, m.start())
        body = s[m.start():end]
        if body.count("<tr") <= max_rows + 1 and "break-inside" not in m.group(0):
            out.append(s[pos:m.start()])
            out.append(m.group(0)[:-1] + ' style="break-inside:avoid">' + body[len(m.group(0)):])
            pos = end
    out.append(s[pos:])
    return "".join(out)


def part_heads(s):
    """Eyebrow + h2 + up to two lede paragraphs. With no lede, the first block after the h2
    instead (unless it is a table or very long), so the heading is never alone."""
    out, pos = [], 0
    for m in re.finditer(r'(?m)^  <div class="eyebrow">', s):
        i = next_start(s, m.start())
        if i < pos:
            continue
        j = block_end(s, i)
        k = next_start(s, j)
        if s.startswith("<h2", k):
            j = block_end(s, k)
        paras = 0
        while paras < 2:
            k = next_start(s, j)
            if not s.startswith("<p", k):
                break
            j = block_end(s, k)
            paras += 1
        k = next_start(s, j)
        # with a lede, heading + lede is enough; pulling a big block too leaves half-empty pages
        if paras == 0 and OPEN.match(s, k) and not s.startswith("<table", k) and not s.startswith("<h3", k):
            e = block_end(s, k)
            if e - k < 6000:
                j = e
        out.append(s[pos:i])
        out.append('<div class="keep">' + s[i:j] + "</div>")
        pos = j
    out.append(s[pos:])
    return "".join(out)


def caption_tables(s):
    """A heading right before a table moves inside it as <caption>, so the table can still split by row."""
    pat = re.compile(r'(?m)^  <h3([^>]*)>(.*?)</h3>\s*<table>')
    return pat.sub(lambda m: '  <table><caption class="tcap"%s>%s</caption>' % (m.group(1), m.group(2)), s)


def main(src, dst):
    s = open(src, encoding="utf8").read()
    if 'data-keepnext="1"' in s:
        sys.exit("already processed")
    s = caption_tables(s)
    s = small_tables_keep(s)
    # part heads: eyebrow, h2, lede paragraphs, and the first block after them
    s = part_heads(s)
    # group headers plus the first item of the group
    s = wrap_groups(s, r'(?m)^  <div class="grp[" ]', 1)
    # top-level h3 headings plus the next element
    s = wrap_groups(s, r'(?m)^  <h3\b', 1)
    s = s.replace("<body>", '<body data-keepnext="1">', 1)
    open(dst, "w", encoding="utf8").write(s)
    print("wrapped headings in", dst)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
