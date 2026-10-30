# The book's shape

One artifact, read on a laptop, grown one chapter at a time. Up to about 100 pages over time is fine. Every part ends in a block called "The answer", written in the words Ash would use once he understood it.

## Parts, in order

1. **Cover:** the book's question as the title. One line: what the book does. Links to each part.
2. **What you're learning, and why.** Headings: "What you're learning", "Why breadth comes first", "After this book, you can", "The problems you can solve once you know this", "Where you are now". Outcomes are written by what they change in his work (see `writing-rules.md`, "Outcomes").
3. **The problem map.** One outcome at the top, named as a problem. Under it, three or four groups, each of at most four problems, drawn as a mind map with arrows for what waits on what (`unlock-order.md`). Under the map, the ideas he'll pick up are shown on the map's branches, never as a long table. No "why chapter one is here" section: the arrows say it.
4. **The shelves.** How the field files itself, like a textbook. Each shelf: its plain name, how lit it is for Ash, the fields on it. Each field: its words, and one problem from Ash's world. Fields he wouldn't know to ask about are marked "suggested". Dark shelves carry suggested problems. No preamble about why words matter. The answer block is a plain summary of the shelves.
5. **Chapters.** One per problem, in the unlock order. Never a topic chapter ("what is a database").
6. **The recipe.** How the book was built, so the next field follows it. Short.
7. **Sources.** The only place people are named.

A live case from Ash's week (a friend's setup, a tool he saw) goes into the book only once the map has a problem it belongs to. Until then it waits in the ticket as a candidate chapter.

## The shelves of technology (the first field, approved by Ash)

1. Making things people want to use: UI and UX, information architecture, product analytics, behaviour design.
2. Where data lives and how it moves: databases, data modelling, data structures and algorithms, APIs, how the web works.
3. How software is built and kept running: software design, Git, cloud and DevOps, testing, migrations and backups, the production workflow.
4. Machines that learn and act: language models, retrieval and knowledge, agents, evaluation, machine learning basics.
5. Keeping it safe and trusted: identity and access, privacy, threats.

## The chapter skeleton

The chapter title is the problem as a question: "How do students hand in their work on the Udyaan site instead of Google Docs, so it's saved, found again later and usable by AI agents?" Under it, one line: the shelf and about how long. Then, in this order, with these headings:

1. **"Where you are now":** two or three lines of his real situation, each with its cost. The chapter opens here, not with what he'll learn.
2. **"After this chapter, you can":** one outcome, by what it changes in his work, with the parts he'll know named in plain words.
3. **"What this looks like for you":** one scenario, labelled as a scenario, with a symptom and a cost.
4. **"What usually happens":** the failure as a two to four step story.
5. **"Where the problem lies":** one or two lines, the root cause drawn from the story.
6. **"Why someone had to invent the answer":** one short paragraph. The problem people hit, and the idea that fixed it. No dates, no names, no quotes.
7. **"The idea that fixes it":** the plain sentence first, then its metaphor, then "What this means in practice" in two bullets.
8. **"How the people who build this think":** three to five ideas, each as a plain sentence, then its metaphor if one helps, then its name. No quotes.
9. **"How it works, from [start] to [end]":** the journey of one real item, A to B: what happens, what it produces, then "This is called X". A small picture only if it explains faster than the words.
10. **"How you'd build it":** the parts and what each is for, as philosophy with a little practice (which kind of tool fits each part). Not a transcript of a chat.
11. **"How you'd run it":** three rounds, one line each, one where something slips and is fixed.
12. **"Where else it applies":** one worked example from his own world with a small flow (Fuji, Udyaan, the micro-SaaS), then two more in a line each. Known or invented examples, no searching.
13. **"When to skip it":** one or two lines, A to B.
14. **"The answer":** the concept, what it means for him practically, and the transfer, with every term embedded right after its plain meaning. Ends with "What this unlocks next": the problems on the map that are now open.

Cut from every chapter: "What you'll learn", first principles and mental models listed up front, "Judge a build", "Words you now own", a glossary, timestamps, people's names, quotes as teaching, a decision procedure at the end, practice exercises, check-yourself questions.
