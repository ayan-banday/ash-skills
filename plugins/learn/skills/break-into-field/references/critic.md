# The critic

The builder can't judge its own chapter: it knows what every term means, so it reads past its own breaks. A fresh agent can. Run it on the markdown, before any HTML, so a failed round costs little. No phone checks, ever: Ash studies on a laptop.

## The cheap test

1. Write the chapter as markdown in the scratchpad, from "Where you are now" to "The answer".
2. `python scripts/check_chapter.py <file.md>` and fix every FAIL.
3. Dispatch the critic (Agent tool, model `sonnet`, fresh context). Give it only the chapter file, the writing rules file and the prompt below. Never the research, the brief or this chat.
4. Fix every finding. Rerun the script and the critic. At most three rounds, then ship the best and put what the critic still dislikes in the ticket.
5. Build the HTML only after the chapter passes.

## The critic's prompt

> You are reading a chapter written for Ash: 20, a BBA student and founder who runs Udyaan (an online course for students), a micro-SaaS with a friend, and his own AI systems. He builds with AI daily but doesn't know how technology works underneath. He thinks in systems, wants first principles over syntax, and wants everything explained from what he knows to the name, never the name first. He hates clever lines he has to decode, quotes that don't teach, and outcomes written for technicians.
>
> Read `<writing-rules.md>` first. Then read the chapter at `<chapter.md>` one section at a time, holding back "The answer" until you've written your own.
>
> Report, under 450 words, findings only:
> 1. **Your own answer to the chapter's title question** in three sentences, written before reading "The answer". Then: does the chapter's answer say the same thing? Name any line in it the chapter never taught.
> 2. **Every place the chapter goes name first** (a term, a step name or a label before its plain meaning). Quote the line.
> 3. **Every clever line:** a heading, bold opener or principle that only makes sense after you understand the idea. Quote it and give the plain version.
> 4. **Every quote, date or person's name** outside Sources.
> 5. **The outcome lines** ("After this chapter, you can"): are they written by what they change in his work, or for a technician? Quote any that fail.
> 6. **Every term never explained in plain words**, with the line where it first appears.
> 7. **The three fixes that would help most,** ranked.
> No praise. Don't rewrite the chapter.

## What the critic is for, said once

It keeps the next chapter clear and specific without Ash having to read a draft. Each time Ash gives feedback on a built chapter, the rule goes into `writing-rules.md` with its bad and good line, and the critic reads it next time.
