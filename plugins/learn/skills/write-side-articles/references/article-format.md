# One article, one deck: the format and the card rules

Open on every run, before writing the first card. **For cards, this file wins over teach-side-chat:** its chapter rules (Markdown tables for sequences, the worn park path as the model metaphor) are for chat chapters, never decks. Every rule here is Ash's, from his comments on the deck prototype (Fuji ticket 39, Nov 5 2026, 14 versions). `scripts/build_deck.py` checks the ones code can check; the rest are yours.

## The file you write

One `<name>.article.html` per article, three blocks, nothing else. The engine (`assets/deck-template.html`) does the trail, the swipe, the island, the Ask pane and the Other questions. Never copy engine code into an article.

```html
<style id="tokens">
/* Palette: No. N, ... · place dark (paste palette.py's comment and :root block, drop its .keyline lines) */
:root{ ...palette.py tokens...;
  --island:var(--b2); /* the combination's colour that isn't the accent, never default blue */
  color-scheme:dark; }
</style>

<script type="application/json" id="article">
{"id": "kebab-case-slug", "title": "Two To Four Words",
 "question": "How do you ...?",
 "world": "Udyaan",
 "expert": "a ten-year expert in <the field that owns this problem>",
 "reader": "Who Ash is for this question, in two plain sentences from his note.",
 "asker": "founder", "askers": "Founders",
 "written_by": "the build session, strongest model",
 "metaphor": "street cricket", "far": "dolphin training",
 "parts": [{"name": "Oneword", "long": "A longer name", "c": "var(--p1)"}, ... 4 in all]}
</script>

<template class="card" data-part="0" data-kind="question"> ... </template>
... one <template> per card, in the order below ...
```

- **`--island`:** pick a `--b` token whose value differs from `--acc`. When `b1` equals `acc`, take `b2` or `b3`; a near-black one disappears on the card, so take the lightest of the rest.
- **Part colours:** four tokens that look different and read on the page, usually `--p1`, `--p2`, `--p3`, `--tx`. Many two-colour combinations give two near-identical pastels; `build_deck.py` rejects them, so re-seed (step 4) until it passes rather than swap in a dull grey.
- **`metaphor` and `far`:** the daily-life scene and the far field, a few words each. The library keeps them so no later deck reuses them (`--avoid-worlds`).
- **Part names:** one contextual word each, at most 9 letters, so four fit at 390px ("Polish, Shouts, Udyaan, Habits"). `long` is what the row under the trail says.
- **`world`:** where Ash applies it, from his note. It fills the Ask pane's prompts and its suggested question ("How would this look in Udyaan?"). `asker` and `askers` name who he is in this question ("Founders ask next"; a BBA finance question might be "a student who runs a business").
- **`@@QUESTION@@`** in the first card's `<h1>` becomes the question.

## The card order

`data-kind`, in this order. Parts 0 to 3 run in order and each has at least one card.

| # | kind | Its heading (Ash's plain question) | What it holds |
|---|---|---|---|
| 1 | `question` | the question (`@@QUESTION@@`) | where Ash is, in two short lines |
| 2 | `promise` | "What will you be able to do?" | the outcome in his context, never the steps |
| 3 | `wrong` | "How does it usually go wrong …?" | three stops down one line (`.stops`), then one box with the problem |
| 4 | `instead` | "What if we do this instead?" | a drawing of the new move, then two or three short lines |
| 5 | `why` | "Why does that work?" | the metaphor: a drawing, a lead line, short lines, the marked result |
| 6 | `concept` | "Where does … ?" | the places or parts, big and numbered (`ol.places`) |
| 7 | `concept` | "How does one … show up in all four?" | one example run through each part, the name last in a box |
| 8 | `team` | "How would it look in a team?" (or the field's own unit) | before and now side by side (`.ba`), each with what it leads to |
| 9 | `world` | "How would you apply this in Udyaan?" | the article applied to his world: who does what, when |
| 10 | `world` (optional) | a second plain question about his world | how it keeps going |
| 11 | `changes` | "What changes for you?" | a real exchange (`.talk`) and two or three short lines |
| 12 | `far` | a plain question from the far field | eyebrow "Far away · <field>", a drawing, the same first principle solving a different problem |
| 13 | `limit` | "When does this stop working?" | one limit and one test |
| 14 | `answer` | the question, short | steps (`.st`: chips, then the numbered places), one marked line, folded Sources |
| 15 | `other` | "What else do you want to know?" | three `button.q`, each `data-q` equal to its label |

## Writing each card

- **Every card stands alone.** It never says "the same draft", "like the kid", "as above" or points back to another card. Read each card with the deck hidden.
- **Picture first, words after.** On a card with a drawing, the drawing comes right after the heading.
- **Every heading is Ash's plain question,** never a clever line.
- **A big concept gets two cards:** first the parts, big and numbered; then one example run through each; the name last ("These four places are called embedding mechanisms").
- **Show the real moment, never a bare category.** No tables, no tile grids of labels. "The designer shares the sign-up screen as a sketch on day 2", not "Transparency".
- **A change is before and now side by side,** each with what it leads to. Never cross-outs.
- **No paragraphs.** Short lines stacked down a thin rule (`.seq`). At most 30 words in any block; most lines are under 14.
- **Cut every line that adds nothing,** above all the hedging kind ("No speech. No values poster.").
- **At most two named concepts in a deck:** the big concept and the far-transfer name. Everything else in plain words.
- **No how-to lines** ("tap Ask", "swipe"): Ash knows how the deck works.
- **No dead space.** Every card but the promise fills at least half of its screen. A short card gets a bigger drawing, `p.big` or `.seq.big` (the question card's two lines), never filler.
- **Every number shows where it came from,** in one line on the same card ("₹9,000 more today skips eleven ₹1,000 payments"). A made-up example amount is fine; an unexplained one is not.
- **The metaphor comes from a daily-life scene Ash has lived,** in a world nothing like the problem's, mapped part by part (teach-side-chat, "How the idea and its metaphor are made"). For money, lending a thing (your scooter for a month) is a metaphor; lending money in another job is an example, not a metaphor.
- **Far transfer** is the same first principle solving a different problem in another field, said in plain short lines ("What happens if you pay an AI one point per target?"). Never the same problem somewhere else.
- **The answer card** comes in steps (pick three as chips; the numbered parts), then one marked line.

## The visual weights, heaviest first

Use each where its job is; a card that needs none of them is fine.

| Weight | Class | Its one job |
|---|---|---|
| The heading | `h1`, `h2` | the question this card answers |
| A lead line in the part's colour | `p.lead` | opens a metaphor |
| Numbered circles | `ol.places` with `<li><span>1</span>…</li>` | steps or places; `.habits` adds a grey line under each, `.small` makes them a 2 by 2 grid |
| A highlighter stroke | `span.mark` | the one result line, once per card |
| A dotted underline | `b.name` | the one concept name |
| One box | `div.keyline` with `span.l` and `span.t` | the principle, the problem or the name, once per card |

The other parts: `.seq` (short lines down a thin rule), `.stops` with `.stop` / `.stop.hit` (`span.w` when, plain span what, `span.r` result), `.stops.watch` (one example through each part), `.ba` (`span.col.was`, `span.col.now`, then per row `span.when`, `div.was`, `div.now`, each `<b>` the move and `<i>` what it leads to), `.rows` (label `span`, `b.quote`, `em`), `.talk` (`span.who` per speaker), `.ans` with `.st` (`span.sn`, `<b>`, `.chips`), `p.big`, `p.line`, `p.line.mu`, `p.eyebrow`. Two example articles use them: `references/example-culture.article.html` (a team habit) and `references/example-money.article.html` (a finance concept, with numbers).

## Drawings

- **Every drawing is new** and comes from this article's world: its own scene for the metaphor, its own new move, its own far field. Never the park, the boat race or any picture from another deck.
- **One inline `<svg>` in `<div class="board">`,** `viewBox` about 340 wide and 160 to 236 tall, with a `<title>` that says what it shows.
- **Colour only with the classes:** fills `s-tx s-mu s-p1 s-p2 s-p3 s-bg2 s-bg3 s-on`, strokes `k-ln k-p1 k-p2 k-p3`. No literal colours, so the article's combination carries through.
- **Labels 13 to 16,** at most six, one to four words, inside the viewBox (a label anchored at the middle must fit both ways).
- **One clear path for the eye,** left to right or top to bottom. At most three drawings per deck (`instead`, `why`, `far`); another only where it explains faster than words.
