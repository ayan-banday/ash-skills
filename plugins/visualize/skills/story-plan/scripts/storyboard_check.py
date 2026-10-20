#!/usr/bin/env python3
"""Check storyboard tables against the rules in references/storyboard.md ("What the checker enforces").

Usage: python storyboard_check.py FILE [FILE...]
Finds every markdown table whose header is: # | Beat | Shot | Bright | Moves | Words | Tension | Plant or payoff
(names matched case-insensitively; tables inside code fences are ignored). Each table is checked on its own and
labelled by the nearest heading above it. One line per problem, prefixed with the row number. Always prints the
tension curve (one line per row), then PASS or FAIL (n problems). Exit 0 only if every table passes, else 1.
"""
import argparse, re, sys

COLUMNS = ['#', 'beat', 'shot', 'bright', 'moves', 'words', 'tension', 'plant or payoff']
BEATS = ['character', 'want', 'obstacle', 'action', 'outcome', 'reaction']
SHOTS = ['extreme wide', 'wide', 'medium', 'close-up', 'extreme close-up']  # widest to tightest
MAX_WORDS = 20
MIN_ROWS, MAX_ROWS = 3, 12


def split_row(line):
    line = line.strip()
    if line.startswith('|'): line = line[1:]
    if line.endswith('|'): line = line[:-1]
    return [c.strip() for c in line.split('|')]


def is_separator(line):
    cells = split_row(line)
    return bool(cells) and all(re.fullmatch(r':?-{1,}:?', c) for c in cells if c) and any(cells)


def find_tables(text):
    """Return a list of (heading, rows) where rows is a list of dicts keyed by column name."""
    lines = text.splitlines()
    tables, heading, in_fence, i = [], '(no heading)', False, 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if s.startswith('```') or s.startswith('~~~'):
            in_fence = not in_fence
        elif not in_fence:
            m = re.match(r'#{1,6}\s+(.*)', s)
            if m:
                heading = m.group(1).strip()
            elif s.startswith('|') and i + 1 < len(lines) and is_separator(lines[i + 1]):
                head = [c.lower().strip() for c in split_row(s)]
                if all(c in head for c in COLUMNS):
                    idx = {c: head.index(c) for c in COLUMNS}
                    rows, j = [], i + 2
                    while j < len(lines) and lines[j].strip().startswith('|'):
                        cells = split_row(lines[j])
                        rows.append({c: (cells[k].strip() if k < len(cells) else '') for c, k in idx.items()})
                        j += 1
                    tables.append((heading, rows))
                    i = j
                    continue
        i += 1
    return tables


def count_words(cell):
    cell = cell.strip()
    if cell.lower() == 'none':
        return 0
    return len(re.sub(r'["“”]', '', cell).split())


def check_table(rows):
    """Return (problems, curve_lines). Each problem is a string already prefixed."""
    probs = []
    n = len(rows)

    def bad(r, msg):
        probs.append((r, f'row {r}: {msg}'))

    shots, tens, beats_seen = [], [], set()
    plants, payoffs = [], []  # (row, key)
    for k, row in enumerate(rows):
        r = k + 1
        # words
        w = count_words(row['words'])
        if w > MAX_WORDS:
            bad(r, f'Words has {w} words (max {MAX_WORDS})')
        # bright, moves
        bright, moves = row['bright'], row['moves']
        if not bright:
            bad(r, 'Bright is empty')
        if not moves:
            bad(r, 'Moves is empty')
        elif moves.lower() != 'nothing':
            low = ' ' + moves.lower() + ' '
            if ' and ' in low or ' + ' in low or ';' in low:
                bad(r, f'Moves describes more than one thing: "{moves}"')
        # beat
        row_beats = [b.strip().lower() for b in row['beat'].split(',') if b.strip()]
        if not row_beats:
            bad(r, 'Beat is empty')
        for b in row_beats:
            if b in BEATS:
                beats_seen.add(b)
            else:
                bad(r, f'unknown beat "{b}"')
        if 'reaction' not in row_beats and bright:
            lowb = ' ' + bright.lower() + ' '
            if ' and ' in lowb or '+' in bright or ',' in bright:
                bad(r, f'Bright lights more than one thing in a row that is not a reaction: "{bright}"')
        # shot
        sh = row['shot'].strip().lower()
        if sh in SHOTS:
            shots.append(SHOTS.index(sh))
        else:
            shots.append(None)
            bad(r, f'unknown shot "{row["shot"]}"')
        # tension
        t = row['tension'].strip()
        if re.fullmatch(r'[1-5]', t):
            tens.append(int(t))
        else:
            tens.append(None)
            bad(r, f'tension must be an integer 1-5, got "{t}"')
        # plant / payoff
        cell = row['plant or payoff'].strip()
        if cell:
            for item in [x.strip() for x in cell.split(',') if x.strip()]:
                m = re.fullmatch(r'(plant|payoff)\s*:\s*(\S+(?:\s+\S+)*)', item, re.I)
                if not m:
                    bad(r, f'cannot read plant or payoff item "{item}"')
                elif m.group(1).lower() == 'plant':
                    plants.append((r, m.group(2).lower()))
                else:
                    payoffs.append((r, m.group(2).lower()))

    # row count
    if n < MIN_ROWS or n > MAX_ROWS:
        probs.append((0, f'table: {n} rows (need {MIN_ROWS} to {MAX_ROWS})'))
    # shots
    if n:
        if shots[0] is not None and shots[0] > 1:
            bad(1, f'first shot is "{rows[0]["shot"]}", must be wide or extreme wide')
        if shots[-1] != shots[0] and shots[-1] is not None and shots[0] is not None:
            bad(n, f'last shot "{rows[-1]["shot"]}" differs from first shot "{rows[0]["shot"]}"')
        if not any(s is not None and s >= 3 for s in shots):
            probs.append((0, 'table: no row is close-up or tighter (the story never goes in)'))
    # tension shape
    for k in range(n - 2):
        run = tens[k:k + 3]
        if None not in run and run[0] == run[1] == run[2]:
            bad(k + 1, f'rows {k + 1} to {k + 3} share tension {run[0]} (flat run)')
    valid = [t for t in tens if t is not None]
    if valid:
        top = max(valid)
        first = tens.index(top)
        if first < n / 3:
            bad(first + 1, f'peak tension {top} comes too early (index {first} of {n}; must be in the last two thirds)')
        if tens[-1] is not None and tens[-1] >= top:
            bad(n, f'last tension {tens[-1]} is not below the peak {top}')
    # beats
    for b in BEATS:
        if b not in beats_seen:
            probs.append((0, f'table: beat "{b}" is missing from the whole board'))
    # plants and payoffs
    for r, key in plants:
        if not any(pr > r and pk == key for pr, pk in payoffs):
            bad(r, f'plant "{key}" has no payoff in a later row')
    for r, key in payoffs:
        if not any(pr <= r and pk == key for pr, pk in plants):
            bad(r, f'payoff "{key}" has no plant in an earlier or the same row')

    probs.sort(key=lambda p: p[0])
    curve = []
    for k, row in enumerate(rows):
        t = tens[k] or 0
        curve.append(f"{k + 1:2d} | {'#' * t:<5}  {row['shot']:<17} {row['bright'][:40]}")
    return [p[1] for p in probs], curve


def main():
    ap = argparse.ArgumentParser(description='Check storyboard tables against the storyboard rules.')
    ap.add_argument('files', nargs='+', metavar='FILE')
    args = ap.parse_args()
    failed = False
    for path in args.files:
        try:
            text = open(path, encoding='utf-8').read()
        except OSError as e:
            print(f'{path}: cannot read ({e})')
            failed = True
            continue
        tables = find_tables(text)
        if not tables:
            print(f'{path}: no storyboard table found')
            failed = True
            continue
        for heading, rows in tables:
            print(f'== {path} | {heading} ({len(rows)} rows)')
            probs, curve = check_table(rows)
            for p in probs:
                print(p)
            print('tension curve:')
            for c in curve:
                print(c)
            if probs:
                print(f'FAIL ({len(probs)} problems)')
                failed = True
            else:
                print('PASS')
            print()
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
