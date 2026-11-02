---
name: match-ash-style
description: "[helper] How do I write and design anything Ash or his readers will see, so he never has to correct the same thing twice? Names who reads it and on what screen, then applies Ash's writing and design rules for that case and fixes the draft before he sees it. Use before any page, prototype, study result, message or chat reply Ash reads, and when he says 'in my style', 'the way I write' or 'my design rules'. Every building skill reads it first."
---

# Match Ash's style

Ash's time goes into correcting the same things: copy that's unclear, and pages that don't fit how he works. This skill holds those corrections in one place, so a session gets it right the first time and Ash only judges the idea.

**The building skill decides the job; this skill decides the voice and the look.** When the two disagree, the rule with the newer date wins; with no date on either, the building skill wins for its own artifact. This skill fills in everything the building skill doesn't say.

## Steps

1. **Name the case.** Find the row in "Which case is this?" below: who reads it, on what screen, and what they do after. Done when you can say it in one line ("A brief for Mohit, read alone on a laptop, ends in a decision").
   - No reader given? It's **for Ash**. If it's leaving his hands, it's **for others**.
   - Two rows fit? Pick the reader who acts on it.
   - A prototype of a tool takes the look of the people who'll use it (a team tool, a course page). Ash judges it first, so if it has a dark mode, show him that.
2. **Write it.** Apply `references/writing.md`: the rules for every case, then your case's section. Done when every heading, sentence and bullet passes "The one test" there.
3. **Decide the visuals, then the look.** Apply `references/design.md`: draw only when "When to draw" says so, then use your case's screen, theme and palette. Done when you can name what each picture explains faster than words.
4. **Fix it yourself before Ash sees it.** Ash should never catch a rule that's in this skill.
   - On HTML, run the copy scan and fix until it's clean: `python ../../../visualize/skills/brief-page/scripts/scan_copy.py page.html`. Furniture headings ("The short answer", "Sources") carry `data-label`.
   - On a page, screenshot it at the case's width (390px for phone, 1280px for laptop) and look for: anything a fixed bar covers, a chart mark with no number, text that runs off or wraps badly, two accents fighting, and the same thing shown twice.
   - Then read it once as Ash: run "Read it as Ash" in `references/writing.md`.
   - Done when the scan is clean and the read-as-Ash check finds nothing.
5. **Show it, then step back.** Lead with the thing itself (the link, the page, the answer), never with what you did.
   - **A page goes out as a link Ash can tap on his phone:** a claude.ai artifact, or `/visualize:post-page-online` for people outside. Never a file path.
   - The reply that carries a page holds the link, one line on what it shows, and the guesses. Nothing the page already says.
   - Then, in 3 lines or fewer: what you guessed and what you made up, so Ash can correct it in one reply. Anything you need from him (a reason, a name) goes here as a guess he can fix, never as a blank.
   - Prototypes and first drafts skip the long grilling. Make your best guess and show it. Ash reacts faster to a guess than to a blank.
6. **When Ash corrects something this skill should have caught,** add the rule to the right reference file in one line, with his words and the date, and bump the version. One rule lives in one place.

## Which case is this?

**For Ash** (he reads, judges, decides)

| Case | Screen | Built by | Shape |
|---|---|---|---|
| **Chat reply or grilling round** | Claude app, often his phone | the chat itself | The answer first; options lettered, recommended first |
| **Study result or report** (a run he started, a hypothesis tested) | **Phone**, from a notification | this skill, "Phone study page" in `design.md` | Verdict first, three reasons, one next step, one screen |
| **Study page or book** (learning a topic) | Laptop, dark | `/learn:study`, `/learn:break-into-field` | Where you are now, the idea, far-away example, your world |
| **Prototype or first look** | His phone first, then laptop | `/plan:try-prototype` | The thing working, then 3 lines of guesses |
| **Plan of action** | Phone or laptop | the chat, or a ticket | The outcome, then up to 5 steps, each with what's done when |

**For others** (they read alone, Ash isn't there to explain)

| Case | Screen | Built by | Shape |
|---|---|---|---|
| **Briefing someone who decides** (boss, official, partner, teammate) | Laptop, often forwarded | `/visualize:brief-page`; printed: `/visualize:polished-doc` | The question, the short answer, how it looks, what they decide |
| **Persuading an outsider** (client, sponsor, panel) | **Phone first** (a WhatsApp link) | `/visualize:pitch-site` | Their asks, one answer each, one named person to contact |
| **Teaching students** | Phone | `/write:course-lesson` | Question-led, one running student, one Do |
| **A message to one person** (WhatsApp, email, a DM) | Phone | the chat, or `/plan:ask-someone` for a questionnaire | What you need, why, by when, in under 120 words |
| **Docs for Claude** (skills, CLAUDE.md, tickets) | none | `/write:agent-docs` | Steps first, each with a done test |

## Reference files

- `references/writing.md`: open for any words, on every run. The rules for every case, then one section per case, then "Read it as Ash".
- `references/design.md`: open whenever there's a page, a prototype or a picture. When to draw, the look per case, phone and laptop, what Ash rejects, and the phone study page.
