# 10 · Awwwards picks: animation devices worth codifying

Researched 2026-10-17. For every site I opened the Awwwards page and then the live site. I downloaded the raw HTML, CSS and JS bundles and read the motion code, and I drove the live pages in a browser where the code was obfuscated or the result needed seeing. Values come from shipped code unless they are marked **seen** (watched on screen) or **listed** (taken only from an Awwwards element title). Raw downloads are in `research/raw/` and `research/raw2/`.

**House filter used for every verdict.** Anthropic/Claude craft plus the TVS site.
- **Anthropic (read from anthropic.com CSS).** Colours are ivory `#faf9f5` / `#f0eee6` / `#e8e6dc`, slate `#141413`, clay `#d97757` and accent `#c6613f`, plus soft swatches (oat `#e3dacc`, manilla `#ebdbbc`, cactus `#bcd1ca`, heather `#cbcadb`). Its own motion is almost nothing: `.2s` colour transitions and one easeOutQuart `cubic-bezier(.165,.84,.44,1)`.
- **TVS.** A kolam that draws itself with `cubic-bezier(.45,.05,.35,1)` and a rice-powder filter, a marker sweep, slow pulses, a snake line, an orbit and a constellation map.

**Verdicts.**
- **fits:** use it, with the values tuned.
- **adapt:** use it after making the stated change.
- **reject:** leave it out, for the stated reason.

---

## A. Site by site

### A1. Heron AI: https://heronaiapp.com (Awwwards SOTD + Dev Award, Oct 12 2026; Bearplus)
- **What it is.** A landing page for an AI agent that sits inside architects' design tools, watches the model, flags code violations and edits after approval.
- **Stack.** Webflow, GSAP 3.12.5 with ScrollTrigger, SplitText and TextPlugin, Lenis 1.1.5, Barba and Canvas. The bundle is obfuscated.
- **Ash likely loves:** an architect's elevation drawing that inks itself line by line and then becomes a hatched pencil rendering on warm paper, with one orange accent marking every problem.
- **Move 1. Blueprint loader that draws itself.**
  - Every SVG line in the building elevation is set to `strokeDasharray = getTotalLength()` and then animated to `strokeDashoffset: 0` over **1.3s** each, with `stagger: {amount: 3, from: "start"}`. The whole drawing takes about 4.3s.
  - At the same time, the spec-sheet lines rise (opacity plus yPercent, **0.5s, stagger .02**). A counter runs 0→60 over **3s** and then 60→100 over **2.5s**, and an orange horizontal scan line travels down.
  - A `clipPath` inset then opens onto the hero. A `sessionStorage` "isLoaded" flag skips the loader on later visits.
  - **Verdict: adapt.** The self-drawing line elevation is the kolam draw-on in another dress. Drop the loader gate and the percentage counter, and draw the picture in place as the hero, at 3s or less and once per session. → *Blueprint that inks itself*
- **Move 2. Ink-bleed mask reveal.**
  - An SVG `<mask>` path has a soft curved edge, `M0 1 Q500 2 1000 1 L1000 0 L0 0Z`. The filter chain is `feTurbulence fractalNoise baseFrequency "0.045 0.055" numOctaves 4 seed 5` → `feDisplacementMap scale 100` → `feGaussianBlur 1.8` → `feFuncA linear slope 2.2 intercept -0.6`, so the edge looks like ink soaking into paper.
  - The path morphs to `M0 1000 Q500 1250 1000 1000…` (full cover), scrubbed between `data-start="35"` and `data-end="55"` of the section's scroll. It uncovers a second image laid over the first (sketch → render).
  - **Verdict: fits.** This is rice-powder or ink texture used for a reveal, with one per page at most. → *Ink-bleed reveal*
- **Move 3. Numbered problem cards.**
  - The cards are labelled `[01] Manual`, `[02] Disjointed`, `[03] Blind` and `[04] Slow`. Each has a mono label, a dashed hairline and a dot, plus an isometric line icon whose paths carry `class="…-draw"` and draw on.
  - The connectors use a dash-dot "construction" pattern, `stroke-dasharray="0.93 2.8 9.35 2.8"`, in `#B3B3AF`.
  - **Verdict: fits.** The dash-dot construction line is a lovely upgrade on the TVS dotted base line. → *Numbered cards on a construction line*
- **Move 4. Sticky steps with callouts on the drawing.**
  - Four steps (Observe, Advise, Act, Learn) pair a hatched illustration with a sticky title. Small black code-violation tags pop onto the drawing, and the steps are separated by a brand-coloured hairline.
  - Headings use a per-character colour sweep: SplitText chars run through `keyframes {color:[from, mid, to]}`, `easeEach "power2.in"`, **0.8–1s, stagger .03–.08**. Highlighted words land on `#FF6B30`.
  - **Verdict: adapt.** The sticky step plus callouts fit. The per-character colour sweep is too busy, so ink whole words in once instead. → *Sticky steps with callouts on the drawing*, *Scroll-lit statement*
- **Move 5. Drag to see violations.** A drag lens over the hero drawing reveals the code problems.
  - **Verdict: adapt.** On tablets dragging fights scroll, so make it a tap toggle. → *Show-the-workings toggle*

### A2. Townhouse: https://townhouse.dev (Nominee, Oct 13 2026; fela)
- **What it is.** A dev tool that reads your code and draws it as a living town: screens are houses, services are towers and routes are pipes.
- **Stack.** React, Three.js/WebGL and painted illustration.
- **Ash likely loves:** a whole technical system turned into a small painted village where you can see at a glance what is healthy, what is broken and what flows where.
- **Move 1. A system drawn as a place.**
  - An isometric town has labelled districts (SCREENS, SERVICES, ROUTES, PROVIDERS, TABLES) and a hint saying the town is live: hover a building, then click to open it. Red tags such as "LEADS NOWHERE" and "MISSING" sit on the map.
  - **Verdict: adapt.** The metaphor is the gift, not the 3D. Draw it as a flat, hand-drawn SVG village or map with labelled zones and tap-to-open cards. → *System drawn as a village*
- **Move 2. Flow along pipes.**
  - Map edges are dashed (`stroke-dasharray: 5 6`) and march with `@keyframes map-flow {to {stroke-dashoffset: -18px}}`: **0.9s linear infinite** for busy flow, **2.4s** for slow flow and **1.6s** for power lines.
  - A broken node pulses a halo ring (box-shadow 6→8px at 12→24% colour mix) over **2s ease-in-out infinite**. A one-time shock ring scales 1→1.18 and fades over **0.7s**.
  - **Verdict: adapt.** Use slow marching (2.4s or more) only on the line being discussed, and play the shock ring once, never on loop. → *Marching dashes on the live line*, *One-time alarm ring*
- **Move 3. Ambient life.**
  - CSS loops run throughout: `hub-breathe` 3.2s (translateY −2px, scale 1.015), `lane-bob` 3.2–4s, `lane-sway` ±5° over 2.8–4.2s, `lane-puff` smoke 2.8s, `lane-cloud` 7s linear and `lane-window` 1.8s.
  - **Verdict: adapt.** Allow one breathing element per screen at 1.5% scale or less, keep everything else still, and pause it off-screen. → *One breathing detail*
- **Move 4. Numbered chapters.**
  - **Seen:** huge pixel numerals ("02", "03"), a thin vertical progress bar, and a right-hand chapter list with the current one highlighted (Your app, Limits, Fixes, Anywhere, Your model, Security, Growth, Start).
  - Painted backdrops crossfade per chapter, with one UI card over each painting (for example, a storage meter at 17%, "full in about three days").
  - Hero lines reveal through `clip-path: inset(-.3em -.2em calc(100% + .3em))` → `inset(-.3em -.2em)`. Tokens: `--ease-out: cubic-bezier(.2,0,0,1)`, `--duration-slow: .32s`.
  - **Verdict: fits** for the chapter rail. Adapt the numerals to serif or hand-lettered ones. → *Chapter rail with big numerals*, *Hero lines rise from their masks*
- **Move 5. Painted story preloader** (an inventor and a gnome, a kitchen of gnomes).
  - **Verdict: reject.** It is a story gate in front of the content, and proposal readers need the point at once.

### A3. Deferred Damage: http://plastic-ocean.com (Nominee, Oct 15 2026; Nikolai Kudriavtsev, Natalia Pugacheva, Uprock)
- **What it is.** A two-minute scroll story of one PET bottle breaking down in the ocean over centuries.
- **Stack.** Taptop builder, GSAP 3.12.2 with ScrollTrigger, Lenis 1.0.23 (`lerp .1`) and plain rAF scripts.
- **Ash likely loves:** one object carries the whole argument, and scrolling literally means time passing and depth growing. Their case note puts it plainly: "The vertical scroll acts as a timeline."
- **Move 1. One object, scroll as time.** **Seen:** a fixed bottle that sinks and degrades (new, crumpled, fragmenting) while a left label shows the time band (0–5, 5–20, 20–100 and 100–450 years) and the right shows one fact per band.
  - **Verdict: fits.** In house style the object is a line drawing that changes state per band. → *One object, scroll as time*
- **Move 2. Scroll-scrubbed counter.** `[data-scroll-counter]` maps the viewport middle as it travels between a start marker and an end marker to `from → to`, with `Math.round` and `toLocaleString('en-US')`. It moves 1:1 with scroll, inside rAF throttling (for example "10,000" metres deep).
  - **Verdict: fits.** → *Scroll-scrubbed gauge number*
- **Move 3. Bottle-shaped portal.**
  - The bottle SVG is used as a CSS `mask-image` on a sticky 100vh layer. `mask-size` runs 0→**88.5vh** over 0.9 screen heights (cubic in-out), holds for 0.2 screens, then runs 88.5→**2000vh** over 1.1 screens, so you fly through the bottle into the next scene.
  - The footer reuses the trick with a circle mask, 0→400vh, smoothed with `1 − exp(−dt/0.2)`.
  - **Verdict: adapt.** Use one hand-drawn portal shape once per page, end at the frame size (no 2000vh rush), and skip it on narrow screens. → *Shape portal into the detail*
- **Move 4. Blur-to-focus statements.** Opacity and `filter: blur()` run from 16px to 0 over the first 25% of a scroll window, hold until 70%, then fade over the last 30%. Blur is disabled at 991px and below.
  - A second "word reveal" splits letters from 10% to 100% opacity: **250ms per letter, 80ms word stagger, 25ms letter stagger**, ease-out cubic.
  - **Verdict: adapt.** Focus in only (never fade text out while it is being read), use 6px blur at most, and animate words, not letters. → *Blur-to-sharp headline*
- **Move 5. Shared-frame split.** **Seen:** a bottle above the waterline and a fish below, in one frame, for the "outweigh fish" fact.
  - **Verdict: fits.** → *Shared-frame split*
- **Move 6. Inverted text clipping.** Dark copy is clipped every frame to the bottle's rect over light copy.
  - **Verdict: reject.** It costs a rAF loop forever and adds no meaning.

### A4. Jithin RP portfolio: https://jithinrp.com (Nominee, Oct 17 2026)
- **What it is.** A senior product designer's portfolio with liquid WebGL, sound and a draw-a-Z entry.
- **Stack.** GSAP with ScrollTrigger and SplitText, Lenis `{lerp: .09}`, Three.js and GLSL. The code is unminified and heavily commented.
- **Ash likely loves:** everything feels handmade and alive: a signature that writes itself, hairlines that draw, ink filling a pen line. The code comments read like a craftsman's notebook.
- **Move 1. Signature writes itself at pen speed.**
  - Each path's duration is `1.9s × length/totalLength`, and the next stroke starts at **82%** of the previous one (the pen never quite lifts), using `power1.inOut`.
  - Ink fill then fades in over **0.5s** `power2.out` and the pen outline dissolves (0.4s). Hover replays at 1.5×.
  - **Verdict: fits.** This is the best hand-drawn timing rule found. → *Pen-speed draw-on*
- **Move 2. Hairlines draw.** Horizontal rules use `scaleX(var(--draw))` with `--draw` 0→1 over **1.6s expo.inOut**, once, at `bottom 95%`. Vertical dividers grow over **1.4s expo.inOut** at `top 90%`.
  - **Verdict: fits.** → *Ledger rules that draw in*
- **Move 3. Picture first, then words, then details.**
  - Media lands from scale 1.3→1 over **1.5s power3.inOut** (fade 0.7s). Title lines rise from masks (`yPercent 105→0`, **0.9s expo.out, stagger .06**), paragraph lines follow (stagger .035), then fact chips (`y 28→0`, 0.8s power3.out, stagger .06).
  - Leaving plays the same path back at 1.8× (his comment calls this spatial consistency). Generic reveals use `y 40→0`, **1.2s expo.out, stagger .08** at `top 88%`, once.
  - **Verdict: fits.** Keep the order, but scale only 1.06→1. → *Picture, then headline, then details*
- **Move 4. Liquid headings, "ball lens" page warp, scroll lean** (skewY up to ±3.2° from scroll velocity, spring 55/10), water shader, draw-a-Z gate and hold-to-burst.
  - **Verdict: reject.** Motion driven by scroll speed and liquid distortion is the opposite of calm, and gates block readers.
  - His own rule is worth keeping: headings are *played, not scrubbed*, so a fast flick cannot strand a line half-animated. → Rule D6

### A5. Pier Gorelli: https://piergorelli.com (Nominee, Oct 16 2026)
- **What it is.** A developer portfolio that turns technical work into maps, plotting and blueprint drawings.
- **Stack.** Astro 7, GSAP and Lenis (`duration 1.15`, easing `1.001 − 2^(−10t)`), a WebGL contour hero (a shader of about 2KB) and native View Transitions. Reading pages ship about 8KB of JS; showcase pages ship about 63KB.
- **Ash likely loves:** work explained as a drawing being plotted: construction lines first, then the build, then the live thing, all on a blueprint grid with rulers.
- **Move 1. Plot → Build → Live stage** (`work-stage.js`; pinned at ≥1024×600). Each project is a timeline of four units, scrubbed:
  - **Plot:** construction strokes draw (`pathLength="1"`, dashoffset 1→0, **0.75 each, stagger 0.3/n, power2.inOut**) and labels fade in (0.45). At 0.9 the blueprint dims to **0.2**.
  - **Build:** real strokes draw (0.7, stagger .1), blocks grow (SVG `width` 0→w, 0.9), wipes run (`scaleX` 0.6) and labels type on with a ▌ cursor (0.6s).
  - **Live (at 2.0):** a clip widens 0→800 while a scan line sweeps x 0→800 (**0.9 power3.inOut**).
  - Between projects, old text fades up 24px (0.6 power2.in) and the art scales to .97 (0.7). A bottom tab bar (Plot, Build, Live) fills under the active tab, beside an `01 / 03` counter.
  - **Verdict: fits.** This is the strongest proposal device in the set: idea sketch, then plan, then result, on one canvas. → *Plot, build, live stage*
- **Move 2. Charts that plot on scroll** (`[data-plot]`).
  - `pathLength="1"` strokes scrub from `top 85%` to `bottom 60%` with stagger `min(.12, .9/n)`. Solid paths fill 0→1. Dots scale 0→1 with `back.out(3)`, bars run `scaleX` 0→1, and labels fade in last.
  - **Verdict: adapt.** Replace `back.out(3)` with a no-overshoot ease. → *Chart that plots as you scroll*
- **Move 3. Reading ruler in the header, with no JavaScript.**
  - CSS `animation-timeline: scroll(root)` drives everything:
    - `hd-compact` over 0–160px;
    - `hd-band` over 0–80px;
    - the rule draws by `clip-path: inset(0 100% -1.5rem 0)` → full over 40–280px;
    - a tag shows `counter(pct, decimal-leading-zero) "%"` from `@property --pct {syntax:"<integer>"}`.
  - Number tiles count down 9→0 with `animation-timeline: view()` and `animation-range: entry calc(var(--i)*15%) entry calc(70% + var(--i)*15%)`. Everything sits inside `@supports`.
  - **Verdict: fits.** → *Reading ruler in the header*, *Scroll-scrubbed gauge number*
- **Move 4. Outline words fill with ink** (`[data-wireframe]`).
  - Each word sits as an outline, and a solid copy wipes in with `clip-path: inset(-0.35em 100% -0.45em 0)` → `inset(… 0% …)`, **stagger 0.6**, scrubbed from `top 65%` to `bottom 60%`. Margin notes dim to .15.
  - **Seen:** used on the home page's two-line statement about keeping the idea and removing what blocks it.
  - **Verdict: fits.** → *Outline words that fill with ink*
- Other reveals use `[data-reveal="lines"] yPercent 110` (1.1s expo.out, stagger .07, at `top 85%`, once) and `[data-reveal="up"] y 48` (1.3s power3.out, stagger .09). Rules use `[data-draw] scaleX` scrubbed from `top 90%` to `top 45%` with `power4.inOut`.
  - CSS tokens: `--dur-1 .4s`, `--dur-2 .8s`, `--dur-3 1.2s`; `--ease-out cubic-bezier(.25,1,.5,1)`; `--ease-in-out cubic-bezier(.76,0,.24,1)`.
- **Move 5. Blueprint cursor, ⌥G grid, ⌘K palette, monogram page transitions.**
  - **Verdict: reject.** These are desktop toys, and a single-page proposal has no page transitions.

### A6. metic. "Take a closer look": https://metic.studio/en (Nominee, Oct 10 2026)
- **What it is.** A one-person Austrian design and code studio. The palette is paper, ink and one red.
- **Stack.** Next.js and Three.js, with CSS-heavy motion.
- **Ash likely loves:** the craft explained as a drawing that builds up step by step on warm paper (a line, a grid, a layout, type, colour, code), ending in the very button you press.
- **Move 1. Build-up that ends in the button.** **Seen:**
  - A pinned stage titled "From a line to a button" runs **eight steps** (01/08 … 08/08), each adding to the same drawing, with a "Build progress 000 %" counter.
  - The final step collapses everything into one CTA with dimension guides (`button · 186 × 56`). The page's line for this moment is roughly: everything you just saw is inside this one button.
  - **Verdict: fits.** This is the best ending found for a proposal. → *Build-up that ends in the button*
- **Move 2. Assemble with construction guides** (`[data-assemble].is-built`).
  - Crosshair guides grow (`cx-h` `scale 0 1 → 1` by 38% of **1.7s**, then fade; the vertical starts **+90ms** later). Labels show the dimensions and fade (1.9s).
  - The content then rises from `blur(4px)` and `0.9rem` after a delay of `.52–.64s`. The house ease is `--ease-lens: cubic-bezier(.23,1,.32,1)`.
  - **Verdict: fits.** → *Assemble with construction guides*
- **Move 3. Boxes and chips draw their own borders.**
  - `box-draw` grows four 1px background gradients (`background-size 0 1px, 1px 0…` → `100% 1px…`) over **0.9s**, in ink until 75% and then settling to the line colour. `chip-draw` wipes a pill with `clip-path inset(0 100% 0 0 round 999px)` over 0.7s.
  - A stamp lands at `rotate(-24deg) scale(1.8)` → `rotate(-11deg) scale(1)` over **0.55s**.
  - **Verdict:** box and chip draws **fit**. The stamp needs **adapt**: no overshoot, starting at `rotate(-14deg) scale(1.15)`. → *Boxes that draw their own border*, *Approval stamp*
- **Move 4. X-ray (hold to see how the page is built), a 3D loupe that magnifies the real page, and 15 hidden finds ending in ink fireworks.**
  - **Verdict:** X-ray **adapt** as a plain toggle. Loupe and Easter eggs **reject** (play over clarity). → *Show-the-workings toggle*
- Exits use a view timeline, `animation-range: exit 20%`, that fades blocks out as they leave the top. A left-edge ruler runs the full page height.

### A7. BLUNT Umbrellas: https://bluntumbrellas.com (Nominee, Oct 9 2026; Studio Almond)
- **What it is.** An e-commerce site for an engineered umbrella.
- **Stack.** Shopify, GSAP 3.12.2 with ScrollTrigger, and a canvas image sequence.
- **Ash likely loves:** an engineering line drawing of the umbrella that becomes the real product, with "+" markers that explain each clever part.
- **Move 1. Line drawing becomes the product, stop by stop.**
  - **Seen:** a technical line drawing sits behind the headline. Then a pinned scene, `end: "+=" + 3*innerHeight`, `scrub: .5`, `snap: {snapTo: "labelsDirectional", inertia: true}`, runs as follows:
    1. Intro text goes `yPercent 100→0→−100` (0.75 each).
    2. The canvas opens with `clipPath: inset(0%)` (1.5 units).
    3. A preloaded frame sequence plays (`frame 0→n−1, snap: "frame"`, 3 units).
    4. The labels layer fades in.
  - **Verdict: adapt.** Image sequences are heavy. Use one SVG line drawing whose fills and details fade in per stop, and keep snapping only inside this one pinned scene. → *Line drawing that fills in, stop by stop*
- **Move 2. "+" hotspots.** **Seen:** markers on Tip, Canopy and Frame open short panels (`[data-popup-trigger]` toggles `.active`).
  - **Verdict: fits.** → *Plus-marker part labels*
- **Move 3. Hero letters drop in with `elastic.out(1,0.9)` over 1.8s (stagger .05), plus archive tiles that rotate up to 45° toward the cursor.**
  - **Verdict: reject.** Bouncy and cursor-driven.

### A8. Fox Valuations: https://foxvaluations.com.au (category pick; Nominee, Oct 15 2026; Black Shard)
- **What it is.** An independent property valuer in Brisbane.
- **Stack.** Hand-written vanilla CSS and JS.
- **Ash likely loves:** a pencil-sketch living room that draws itself with a fox curling up asleep on the couch, and a site that otherwise refuses to move. The main.js header comment states the rule outright: motion is reserved for the report's own grammar (lines rising from masks, ledger rules drawing in), and nothing else moves.
- **Move 1. Sketch hero that draws itself.**
  - Three videos play in sequence: the fox runs, then the interior pencil sketch draws itself, then the fox curls up. The title is revealed when the curl passes 55%.
  - It plays once per session (`sessionStorage foxseq`). Reduced motion and repeat visits land on the finished sketch, and a Skip button is provided.
  - **Verdict: adapt.** Build it with SVG stroke draw-on instead of video, and keep "once per session, land on the finished drawing". → *Blueprint that inks itself*
- **Move 2. Ledger rows.**
  - Each row's hairline (`::after`) runs `scaleX 0→1` over **0.8s `cubic-bezier(0.22,1,0.36,1)`** with `--row-delay: min(i×90ms, 450ms)`. Row text fades in **0.7s**, 0.15s after its rule. The observer uses `rootMargin "0px 0px 12% 0px"`.
  - An underline under the phone number draws in 0.8s after 0.15s, and blocks fade up 10px (0.8s, +0.3s).
  - **Verdict: fits.** → *Ledger rules that draw in*
- **Move 3. A sleeping fox that breathes.** The body scales `(1.004, 1.013)` on a **4.7s** ease-in-out loop, and the ears twitch (`scaleY .89` at 4.8%) every **9.3s**.
  - **Verdict: fits** as the page's single ambient detail. → *One breathing detail*

### A9. Chladni · A Geometry of Sound: http://chladni-plate-experiment.vercel.app (category pick; Nominee, Oct 10 2026)
- **What it is.** A seven-chapter science explainer on how sound draws figures in sand on a vibrating plate.
- **Stack.** Next.js, Three.js and GSAP 3.15.
- **Ash likely loves:** one plate stays on stage while each chapter turns exactly one knob, and sand gathering into crisp lines looks like rice-powder kolam.
- **Move 1. Fixed stage, one knob per chapter.**
  - Each chapter (`01 / 07` … `07 / 07`) sets a scene on enter (start → `bottom 40%`). Its scroll progress then scrubs a single parameter:
    - drive frequency, log-lerped **250→2600 Hz**;
    - grain bounciness, **0.45→1.7**;
    - drive point, lerped across the plate;
    - camera drift.
  - Values ease toward their targets over **0.3s** (`SCENE_DUR.follow`). `SCRUB = .8`.
  - Tokens: `DUR {micro .15, ui .3, reveal .7, signature 1.4}`, `EASE {out expo.out, inOut power3.inOut, brand cubic(.16,1,.3,1), breathe sine.inOut}`, `STAGGER .045`. Text rises 24px over 0.7s at `top 88%`, once.
  - **Verdict: fits.** → *Fixed stage, one knob per chapter*
- **Move 2. Drive steps.** Chapter progress steps through four discrete figures that morph into one another without snapping.
  - **Verdict: fits** (it is part of the entry above).
- **Move 3. Sand grains settle onto still lines** (a WebGL particle simulation).
  - **Verdict: adapt.** Use Canvas 2D with 2–4k grains that random-walk and settle onto a kolam or diagram path. → *Grains settle into the line*

### A10. Neutomni: https://neutomni.com (category pick; SOTD + Dev Award, Oct 13 2026)
- **What it is.** A Polish brand and web studio, editorial and retro.
- **Stack.** Webflow, GSAP 3.15 (MorphSVG, ScrollTrigger, SplitText, Observer) and Lenis 1.3.21.
- **Ash likely loves:** the process drawn as a square wheel rolling along a road of arches, gaining sides at every step until it is a perfect circle.
- **Move 1. Rolling shape** (sticky canvas `#pw-canvas`; Awwwards **listed** it as "Process Animation").
  - A polygon rolls left to right over a road of **catenary arches**. The road's shape keeps the axle level, and a dashed axle guide (`setLineDash([5,10])`) shows it.
  - Over the first 30% of the morph the sides go **4→12**. After that the shape rounds into a circle while the road flattens.
  - Lines are 1.5px with round joins. Progress uses `lerp(progress, target, 0.2)` per frame, the curve is smoothstep `t²(3−2t)`, and reduced motion jumps straight to the target.
  - **Verdict: fits.** It is line-only, scroll-linked, one moving thing, and the metaphor reads clearly (a rough start becomes smooth). → *Square wheel that rounds as it rolls*
- **Move 2. Snapping portfolio slides.**
  - Each image reveals by clip-path (**0.9s power2.inOut**) while the previous one scales and dims. The rule: snap forward once 10% in, snap back if under 90%, 90ms after scrolling stops, over 0.45–0.65s power1.inOut.
  - **Verdict: adapt.** Snapping fights trackpads, so use buttons inside one rail. → *Numbered rail with step buttons*
- **Move 3. Blur reveal and logo paths.** The blur reveal runs **0.4s power1.out, stagger .12** at `top 85%`. Logo paths animate over 2s with `stagger {each .05, from "center"}`.
  - **Verdict: fits** (keep blur at 4px or less). → *Blur-to-sharp headline*

### A11. Wafer: https://www.wafer.ai (category pick; Nominee, Oct 14 2026)
- **What it is.** An AI inference platform whose service "keeps getting better" over time.
- **Stack.** Astro, with native SVG and CSS animation.
- **Ash likely loves:** one performance curve sweeps in and is annotated at three moments, so the whole pitch reads as one line: engine tuned 230 tok/s, kernels fused 315, traffic re-tuned 400.
- **Move 1. Feathered chart sweep.**
  - The line-and-area SVG sits under `mask-image: linear-gradient(to right, #000 0, #000 50%, transparent calc(50% + 7%))` with `mask-size: 200% 100%`.
  - `mask-position` transitions over **3s ease-in-out** (`--chart-draw-ms`), so the line appears left to right with a soft edge instead of a crisp dash.
  - **Verdict: fits.** → *Feathered line sweep with milestone pins*
- **Move 2. Milestone pins.** Markers fade in and rise 4px over **0.48s ease-out**, at **0.9s + i×0.62s**. Each hangs on a dashed tie line (gradient dashes 13px on, 20px off), with a small caption and a mono value.
  - **Verdict: fits** (it is part of the entry above).
- **Move 3. Native-motion controller.** `getAnimations()` and `svg.pauseAnimations()` pause loops when an IntersectionObserver says the element is off-screen. Under reduced motion they are cancelled; otherwise they resume from the saved time.
  - **Verdict: fits** (utility). → *Loops that sleep off-screen*
- **Move 4. Auto-rotating quote deck** (every 6000ms, stacked plates).
  - **Verdict: adapt.** No auto-rotation; the reader steps. → *Number-first proof card*

### A12. Roveia Health: https://www.roveia.com (category pick; Nominee, Oct 11 2026)
- **What it is.** A growth agency for health brands, with a calm clinical-white site.
- **Stack.** Webflow, GSAP 3.15 and Lenis 1.3.11 (`duration 1.2`).
- **Ash likely loves:** the calm and the focus. The hero picture grows out of a slot in the headline into the full frame, and a long client list lights one name at a time.
- **Move 1. Slot grows to full frame.** The hero is pinned for **1.1 viewport heights** with `scrub: 1`. The video's left, top, width and height tween from the slot's measured rect to the container, an overlay goes to 0.75 black, and the text turns white at 0.1.
  - **Verdict: adapt.** Grow a framed drawing, not a video, to say "now we zoom in". → *Thumbnail grows into the stage*
- **Move 2. Focus wheel list.**
  - The section is pinned for `(n−1)×300px` with `scrub: 0.1` and `snap: 1/(n−1)`. The list translates so the active item sits in the middle. Opacity falls off by distance: 1 / .5 / .25 / .1 / .05.
  - Matching background and content crossfade over **0.4s** when progress is within 0.15 of an index.
  - **Verdict: fits** (keep it short: 5–9 items). → *Focus wheel list*
- **Move 3. Horizontal service cards** (pinned, `scrub: 1`).
  - **Verdict: adapt.** Use buttons and a rail; sideways scroll hides content. → *Numbered rail with step buttons*
- **Move 4. Gradient wave footer.**
  - Three SVG Catmull-Rom layers each sum two sines per anchor (`0.62·sin(a) + 0.38·sin(b)`) at speeds .5, .6 and .7 and opacities .6, .75 and 1. They are paused off-screen and static under reduced motion.
  - **Verdict: adapt.** Keep one slow chalk-tinted line as a horizon behind the CTA. → *Chalk horizon wave*
- **Move 5. Testimonial cards fly in from the right, rotated 10°, and exit left.**
  - **Verdict: reject.** Whooshy.
- The "orbital service navigation" in the Awwwards blurb is not in the home page code, so it is not verified.

### A13. AI COMMON: https://aicommon.creamu.co.jp (category pick; Nominee, Oct 14 2026; creamu)
- **What it is.** An AI advisory service for company presidents, with warm tones and editorial Japanese type.
- **Stack.** Vanilla JS, Lenis and a WebGL sphere.
- **Ash likely loves:** the restraint. Only the first screen gets a line-by-line reveal; everything else simply fades up once, and the day-in-the-life row tells the story in times of day.
- **Move 1. Measured line reveal.**
  - The script measures the real visible line breaks (from each character's rect) and wraps each line in `.ln > .ln__in`. Lines rise from `translate3d(0, calc(100% + .3em), 0)` over **1.25s `cubic-bezier(.2,.75,.1,1)`**, with **110ms per line** (90ms in the title). The hero is the only place this runs.
  - Lines are re-split on resize and when fonts load.
  - **Verdict: fits.** → *Hero lines rise from their masks*
- **Move 2. One-shot fade-up for everything else.**
  - Elements go from opacity 0 and `translateY(16px)` to rest over **1s `cubic-bezier(.22,.61,.36,1)`**, with observer `rootMargin "0px 0px -6% 0px"`, unobserved after the first show.
  - Photos use the same reveal (a code comment says there is no competing scroll transform).
  - **Verdict: fits.** → *One-shot fade-up*
- **Move 3. Day-in-the-life row.** Four times of day (06:00, 08:30, 14:00 …) sit on one 1px hairline across a four-column grid.
  - **Verdict: fits.** → *Day-in-the-life hairline*
- **Move 4. Logo mark spins** (`rotateY` one turn every 12s, resting for 75% of the cycle).
  - **Verdict: reject.** It is ambient motion in the corner of the eye.

### A14. fps ecosystem: https://www.fps.hu (category pick; Nominee, Oct 10 2026)
- **What it is.** A Hungarian digital product agency.
- **Stack.** Angular, GSAP and Lottie.
- **Ash likely loves:** pixel precision with hand-drawn gestures. A pen loop circles the key word in the hero, the way you would circle it on paper.
- **Move 1. Pen circle around a word.** `line-anim.json` is 544×178 at 24fps, and its trim-path start runs 100→0 from frame 12 to frame 33. That means a **0.5s delay and about 0.9s of drawing** with default Lottie ease (0.167/0.833), a 2px stroke, playing once.
  - **Verdict: fits** (build it in SVG, no Lottie). → *Pen circle around a word*
- **Move 2. Letters rise.** Letters rise 20px over **0.4s ease**, with **30ms per letter** offset per word.
  - **Verdict: adapt.** Animate whole words or lines. → *Hero lines rise from their masks*
- **Move 3. Tap-to-cycle collage.** A click steps through four states (`state-0…3`), and boxes with eye, pencil, glass and bulb GIFs rearrange with `transition: all .6s linear`.
  - **Verdict: adapt.** Use line icons and ease-out. → *Tap to cycle four views*

### A15. Concrete: https://www.concretemanagement.fr (category pick; Nominee, Oct 13 2026)
- **What it is.** A Paris real-estate management firm.
- **Stack.** Webflow with a Vite bundle, GSAP 3.14, Lenis and Swup.
- **Ash likely loves:** a calm first screen that asks whether you are an owner or a tenant, and a before/after slider that proves a renovation in one drag.
- **Move 1. Choice screen.** Two buttons route the reader: I am an owner / I am a tenant.
  - **Verdict: fits.** → *Who-are-you doors*
- **Move 2. Before/after splitter.** A draggable handle sets `clip-path: inset(0 0 0 X%)` on the "after" image, starting at 50%.
  - **Verdict: fits.** → *Drag splitter before/after*
- **Move 3. Stacking cards.**
  - The section is pinned at `height: 500svh`. Cards stack with a `y` offset of 10px×n and `z` depth, and each lifts off as the scroll reaches its slot. The title drops in from `y: -innerHeight` and the cards rise from `yPercent 100` with `power4.out`.
  - **Verdict: adapt.** Use 3–5 equal items and no 3D depth. → *Stacking cards*
- **Move 4. Step numbers slide.** Step numerals slide `yPercent −150→0` while content slides `xPercent 20→0`, scrubbed with `power4.out`.
  - **Verdict: fits** (reduce the travel). → *Step numbers that slide into place*
  - The intro (logo halves split, centre clip opens over 2.4s expo.inOut) is a **reject**: a gate.

### A16. Twain: https://twain.ai (category pick; Nominee, Oct 14 2026)
- **What it is.** An AI outbound-email platform.
- **Stack.** React and Three.js (paper plane and paper bin GLB models).
- **Ash likely loves:** a pain statement you read by scrolling, words turning from grey to ink and then a marker stroke dragged across the last words, while a paper plane carries the story.
- **Move 1. Scroll-read paragraph.** Each word's colour interpolates from the "unread" grey to ink as scroll passes, over a rolling window of **3 words**, quantised to **0.02** steps to save repaints.
  - **Verdict: fits.** → *Scroll-lit statement*
- **Move 2. Procedural marker strokes.**
  - For the last three words, the script measures each rendered line's rect and builds one cubic path per line, with a seeded **±10% of line-height** wobble at four points. Stroke width is **72% of line height** at opacity **.72**.
  - Lines draw one after another by dashoffset, in proportion to scroll.
  - **Verdict: fits.** This is the marker sweep that hugs real line breaks. → *Marker stroke that hugs the line breaks*
- **Move 3. Paper plane and shatter.**
  - A paper plane flies through (Three.js). Title letters "shatter" with random `dx 15–60`, `dy 60–190`, `rotation ±40°`, `scale → .15`.
  - **Verdict:** plane **adapt** as a 2D line plane on a dashed route. Shatter **reject**. → *Paper plane on a dashed route*
- **Move 4. Proof cards.** The big metric leads ("12% positive", "25 minutes" against six hours), with the quote on the back. The cards flip and dissolve.
  - **Verdict: adapt.** Lead with the number, reveal the quote below on tap, and skip the 3D flip. → *Number-first proof card*

### A17. Pigeon's Mission: https://pigeonsmission.com (category pick; Nominee, Oct 7 2026)
- **What it is.** A pixel platformer drawn by a six-year-old and built with his dad.
- **Stack.** React design-system bundle and CSS keyframes.
- **Ash likely loves:** a child's sketchbook becoming a finished game, told as a numbered rail that runs from the idea to the cast coming to life, plus a world map of levels.
- **Move 1. Sketch-to-final story rail.**
  - Six numbered cards (1, the idea … 6, the cast comes to life) drift as a marquee at **0.045px/ms (45px/s)**, pausing **2.5s** on touch or wheel. The first deliberate drag stops the drift and turns on snapping.
  - Prev/next buttons snap to real card offsets in **450ms** with ease-out cubic.
  - **Verdict: adapt.** No auto-drift (readers lose their place). Keep the numbered rail, buttons and snapping. → *Numbered rail with step buttons*
- **Move 2. Parallax sky.** Layers travel up to 30px (clouds), 40px (hills) and 25px (middle) across the section.
  - **Verdict: adapt.** Two layers at 16px or less, in chalk tints. → *Two-layer paper parallax*
- **Move 3. World map with a level list** (**listed** and **seen** in copy: seven worlds, eight bosses).
  - **Verdict: fits** as a roadmap. → *Level map roadmap*
  - The running-character footer loops (`pm-drift` at 2880px and 3456px) are a **reject**.
- **Move 4. Loader.** It holds for at least 3.3s, once per session.
  - **Verdict: reject.**

---

## B. Common threads

1. **A persistent stage carries the story.** Nine of seventeen sites keep one object or canvas fixed while short chapters scroll past: the bottle (Deferred Damage), the plate (Chladni), the build drawing (Metic), the work stage (Pier), the wheel (Neutomni), the town (Townhouse), the umbrella (BLUNT), the sticky steps (Heron) and the hero slot (Roveia). Pins run **1.1 to 5 viewport heights** (Roveia 1.1vh, BLUNT 3vh, Concrete 500svh). The best ones change **one thing per chapter**.
2. **They speak in technical-drawing vocabulary.** Construction lines (dash-dot `0.93 2.8 9.35 2.8` at Heron, `[5,10]` at Neutomni), crosshair guides that grow and then fade (Metic, 1.7s), dimension labels (`186 × 56`), rulers (Pier's header, Metic's left edge), `+` hotspots (BLUNT) and ledger hairlines (Fox). It reads as "someone measured this", which is the proof-trust note a proposal needs.
3. **Lines are drawn, not faded.** `strokeDasharray = length` then `strokeDashoffset → 0` is everywhere (Heron, Pier with `pathLength="1"`, Metic, Jithin, Fox's sketch, TVS). Durations sit between **0.7 and 1.6s per stroke**. Jithin ties duration to path length (1.9s per signature, 82% overlap). Rules use `scaleX` over **0.8s** (Fox) to **1.6s** (Jithin).
4. **The easing family is narrow.**
   - **Arrivals** use a long ease-out: `expo.out`; `cubic-bezier(.22,1,.36,1)` (Fox, Townhouse); `(.23,1,.32,1)` (Metic); `(.16,1,.3,1)` (Chladni); `(.2,.75,.1,1)` (AI COMMON); `(.25,1,.5,1)` (Pier).
   - **Drawing and moving between states** uses in-out: `expo.inOut`, `power2.inOut`, `power3.inOut`, `(.76,0,.24,1)`.
   - **Anything scrubbed** is `ease: "none"`; the scroll is the easing.
   - Only the loudest sites use `elastic` or `back` (BLUNT, Jithin, Pier's dots).
5. **Text reveals are played once; drawings are scrubbed.**
   - Start points are `top 85–92%`, with `once: true`. Travel is **14–48px** or a line-mask `yPercent 100–110`. Durations are **0.7–1.3s** and line staggers **35–110ms**, capped (Fox caps the total at 450ms).
   - Jithin and Chladni both say why in code: a played reveal cannot be stranded half-way by a fast flick.
6. **Reading order is fixed: picture, then headline lines, then details** (Jithin's works rows; Metic assembles guides, then content; Wafer draws the line, then pins at 0.9s + i×0.62s).
7. **Wayfinding is explicit.** Counters (`01 / 07`, `01 / 08`, `01 / 03`, big `02`), percent meters (Metic "Build progress 000 %", Pier's header `%`, Heron's loader), chapter lists with the current item lit (Townhouse) and Plot/Build/Live tabs with fill bars (Pier).
8. **One accent colour does the pointing.** Heron orange `#FF6B30` marks violations, Metic's single red dot travels through the build, Fox uses rust, and Townhouse reserves red for broken states. Everything else is neutral.
9. **Type pairs a large display face with mono labels.** Mono carries numbers, labels and data (Heron, Pier, Wafer, Metic, Townhouse). Fox adds a serif for reading. Headlines split by measured lines, not by `<br>`.
10. **Ambient life is tiny and slow.** Fox's fox breathes at `scale 1.004/1.013` over 4.7s, and Townhouse's hub at `1.015` over 3.2s. Loops last **3–7s**, and the careful sites pause them off-screen (Wafer, Roveia, TVS).
11. **The best sites handle reduced motion and repeat visits.** They land on the finished drawing (Fox, Pier, Chladni, Neutomni) and run intros once per session through `sessionStorage` (Fox, Pigeon, Heron, Pier). Pier splits its pages into 8KB reading pages and 63KB showcase pages.
12. **What they get wrong for our readers.** Gates and loaders (Jithin's Z, Townhouse, Pigeon at 3.3s, Heron at about 5.5s). Smooth-scroll libraries on almost every site (Lenis `lerp .09–.1` or `duration 1.15–1.2`). Snapping on content (Neutomni, Roveia). Velocity-driven warps (Jithin). Auto-advancing marquees and decks (Pigeon, Wafer). Cursor toys (Pier, Metic, BLUNT).

---

## C. Catalogue entries (fits and adapt only)

### Blueprint that inks itself
- Shape: big-idea, part-whole, atmosphere · fits 1 drawing, 20-120 strokes
- Reader sees: The opening picture (a building, a farm, a machine, a kolam) draws itself line by line in ink on paper, then a light wash or hatch settles in and the headline is there.
- Moves: load - each stroke `strokeDashoffset L→0`, 0.8-1.4s, `cubic-bezier(.45,.05,.35,1)`, starts staggered so the whole drawing completes in 2.5-3.5s; wash/hatch layer fades .6s at the end; headline lines rise in parallel (never waits for the drawing).
- Build: inline SVG, every path `fill:none`; on load `L=getTotalLength()`, set `stroke-dasharray:L; stroke-dashoffset:L`, then add a class with `transition: stroke-dashoffset var(--d) cubic-bezier(.45,.05,.35,1) var(--delay)`.
  Delay per path from document order (`i * total/ n`), or by group (outline first, details next, hatch last).
  `sessionStorage` flag: second visit renders finished. No gate, no counter, no loader.
- Narrow: same drawing, fewer detail paths (hide `.detail` under 700px) · Reduced motion: drawing shown finished.
- Use when: the proposal has one hero object everyone should picture · Avoid when: there is no real object to draw (don't draw abstract blobs).
- Effort: M · Source: https://heronaiapp.com (loader timeline in https://heronai-bp.netlify.app/main.js), https://foxvaluations.com.au

### Pen-speed draw-on
- Shape: emphasis, atmosphere · fits 1-12 strokes (a signature, a logo, an icon, a short line drawing)
- Reader sees: A line drawing or handwritten word appears as if a pen is writing it right now, long strokes taking longer than short ones, then the ink fills in.
- Moves: in-view (once) or load - stroke i duration = `T × Li / ΣL` with T 1.4-1.9s; next stroke starts at 82% of the previous; `power1.inOut`-like `cubic-bezier(.45,.05,.55,.95)`; optional fill fades .5s ease-out then the outline fades .4s.
- Build: compute lengths, build start times cumulatively (`t += d*0.82`), set per-path `transition-delay` and `transition-duration` inline; trigger with one IntersectionObserver (threshold .4).
  Fill layer is a duplicate group with `fill` and opacity transition.
- Narrow: same · Reduced motion: drawn and filled at once.
- Use when: a name, signature, motif or one icon deserves a moment · Avoid when: many drawings are on screen together (draw only the one being read).
- Effort: S · Source: https://jithinrp.com/site.js

### Ink-bleed reveal
- Shape: before-after, atmosphere · fits 1 picture pair
- Reader sees: As they scroll, ink seems to soak down the paper and, where it has soaked, the sketch underneath turns into the finished picture.
- Moves: scroll-linked - mask path morphs from a hairline at the top to full cover between 35% and 55% of the section's progress; edge is ragged like wet ink; linear with scroll.
- Build: `<svg><defs><mask id=m><path fill=white filter="url(#bleed)" d="M0 1 Q500 2 1000 1 L1000 0 L0 0Z"/></mask><filter id=bleed><feTurbulence type=fractalNoise baseFrequency=".045 .055" numOctaves=4 seed=5/><feDisplacementMap in=SourceGraphic scale=100 xChannelSelector=R yChannelSelector=G/><feGaussianBlur stdDeviation=1.8/><feComponentTransfer><feFuncA type=linear slope=2.2 intercept=-.6/></feComponentTransfer></filter></defs><image href=after mask=url(#m)/></svg>` over the "before" image.
  On scroll, interpolate the path's y values (top edge y = p×1000, curve control y = p×1250) and set `d`; filter is static (only the path moves).
  Cap the masked area near 900px wide; one per page.
- Narrow: crossfade before→after on in-view (.8s) · Reduced motion: show "after" with a "before" thumbnail beside it.
- Use when: sketch to real, plan to built, dry field to green field · Avoid when: the two pictures are not the same framing.
- Effort: M · Source: https://heronaiapp.com

### Numbered cards on a construction line
- Shape: list-of-equals, sequence · fits 3-6 cards
- Reader sees: Problem cards labelled [01]–[04], each joined by a faint dash-dot drafting line, and each card's small line icon drawing itself as the card arrives.
- Moves: in-view - card fades up 12-16px over .8s ease-out; its icon strokes draw 1.0s in-out after .2s; the connector to the next card draws .9s; stagger between cards 90ms, total capped at 450ms.
- Build: CSS grid of cards; connector is an absolutely positioned SVG path with `stroke-dasharray: .93 2.8 9.35 2.8` at about `#B3B3AF` (or 22% ink) for the base; on reveal a solid ink copy draws over it with dashoffset.
  Labels in mono 11-12px: `[01] MANUAL`. Icons are 1.5px isometric line drawings, `class=draw`.
- Narrow: single column, connector runs vertically down the left gutter · Reduced motion: everything visible, connectors solid.
- Use when: listing the 3-6 problems or reasons before the solution · Avoid when: the items have an order of cause (use the snake or a sequence instead).
- Effort: S · Source: https://heronaiapp.com

### Sticky steps with callouts on the drawing
- Shape: sequence, part-whole · fits 3-5 steps
- Reader sees: A drawing stays on one side; the step name on the other side changes as they scroll (Observe, Advise, Act, Learn), and small labels pop onto the exact spot in the drawing that each step is about.
- Moves: scroll-linked (step index) + in-view - step title swaps with a .3s fade/12px rise; callout tags scale .96→1 and fade .4s ease-out at their anchor; a 1px accent hairline draws under the active step .8s.
- Build: two-column grid; drawing column `position: sticky; top: 12vh`; each step block `min-height: 80vh`; IntersectionObserver with `rootMargin: "-45% 0px -45% 0px"` sets `stage.dataset.step`; CSS shows callouts `[data-for~="2"]` for the active step.
  Callouts are absolutely positioned on the SVG using viewBox percentages so they stay on their spot.
- Narrow: drawing becomes a sticky band (top, 40vh) and steps scroll beneath it, or each step gets its own cropped drawing · Reduced motion: all callouts visible, numbered, with a legend.
- Use when: explaining how a service works on one picture · Avoid when: steps have nothing to point at in the drawing.
- Effort: M · Source: https://heronaiapp.com

### Show-the-workings toggle
- Shape: part-whole, proof-trust · fits 1 drawing, 3-12 hidden notes
- Reader sees: A small switch reading "show the workings". When on, the clean picture gains its construction lines, measurements and margin notes, the way an architect shows the plan behind a rendering.
- Moves: tap - guides draw .6s in-out (stagger 40ms), labels fade .3s; off reverses at 1.5× speed.
- Build: two SVG layers (`.final`, `.workings`); a real `<button aria-pressed>` toggles `data-xray` on the figure; CSS transitions dashoffset on `.workings path` and opacity on labels.
  Default off. No drag lens (it fights scrolling on tablets).
- Narrow: same · Reduced motion: instant swap.
- Use when: the reader may want proof that the plan is measured (budgets, layouts, timelines) · Avoid when: the workings would overwhelm (more than about 12 notes).
- Effort: S · Source: https://heronaiapp.com, https://metic.studio/en

### System drawn as a village
- Shape: place-network, part-whole, many-to-many · fits 5-12 parts
- Reader sees: The whole programme drawn as a little village map: each team or service is a house, the paths between them are the hand-offs, labels name the districts, and tapping a house opens its card.
- Moves: in-view - houses draw on in two waves (outlines 1.2s, then details), paths draw after their two ends exist; tap - house lifts 2px, its card opens .3s, unrelated paths dim to 30%.
- Build: one flat hand-drawn SVG (top-down or simple isometric, no WebGL), `<g data-node>` per building, paths with `data-from data-to`; district labels in mono caps.
  Tap handler toggles `.focus` on the node and the paths whose ends match; card is a `<dialog>` or an aside.
- Narrow: map scales to width; cards open as a bottom sheet; also render the list of parts below the map · Reduced motion: map shown finished.
- Use when: the reader needs to see who and what exists and how they connect · Avoid when: the parts don't have real relations (use a list).
- Effort: L · Source: https://townhouse.dev

### Marching dashes on the live line
- Shape: cause-effect, place-network · fits 1 active line at a time
- Reader sees: On the one connection being discussed, little dashes walk slowly from the giver to the receiver; every other line is still.
- Moves: ambient (only while its section is in view and the line is active) - `stroke-dashoffset` 0→-18px per cycle, 2.4-3.2s linear infinite, `stroke-dasharray: 5 6`.
- Build: `@keyframes flow{to{stroke-dashoffset:-18px}}` on `.edge.is-live`; set `.is-live` from the step observer; pause via `animation-play-state` when off-screen.
  Direction: draw the path from source to target so negative offset reads as forward.
- Narrow: same · Reduced motion: no marching; the live line is drawn solid with an arrowhead.
- Use when: showing what flows (money, data, produce) along a relationship · Avoid when: more than one flow matters at once (use a still diagram with arrows).
- Effort: S · Source: https://townhouse.dev (static/index.BN4-bxXu.css)

### One-time alarm ring
- Shape: emphasis, cause-effect · fits 1-3 problem points
- Reader sees: A single ring ripples out once from the spot where things break, then a calm marker stays to show "here".
- Moves: in-view - ring scale 1→1.18 (or radius r→1.8r for SVG) and opacity .9→0 over .7s ease-out, once; the static marker remains in the accent colour.
- Build: SVG `<circle class=ring>` duplicated at the node; on reveal add `.ping` with `animation: ping .7s cubic-bezier(.22,1,.36,1) 1 forwards`.
  Never infinite. If the reader taps the node, it can ring once more.
- Narrow: same · Reduced motion: no ring; marker only.
- Use when: pointing at the one broken link, risk or bottleneck · Avoid when: everything is "a problem" (pick one).
- Effort: S · Source: https://townhouse.dev

### One breathing detail
- Shape: atmosphere · fits 1 per screen
- Reader sees: In an otherwise still drawing, one small thing gently breathes (a sleeping animal, a lamp glow, the centre dot of a kolam), so the page feels alive without asking for attention.
- Moves: ambient - scale 1→1.004/1.013 (or ≤1.5%) and/or translateY ≤2px, 3.2-4.7s ease-in-out infinite; optional one tiny accent every 9s (an ear twitch).
- Build: CSS keyframes on one `<g>` with `transform-box: fill-box; transform-origin: center bottom`; pause with an IntersectionObserver toggling `animation-play-state`.
- Narrow: same · Reduced motion: still.
- Use when: a hero or closing illustration needs warmth · Avoid when: anything else on the screen is moving.
- Effort: S · Source: https://foxvaluations.com.au (assets/styles.min.css), https://townhouse.dev

### Chapter rail with big numerals
- Shape: sequence, utility · fits 4-9 chapters
- Reader sees: Each section opens with a large number (01, 02 …) and a short title; a slim list at the side shows every chapter with the current one lit and a thin line filling as they read.
- Moves: scroll-linked - side line `scaleY` follows page progress; current chapter label gets ink and a dot (.3s); numeral rises from its mask on entry (.9s ease-out).
- Build: chapters are `<section data-ch>`; one IntersectionObserver (`rootMargin "-40% 0px -55% 0px"`) sets the active one; rail is a fixed `<nav>` of anchor links (also usable as a menu); progress via one rAF scroll handler or CSS `animation-timeline: scroll(root)` inside `@supports`.
  Numerals in a serif or hand-lettered style at about 96-160px.
- Narrow: rail hides; a thin top bar shows `02 / 07` · Reduced motion: no fills; current chapter still marked.
- Use when: the page is long enough that readers need to know where they are · Avoid when: under 4 sections.
- Effort: S · Source: https://townhouse.dev, http://chladni-plate-experiment.vercel.app

### One object, scroll as time
- Shape: time-roadmap, before-after, cause-effect · fits 1 object, 4-6 time bands
- Reader sees: One drawing stays in the middle (a field, a building, a seedling, a ledger) and changes as they scroll; on the left the time band ("Year 1", "Years 2-3") and on the right one plain fact for that band.
- Moves: scroll-linked - object state crossfades between band drawings (.4s at each threshold, or 1:1 opacity between neighbours); band label and fact swap with a 12px rise; optional gauge number on the side.
- Build: tall section (bands × 100vh) with a sticky inner `100vh` stage; progress `p = clamp(-rect.top/(rect.height-innerHeight))`; band index `floor(p*n)`.
  Object states are stacked SVG groups (same viewBox) so lines stay in register.
- Narrow: stage becomes a sticky top band (45vh) with the label/fact below · Reduced motion: each band shown as a still frame in a column.
- Use when: the argument is "this is how it changes over time" · Avoid when: there is no single object that changes.
- Effort: M · Source: http://plastic-ocean.com

### Scroll-scrubbed gauge number
- Shape: quantity-scale, time-roadmap · fits 1 number per gauge
- Reader sees: A number beside a ruler counts up (or down) exactly as fast as they scroll, so the distance they travel is the amount: metres, years, rupees, hectares.
- Moves: scroll-linked - value = from + (to-from)×progress between two markers, rounded to meaningful steps; ruler tick under the reading line lights.
- Build: two invisible marker elements; on scroll (rAF throttled) compute progress of the viewport centre between their centres; `textContent = Math.round(v/step)*step` formatted with `toLocaleString('en-IN')`.
  CSS-only alternative: `@property --n {syntax:"<integer>"}`, `counter-reset: n var(--n)`, `content: counter(n)`, `animation-timeline: view()` inside `@supports`.
- Narrow: same · Reduced motion: show the final value with the range ("0 → 10,000 m").
- Use when: scale is the point (how deep, how long, how much) · Avoid when: the number needs to be read exactly at every moment.
- Effort: S · Source: http://plastic-ocean.com, https://piergorelli.com

### Shape portal into the detail
- Shape: part-whole, emphasis · fits 1 per page
- Reader sees: A hand-drawn outline (a doorway, a kolam loop, a seed) opens wider as they scroll until they are inside it, and the next section, the close-up, is on the other side.
- Moves: scroll-linked - `mask-size` 0→frame size over 0.9 screen heights (ease-in-out cubic), hold 0.2 screens, then grow to just past the viewport over 0.6 screens; no rush to 2000vh.
- Build: sticky 100vh layer with `mask-image: url(#shape)` or an inline SVG data URI, `mask-repeat: no-repeat; mask-position: 50% 50%`; set `mask-size` from scroll progress with `t<.5 ? 4t³ : 1-(-2t+2)³/2`.
- Narrow: plain in-view crossfade into the close-up · Reduced motion: hard cut with the shape shown as a small icon on the close-up.
- Use when: moving from the whole programme into one site, one person, one farm · Avoid when: used more than once, or for every section change.
- Effort: M · Source: http://plastic-ocean.com

### Blur-to-sharp headline
- Shape: emphasis, big-idea · fits 1 statement per screen
- Reader sees: A key sentence comes into focus as it arrives, like eyes adjusting, and then stays sharp.
- Moves: in-view (once) - opacity 0→1, blur 6px→0 and translateY .24em→0 over .9-1.1s `cubic-bezier(.23,1,.32,1)`; by words with 60-80ms stagger, or by lines with 110ms.
- Build: split words into `<span>` (keep `aria-label` on the parent); CSS transition on `filter, opacity, transform`; IntersectionObserver threshold .5 adds `.in`.
  Never fade out while still in view.
- Narrow: same (drop blur under 600px if it stutters) · Reduced motion: visible at once.
- Use when: the one sentence the reader must remember from a section · Avoid when: body text or more than one statement per screen.
- Effort: S · Source: http://plastic-ocean.com, https://metic.studio/en, https://neutomni.com

### Shared-frame split
- Shape: comparison, before-after · fits 2 states
- Reader sees: One picture split by a horizon: above, one world (the bottle, today's way); below, the other (the fish, the new way); the line between them is the point.
- Moves: in-view - the dividing line draws across 1.0s in-out, then each half's caption fades .6s, top first.
- Build: one SVG with two clipped groups sharing a horizon; a single `<line>` drawn with dashoffset; captions sit in each half.
- Narrow: stack halves vertically, horizon stays · Reduced motion: shown finished.
- Use when: a stark contrast in one image (old process vs new, without vs with) · Avoid when: the two sides need many details (use two columns).
- Effort: S · Source: http://plastic-ocean.com

### Ledger rules that draw in
- Shape: list-of-equals, proof-trust, ranked-list · fits 3-12 rows
- Reader sees: Rows of a neat ledger (facts, prices, deliverables) where each ruled line draws itself left to right and then its words appear, row by row, like someone filling a report.
- Moves: in-view - rule `scaleX 0→1` .8s `cubic-bezier(.22,1,.36,1)`, delay `min(i×90ms, 450ms)`; text fades .7s 150ms after its rule; long section rules 1.4-1.6s in-out.
- Build: `.row{position:relative}.row::after{content:"";position:absolute;left:0;right:0;bottom:-1px;height:1px;background:var(--line);transform:scaleX(0);transform-origin:left}` + `.in` state; set `--row-delay` inline; IntersectionObserver `rootMargin "0px 0px 12% 0px"`.
- Narrow: same · Reduced motion: rules and text visible.
- Use when: key facts, fee lines, what-you-get lists · Avoid when: rows are long paragraphs.
- Effort: S · Source: https://foxvaluations.com.au, https://jithinrp.com

### Picture, then headline, then details
- Shape: utility, hierarchy · fits any section with a visual
- Reader sees: In each section the picture settles first, the headline lines rise next, and only then the small facts appear, so the eye always knows where to start.
- Moves: in-view (once) - picture fades .7s and scales 1.06→1 over 1.2s in-out; title lines rise from masks .9s ease-out, 60ms apart, starting .2s; body lines 35ms apart at .3s; detail chips rise 16px at .45s, 60ms apart.
- Build: one timeline per section using CSS custom properties: each element gets `--t` (start) and the `.in` class sets `transition-delay: var(--t)`. Line masks via measured lines (see *Hero lines rise from their masks*) or simple block reveals for body.
  Going back up shows everything (no reverse play).
- Narrow: same order, shorter delays (×0.7) · Reduced motion: all visible.
- Use when: every content section · Avoid when: the section has no visual (just fade-up).
- Effort: S · Source: https://jithinrp.com/site.js

### Plot, build, live stage
- Shape: sequence, before-after, big-idea · fits 1-3 projects, 3 stages each
- Reader sees: The idea is first sketched in pale construction lines with notes, then the real parts are drawn and filled in, then a scan line sweeps across and the finished thing appears; tabs underneath read Plot / Build / Live.
- Moves: scroll-linked (pinned) - Plot: guides draw (.75 each, stagger .3/n, in-out), labels fade; at 30% guides dim to .2; Build: real strokes draw (.7, stagger .1), blocks grow, labels type on; Live: clip widens with a 1px scan line (.9 in-out); tab bar fill follows progress.
- Build: pinned section 250-300vh, sticky stage; one SVG with three groups (`.plot`, `.build`, `.live`); paths use `pathLength="1"` so dashoffset 1→0 is uniform; map progress to a hand-rolled timeline (array of `{el, prop, from, to, start, end}` interpolated each scroll frame).
  Library not needed; GSAP is a convenience only.
- Narrow: three stacked frames (Plot, Build, Live) each revealing on view · Reduced motion: three static frames with the tabs as labels.
- Use when: showing how an idea becomes a deliverable (site plan, curriculum, product) · Avoid when: you can't draw the plot stage honestly.
- Effort: L · Source: https://piergorelli.com (work-stage module https://piergorelli.com/_astro/work-stage.DzNATKeh.js)

### Chart that plots as you scroll
- Shape: quantity-scale, time-roadmap · fits 1 line or 3-8 bars
- Reader sees: A simple chart draws itself as they read: the axis first, then the line travelling left to right, the points landing, and labels last.
- Moves: scroll-linked - from top 85% to bottom 60% of the chart: paths `pathLength=1` dashoffset 1→0 with stagger min(.12, .9/n); points scale 0→1 (no overshoot, `cubic-bezier(.22,1,.36,1)`); bars scaleX 0→1 from 35%; labels fade from 40%.
- Build: SVG chart; one scroll handler computes p for the chart and sets each element's local progress `clamp((p - start)/dur)`.
  Or played version: one IntersectionObserver and CSS transitions with the same order.
- Narrow: played (not scrubbed) on view · Reduced motion: finished chart.
- Use when: one trend carries the argument · Avoid when: the reader needs to compare exact values (show a table twin).
- Effort: M · Source: https://piergorelli.com

### Reading ruler in the header
- Shape: utility · fits 1 per page
- Reader sees: A thin ruler under the top bar fills as they read, with a tiny tag showing how far along they are (35%).
- Moves: scroll-linked - rule clip-path `inset(0 100% 0 0)` → `inset(0)` over the page; tag counts 00→100.
- Build: CSS only inside `@supports (animation-timeline: scroll())`: `.rule{animation:draw linear both;animation-timeline:scroll(root)}`, `@property --pct{syntax:"<integer>";inherits:true;initial-value:0}`, `.tag::before{content:counter(pct, decimal-leading-zero) "%"}` with `counter-reset:pct var(--pct)`.
  JS fallback: one passive scroll listener setting `--p`.
- Narrow: same, 2px tall · Reduced motion: keep (it is not decorative motion; it follows the reader).
- Use when: long pages · Avoid when: the page fits in 3 screens.
- Effort: S · Source: https://piergorelli.com (_astro/Base.CCmxeWj5.css)

### Outline words that fill with ink
- Shape: emphasis, big-idea · fits 1 headline of 5-12 words
- Reader sees: A headline first appears as hollow outline letters; as they scroll, each word fills with solid ink, one after another, until the whole sentence is solid.
- Moves: scroll-linked - each word's solid copy wipes left→right via clip-path, stagger 0.6 of a word-duration, from top 65% to bottom 60% of the block; margin notes dim to .15.
- Build: two stacked copies: `.outline` (`-webkit-text-stroke:1px var(--ink); color:transparent`) and `.solid` per word with `clip-path: inset(-.35em calc(100% - var(--w)*100%) -.45em 0)`; set `--w` per word from progress.
- Narrow: played on view (1.2s total) · Reduced motion: solid text.
- Use when: the promise or thesis line of the page · Avoid when: more than once per page.
- Effort: S · Source: https://piergorelli.com

### Build-up that ends in the button
- Shape: sequence, call-to-action, big-idea · fits 5-8 steps
- Reader sees: One drawing builds up step by step (a line, then a frame, then parts, then colour), a counter reads "built 60%", and at the last step everything folds into the single button they are being asked to press, with its size marked in pencil.
- Moves: scroll-linked (pinned) - each step adds one layer (draw .7-.9s in-out or fade .4s); counter 000→100% follows progress; final step: layers scale/translate into the button's box over .9s in-out, guides show `button · 186 × 56` then fade.
- Build: pinned stage (steps × 60-80vh); SVG layers per step; progress → step index plus local progress; final collapse uses FLIP (measure the button rect, transform the group from its box to the button box).
  The real `<a class=cta>` replaces the drawing at the end (it is a working link).
- Narrow: steps as a short vertical stack, then the real button · Reduced motion: final state with a numbered list of what went into it.
- Use when: the close of a proposal: "everything above is what this one decision buys" · Avoid when: the CTA is not a single clear action.
- Effort: L · Source: https://metic.studio/en

### Assemble with construction guides
- Shape: emphasis, proof-trust · fits 1 block per screen (a card, a figure, a price)
- Reader sees: Before a block appears, pencil guide lines cross where it will sit and a small measurement note shows its size; then the guides fade and the block settles into exactly that spot.
- Moves: in-view - horizontal guide `scale 0 1 → 1` to 38% of 1.7s then fades; vertical starts +90ms; label shows 22%-70% then fades (1.9s); content rises .9rem from blur(4px) after .52-.64s, `cubic-bezier(.23,1,.32,1)`.
- Build: `.cx-h`, `.cx-v` absolutely positioned 1px lines (accent at 60%); `@keyframes cx-h{0%{scale:0 1}38%{scale:1}to{opacity:0}}`; `.is-built` class from IntersectionObserver; `--d` per block.
- Narrow: same, guides shorter · Reduced motion: no guides; block visible.
- Use when: the key figure, price or deliverable box (a "this was measured" moment) · Avoid when: used on every block.
- Effort: S · Source: https://metic.studio/en (_next/static/chunks/11yn5wfwhtw_z.css)

### Boxes that draw their own border
- Shape: grouped-list, list-of-equals · fits 2-8 boxes or chips
- Reader sees: Each card or pill traces its outline in ink, then the ink softens to a light rule and the contents appear.
- Moves: in-view - four sides grow over .9s (`cubic-bezier(.23,1,.32,1)`) in ink, at 75% colour eases to the line tone; chips wipe left→right .7s; stagger 70ms.
- Build: `background: linear-gradient(var(--draw),var(--draw)) top left/0 1px no-repeat, …` for the four sides, animated to `100% 1px` / `1px 100%`; chips use `clip-path: inset(0 100% 0 0 round 999px)` → `inset(0 round 999px)`.
- Narrow: same · Reduced motion: drawn.
- Use when: options, packages, team chips · Avoid when: boxes are large panels (border draw reads slow).
- Effort: S · Source: https://metic.studio/en

### Approval stamp
- Shape: proof-trust, emphasis · fits 1 per page
- Reader sees: A round rubber stamp ("Approved", "Funded", "Done in 2025") lands slightly tilted on a card, like an official mark on paper.
- Moves: in-view - from rotate(-14deg) scale(1.15) opacity 0 to rotate(-11deg) scale(1) opacity 1 over .4s `cubic-bezier(.22,1,.36,1)`, once; ink texture static.
- Build: SVG circle text stamp with the rice-powder/grain filter applied once (static); class toggle on view.
- Narrow: same · Reduced motion: shown.
- Use when: proof points (a past result, an endorsement, a certification) · Avoid when: the claim is not real or not verified.
- Effort: S · Source: https://metic.studio/en

### Line drawing that fills in, stop by stop
- Shape: part-whole, before-after · fits 1 object, 3-5 stops
- Reader sees: A technical line drawing of the product or site; as they scroll it fills in stage by stage (structure, materials, colour), pausing at each stage with a short label.
- Moves: scroll-linked (pinned) - each stop: one layer fades/draws in .6-.9s; labels swap with a 12px rise; snapping only within this pinned scene, to stops.
- Build: pinned section 3 viewport heights; SVG groups per stop over a base line drawing; progress → stop; optional soft snap: after scrolling stops for 150ms inside the section, `scrollTo` the nearest stop with `behavior: smooth`.
  No image sequence (too heavy for one file).
- Narrow: stops as stacked frames · Reduced motion: final drawing plus a numbered legend.
- Use when: showing what a thing is made of · Avoid when: the layers aren't visually distinct.
- Effort: M · Source: https://bluntumbrellas.com (cdn/shop/t/91/assets/home-anim.bundle.js)

### Plus-marker part labels
- Shape: part-whole, definitions-jargon · fits 3-7 parts
- Reader sees: Small "+" marks sit on parts of a drawing; tapping one opens a short note naming the part and why it matters.
- Moves: tap - "+" rotates to "×" (.2s), note opens .25s ease-out (opacity + 6px); only one open at a time.
- Build: `<button class=hot style="left:62%;top:30%" aria-expanded>` over the SVG; note is a sibling `<div role=region>`; close on outside tap or Escape.
- Narrow: show all labels as a numbered list under the drawing with numbers on the markers · Reduced motion: no rotation; instant open.
- Use when: naming parts of a site, a product, a kit, a curriculum · Avoid when: more than 7 parts.
- Effort: S · Source: https://bluntumbrellas.com

### Fixed stage, one knob per chapter
- Shape: cause-effect, sequence · fits 4-7 chapters
- Reader sees: One diagram stays on screen; each chapter of text changes just one thing in it (more water, a later date, a bigger team), so cause and effect are obvious.
- Moves: scroll-linked - within each chapter, progress maps to one parameter (linear or log); the diagram eases toward the target over .3s so it never jumps; chapter title rises 24px, .7s, once.
- Build: chapters as `<section data-param="rain" data-from="0" data-to="1">`; one scroll handler finds the active chapter and sets `target`; a rAF loop does `value += (target-value)*(1-exp(-dt/0.3))` and redraws the SVG (attributes) only when the value changes.
  Chapter counter `01 / 07`.
- Narrow: stage as sticky band; or each chapter shows two static states (from, to) · Reduced motion: value jumps per chapter; diagram static between.
- Use when: explaining a mechanism (how spend drives reach, how rain drives yield) · Avoid when: several things change together.
- Effort: L · Source: http://chladni-plate-experiment.vercel.app

### Grains settle into the line
- Shape: atmosphere, big-idea · fits 1 figure
- Reader sees: Scattered rice-powder dots drift and then gather into a clean kolam line or the outline of the idea, as if the pattern was always hiding in the dust.
- Moves: in-view - 2-4k grains random-walk with step size proportional to distance from the target path; settle in about 2.5-3.5s; then the crisp SVG line fades in .6s under them.
- Build: Canvas 2D (devicePixelRatio aware) with target points sampled along the SVG path (`getPointAtLength` every 1-2px); each grain eases toward a random nearby target with jitter that decays; stop the loop when settled; static thereafter.
  No WebGL. Off-screen pause.
- Narrow: 1-1.5k grains · Reduced motion: final line with a static grain texture.
- Use when: an opening or closing moment that ties to the kolam/rice-powder identity · Avoid when: anything else animates nearby.
- Effort: L · Source: http://chladni-plate-experiment.vercel.app

### Square wheel that rounds as it rolls
- Shape: sequence, before-after, big-idea · fits 4-8 steps
- Reader sees: A rough square rolls along a bumpy road of arches as they scroll; at each step it gains corners and rolls more smoothly, and by the end it is a circle on a flat road: the process makes things smooth.
- Moves: scroll-linked - x from left to right edge; sides 4→N over the first 30%, then vertices push out to a circle while the arches flatten; dashed axle guide stays level; 1.5px lines; smoothing `lerp .2` per frame; smoothstep curve.
- Build: Canvas 2D or SVG path regenerated per frame: polygon vertices `cos/sin(π/2 + 2πi/n)·R`, insert a midpoint to morph n→n+1; road = catenary `y = peak + a·cosh(x/a) - a` with arch width `s = 2R·sin(π/n)`; rotation `= distance/s × 2π/n`.
  Step labels sit under the road at each arch where n increases.
- Narrow: same, smaller R; labels below in a list · Reduced motion: four still frames (square, hexagon, 12-gon, circle) with labels.
- Use when: a process that refines something over stages (pilot to scale, rough plan to smooth operation) · Avoid when: the steps are unrelated.
- Effort: M · Source: https://neutomni.com

### Feathered line sweep with milestone pins
- Shape: time-roadmap, quantity-scale, proof-trust · fits 1 line, 2-4 pins
- Reader sees: One rising line sweeps across from left to right with a soft edge, and pins drop on it at the moments that mattered ("pilot done, 230 → 315").
- Moves: in-view - mask-position transitions over 3s ease-in-out; pins fade + rise 4px over .48s ease-out at .9s + i×.62s; pins hang on dashed ties.
- Build: wrap the SVG in `.sweep{mask-image:linear-gradient(to right,#000 0,#000 50%,transparent 57%);mask-size:200% 100%;mask-position:100% 0;transition:mask-position 3s ease-in-out}` and `.in .sweep{mask-position:0 0}`; remove the mask after `transitionend`.
  Tie: `width:2px;height:45px;background:linear-gradient(currentColor 0 13px,#0000 13px 33px,currentColor 33px 45px)`.
- Narrow: show 2 pins; shorter ties · Reduced motion: drawn line, pins visible.
- Use when: before→after progress over time, results of a pilot · Avoid when: the data is noisy (draw the trend honestly).
- Effort: S · Source: https://www.wafer.ai

### Loops that sleep off-screen
- Shape: utility · fits every ambient loop on the page
- Reader sees: Nothing (the page simply stays fast and still where they are not looking).
- Moves: in-view - CSS and SMIL loops pause when out of view and resume where they left off; reduced motion cancels them.
- Build: one IntersectionObserver per animated figure; on leave: `el.getAnimations({subtree:true}).forEach(a=>a.pause())` and `svg.pauseAnimations()`; on enter: `play()` / `unpauseAnimations()`; `matchMedia('(prefers-reduced-motion: reduce)')` → cancel and render finished; also pause on `visibilitychange`.
- Narrow: same · Reduced motion: loops off.
- Use when: always, if anything loops · Avoid when: never.
- Effort: S · Source: https://www.wafer.ai (_astro/nativeIllustrationMotion.O-53HXvT.js), https://www.roveia.com

### Thumbnail grows into the stage
- Shape: part-whole, emphasis · fits 1 per section
- Reader sees: A small framed picture sitting inside the text grows smoothly until it fills the whole frame, signalling "now we look closely at this".
- Moves: scroll-linked (pinned ~1.1 viewport heights) - left/top/width/height from the thumbnail's rect to the stage rect, linear with scroll; a soft paper veil to 40% so the caption stays legible; caption fades in last 30%.
- Build: measure both rects on load and resize; transform with `translate` and `scale` (cheaper than width/height) on a fixed-size SVG drawing; sticky container.
- Narrow: plain in-view: thumbnail fades out, full figure fades in .6s · Reduced motion: full figure with the thumbnail beside the text.
- Use when: zooming from the overview to the main exhibit · Avoid when: the picture doesn't hold up large.
- Effort: M · Source: https://www.roveia.com

### Focus wheel list
- Shape: ranked-list, list-of-equals · fits 5-9 items
- Reader sees: A column of names rolls past a fixed reading line; the name on the line is full ink, its neighbours fade with distance, and a short note beside it changes to match.
- Moves: scroll-linked (pinned (n-1)×300px) - list translateY keeps the active index centred; opacity by distance 1 / .5 / .25 / .1 / .05; side note crossfades .4s when within .15 of an index.
- Build: sticky container; `virtualIndex = p*(n-1)`; `list.style.transform = translateY(mid - (vi*itemH + itemH/2))`; per item opacity step function; note swaps on `Math.round(vi)`.
  No forced snap; settle naturally.
- Narrow: normal list with the note under each name · Reduced motion: normal list.
- Use when: clients, partners, regions where one-at-a-time focus helps · Avoid when: the reader needs to compare items side by side.
- Effort: M · Source: https://www.roveia.com

### Chalk horizon wave
- Shape: atmosphere, call-to-action · fits 1 per page (closing)
- Reader sees: Behind the final ask, one soft chalk-coloured line moves like a slow tide along the bottom of the page.
- Moves: ambient - one SVG path, 8 anchors, each `y = mean + amp×(0.62 sin(ωt f1 + φ1) + 0.38 sin(1.62 ωt f2 + φ2))`, ω about .5 rad/s, amp 12-20px; paused off-screen.
- Build: Catmull-Rom to cubic Bézier per frame (`c1 = p1 + (p2-p0)/6`, `c2 = p2 - (p3-p1)/6`); fill a chalk tint gradient to transparent; seeded RNG for phases.
- Narrow: same · Reduced motion: static wave.
- Use when: the CTA band needs a calm ground · Avoid when: anything else in view moves.
- Effort: S · Source: https://www.roveia.com

### Hero lines rise from their masks
- Shape: big-idea, emphasis · fits 1-3 lines (hero only)
- Reader sees: The opening headline appears line by line, each line sliding up from just below an invisible edge, like type being set.
- Moves: load - each line `translateY(calc(100% + .3em))` → 0 over 1.25s `cubic-bezier(.2,.75,.1,1)`, 90-110ms per line; sub-copy fades up 16px at +.3s.
- Build: measure real line breaks (wrap characters in spans, group by `getClientRects()` bottom), then rewrap as `<span class=ln style="--li:i"><span class=ln__in>…</span></span>` with `overflow:hidden; padding-block:.1em`; re-measure after `document.fonts.ready` and on width change; keep the plain text for screen readers via `aria-label`.
- Narrow: same · Reduced motion: visible.
- Use when: the hero and maybe one closing line · Avoid when: every heading (fade-up the rest).
- Effort: S · Source: https://aicommon.creamu.co.jp (assets/js/main.js), https://townhouse.dev

### One-shot fade-up
- Shape: utility · fits every block below the fold
- Reader sees: Sections gently appear as they come into view and then never move again.
- Moves: in-view (once) - opacity 0→1 and 16px→0 over .8-1s `cubic-bezier(.22,.61,.36,1)`; siblings 80-90ms apart, total capped at 450ms; observer bottom margin -6%.
- Build: `.js [data-rv]{opacity:0;transform:translateY(16px)}` `[data-rv].in{…transition…}`; IntersectionObserver unobserves after first show; add `.js` only if motion is allowed so content is never hidden without JS.
- Narrow: same · Reduced motion: no transform; content visible.
- Use when: all body blocks · Avoid when: above the fold (render it visible).
- Effort: S · Source: https://aicommon.creamu.co.jp

### Day-in-the-life hairline
- Shape: time-roadmap, people-roles · fits 3-6 moments
- Reader sees: One thin line runs across the page with times of day on it (06:00, 08:30, 14:00, 18:00); under each, one sentence of what happens for the person.
- Moves: in-view - the line draws left→right 1.2s in-out; each time stamp and its sentence fade up 12px as the line reaches it (stagger equal to its x position over the draw).
- Build: CSS grid of 4 columns with `::before` 1px rule at a fixed top; rule `scaleX` transition; items with `--d = col/4 × 1.2s`.
- Narrow: vertical line down the left with times stacked · Reduced motion: shown.
- Use when: showing what a typical day looks like after the change (for a farmer, a student, a manager) · Avoid when: events aren't in one day.
- Effort: S · Source: https://aicommon.creamu.co.jp

### Pen circle around a word
- Shape: emphasis · fits 1 word per section
- Reader sees: A loose hand-drawn loop circles the one word that matters in a heading, as if someone took a pen to it.
- Moves: in-view - .5s after the heading lands, loop draws over .9s `cubic-bezier(.45,.05,.55,.95)`, 2px stroke, once; overlap of the loop's ends like a real pen.
- Build: inline SVG ellipse-ish path (slightly open, start and end overlapping) absolutely positioned around the `<span class=circled>`; sized with `inset: -.25em -.4em`; dashoffset draw.
- Narrow: same, thinner stroke · Reduced motion: loop shown.
- Use when: the single key word in a headline · Avoid when: more than one per screen (use the marker for phrases).
- Effort: S · Source: https://www.fps.hu (line-anim.json)

### Tap to cycle four views
- Shape: comparison, part-whole · fits 2-4 views of one thing
- Reader sees: One diagram with a small "next view" control; each tap rearranges the same pieces to show the thing from another angle (by cost, by team, by time, by place).
- Moves: tap - pieces move to new positions .6s `cubic-bezier(.22,1,.36,1)` (not linear), labels crossfade .3s; a 1-of-4 dot row marks the view.
- Build: pieces as absolutely positioned elements or SVG groups with per-view coordinates in `data-v0..v3`; FLIP-style transform transitions; `<button>` cycles `data-view`.
- Narrow: same, or tabs above the diagram · Reduced motion: instant switch.
- Use when: the same parts regroup to answer different questions · Avoid when: views don't share pieces.
- Effort: M · Source: https://www.fps.hu

### Who-are-you doors
- Shape: choice-fork, people-roles · fits 2-3 doors
- Reader sees: Near the top: two or three plain doors ("I fund this", "I run this", "I join this"); choosing one jumps to the part written for them and marks the page as theirs.
- Moves: tap - chosen door fills with the accent .3s, others dim; smooth jump to the section (native `scrollIntoView({behavior:"smooth"})`); a small "reading as: funder" chip appears in the header.
- Build: buttons with `data-role`; store the choice in `localStorage` (wrapped in try/catch); sections with `data-for` get a "for you" marker.
- Narrow: stacked doors · Reduced motion: instant jump.
- Use when: the proposal has distinct readers · Avoid when: everyone needs the whole story in order.
- Effort: S · Source: https://www.concretemanagement.fr

### Drag splitter before/after
- Shape: before-after, comparison · fits 1 pair
- Reader sees: Two pictures of the same place, before and after, with a handle in the middle they can drag to wipe between them.
- Moves: tap/drag - `clip-path: inset(0 0 0 X%)` follows the pointer; starts at 50%; on first view the handle eases from 50% to 35% and back once (1.2s) to show it moves.
- Build: two stacked images or SVGs; `<input type=range>` styled as the handle for keyboard and touch access, its value setting `--x`; `.after{clip-path:inset(0 0 0 var(--x))}`.
- Narrow: same (range input works on touch) · Reduced motion: no hint animation.
- Use when: transformation (land, building, workflow screen) · Avoid when: the two images differ in framing.
- Effort: S · Source: https://www.concretemanagement.fr

### Stacking cards
- Shape: list-of-equals, sequence · fits 3-5 cards
- Reader sees: A neat stack of cards; as they scroll, the top card lifts away to reveal the next, like turning pages on a desk.
- Moves: scroll-linked (pinned) - each card's slot = pinned height / n; card translates up and fades over its slot; the remaining stack steps up 10px.
- Build: sticky container; cards absolutely positioned with `translateY(i×10px)` and `z-index` reversed; per-card progress from scroll; no 3D depth.
- Narrow: plain vertical list of cards · Reduced motion: plain list.
- Use when: a few parallel offers or pillars · Avoid when: more than 5, or when cards need to be compared.
- Effort: M · Source: https://www.concretemanagement.fr

### Step numbers that slide into place
- Shape: sequence · fits 3-6 steps
- Reader sees: Each step's big number slides into its slot as the step arrives, with the step text easing in beside it.
- Moves: scroll-linked - numeral `translateY(-60%)→0` and text `translateX(8%)→0` across the step's entry (top 90% → top 50%), linear with scroll (the scroll is the ease).
- Build: per step compute local progress; set `--p` and use `transform: translateY(calc((1 - var(--p)) * -60%))`; numerals in serif with tabular figures.
- Narrow: played on view (.8s ease-out) · Reduced motion: static.
- Use when: how-it-works steps · Avoid when: steps already sit on a drawn path (use the snake).
- Effort: S · Source: https://www.concretemanagement.fr

### Scroll-lit statement
- Shape: emphasis, big-idea · fits 1 paragraph (20-60 words) per page
- Reader sees: A short paragraph starts pale grey; as they scroll, the words turn to ink one by one, so they read at the speed of the ink.
- Moves: scroll-linked - each word's colour interpolates grey→ink over a rolling window of 3 words, quantised to .02 steps; optional played variant (once on view, 60ms per word).
- Build: split into word spans; progress p over the paragraph's pass (top 80% → bottom 40%); word i value `clamp((p×(n+3) - i)/3)`; colour via `color-mix(in oklab, var(--ink) calc(v×100%), var(--unread))`; update only words whose quantised value changed.
- Narrow: same · Reduced motion: ink text.
- Use when: the "why this matters" paragraph · Avoid when: long copy, or more than once.
- Effort: S · Source: https://twain.ai

### Marker stroke that hugs the line breaks
- Shape: emphasis · fits 1 phrase (1-8 words) per section
- Reader sees: A highlighter stroke is dragged across the key phrase, following it even when the phrase wraps onto two lines, slightly wobbly like a real marker.
- Moves: scroll-linked (or played on view) - per rendered line, a cubic path draws by dashoffset; lines draw in order, each in proportion to its width; stroke width 72% of line height, opacity .72, round caps.
- Build: `range.getClientRects()` on the phrase; merge rects by row; for each row build `M x0 y C x0+.3w y1, x0+.7w y2, x1 y3` with a seeded ±10% line-height wobble; one SVG overlay behind the text (`mix-blend-mode: multiply` on paper); recompute on resize.
- Narrow: same (rects recompute) · Reduced motion: marker shown.
- Use when: the outcome phrase in a section · Avoid when: it would cover more than 8 words.
- Effort: S · Source: https://twain.ai (assets/routes-DJXdf6qw.js)

### Paper plane on a dashed route
- Shape: sequence, time-roadmap · fits 3-6 stops
- Reader sees: A small line-drawn paper plane flies along a dashed route between sections, carrying the story from the problem to the answer.
- Moves: scroll-linked - plane position = `getPointAtLength(p×L)`, rotation from the path tangent; the dashed route behind it turns solid; at each stop the plane pauses for 10% of the segment.
- Build: one tall SVG overlay along the page margin; progress from the overlay's rect; easing per segment with smoothstep to create the pauses; plane is a 24px line icon.
- Narrow: route runs down the left gutter, plane 18px · Reduced motion: route drawn, plane parked at the current stop.
- Use when: a journey story (message, produce, application) · Avoid when: the snake path already carries the page.
- Effort: M · Source: https://twain.ai

### Number-first proof card
- Shape: proof-trust, quantity-scale · fits 2-4 cards
- Reader sees: Cards that lead with one big result ("12% replied", "25 minutes instead of 6 hours"); a tap opens the quote and the name behind the number.
- Moves: in-view - number counts up over .9s ease-out (or appears with a 12px rise); tap - quote panel opens below .3s; no auto-rotation, no 3D flip.
- Build: `<details>`/`<summary>` or a button-driven region; number in serif, unit in mono; quote in italic serif.
- Narrow: same, stacked · Reduced motion: final number, quote open by default.
- Use when: results, testimonials, pilot outcomes · Avoid when: the number lacks a source.
- Effort: S · Source: https://twain.ai, https://www.wafer.ai

### Numbered rail with step buttons
- Shape: sequence, time-roadmap · fits 4-8 cards
- Reader sees: A row of numbered cards (1 The idea … 6 It comes to life) with next/previous buttons; each press glides to the next card.
- Moves: tap - glide to the next card's offset in 450ms ease-out cubic; swipe/drag works too and snaps to cards; no auto-drift.
- Build: `overflow-x:auto; scroll-snap-type:x mandatory` track; buttons call `scrollTo({left: card.offsetLeft - pad, behavior:"smooth"})`; counter `2 / 6` updates via IntersectionObserver on cards.
- Narrow: same (native swipe) · Reduced motion: instant jump.
- Use when: a story that is naturally a short sequence of pictures · Avoid when: content must be read in full (use a vertical list).
- Effort: S · Source: https://pigeonsmission.com, https://neutomni.com

### Two-layer paper parallax
- Shape: atmosphere · fits 1 scene
- Reader sees: A layered paper landscape (hills behind, field in front) shifts very slightly as they scroll, giving depth like cut paper.
- Moves: scroll-linked - back layer moves up to 8px, front up to 16px across the scene's pass; linear.
- Build: two SVG layers; progress `t = (vh - rect.top)/(vh + rect.height)*2 - 1`; `transform: translate3d(0, t×k px, 0)` in one rAF-throttled handler.
- Narrow: same, halved · Reduced motion: static.
- Use when: a place-based opening (village, farm, campus) · Avoid when: the layers carry information (keep them still).
- Effort: S · Source: https://pigeonsmission.com

### Level map roadmap
- Shape: time-roadmap, place-network · fits 4-8 milestones
- Reader sees: A hand-drawn map with numbered stops (like levels in a game); the path between stops draws as they reach each one, and each stop has a one-line goal.
- Moves: in-view per stop - path segment draws 1.0s in-out, stop marker fills with accent .3s, label fades up 12px; the current stop has one-time ring (see *One-time alarm ring*, calm version).
- Build: SVG map with stop circles and one path; segments via cumulative lengths (`stroke-dasharray` + per-segment offset); stops observed by IntersectionObserver against an HTML list twin beside the map.
- Narrow: map becomes a vertical winding path with stops stacked · Reduced motion: map drawn, stops marked.
- Use when: phases of a programme or project roadmap · Avoid when: the milestones aren't sequential.
- Effort: M · Source: https://pigeonsmission.com

---

## D. The house animation style (rules for the builder)

1. **Motion explains or it does not ship.** Every moving thing must show what changed, what connects to what, or what comes next. If the reason can't be said in a sentence, leave it still. Fox Valuations' discipline is the bar: one sketch draws itself and the ledger rules draw, and nothing else moves.
2. **One moving thing per screen.** At any scroll position only one element animates with intent. At most one ambient loop per screen (a breathing detail, one marching line), and it pauses off-screen (*Loops that sleep off-screen*).
3. **Lines draw like a pen.**
   - Use `stroke-dashoffset` from length to 0. Make the duration proportional to length (about 500–700 px/s, minimum 0.6s, maximum 2.2s per stroke), and start the next stroke at 80–85% of the previous one.
   - Draws use the house in-out `cubic-bezier(.45,.05,.35,1)`. Lines never overshoot, bounce or erase themselves.
4. **Keep to one easing family.**
   - Arrivals: ease-out `cubic-bezier(.22,1,.36,1)` (`.23,1,.32,1` is acceptable).
   - Drawing and moving between states: `cubic-bezier(.45,.05,.35,1)`.
   - Anything tied to scroll: linear (the scroll is the ease).
   - Never use `back`, `elastic` or bounce. Never spring to scroll velocity.
5. **Pace by type of motion.**
   - Arrivals take 0.6–1.0s, line draws 0.8–2.2s, and taps and UI 0.2–0.3s. Ambient loops run 3–7s.
   - Staggers are 60–110ms per line or item, with the whole group capped at 450ms. A hero draw-on finishes within 3.5s.
6. **Text is played; drawings may be scrubbed.**
   - Headlines and paragraphs reveal once as they enter (top at about 88%) and always finish, whatever the scroll speed.
   - Diagrams, paths, gauges and the one scroll-lit statement may follow scroll 1:1. Never fade out text that is still on screen.
7. **Reading order: picture, then headline, then details.**
   - Reveal travel is 16px or less (line masks excepted), blur 6px or less, and scale-in 1.06 or less.
   - Nothing enters from the side, rotates or flies.
8. **One stage, one knob.** To explain a process or a change, keep a single drawing on a sticky stage and let short captions scroll past. Each chapter changes exactly one thing in the drawing, and a counter (`01 / 05`) says where the reader is.
9. **Lines are the connective tissue.**
   - Relationships start as faint dash-dot construction lines (`.93 2.8 9.35 2.8` or dotted `1 8` at 22% ink) and draw solid in ink when explained.
   - Pulses and marching dashes run only on the line being discussed and travel slowly (2.4s or more per traverse).
   - Guides appear, measure, then fade.
10. **Texture is static.**
    - The rice-powder, ink and grain filters (`feTurbulence` plus `feDisplacementMap`) are applied once and never animated per frame.
    - The only moving texture allowed is a mask edge during a one-time reveal (*Ink-bleed reveal*). Chalk section tints stay flat.
11. **One accent does the pointing.**
    - Use the paper neutrals (`#faf9f5`, `#f0eee6`, `#e8e6dc`), ink (`#141413`) and one accent (clay `#d97757` or the TVS kumkum).
    - The accent arrives through motion (a marker sweep, a pen circle, a dot, a single ring) on exactly the thing being argued, and is never a large animated fill.
12. **Number what the reader walks through.** Chapter numerals, `n / N` counters, a reading ruler and step numbers mean that a reader who won't read still knows where they are and how much is left.
13. **Never block or hijack.**
    - No loaders or gates, no smooth-scroll library and no snapping on reading sections. No auto-advancing rails or carousels, and no cursor-only effects.
    - Pinned sections run 3 viewport heights or less.
    - Every pinned or scrubbed sequence has a stacked, static twin below 768px, and every hover has a tap equivalent.
14. **Respect stillness.** Under `prefers-reduced-motion`, and on repeat visits (`sessionStorage`), land on the finished drawing and show the end state with its labels. Content is never hidden from a reader without JS.
15. **End in the ask.** The last meaningful motion on the page resolves into the call to action: the build folds into the button, a pen line underlines the contact, or the route arrives at the final stop.
