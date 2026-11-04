# The book's shape

One book per unit (or per study session), read on a laptop: one link, the chapters as tabs (Ash, Nov 4 2026: "all the different things, like variance, budgets, combined into one session"). `example-page.html` is the approved look for a chapter's insides: copy its `<head>`, CSS and class names. Its words and its single-page frame predate Ash's comments, so this file and `writing-rules.md` win wherever they differ.

## The frame

```html
<nav class="bar" aria-label="Book"><div class="in"><span class="bk">[Subject] · [Unit]</span><button class="notesbtn" id="gapsbtn" type="button">Gaps</button></div></nav>
<main>
  <header class="cover part" id="top"><div class="wrap">…</div></header>
  <section class="part chapter" id="ch1" data-chapter="ch1" data-tab="[Concept, the course's words]"><div class="wrap">…</div></section>
  <section class="part chapter" id="ch2" data-chapter="ch2" data-tab="…"><div class="wrap">…</div></section>
  <section class="part endpart" id="fq" data-chapter="ch3" data-tab="Founder questions"><div class="wrap">…</div></section>
</main>
```

- **Tabs hang off the right edge like notebook dividers,** one per `data-tab`, each showing its concept name; a click flips to that chapter. The cover gets a small ⌂ tab. `assets/tabs.html` builds them; never hand-write the tab list.
- **Each tab has its own palette, never red** (Ash, Nov 4 2026): `data-chapter="chN"` picks the block that `palette.py --chapters` printed, which colours the tab and, while it is open, the whole page and the tutor. Number the blocks in tab order, the founder questions included.
- **Links between chapters** use the target's id (`#ch2`, or any id inside it); the tabs script opens the right tab.

## The cover

The kicker (`Subject · Unit`), the book's problem as the `h1`, and the book's big concepts as tags, each opening its chapter. **No summary line, no problem cards** (Ash, Nov 4 2026: "I would just want to see what the big concepts are that we are covering").

```html
<div class="kicker">Managerial Accounting · Unit 2</div>
<h1>[The unit's founder problem, about the running company]</h1>
<ul class="ctags"><li><a href="#ch1" data-chapter="ch1">Budgeting and Working Capital</a></li>…</ul>
```

## A chapter

The tab and the kicker carry the concept's name in the course's words ("Budgeting and Working Capital"). The `h2` is a founder problem about the running company ("How many sensors must Sensa sell before it stops losing money, and how does it plan the quarter?"). Under it, the concepts the chapter covers as small tags (`<ul class="ctags"><li>Break-even point</li>…</ul>`), then a `.sub` line (about how long). These headings, in order:

1. **"Where you are now":** plain bullets, one per thing he has or lacks on this problem. No "So what" (Ash, Nov 4 2026).
2. **"After this chapter, you can":** one bold outcome by what it changes in running a company, then the parts he'll know in plain words.
3. **"What this looks like for you":** a scenario in a `.filled` block, labelled as made up, with the running company's numbers and a symptom.
4. **"What usually happens":** the failure as 2 to 4 numbered steps (`ol.steps`) with real numbers.
5. **"Where the problem lies":** the root cause in one or two lines, someone doing something.
6. **"Why [something about this problem]":** two or three paragraphs, each standing alone (writing rule "Every section stands alone"): the mistake people made, with numbers, and the idea that fixed it, ending in the course's name for it.
7. **"The idea that fixes it":** the `.idea` box: a plain bold first line, then a mini example straight after inside the box that stands on its own. A metaphor follows only if the idea is hard. Then "What this means in practice:" and two bullets. A paper-board picture (`.board` with an SVG in Patrick Hand) only where it explains faster than words.
8. **The problem sections, one per concept, 3 to 6:** each a `.q` block whose `h3` is a problem the founder sees ("Sensa expects to sell 300 sensors in January. How many must it build?"; writing rule "Every big heading is a founder's problem"). Inside: the teaching paragraphs from the problem to the name, the factory mini for Managerial Accounting, and the practice pair. **The professor's strong questions become this section's worked example or "Your turn"**, rewritten into the chapter's story with the numbers he set; weak or repeat ones are dropped. **An assignment gets one line here** ("You have an assignment on this: …"), never a solved copy. No numbered label ("Question one") and no lead-in heading over the sections.
9. **Only when it shows how the idea helps build Ash's tech company**, any of: "How it works, from [start] to [end]" (3 steps of one real item's journey, then a `.mini` flow strip), "How you'd build it" (procedural) or "How you'd use it" (theory), "How you'd run it" (three rounds, one where something slips and is fixed), "Where else it applies" (one worked example in another kind of tech company, then two in a line each), "When to skip it". Otherwise cut them (Ash, Nov 4 2026).
10. **"The answer"** (`.answer` block, last heading): the concepts in his words with each name right after its meaning, ending in the bold line "What this unlocks next:" naming the next chapter's problem plainly.

**Rings** (`tutor.md`): one before each problem section, and one before "The idea that fixes it" while that keeps the chapter at 6 or fewer. A chapter with six concepts keeps six sections, one concept each, and drops the idea's ring; with more than six, split it into two chapter tabs.

## A short chapter

**A concept he has already studied gets a short chapter that re-teaches only the gaps he marked** (Ash, Nov 4 2026, on Budgeting). It keeps the frame: "Where you are now" (what he has, and the gaps he marked, in plain words), "After this chapter, you can", "The idea that fixes it" in one box, one problem section per marked gap, taught from the start with a new worked example and "Your turn", and "The answer". Every other section is cut. Rings: one before the idea and one before each gap's section (3 at least; with one gap, add one before "The answer").

## Questions a founder might still have

**The book's last tab** (`id="fq"`, `class="part endpart"`): 2 to 4 questions a founder would ask that the class didn't cover, each a `.q` block whose `h3` is the founder's problem about the running company ("Sensa's sales look fine. Why can't it pay salaries this month?"). Each is taught like a chapter's first section: what goes wrong, why it matters to the company, then the idea and its name. **Theory by default**; worked numbers only where they make the idea clearer. **Never say where the material came from, or that it goes past class** (Ash, Nov 4 2026: "I don't need to know that this is past what [the professor] taught"). One ring for the part, before its first question.

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
  <details class="check"><summary>Show one strong answer</summary><div class="filled scroll-x">[same table shape]</div></details>
</div>
```

**The factory mini** (Managerial Accounting only), after a concept's teaching paragraphs:

```html
<div class="filled"><p><b>In a factory:</b> [two or three lines with its own numbers, same concept].</p></div>
```

## Checker traps

`../break-into-field/scripts/check_chapter.py` fails the build on: a list of 4 or more items inside a chapter (use a table or merge steps); a heading containing "practice" or "check yourself" (use the `.lbl` labels); a block quote; an em dash; a year; a map ID like A1; a paragraph over 3 sentences or 60 words; a 2-sentence paragraph with no bold lead-in; a chapter that doesn't open with "Where you are now" or close with "The answer". `scripts/check_book.py` fails a summary line on the cover, a class-questions or beyond-class part, a teacher's name, a chapter heading that isn't a question, and a heading that says "you" or "we".
