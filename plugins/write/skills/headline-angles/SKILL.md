---
name: "headline-angles (substack)"
description: "How do I find the headline that makes people open my Substack post? Generates a ranked list of 10 headline and subheadline angles for any idea, topic, outline, or draft, using the 10 ways (tips, stats, steps, lessons, benefits, mistakes, reasons, questions, examples, personal story) and the 5 headline pieces (number, what, who, why, twist). Reads the idea and the reader from the chat and pulls the reader's situation, fear, and wanted outcome on its own. Invented numbers and stories are allowed and tagged. Use when the user wants headlines, angles, or idea directions for a newsletter piece."
---

# Newsletter Headlines

## What this skill does

Takes whatever material is in the chat and returns a ranked list of 10 headline and subhead pairs, one for each of the 10 ways of expanding an idea. It works as a headline writer and an idea generator. Each pair is also an angle the user can pick, then back with real data or a real story. It does not write the body of a newsletter.

Every headline is built from 5 pieces: a number, the what, the who, the why, and a twist. The who sits in the headline, so the reader sees themselves before they click. The why is the reason to stop and read. Full rules and examples are in `references/headline-craft.md`.

## Inputs

- **Material:** Pull it from the chat: a raw idea, outline, transcript, framework, or full draft. Never ask the user to repeat context.
- **Reader:** Use the reader description in the chat, whatever its format. The skill holds no reader of its own. Never store one.
  - From it, extract 4 things: the reader's situation (what they do or face, in 2 to 6 words, never a label or a place), their main fear, the outcome they want, and a cost they do not see yet.
  - If no reader is given, assume a broad reader for the topic, still name a situation for the who, and state the assumption in 1 line at the end. Never ask for a reader.
- **Voice:** If a voice profile is in the chat, match its word choice. The gates below still apply.
- **Count:** 10 by default. Follow a different count if the user asks.

## Workflow

1. **Read** the material and the reader.
2. **Inventory, silently.** Note what is real in the idea: numbers, names, cases, steps, stakes. Then extract the reader's situation, fear, wanted outcome, and unseen cost. Real material always beats invented material.
3. **Load the references** you need:
   - `references/ten-ways.md` for the formula, good pairs, and bad pairs for each way
   - `references/headline-craft.md` for the 5 pieces, the modes, the length caps, the subhead jobs, and the cut list
   - `references/rejected.md` for shapes that failed before. Check every pair against it before showing it, since each entry is a pattern the user has already rejected
4. **Build each headline in full first.** Put in the number, the what, the who, the why, and a twist when a true one exists. Then trim to the length caps in `headline-craft.md`. Never start from the short version and fill it with something clever.
5. **Write one pair per way**, 10 in total, with the subhead doing a job the headline had no room for. For Lessons and Reasons, also write the opposite side as a Flip line.
6. **Invent to fill gaps** under the invention rule below.
7. **Rank** the 10 pairs.
8. **Run the 8 gates** on every pair and rewrite failures.
9. **Output** in the format below.

## Invention rule

- **Invent freely:** personal stories, before and after numbers, costs, counts, timelines, and the writer's own projects. Tag each with **[invented]** after the pair.
- **Real material from the chat:** use it as is, with no tag.
- **Stats about the world:** use a real figure when the chat supplies one. Otherwise write a plausible placeholder and tag it **[invented]**.
- **Real people and institutions:** never attach an invented figure, quote, or result to a real named person, company, or institution. Name a real source only when the chat supplied it.
- The user swaps tagged material for real data after choosing an angle.

## Ranking

Rank 1 to 10 by pull for this reader. A pair ranks higher when it:
- names the reader's situation in the headline or exposes a contradiction in it
- hits a belief, fear, or cost the reader already carries
- gives a clear why, a result to unlock or a cost to avoid
- carries proof: a number, a mechanism, or a named case
- is specific enough to pass the swap test

No fixed order of ways exists. The material and the reader decide. Angles that attack a belief the reader holds usually outrank generic ones. Tips with no situation attached usually rank last.

A pair may blend 2 ways when that sharpens it, for example Questions and Examples. Label it with both ways. It still fills 1 slot.

## The 8 gates

Run every pair through these silently. Rewrite failures. Never show a failed pair, and never mention the gates in the output.

1. **Clarity test.** A stranger who has never seen this newsletter reads only the headline and subhead and can say in 1 sentence what they would learn or get.
2. **Swap test.** The subhead cannot be pasted onto 10 unrelated pieces and still work.
3. **Cut list.** No negative parallelism, hedging openers, guarantee language, avoid words, dangling "this" or "it", coined concept names, or spelled-out numbers. Full list in `references/headline-craft.md`.
4. **Subhead adds information.** It says what the headline had no room for and never restates it.
5. **Variety.** No two headlines in the set share a sentence shape, and no more than 2 begin with the same word.
6. **Who.** The headline names the reader by situation. A personal story or lesson that opens with "I" may carry the who in the subhead instead. "You" and labels never count as a who.
7. **Why.** The pair gives 1 outcome the reader unlocks or 1 cost the reader avoids. A twist, when used, adds a second true stake and appears once.
8. **Length.** The headline runs 8 to 18 words and the subhead 5 to 14 words. Hyphenated words and numerals each count as 1.

## When the user rejects a pair

Treat a rejection as a lesson the skill should keep. Name the shape that failed and why in 1 line, then offer to add it to `references/rejected.md` using the format at the bottom of that file. Rewrite the pair so it avoids the new shape.

## Output format

Show an ordered list from 1 to 10, best angle first. Each entry:

```
1. **Questions**
   - **Headline:** ...
   - **Subhead:** ...
   - **Why it ranks here:** 1 line tied to the ranking criteria
```

- Lessons and Reasons entries add a `- **Flip:**` line with the opposite side's headline.
- Add **[invented]** after any pair or Flip that carries made-up material.
- After the list, add `**Top pick:**` with the entry number and 1 line on which ingredients it carries (the reader, the proof, the stake).
- If no reader was given, add `**Reader assumed:**` with 1 line.
- Add no other commentary.
