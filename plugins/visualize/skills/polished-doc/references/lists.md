# Long lists

A flat list of twelve items asks the reader to hold twelve things. Three groups of four ask them to hold three. This file says which structure a list gets, how to build each one, and what bad looks like.

## Contents
- Pick the structure by size and links
- Grouping into three
- Nesting
- Mind maps
- Decision trees, tiered tables, and matrices
- Bad patterns

## Pick the structure by size and links

| List size | Structure | Template or reference |
|---|---|---|
| Up to 7 items | Keep the list. Bullets, each with a bold lead and one plain line. | `<ul>` in template.html |
| 8 to 15 items | Group into three named groups. | `.gbox` chips, or `.grp` headers over rule blocks |
| 16 to 30 items | Nest: groups inside groups, two or three levels. | `.outline` in reference-playbook.html, Part 4.3 |
| Over 30, or items that link to each other | Draw a mind map, or a decision tree if the reader must pick one. | Mind map: Part 4.4. Tree: Part 3.1 |

These are defaults. A 9-item list of steps the reader follows in order stays a numbered list, because order is the structure. A 6-item list of options the reader must choose between may become a decision tree.

The rule also covers lists inside the document's own structure: ten rules, twelve visuals, eleven roles. If the writer's section has more than 7 parallel items, group them.

## Grouping into three

1. **Write each item on its own line** and read them for what they share.
2. **Find three groups a reader would name themselves.** Good groups answer one question each ("What is it about? People, steps, or amounts"). Two groups feel like a split; four start to become a list again.
3. **Balance them.** 4, 4, 4 or 4, 3, 3 reads better than 8, 2, 2. If one group swallows everything, the grouping is wrong.
4. **Name each group with what its items share,** in plain words: "Cut what carries no weight", "Steps, time, and action". Avoid "Other" or "Miscellaneous".
5. **Add a one-line description** under each group name.
6. **Keep the writer's items intact.** Grouping changes the order; it never drops or merges items without asking.
7. **Renumber after regrouping** and update every cross-reference to the old numbers.

Good:
> **Cut what carries no weight:** hedges, untrue framings, setup lines, decoration
> **Make it specific:** named things, one running example, a visible result
> **Connect it and keep the voice:** hand-offs, answer headings, the writer's voice

Bad:
> **Group 1:** hedges, examples, voice, setup lines
> **Group 2:** headings
> **Other:** everything else

## Nesting

Use when grouping alone would leave groups of 8 or more.

- Level 1: a few big areas (Writing, Visuals, Colour).
- Level 2: groups inside each area (Cut, Sharpen, Connect).
- Level 3: the items, as a comma-separated line in muted text. Not a third level of bullets.
- Lay level 1 out in two columns when the page is wide enough.

## Mind maps

A mind map trades detail for the whole picture. Use it when the reader needs to see how the parts relate, or as a one-page overview of a long document. Keep the nested or grouped version nearby for detail.

Build rules (see Part 4.4 in reference-playbook.html):
- **One centre**, filled with the primary colour, holding the topic in two or three words.
- **Four to six branches.** More than six becomes a hairball.
- **Two to four leaves per branch,** one or two words each. Short labels are what make a map readable.
- **Branch colour** in primary; one special branch type (for example the two that are processes) in accent. No rainbow.
- **Leaves on the outside edge,** text anchored away from the centre so labels never cross lines.
- **Hand-lettered font** for the map, because it is a sketch of ideas, not data.
- Check that no label is cut off at the SVG edge; widen the viewBox before shrinking text.

## Decision trees, tiered tables, and matrices

| Shape | Use when | Example |
|---|---|---|
| Decision tree | The reader must pick one item from many | Twelve visuals become two questions: "What is it about?" then a question per group |
| Tiered table | Items rank by importance, and readers look things up | Ten design rules in three tiers: can they read it, does the key part stand out, does it feel finished |
| Matrix | Items differ on two traits at once | Fixes placed by effort and impact |
| Numbered steps | Order matters | A process the reader follows |

## Bad patterns

- **A twelve-row table** where every row has the same shape. Group it or turn it into a tree.
- **Groups of one.** Fold the lone item into a neighbour or rethink the groups.
- **A mind map with sentences on the branches.** Shorten to one or two words or use a nested outline.
- **The same list shown twice** in two formats with no reason. Show it once; if both a map and an outline appear, say why (overview and detail).
- **Grouping that hides the writer's order** when order mattered (steps, ranked priorities).
