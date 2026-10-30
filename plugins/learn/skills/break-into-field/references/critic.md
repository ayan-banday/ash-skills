# The critic

The builder can't judge its own chapter: it knows what every term means, so it reads past its own breaks. A fresh agent can, in one pass on the built HTML. Ash studies on a laptop; the only phone check is no sideways scroll at 390 px.

## One pass, on the HTML

Ash (Oct 30 2026): writing a markdown draft, fixing it, then building the HTML is excessive. The writing rules go into the build itself, so the first HTML is close, and the critic only trims.

1. Build the chapter into the book's HTML by the skeleton and the writing rules.
2. `python scripts/check_chapter.py <book.html>` and fix every FAIL.
3. Dispatch the critic once (Agent tool, model `sonnet`, fresh context). Give it the HTML path, the writing rules path and the prompt below; it strips the tags itself. Never the research, the brief or this chat.
4. Fix what it found, rerun the script, publish. A second pass only when the critic's own answer to the chapter's question disagrees with the chapter's answer in substance.

## The critic's prompt

> You are reading a chapter written for Ash: 20, a BBA student and founder who runs Udyaan (an online course for students), a micro-SaaS with a friend, and his own AI systems. He builds with AI daily but doesn't know how technology works underneath. He thinks in systems, wants first principles over syntax, and wants everything explained from what he knows to the name, never the name first. He hates clever lines he has to decode, quotes that don't teach, and outcomes written for technicians.
>
> Read `<writing-rules.md>` first. Then read the chapter at `<book.html>`: strip the HTML to text with a short script (the chapter is the section whose id starts with `ch`), and read it one section at a time, holding back "The answer" until you've written your own.
>
> Report, under 450 words, findings only:
> 1. **Your own answer to the chapter's title question** in three sentences, written before reading "The answer". Then: does the chapter's answer say the same thing? Name any line in it the chapter never taught.
> 2. **Every place the chapter goes name first** (a term, a step name or a label before its plain meaning). Quote the line.
> 3. **Every clever line:** a heading, bold opener or principle that only makes sense after you understand the idea. Quote it and give the plain version.
> 4. **Every quote, date or person's name** outside Sources.
> 5. **The outcome lines** ("After this chapter, you can"): are they written by what they change in his work, or for a technician? Quote any that fail.
> 6. **Every term never explained in plain words**, with the line where it first appears. Include basic ones (dashboard, database, script, language model): the first use needs its meaning beside it.
> 6b. **Every paragraph that holds two ideas,** or whose bold lead-in doesn't say its point. Quote the lead-in.
> 7. **The fixes, ranked, at most eight.** For each, the exact old line and the new line, so the builder can apply them as edits.
> No praise. Don't rewrite the chapter.

## What the critic is for, said once

It keeps the next chapter clear and specific without Ash having to read a draft. Each time Ash gives feedback on a built chapter, the rule goes into `writing-rules.md` with its bad and good line, and the critic reads it next time.
