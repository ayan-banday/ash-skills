# Colour research for the document palette generator

Based on four Figma Resource Library pages (listed under Sources). All text below is paraphrased. Where the Figma pages say nothing, the spec is marked as our own engineering choice, not Figma guidance.

## What the Figma pages teach

**Colour wheel basics.** Figma uses the traditional red-yellow-blue wheel. Primaries are red, yellow and blue. Secondaries (orange, green, violet) come from mixing two primaries. Tertiaries come from mixing a primary with its neighbouring secondary. Every harmony type is just a rule about which wheel positions to pick.

**Why harmony matters.** A harmonious set of colours makes a design easier to scan, sets up a visual hierarchy, carries a mood, supports brand recognition and helps with readable text.

**Four properties change how a colour feels.**
- Hue is the colour family.
- Value is how light or dark it is. Light values feel airy, dark values feel bold.
- Saturation is intensity. Lowering it makes a loud colour calmer (Figma's example: a bold red becomes less alarming; bold yellow turns soft and calm when whitened).
- Temperature is warm (reds, oranges, yellows: energy, appetite, urgency) versus cool (blues, greens: trust, calm, growth).

**Proportion (60-30-10).** One page describes a palette as one primary, one secondary and one or two accents, split roughly 60 percent dominant, 30 percent secondary, 10 percent accent. The triadic and analogous descriptions repeat the same idea: one colour dominates, the others support or accent.

**Contrast and accessibility.** Contrast is the value difference between text and its background. The WCAG minimums quoted are 4.5:1 for normal text and 3:1 for large text. Figma's practical advice: light shades for backgrounds, dark shades for text and primary controls. Light or dull colours on a weak background hurt readability. The complementary page points to a contrast checker (WebAIM).

**Using saturation sparingly.** Bright, saturated colours should be kept for the few things that must stand out (calls to action, key numbers). Too much vibrancy overwhelms. Neutrals balance strong palettes, and brands with a signature colour usually pair it with black, white or grey.

**Mood.** Dark blue reads as calm and reliable, maroon as confident and stable, green as growth, red and yellow as urgency, pink as playful, white as clean. Meanings differ between cultures, so check them against the audience. Build in greyscale first to settle hierarchy, then add colour.

**Medium.** RGB is additive and for screens. CMYK is subtractive and for print. Complementary pairs differ slightly between the two models. Relevant for us: PDF and Word documents are often printed, so keep chroma modest, since saturated screen colours shift or dull in CMYK.

**Combination families listed on the colour-combinations page** (names only; the page shows no hex values). Useful as mood vocabulary for naming and filtering palettes:
- Monochromatic: "Stormy morning" (blue-grey), "Mossy hollow" (olive), "Blue eclipse" (midnight blue), "Lush forest" (forest green), "Ink wash" (charcoal, cool grey, ivory), "Golden taupe" (gold, taupe, cream), "Burnt sienna" (terracotta, beige, sand), "Chocolate truffle" (browns, caramel, cream).
- Neutral: "Quiet luxury", "Harbor haze", "Stone path", "Urban loft", "Old photograph", "Cappuccino".
- Tranquil: "Calm blue", "Mountain mist", "Eucalyptus grove", "Olive grove", "Siltstone", "Frozen lake", "Coastal morning".
- Seasonal and Romantic (muted-friendly): "Autumn orchard", "Harvest moon", "Winter berry", "Desert dusk", "Tuscan sunset".
- The Vibrant and Playful families (neon, electropop, bubblegum and similar) are the opposite of what a professional document needs and should not be sampled.

What the pages do not say: no hex values, no lightness or chroma numbers, and no ratio guidance beyond 60-30-10 and the WCAG minimums. Everything numeric below is our own spec.

## Harmony types

Hue offsets are from the base (primary) hue. Figma describes them on the RYB wheel; a generator works in OKLCH hue degrees, which are perceptual and not the same as RYB, so treat offsets as approximate and let the lightness and chroma rules do the real work. Add random jitter of up to plus or minus 8 degrees so palettes do not look machine-regular.

| Type | How it is built (Figma) | Hue assignment for a document | Character |
|---|---|---|---|
| Monochromatic | Tints and shades of one hue | Primary = H. Accent = same hue with higher chroma and a different lightness (deeper, richer), or a warm neutral accent (ochre or clay, hue about 70). | Cleanest, hardest to clash, can feel flat; needs a visible lightness ladder. |
| Analogous | Three neighbours: one dominant, one supporting, one accent | Primary = H. Accent = H + 30 (or H - 30). Optional supporting hue on the other side. | Calm, natural, cohesive. Hues are close, so the accent must differ in lightness. |
| Complementary | Two opposite hues; strong contrast; each looks brighter beside the other | Primary = H. Accent = H + 180, kept small and slightly lower chroma. Never use the pair at equal strength. | Energetic, eye-catching, easy to overdo. Best for one call-out colour. |
| Split complementary | Base plus the two hues flanking its opposite | Primary = H. Accent = H + 150 or H + 210 (pick one; the other can serve a second chart colour). | Contrast with less tension than a true complement. Good default. |
| Triadic | Three hues 120 degrees apart; one dominant, two accents | Primary = H. Accent = H + 120 or H + 240. Third hue only for chart series. | Lively; needs muted chroma to stay professional. |
| Tetradic (rectangle) | Two complementary pairs | Primary = H, accent = H + 180 or H + 60. Other two for charts only. | High contrast, hard to balance. Allowed but rare. |
| Square | Four hues 90 degrees apart | Primary = H, accent = H + 90 or H + 270. Rest for charts. | Rich; needs neutrals to calm it. |

Suggested random weights for documents: analogous 25 percent, split complementary 25, monochromatic 20, complementary 15, triadic 10, tetradic or square 5. This keeps results quiet by default and only occasionally bold.

Base hue choice: pick H at random, then filter for tone. Cool hues (about 190 to 270: teal, blue, indigo) read as trust and calm and suit reports and proposals. Warm hues (about 30 to 90: terracotta, ochre) suit course pages and memos with a human voice. Mix temperature: a cool primary gets a warm accent and the other way round (Figma's warm-cool contrast tip).

## Palette spec for documents

Target: documents read on screen or printed on a light page. Values are OKLCH (L 0 to 1, C chroma, H degrees). H is the primary hue and A the accent hue from the harmony type. These ranges are our own engineering choices, informed by the Figma principles of muted saturation, light backgrounds and dark text.

### Roles and ranges

| Role | L | C | Hue | Contrast requirement | Notes |
|---|---|---|---|---|---|
| page (background) | 0.985 to 1.00 | 0.000 to 0.010 | H | n/a (reference) | White or a barely warm or cool off-white. For print prefer white or no fill. |
| surface (cards, table banding, callouts) | 0.955 to 0.975 | 0.006 to 0.016 | H | Ink on surface at least 4.5:1 (target 7:1) | Slightly darker than page so boxes show without borders. |
| ink (body text) | 0.20 to 0.30 | 0.010 to 0.030 | H | At least 7:1 on page (above the 4.5 minimum, for long reading) | Never pure black or pure grey. Tinted toward the primary hue. |
| muted text (captions, footers, notes) | 0.42 to 0.52 | 0.015 to 0.035 | H | At least 4.5:1 on page and on surface | Hard upper bound: above L of about 0.55 plain text fails 4.5:1 on white. |
| rule / line | 0.86 to 0.92 | 0.008 to 0.020 | H | Decorative: none. If a line carries meaning (chart axis, input border) at least 3:1, about L 0.65 or darker | Thin and light; structure visible without shouting. |
| primary | 0.38 to 0.52 | 0.06 to 0.13 | H | At least 4.5:1 on page and on surface (used for headings, links, bars) | Mid-dark and muted. Headings may use L 0.30 to 0.40 for extra contrast. Clamp chroma to the sRGB gamut, never let output clip. |
| primary-soft (fills, table header bands, callout backgrounds) | 0.92 to 0.96 | 0.02 to 0.045 | H (+/- 5) | Ink at least 7:1; primary on it at least 4.5:1 | A tint of the primary, same hue. |
| accent (sparingly) | 0.48 to 0.62 | 0.08 to 0.15 | A | At least 3:1 on page for shapes or large text; 4.5:1 for any small text | Slightly higher chroma than primary is fine because of its tiny area. Differs from primary by 30 degrees or more of hue, and ideally 0.06+ of lightness. |
| accent-soft | 0.93 to 0.97 | 0.025 to 0.05 | A | Ink at least 7:1 | For a single highlight box, quote band or key-number background. |
| alert (bad, cost, risk) | 0.46 to 0.56 | 0.10 to 0.15 | 25 to 40 (brick, terracotta) | At least 4.5:1 on page | Muted brick, not fire-engine red. If primary or accent falls within 25 degrees of this band, move the primary or accent, not the alert. |
| ok (good, saving, pass) | 0.48 to 0.58 | 0.07 to 0.12 | 150 to 175 (teal-green, deep green) | At least 4.5:1 on page | Leaning toward teal keeps it separable from brick for red-green colour blindness. |
| alert-soft, ok-soft (optional) | 0.94 to 0.97 | 0.02 to 0.04 | as strong versions | Ink at least 7:1 | Tinted status rows. |

### Lightness guide for contrast on a white page
For low-chroma colours, contrast against white is about 3:1 at OKLCH L of about 0.66, about 4.5:1 at L of about 0.57, and about 7:1 at L of about 0.43. These are rough guides only. The generator must compute real WCAG 2.x relative-luminance contrast after gamut clamping and, if a role fails, step lightness in 0.01 increments (darker for text roles, lighter for fill roles) until it passes. Never loosen the threshold.

### Neutral tinting
Every neutral (page, surface, ink, muted, rule) takes hue H with the small chroma values above, so greys feel part of the palette. For a warmer, more human feel (courses, memos), pull neutral hue partway toward 70 when the primary is cool. Keep neutral chroma at or under 0.035.

### How much of the page each role covers (60-30-10 for documents)
In a text document the page itself is the 60 percent, so apply the rule to coloured pixels and visible emphasis:
- 60 percent or more: page background and ink text (neutral, tinted).
- About 30 percent: surface, primary-soft, rules and muted text (the quiet supporting layer: table bands, callout boxes, footers).
- About 10 percent or less: primary for headings, links, key chart bars and the title block; accent for no more than one or two things per page (a key number, one highlight band, a pull-quote mark).
- Alert and ok sit inside that 10 percent and appear only where meaning demands it, at most about 2 percent of a page.
- Squint test: a page thumbnail should be mostly white and grey, primary giving structure, and at most one small spot of accent.

### Other rules for the generator
- Chroma budget: primary C at most 0.13, accent C at most 0.15, everything else lower. Mean chroma across a palette under about 0.07.
- Lightness ladder: roles must be separable by lightness alone (page, surface, rule, muted, primary, ink in clear steps) so the document still reads in greyscale and on a black-and-white printer (Figma's greyscale-first tip).
- Charts and tables: up to 4 series colours from the harmony hues at similar L of about 0.55 and C of about 0.09, with small lightness variation, plus direct labels, markers or patterns so colour is never the only cue.
- Word and PDF export: convert OKLCH to sRGB hex after gamut clamping (reduce C, keep L and H), emit hex tokens for styles. For print, favour primary chroma of 0.10 or lower.
- Dark backgrounds are out of scope. If a cover or title band uses primary as a fill, white text on it must reach 4.5:1 (primary L at most about 0.50); body pages stay light.
- Use a deterministic seed and record it in the output so a palette can be regenerated.
- Self-test before returning: all contrast thresholds above, hue gap between primary and accent of at least 30 degrees (except monochromatic), alert and ok at least 100 degrees apart.

## Avoid

- Neon, electric and very saturated colours (Figma's "vibrant" and "playful" families); any main role with chroma above about 0.15.
- Pure greys and pure black on white. Use tinted neutrals.
- Purple-to-blue gradients, and gradients in general for documents. Flat fills read cleaner in print and in Word.
- Too many hues. Two hue families for interface roles (primary, accent) plus the fixed alert and ok. Extra harmony hues only in charts, and at most four there.
- Red and green as the only difference between two things. Add a label, icon, sign (plus or minus), position or pattern, and keep alert and ok at different lightness as well as hue.
- Equal-strength complementary pairs side by side (they vibrate and tire the eye, a point Figma raises about strong complements). Make one dominant, the other tiny.
- Low-contrast grey text on tinted fills, and pale primary on white. Check every text and fill pair, including text on primary-soft and accent-soft.
- Accent everywhere. Beyond two or three items per page it stops being an accent.
- Coloured page backgrounds in printed documents: wastes ink and prints unevenly.
- Ignoring tone and culture: choose base hue ranges that fit the document type, and avoid red as the primary in financial or medical documents unless asked.
- Judging colour on a screen alone. Check the palette in greyscale and at reduced chroma.

## Sources

URLs read:
- https://www.figma.com/resource-library/color-combinations/ (first 100,000 of 103,407 characters read; the unread tail is combination listings)
- https://www.figma.com/resource-library/what-is-color-theory/ (the fetch tool reported the text as partly cut off)
- https://www.figma.com/resource-library/types-of-color-palettes/
- https://www.figma.com/resource-library/what-are-complementary-colors/

Note: the Figma pages gave no hex values, OKLCH numbers or document-specific 60-30-10 guidance. The role ranges, lightness estimates, hue offsets and weights are our own engineering choices, informed by those pages and standard WCAG 2.x contrast maths.
