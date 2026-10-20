---
name: "study (shasta)"
description: "How do I learn a topic the Shasta way? Ash's way of learning any topic through Shasta, his learning library. Use whenever Ash says he wants to study, learn, understand or is curious about something (\"I want to study design thinking\", \"I'm curious about AI agents\", \"teach me pricing\", \"help me understand how skills work\"), asks what he could learn about a topic, or asks for a study page, cluster or learning brief. It runs the evening from first question to an approved learning brief, then builds the study page."
---

# Study

Ash learns by first principles, mental models and thinking tools, so he understands enough to experiment on his own. The full process lives in Shasta's rule files. This skill points at them; **the rule files win** if anything here disagrees.

## Find Shasta

- **On Ash's laptop:** `D:\Shasta`.
- **In a cloud session of the Shasta repo:** the repo root.
- **Anywhere else:** say Shasta isn't reachable from here, and stop.

Read `CLAUDE.md` at the Shasta root first. Write only inside Shasta, never into the project this session started in, unless Ash asks.

## Steps

1. **The evening, up to an approved learning brief:** follow `_rules\Menus and Learning Briefs.md`, after reading `_reference\Evening Example (Half Marathon).md`. Done when Ash says yes to the brief.
2. **The study page:** follow `_rules\Clusters.md`, after reading `_reference\Study Page Example (Your SaaS's Own Look).md`. Build the HTML straight from the approved brief. Done when `python _reference\check_study_page.py <page>` prints no FAIL and the page passes the desktop and phone checks.
3. **The fresh check:** follow `_rules\Fresh Check.md`. Two fresh sub-agents check the page: a reader answers each question itself, and a rule checker goes through every judgement rule in `Clusters.md`. Done when both come back clean. Only then show Ash.
4. **After he studies:** Ash explains the key takeaways back in his own words, Claude points out the gaps, and one line goes in `study log.md`.
