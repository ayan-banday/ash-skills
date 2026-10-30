# Writing rules for proposal sites

The base rules are brief-page's `references/writing-rules.md` (7th-grade words, headings that carry the
answer, one or two highlighted phrases per paragraph, no filler). Read `copy-rules.md` first: it decides what each
line says (the message spine), when a heading is a question or a statement, and how to cut words. Where the two
disagree, `copy-rules.md` wins. This file adds what a proposal for a reader who
won't read needs on top, with the TVS lines that taught each rule.

## Contents
- The one test
- Asks and wording
- Headlines
- Capability, then impact
- Honesty: numbers, goals, examples
- Emphasis
- Banned words and patterns
- Check your own edits

## The one test

Read only the headlines, the drawings' labels and the highlighted phrases. If that path does not tell the whole
argument in order, the copy is not done.

## Asks and wording

- **Quote the reader's asks verbatim** and say where they were said. Never put a paraphrase in quote marks.
- **One wording per need, reused word for word everywhere:** the need card, the "You told us" block, the motif key,
  the badge label, the map. The Fable reviewer caught three names for one need on the TVS v2 page.
- **Explain every acronym and internal name on first use**, in the reader's terms: "CMDC (JAIN's interview method)",
  "small supplier plants (MSMEs)". Then keep the same short name.
- **Names come from written sources.** Ash dictates by voice, so names arrive garbled ("Gento", "Jento" for Jinto;
  "cobra", "column", "Cura" for kolam; "TBS" for TVS). Confirm every name and spelling against an email, a document
  or the client's site before it goes on the page.

## Headlines

- **Say what the section is about, as an action:** "Give every leader the full picture", "See inside your supplier
  plants", "Bring every process online". Ash asked for "a little bit more of a funk" over flat labels.
- **Collaborative, never credit-taking:** "How JAIN can support...", "can help...". Never imply the reader lacks
  something ("we're not roasting them"). TVS v2's "building leaders at every level" became "supporting them and giving them data".
- **No slot headings:** "Our approach", "Why us", "Next steps", "Overview". The heading is the content.
- **Two lines at most at laptop width.** Cut words before shrinking type.
- **The funk comes from the action verb and the client's world,** never from wordplay, aphorisms or counting what the section holds.

**Clever headings fail.** A heading passes when someone who hasn't read the section knows exactly what it covers. It is one of three things: a plain question the reader would ask, a concrete answer in everyday words, or a plain label for a recap or reference part ("Key takeaways", "Sources").

- Bad: "Two pictures to think with, and three rules that hold everywhere". It counts the contents and hides them.
- Bad: "Three rules, two pictures and two questions to carry into your own tests"
- Bad: "Symmetry is the language of trust". An aphorism makes the reader decode it.
- Good: "How do you know people will pay for your SaaS before you build it?" A question the reader would ask.
- Good: "New hires take 9 days to set up". A concrete answer.
- Good: "Key takeaways". A plain label for a recap.
- **Why:** a clever heading is a puzzle the reader solves before reading. A plain one tells them where they are.

**Test:** read the heading alone. If you can't say what the section will tell you, rewrite it in plainer words.


## Capability, then impact

- **No buzzword in isolation.** Every capability ends in a concrete effect on the reader: "We fit three small
  sensors" → "your night manager gets a message while there is still time to save the load".
- **Problem first:** the reader's problem, then who solves it (chip), then what they do (small, muted), then what the
  reader gets (highlighted).
- **Show the mechanism when proof is thin.** A worked example the reader can picture beats an adjective.

## Honesty: numbers, goals, examples

- **Never invent a number, client, result or quote.** Sourced numbers only, and only from facts.md.
- **Outcomes are goals until they happen:** "The goal: steadier supply." Never state a future result as fact.
- **Label every example:** "An example, chosen to show how we would work." Illustrative steps inside a labelled
  example may use times of day and places; never invented measurements.
- **Mention sensitive proof the way the client allows** ("JAIN has already built digital tools for TVS", unnamed).
- **Never pull Ash's own vault projects into client work** (Udyaan was cut from TVS on his instruction).

## Emphasis

- **Highlight with colour, not bold alone:** the marker sweep on the one phrase that says what the reader gets.
  Ash: "with different color palettes that make the text that is important get highlighted".
- **One highlight per screen.** A second one cancels the first.
- **Team names carry their chip colour** wherever they appear, so "who does what" reads by colour.

## Banned words and patterns

- No em dashes or en dashes in copy (use commas, colons or full stops).
- No "not X but Y", "isn't just X, it's Y", or any correction structure. State the thing.
- No hedges: could, might, perhaps, kind of, "nothing here is fixed yet". Say it plainly or cut it.
- No hype: unlock, unleash, elevate, seamless, supercharge, empower, streamline, effortless, robust, cutting-edge,
  next-gen, world-class, revolutionize, leverage, journey, holistic, synergy, stewardship, value chain.
- No tricolon slogans ("Fast. Simple. Powerful."). No "Get started", "Learn more", "Let's talk".
- No scaffolding text on the page ("Prototype · three of seven sections", "Section coming soon").

## Check your own edits

Run `python scripts/scan.py page.html --facts facts.md` after every copy change. It catches dashes, hedges, hype,
negative parallelism, slot headings and numbers that are not in the facts sheet, including text inside SVG and JS
strings. In TVS, the first fix pass re-introduced a hedge ("Nothing here is fixed yet") that only the scan caught.
