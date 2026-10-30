# Architecture: how the page is built

One static HTML file, published as a private claude.ai artifact. Vanilla JS, SVG and CSS. It is assembled from a
starter plus one fragment per section, so sections can be built (and rebuilt) independently, even by parallel agents.

## Contents
- Folder layout
- The starter
- Fragments and modules
- Build, preview, publish
- Libraries
- Devices
- Architectures: three ways to read the same sections

## Folder layout

```
work/
  facts.md            every usable fact, with its source
  story.md            the argument and the story map (references/story.md)
  starter.html        copied from assets/starter.html, tokens filled from the chosen direction
  frag-1-hero.html    one fragment per section, numbered in page order
  frag-2-....html
  index.html          built by scripts/build.py (publish this)
  preview/index.html  the same page with a doctype wrapper, for the local preview server
  shots/              sweep.py frames
```
Keep the work folder path short (Windows paths over 260 characters break Chrome).

## The starter

`assets/starter.html` holds:
- the token block: fill it from the direction's palette (`--ground`, `--paper`, `--card`, `--ink`, `--muted`,
  `--line`, `--tint-1..4`, `--marker`, `--marker-ink`, `--accent-1`, `--accent-2`) and its fonts
- base type (display, body, label, hand), `.band` colour blocks, `.wrap`, `.lede`, `.label`, chips, `mark`, `.btn`
- helpers: `$`, `$$`, `onView(el, fn, threshold)`, `prepDraw(paths)`, `penDraw(paths, {delay, parallel})`,
  `FINAL`, `reduce`, `NS`, reveal (`.rv` → `.in`)
- the phone gate (CSS plus the JS screen check)
- a `/*MOTIF*/` slot for the direction's generator (assets/motifs/kit.js plus `<direction>.js`)

The artifact is a single deliberate theme (paper with dark bands). Keep `color-scheme: light` in both the light
and dark media blocks so the artifact contract is met and the page looks the same in dark mode.

## Fragments and modules

- A fragment is `<section id="..." class="band ...">` markup, then a `<style>`, then a `<script>` IIFE.
- **Every class and id carries the section prefix** (`hero-`, `echo-`, `stg-`). Generic names collided in TVS.
- `assets/modules/` holds proven fragments to copy and adapt (see its README): the pinned stage, the snake,
  the switchboard, the constellation map, the translator, the orbit with a fork, the teaching circle, the layers
  ladder, paper versus screen, two roads, echo cards, the drawn hero, the pictured close with portrait and contact
  card. Change the content and the drawing; keep the mechanics and the values.
- `assets/examples/` holds two complete pages: `tvs.html` (JAIN to TVS, kolam) and `coastline.html` (a fictional
  cold-chain proposal, drafting). Open one when you need to see how a whole page fits together.
- Parallel building works: write the starter, the facts sheet and all the copy yourself first, then give each
  builder agent one or two fragments with the exact copy, the pattern IDs and the prefix. Builders check their own
  fragments with `scripts/build.py --only frag-3` and `scripts/sweep.py`.

## Build, preview, publish

- `python scripts/build.py work/` joins the starter and fragments into `work/index.html` and `work/preview/index.html`.
- Preview: add a `.claude/launch.json` entry running `python -m http.server <port> --directory <work>/preview`, then
  `preview_start` it. The browser pane cannot open `file://` pages. Reload with `?v=N` after each build.
- Publish: load the artifact-design skill, then publish `work/index.html` with the Artifact tool (private by default).
  Republish to the same URL after fixes.

## Libraries

Default: none. IntersectionObserver, `position: sticky`, CSS transitions and `stroke-dashoffset` cover every pattern
in the catalogue. Opt in only when a section needs it, from cdnjs or jsDelivr at an exact version:
- GSAP 3.15.0 (all plugins free, proprietary licence): `https://cdnjs.cloudflare.com/ajax/libs/gsap/3.15.0/gsap.min.js`
  plus `ScrollTrigger.min.js`, `DrawSVGPlugin.min.js`, `MorphSVGPlugin.min.js` from the same folder, for a scrubbed
  timeline that must work in Firefox or a morph between unlike shapes. Wrap scenes in `gsap.matchMedia()` for reduced motion.
- Rough Notation 0.5.1 (`rough-notation.iife.min.js` on cdnjs) and rough.js 4.6.6 (jsDelivr `roughjs@4.6.6/bundled/rough.js`,
  fixed `seed`) when the concept is hand-drawn.
- d3 single modules from jsDelivr (`d3-shape@3.2.0`, `d3-hierarchy@3.1.2`, `d3-force@3.0.0`) for computed geometry;
  d3-geo with topojson-client only for a true map or globe.
Do not use Lenis or any smooth-scroll library, Motion, anime.js, Three.js or Splitting.js.

## Devices

Laptops and tablets are the audience. Check 1280x800, 1024x768, 768x1024 and 744x1133. Phones (short side under
540px) see the gate. Below 820px, side-by-side layouts stack; below 768px, pinned or scrubbed sequences become a
stacked static twin.

## Architectures: three ways to read the same sections

The same `main > section` fragments can be read three ways. Pick one with the story map (step 3). A shell in
`assets/architectures/` changes how the page reads; no section is rewritten.

- **Scroll** (default, no shell; `scroll.html` is only a note): one long page of colour bands. Suits most briefs.
- **Paged, the paper deck** (`paged.html`): each section is one sheet of paper on the dark ground, one at a time,
  turned with Next. Suits boards and committees who expect a deck or a document, and content that splits into a
  handful of self-contained pages.
- **Horizontal, the scroll painting** (`horizontal.html`): sections sit side by side on one track that scrolling
  unrolls sideways, with an optional ground line (a road, a river, a thread) drawing itself along the bottom.
  Suits a journey, a supply chain, a process across places or time, or one continuous motif.

**Plug one in.** Copy the shell to `work/frag-00-arch.html` so it loads first, then build as usual. Section-specific
fit rules go in `work/frag-00-fit.html`, scoped `html.arch-paged #id` or `html.hz-on #id`, never in the shell.
For the ground, define `window.CPS_GROUND = ({W, H, x, y, panels}) => svgMarkup` in a fragment: `x(u)` maps panel
units (100 per panel) to px, `y(v)` maps 0 to 100; `hz-draw` paths pen-draw with progress, `hz-guide` is the faint
construction line, anything with `data-x` lights when the line reaches it. `demo-paged.html` and
`demo-horizontal.html` show both on the Coastline sections (fit and ground fragments included).

**What to change in sections.**
- Fit one sheet or panel. At 1280x800 a sheet is about 1244x718 and a panel 1280x708 (760 tall with no ground).
  Overflow makes the shell try tighter type, a narrower column, then head beside visual (`data-cps-fit` 1 to 6).
  If nothing fits, the sheet scrolls inside itself and Next reads "More". Head beside visual is skipped when the
  visual places HTML text by %, or when a fit rule sets `--cps-split: no` on the section.
- Use builds instead of a pinned stage: in paged, elements with `data-step="1"` to `"n"` fade in one per Next before
  the page turns. Never ship the pinned stage or the switchboard with a shell: the sheet or the track is the stage
  (the pinned stage also writes `data-step`).
- Start drawings with `onView` as usual. Waiting sheets sit off screen and panels keep their real sideways
  positions, so IntersectionObserver fires when they arrive. A scroll listener that reads a section's top will not
  move on the horizontal track; use `onView`.
- Keep all content inside top-level sections, avoid `100vw` sizes, and never hide content until a `cps:` event
  arrives (scroll sends none). `data-title` on a section names it in the page bar or rail (default: its first h2).

**Events**, dispatched on the section and bubbling:
- `cps:enter` and `cps:leave` `{index, total, dir}`: a sheet became or stopped being current; in horizontal, the
  panel under the middle of the screen changed.
- `cps:step` `{step, steps}` (paged): a build changed; also sent on enter for a sheet with builds.
- `window.CPS` has `go(n)` and `index()`, plus `next()` and `prev()` on paged. Both shells replace the starter's
  `.rv` observer (paged counts the whole screen; horizontal reveals 8% in from the right).

**Reader controls.** Paged: Next and Previous bottom right, arrow keys, PageUp/PageDown, Space, Home/End, swipe,
deep links `#page-3` or `#<id>`; the wheel never turns a page, it only nudges Next. Horizontal: wheel, trackpad
(sideways too), touch, ArrowLeft/ArrowRight one panel, rail markers to jump.

**FINAL and devices.**
- `?final=1` or reduced motion: paged stacks every sheet on the ground with every build shown and no controls
  (screenshots, print-like reading); horizontal becomes the ordinary vertical page. Judge layout with `?final=1`,
  then check the live deck or track at 1280x800, 1024x768 and 768x1024.
- Paged keeps the deck on every tablet, portrait included; tall sheets scroll inside. Printing gives one sheet per page.
- Horizontal stacks vertically below 820px wide, so tablet portrait reads it as a scroll page.
- Phones get the starter's gate in all three, unless the build has a phone cut (`references/phone.md`).
