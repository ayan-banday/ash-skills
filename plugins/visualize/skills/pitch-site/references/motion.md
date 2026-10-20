# Motion: the house animation style

Built from Anthropic's claude.com code, the TVS site, a Washington Post line-drawn scrollytelling piece Ash loves
(one subject pinned while the world changes around it), and seven Awwwards sites he picked (Heron, Pier Gorelli,
Metic, Jithin, Townhouse, Blunt, Deferred Damage), filtered for clarity. Values here are exact; use them.

## Contents
- The sixteen rules
- Values to copy
- The pinned stage
- Reduced motion, FINAL, and the phone gate
- Direction motion lines
- Loops run once
- What never ships

## The sixteen rules

1. **Motion explains or it does not ship.** Every move shows what changed, what connects to what, or what comes
   next. If you cannot say its job in one sentence, keep it still.
2. **One moving thing per screen.** At most one ambient loop per screen, and it sleeps off-screen.
3. **Lines draw like a pen.** `stroke-dashoffset` from length to 0; duration = length / 600 px/s, clamped 0.6 to
   2.2s; the next stroke starts at 80 to 85% of the previous one; ease `cubic-bezier(.45,.05,.35,1)`. Lines never
   overshoot, bounce or erase themselves. Use `penDraw()` from the starter.
4. **One easing family.** Arrivals `cubic-bezier(.22,1,.36,1)`; drawing and moving between states
   `cubic-bezier(.45,.05,.35,1)`; anything tied to scroll is linear. Never back, elastic or bounce.
5. **Pace by type.** Arrivals 0.6 to 1.0s; line draws 0.8 to 2.2s; taps and UI 0.15 to 0.3s; ambient loops 3 to 7s.
   Staggers 60 to 110ms per item, the group capped at 450ms. A hero draw-on finishes within 3.5s.
6. **Text plays once; drawings may follow the scroll.** Headlines and paragraphs reveal once and always finish.
   Diagrams, paths and the one scroll-lit statement may follow scroll 1:1. Never fade out text still on screen.
7. **Picture, then headline, then detail.** Reveal travel 16px or less, blur 6px or less, scale-in 1.06 or less.
   Nothing enters from the side, rotates or flies.
8. **One stage, one knob.** To explain a process, keep one drawing on a sticky stage and let short captions scroll
   past. Each chapter changes exactly one thing. A counter (`02 / 05`) says where the reader is.
9. **Lines are the connective tissue.** Relationships start as faint construction lines (`stroke-dasharray: 3 5` at
   25 to 30% ink) and draw solid when explained. Pulses travel only on the line being discussed, 2.4s or slower.
10. **Texture is static.** Grain, powder, graphite and ink filters are applied once and never animated per frame.
11. **One accent does the pointing.** The direction's accent arrives through motion (a marker sweep, a pen circle,
    a dot, a ring) on exactly the thing being argued. Never a large animated fill.
12. **Number what the reader walks through.** Ask numbers, `n / N` counters and step numbers, only for real sequences.
13. **Never block or hijack.** No loaders, no smooth-scroll library, no snapping on reading sections, no auto-advancing
    carousels, no cursor-only effects. Pinned sections run 3 viewport heights or less. Every pinned or scrubbed
    sequence has a stacked static twin below 768px. Every hover has a tap equivalent.
14. **Respect stillness.** Under `prefers-reduced-motion` and `?final=1`, land on the finished drawing with every
    label. Content is never hidden from a reader without JS (`.js .rv` only hides when the script runs).
15. **End in the ask.** The last meaningful motion resolves into the call to action: a pen ring circles the
    recommended option, the portrait draws itself, the route arrives at the final stop.
16. **Hover snaps, never glides.** Nothing follows the pointer. Hover and tap answers appear at once and whole; a
    reveal with parts runs on stepped timing (`steps()`), like an ink stamp; words arrive whole, about 40ms apart.
    Only a move between places (a camera move, walking to a panel) eases. Ash: "I'm not a fan of how smooth it is."

## Values to copy

- Reveal (`.rv` → `.in`): opacity 0 → 1 and `translateY(12px)` → 0 over .8s `cubic-bezier(.22,1,.36,1)`, stagger with `--d`.
- Marker sweep: `background-size` 0% → 100% at 40 to 42% band height, .8s `cubic-bezier(.22,1,.36,1)`, .35s delay.
- Labels in diagrams: opacity .5s plus transform 1.1s `cubic-bezier(.19,1,.22,1)`, delay `0.08 + 0.72 × distance / max distance` from the centre (claude.com's constellation).
- Line draws in maps: `pathLength="1"`, `stroke-dasharray: 1`, dashoffset 1 → 0 over .9s.
- Hover dimming: others to opacity .22, lines to .55, .3s, only under `@media (hover: hover)`.
- Press: `scale: .96` over 150ms ease-out, never on disabled buttons.
- Scroll-linked line (the snake): `reach = clamp(0, h, innerHeight × .62 − top)`, `dashoffset = L × (1 − reach / h)`;
  read layout once per frame inside requestAnimationFrame.
- Name every transitioned property. Never `transition: all`.

## The pinned stage

The signature move from the Washington Post reference (catalogue ARC-02, SEQ-02, STR-25, STR-26, MOT-04, MOT-05).
- Stage `position: sticky; top: 10vh; height: 80vh` beside caption blocks of about 60vh; one IntersectionObserver
  with `rootMargin: "-45% 0px -45% 0px"` writes `data-step`; scrolling back undoes the step.
- The step vocabulary: an x-ray (the shell ghosts to .25 while the inside pen-draws in the accent), one hue arriving
  (a region fills with a chalky tint), labels landing inside out, a pull-back (the subject scales down onto its
  bigger world, linear with scroll), a match-cut on a shape.
- No ancestor of the sticky element may have `overflow: hidden` or `clip`. Bands use `overflow-x: clip`, so the
  stage band overrides it to `visible` and keeps its own content inside the gutter.
- Five steps at most; a second stage needs a normal reading band before it.

## Reduced motion, FINAL, and the phone gate

- `FINAL = reduce || /[?&]final=1/` in the starter. Every helper (`onView`, `prepDraw`, `penDraw`, `.rv`) lands on
  the finished state under FINAL. Screenshots use `?final=1` because hidden browser panes throttle animation frames.
- Phone gate: when the screen's short side is under 540px, show only "Open this on your laptop or tablet"
  (CSS `@media (max-width:539px), (pointer:coarse) and (max-height:499px)` plus the JS screen check, which catches a
  phone held sideways). iPads and Galaxy Tabs get the page.

## Direction motion lines

Each direction file has a **Motion** line. It sets tempo and character inside the rules above, never against them.
A loud direction (truck art, Memphis, risograph) is loud in colour, shape and type; its motion is quick, and still
never bounces, springs, rotates or jitters.

## Loops run once

An orbit dot runs one lap and stops with every step lit; a teaching circle steps through its callouts once and holds;
a map pulses only on the branch being read. The TVS review counted six things looping forever, off-screen included.
Typewriter text and per-word blur on a glossary are slow to read: set the term at once and fade the meaning in.

## What never ships

Fade-and-rise on every block as the only motion, parallax for its own sake, pulsing "live" dots, counters ticking to
numbers nobody supplied, marquees, custom cursors, a page-long line running behind the copy (Ash: "distracting from
the message"), auto-playing sequences the reader cannot pace (give progress bars that are tappable buttons).
