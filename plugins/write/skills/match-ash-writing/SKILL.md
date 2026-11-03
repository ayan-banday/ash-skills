---
name: match-ash-writing
description: "[helper] How do I write anything Ash or his readers will read, so he never has to correct the same words twice? Names who reads it and on what screen, then applies Ash's writing rules for that case and fixes the draft before he sees it. Use before any page copy, study result, message or chat reply Ash reads, and when he says 'in my style' or 'the way I write'. Every building skill reads it first; for the look, use match-ash-design."
---

# Match Ash's writing

Ash's time goes into correcting the same things, and copy that's unclear tops the list. This skill holds his writing corrections in one place, so a session gets the words right the first time and Ash only judges the idea. **The look (pictures, colour, type, screens) lives in `/visualize:match-ash-design`** (`../../../visualize/skills/match-ash-design/SKILL.md`); anything with a page, a prototype or a picture runs both.

**The building skill decides the job; this skill decides the voice.** When the two disagree, the rule with the newer date wins; with no date on either, the building skill wins for its own artifact. This skill fills in everything the building skill doesn't say.

## Steps

1. **Name the case.** Find the row in "Which case is this?" below: who reads it, on what screen, and what they do after. Done when you can say it in one line ("A brief for Mohit, read alone on a laptop, ends in a decision").
   - No reader given? It's **for Ash**. If it's leaving his hands, it's **for others**.
   - Two rows fit? Pick the reader who acts on it.
2. **Write it.** Apply `references/writing.md`: the rules for every case, then your case's section. Done when every heading, sentence and bullet passes "The one test" there.
3. **Fix it yourself before Ash sees it.** Ash should never catch a rule that's in this skill.
   - On HTML, run the copy scan and fix until it's clean: `python ../../../visualize/skills/brief-page/scripts/scan_copy.py page.html`. Furniture headings ("The short answer", "Sources") carry `data-label`.
   - Then read it once as Ash: run "Read it as Ash" in `references/writing.md`.
   - Done when the scan is clean and the read-as-Ash check finds nothing.
4. **Show it, then step back.** Lead with the thing itself (the link, the page, the answer), never with what you did.
   - **A page goes out as a link Ash can tap on his phone:** a claude.ai artifact, or `/visualize:post-page-online` for people outside. Never a file path.
   - The reply that carries a page holds the link, one line on what it shows, and the guesses. Nothing the page already says.
   - Then, in 3 lines or fewer: what you guessed and what you made up, so Ash can correct it in one reply. Anything you need from him (a reason, a name) goes here as a guess he can fix, never as a blank.
   - Prototypes and first drafts skip the long grilling. Make your best guess and show it. Ash reacts faster to a guess than to a blank.
5. **When Ash corrects the words in a way this skill should have caught,** add the rule to `references/writing.md` in one line, with his words and the date, and bump the version. One rule lives in one place; a look correction goes to `/visualize:match-ash-design`.

## Which case is this?

**For Ash** (he reads, judges, decides)

| Case | Screen | Built by | Shape |
|---|---|---|---|
| **Chat reply or grilling round** | Claude app, often his phone | the chat itself | The answer first; options lettered, recommended first |
| **Study result or report** (a run he started, a hypothesis tested) | **Phone**, from a notification | the chat, "Phone study page" in `/visualize:match-ash-design` | Verdict first, three reasons, one next step, one screen |
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
