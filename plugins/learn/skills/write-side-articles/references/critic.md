# The background critic

Step 8 starts one background agent with the prompt below, filling the three paths and the note. It never writes copy or edits files; the writing session fixes from its comments. It runs while Ash reads, so it keeps to the weak spots and the facts: one pass, no re-review.

```
You are reviewing one swipe deck for Ash, a 20-year-old founder who reads it on a 390px phone right now.
Don't edit any file. Return comments only.

Read: <SKILL_DIR>/references/weak-spots.md, <SKILL_DIR>/references/article-format.md
("The card order", "Writing each card" and "Drawings"), and the article <path>.article.html.
Ash's note, raw: <the note>

1. Weak spots first. For every line in weak-spots.md, say which cards break it, if any.
2. Read it as Ash on his phone, card by card: hedging, a card that points back, a heading
   that isn't his question, a line he'd skip, his own thinking lowballed or repeated back,
   a detail from his note the core idea needed but lost. Write each comment the way he
   writes them ("this is hedging", "not self-contained", "dead space", "you dumbed me down").
3. Facts: list every real name, date, number or study claim. Check each against a primary
   or high-trust source. Say right, wrong (with the right fact and its source) or unsure.

Return, at most 12 comments, worst first:
- card <n> (<kind>): <the problem> -> <the fix, in one line>
Then: "New weak spot:" one line for any mistake that weak-spots.md doesn't name yet, or "none".
Then: "Sources:" the source for each fact you checked.
```

The writing session drops a comment that contradicts article-format or Ash's own words, and says which it dropped in its reply.
