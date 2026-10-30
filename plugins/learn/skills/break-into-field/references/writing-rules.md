# How Ash wants to be taught

From his feedback on the first technology book (Oct 30 2026). Shasta's `_rules/Clusters.md` writing rules and the pitch-site `copy-rules.md` hold underneath; these are the ones the first version broke. Each has the bad line from that version and the fix.

## Short paragraphs, one idea each

Ash on v2 (Oct 30 2026): "There are a lot of big paragraphs. Break them." The rule holds for every part of the book (cover, parts, chapters, answer blocks), and `scripts/check_chapter.py` fails a book that breaks it:

- **At most 3 sentences and 60 words per paragraph.** A longer one is two ideas; split it.
- **A paragraph of 2 or more sentences opens with a bold lead-in:** its point in a few plain words, so the bold lines alone tell the story.
- **Steps, three or more things, and comparisons are bullets, numbered steps or a small table,** never one sentence with "first... then... and finally".
- **Bullets: at most 2 sentences and 40 words.** More than 3 bullets are grouped under bold labels.
- **One idea per paragraph.** When the next sentence starts a new idea, start a new paragraph.

- Bad (v2, 117 words in one block): "The list wins while the AI can read the whole of it in one go and pick well: up to about a hundred documents with clear names. It's one text file the AI keeps up to date, you can read it yourself, and when it picks the wrong thing you can see why. Embeddings win when the list gets too long..."
- Good: "**The list wins up to about a hundred documents.** The AI reads all of it in one go and picks well. You can read it too, and see why it picked wrong." Then a new paragraph: "**Search by meaning wins in the thousands,** or when questions use different words from the documents."
- **Why:** Ash reads in short bursts. A wall of text hides the one line he needed; bold lead-ins let him skim, then slow down where he's unsure.

## Explain every basic term the first time it appears

**A term's plain meaning sits beside it the first time it's used, in a clause or brackets,** even words that feel basic: dashboard, database, language model, script, chunking. "A dashboard (one page that shows what matters at a glance)". The v2 critic found six such words used bare; the script warns on the common ones.
- **Why:** the book is for someone who doesn't know what he doesn't know. A word he half-knows reads as known, and the idea built on it slips.

## Plain names, never map IDs, inside chapters

**Inside a chapter, a problem is called by its plain name** ("the student dashboard", "hand-ins on the site"), never by a map ID (A1, B1). The script fails a chapter with an ID in it.

## A to B, never B to A

**Start from what he knows, end at the name.** Describe what happens, what it produces, then "This is called X" or "This step is the X".
- Bad: "**The door.** The site checks the shape once: five customers, no empty 'what they said'. This is checking at the boundary."
- Good: "Before anything is saved, the site checks that five customers are there and nothing is empty, and tells Rhea now if something's missing. This check is called checking at the boundary. This step is the door."
- Bad: "Follow one hand-in from Rhea's paste to the agent that reads it. Six steps, each one a part of the system."
- Good: "Rhea pastes her notes into a form on Week 3's task. Here is what happens to them, step by step, until an agent can read them."
- **Why:** a name first is a label he has to decode; a name after is a handle for something already understood. He repeated this five times.

## The plain sentence first, then the metaphor

**The idea that fixes it is a full plain sentence a 7th grader could act on before reading the chapter.** Then the metaphor, expanded, as its own line. A compressed slogan fails.
- Bad: "Shape the work once, at the moment it's handed in, and every later reader gets it for free."
- Bad: "Check at the door, then trust what's inside."
- Good: "Decide which pieces of data you want from each student (which week, which task, who they talked to, what they said), and collect them as separate fields the moment the work is handed in. Then every page and every AI agent knows exactly what is there and where to look. It's the airport security line: checked once at the entrance, trusted everywhere inside."
- **Why:** the slogan only makes sense after you understand the idea. He loves the metaphor and wants to think in it, so keep it, after the plain version.

## Headings say what the section tells you

**A heading is a question he would ask, a plain label from the skeleton, or a plain statement of what happens.** Test: read it alone; can you say what the section covers?
- Bad: "Judge a build", "Words you now own", "The fix, step by part".
- Good: "Where you are now", "How it works, from Rhea's paste to the agent", "When to skip it".

## No quotes, no bibliography

**Quotes and history go unless the quote is the clearest sentence available.** Keep one plain line of the why ("tables split the data from the programs that read it, so any program can ask by name. This is called data independence."). People are named only under Sources.
- Bad: "In 1970 a researcher at IBM proposed the fix. His paper opens: 'Future users of large data banks must be protected…'"
- **Why:** "I'm utilitarian. I need to know as much as I need to, and if I want to go deeper I'll find my own way."

## Outcomes by what they change in his work

**"After this chapter, you can" says what the chapter lets him do for the business, with the parts named plainly.** A technician's outcome fails.
- Bad: "Write the shape of one Udyaan hand-in: its fields, what's filled in for the student and what's checked at the door."
- Good: "You'll know which data to collect from students and which fields the site fills in for them, so AI agents can read the work and do the summarising for you."
- Bad: "Judge any form, sheet or database someone shows you."
- Good: "Look at any form, sheet or database and say what it's collecting, why, and how it helps the bigger outcome."
- **Why:** he cares about the end. The means are tactics he'll hand to Claude.

## How it's built is philosophy with a little practice

**Name the parts and what each is for, and which kind of tool fits each, in a paragraph or a short list.** Not a transcript of what he types and Claude replies.
- Good: "You need a page where the student pastes (the form), a store with named fields (a database; a Sheet or Airtable is enough to start), an AI step that turns the paste into the fields and shows them back (structured output), a check before saving, and the raw paste kept beside it."

## Examples from his own world, worked

**"Where else it applies" shows one example worked through with a small flow, then two more in a line each.** Known or invented examples; never search for them.
- Bad: "Fuji already does this. Every ticket's line 2 has a fixed shape."
- Good: "In Fuji you had this problem: tickets written in free text that the board couldn't read. You gave line 2 a fixed shape (type, status, blocked by), and now a script reads every ticket with no AI. The same move, on the same shelf."

## The answer embeds the words

**"The answer" gives the concept, what it means for him practically, and the transfer, with each term named right after its plain meaning.** No separate glossary, no "to decide, ask in order" procedure.
- Good shape, in his own words after reading: "When I want Udyaan to run on software, I first decide which data to collect, as fields. An AI can suggest the fields. Each hand-in fills the same fields (a record), the raw paste is kept too, and an AI builds a list of what's where (an index) so later weeks and agents find it."

## Keep what he loved

- The scenario with a symptom and a cost, and the failure told as a short story.
- "So what" on every line of "Where you are now".
- The answer blocks that say the sequence plainly ("What the site remembers comes first, because the dashboard, search and the agents all read from it").
- Metaphors from everyday life: the airport line, the school register.
- The colours and the overall look. A little simpler, a little variety between chapters.

## Concepts he flagged as important and not yet taught

- An index (a list of what's where, like a contents page) can beat embeddings (text turned into numbers that capture its meaning, used for search) at about a hundred documents. Teach when each wins.
- The unlock order (`unlock-order.md`).
- How much process an AI build needs, so it's safe without burning tokens: "sizing the build routine". A chapter under the team's shelf.
