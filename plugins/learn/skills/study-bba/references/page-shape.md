# The page's shape

One page per problem, read on a laptop. `example-page.html` is the approved look: copy its `<head>`, CSS and class names. Its words predate Ash's comments, so `writing-rules.md` wins wherever they differ.

## Parts, in order

**Cover** (`header.cover`): a kicker line (`Subject · Unit · Problem A of three`), the problem as the `h1`, one bold lede saying what the unit is about in one sentence, and the `.three` cards for the opening's problems (this page marked `.on`).

**The chapter** (`<section class="part" id="ch1">`), the problem as its `h2`, then a `.sub` line (subject, about how long). These headings, in order:

1. **"Where you are now":** three bullets of where Ash stands on this problem, each ending "So what:" and its cost to him.
2. **"After this chapter, you can":** one bold outcome by what it changes in running a company, then the parts he'll know in plain words.
3. **"What this looks like for you":** a scenario in a `.filled` block, labelled as made up, with the running company's numbers and a symptom.
4. **"What usually happens":** the failure as 2 to 4 numbered steps (`ol.steps`) with real numbers.
5. **"Where the problem lies":** the root cause in one or two lines, someone doing something.
6. **"Why [something about this problem]":** two or three paragraphs, each standing alone (writing rule 1): the mistake people made, with numbers, and the idea that fixed it, ending in the course's name for it.
7. **"The idea that fixes it":** the `.idea` box: a plain bold first line, then a mini example straight after inside the box that stands on its own. A metaphor follows only if the idea is hard (writing rule 3). Then "What this means in practice:" and two bullets. A paper-board picture (`.board` with an SVG in Patrick Hand) only where it explains faster than words.
8. **"[N] questions [people who do this] ask about [the problem's object]":** one `.q` block per concept, 3 to 5 in all. Each holds a `.n` label ("Question one"), an `h3` that is a full self-contained question, the teaching paragraphs A to B (what happens, then the name), the factory mini for Managerial Accounting, and the practice pair.
9. **"How it works, from [start] to [end]":** 3 to 5 steps of one real item's journey, then a `.mini` flow strip.
10. **"How you'd build it"** (procedural: the sheet, tool or routine, part by part) or **"How you'd use it"** (theory: when, with whom, what it produces).
11. **"How you'd run it":** three rounds, one line each, one where something slips and is fixed.
12. **"Where else it applies":** one worked example in another kind of tech company with a `.mini` flow, then two more in a line each.
13. **"When to skip it":** one or two lines.
14. **"The answer"** (`.answer` block, last heading): the concepts in his words with each name right after its meaning, ending in the bold line "What this unlocks next:" naming the next problem plainly.

**The exam section** (`<section class="part" id="exam">`), only when the material holds questions or a key: each question answered in the course's terms with one worked number or example, tagged with its question letter. A question that needs more than a definition gets its own practice pair here.

## The practice pairs

**Procedural** (the example page's `.pair`):

```html
<div class="pair">
  <div class="lbl">Worked example: [what it finds]</div>
  <p><b>[The full situation, with every number.]</b> [The ask, naming each thing to find.]</p>
  <div class="filled scroll-x"><table><thead><tr><th>Step</th><th>Working</th></tr></thead><tbody>
    <tr><td>[Step name]</td><td>[formula in words] = [numbers] = [answer with unit]</td></tr>
  </tbody></table></div>
  <div class="lbl turn">Your turn: [what it finds]</div>
  <p><b>[A new full situation, every number given again.]</b> [The ask, naming each thing to find.]</p>
  <details class="check"><summary>Show the answer</summary><div class="filled scroll-x">[same table shape]</div></details>
</div>
```

**Theory** (same frame, reasoning in place of sums):

```html
<div class="pair">
  <div class="lbl">Worked example: [the judgement it makes]</div>
  <p><b>[A short scenario in a tech company, with names and stakes.]</b> [The question it raises.]</p>
  <div class="filled scroll-x"><table><thead><tr><th>Step</th><th>Thinking</th></tr></thead><tbody>
    <tr><td>[The concept's first move]</td><td>[What it shows in this scenario]</td></tr>
    <tr class="c"><td>Decision</td><td>[The call, and the one reason that settles it]</td></tr>
  </tbody></table></div>
  <div class="lbl turn">Your turn: think it through</div>
  <p><b>[A new scenario, complete on its own.]</b> [The question, one ask.]</p>
  <div class="think"><textarea rows="5" placeholder="Write your thinking, rough is fine."></textarea><button class="btn" type="button">Send to the tutor</button></div>
  <details class="check"><summary>Show one strong answer</summary><div class="filled scroll-x">[same table shape]</div></details>
</div>
```

**The factory mini** (Managerial Accounting only), after a concept's teaching paragraphs:

```html
<div class="filled"><p><b>In a factory:</b> [two or three lines with its own numbers, same concept].</p></div>
```

## Checker traps

`../break-into-field/scripts/check_chapter.py` fails the build on: a list of 4 or more items inside `#ch1` (use a table or merge steps); a heading containing "practice" or "check yourself" (use the `.lbl` labels); a block quote; an em dash; a year; a map ID like A1; a paragraph over 3 sentences or 60 words; a 2-sentence paragraph with no bold lead-in.
