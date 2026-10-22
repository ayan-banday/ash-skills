# Mobile Site Playbook: Turn a Desktop Pitch Page Into a Great Phone Page

From the TVS pitch page, 2026-10-22: [Carrying the TVS Way](https://ayan-banday.github.io/sites/carrying-the-tvs-way/).

## What this playbook is for

You built a pitch site on a laptop. It looks great at 1440px wide. Now it has to look just as good on a phone, where most people will open the link. This page gives you the steps, the decisions and the traps from the TVS job, so the next one takes an evening.

Three versions of the TVS page taught these lessons:

- **Version 1** blocked phones with a screen that said "Open this on your laptop".
- **Version 2** gave phones their own layout, but lost much of the motion.
- **Version 3** brought the motion back and kept the desktop exactly as it was.

## The process: eight steps

1. **Get both versions and diff them.** A diff shows every line that changed between two files. On TVS it proved the desktop CSS was untouched; only phone CSS and script were added.
   ```bash
   diff old/index.html new/index.html | less
   ```
2. **Shoot the page like a visitor.** Run `shoot.js` at phone size (390 x 844, touch on), then at desktop size (1440 x 900). It scrolls down and screenshots every screen. Tile the shots into contact sheets so you can compare twenty screens in one look:
   ```bash
   montage out/*.png -tile 6x -geometry 260x+8+8 sheet.png
   ```
3. **List every desktop moment and what the phone does with it.** A moment is one animation or interaction. Write a two-column table: desktop moment, phone version. The TVS table is below.
4. **Find where the phone lost motion.** Scroll the phone shots and ask, "does this chapter move when I arrive?" On TVS we found five losses (listed below).
5. **Fix with a scripted patch.** Write a small Python script where each replacement must match the old text exactly once. If a match fails, the script stops before writing anything, so the file is never half-edited.
6. **Test the matrix.** Four runs: phone 390 with normal motion, phone 390 with reduce motion, tablet 768, desktop 1440. Check for script errors, elements stuck hidden and a page wider than the screen.
7. **Publish with `post-page-online`.** It wraps the page, runs `check_page.py`, adds the page to the sites repo's root `index.html` and README, pushes, confirms the GitHub Pages build and takes a live phone screenshot through Firecrawl.
8. **Check on your real phone and send screenshots.** On TVS, Ash's first real check found icons sitting off-centre in the orbit dial. The test screenshots showed it too, but at contact-sheet size nobody saw it. Zoom in on every small part (icons, badges, labels) before you call it done; real-phone screenshots are the final test.

## The TVS moment table

| Desktop moment | Phone version |
|---|---|
| Hero kolam draws itself | Kept; it also turns slowly as you scroll away |
| Four needs cards in a row | A sticky deck: each card pins and the next slides over it |
| Kolam key cycles through its parts on a timer | Scroll lights each part, one at a time |
| Chapter medallions, static | Each one draws itself as it arrives |
| Snake line, paper-to-screen, translator, design frames | Kept, each plays when it reaches the screen |
| Constellation map | One-screen map: tap a point to focus it, pulses travel the lines |
| Orbit with a travelling dot | A pinned dial moved by your scroll |
| Guru circle | Pins in place; callouts light up as you read |

## The five places the phone lost motion

1. **Reduce motion froze the whole page.** `prefers-reduced-motion: reduce` is a phone setting that asks sites to move less. Many Android phones switch it on with battery saver; iPhones call it "Reduce Motion". The old CSS killed every animation with `*{transition:none!important;animation:none!important}`, and the script skipped every animation too.
2. **The big Indian-way kolam shrank to a 112px icon.**
3. **The kolam key never drew itself on phones.**
4. **The orbit dial never moved on its own.**
5. **"The guru" label sat on top of the ring drawing.**

## The decisions to reuse

### Tell the same story with the same words, staged for a thumb

Keep every word. Change only how each moment plays:

- **Turn hover into tap or scroll.** Phones have no mouse to hover with.
- **Turn auto-playing cycles into scroll-driven steps.** The reader controls the pace with a thumb.
- **Turn wide diagrams into pinned dials or one-screen maps.**
- **Turn card rows into a sticky deck.**

"Sticky" means CSS `position: sticky`: the element scrolls normally, then pins to the top of the screen while its section scrolls past.

### Let reduce motion keep gentle motion

Keep line drawing, fades, colour changes and highlights. Stop anything that slides, spins, scales on scroll or loops forever. Use two separate flags in the script:

```js
// still: the reader asked for less motion. Use it only to stop movement.
const still = matchMedia('(prefers-reduced-motion: reduce)').matches;
// noIO: an old browser with no IntersectionObserver. Show everything at once.
const noIO = !('IntersectionObserver' in window);
```

IntersectionObserver is a browser feature that tells your script when an element scrolls into view. It is how "play when it arrives" works.

In CSS, cancel only the movement:

```css
@media (prefers-reduced-motion: reduce) {
  .pre, .plain .w { transform: none !important; }
}
```

A media query is a block of CSS that applies only when the screen or setting matches a condition.

### Keep the centrepiece big

The main visual should fill about three-quarters of the phone's width and draw itself, as it does on desktop.

```css
.way .key-kolam { width: min(76vw, 38svh); justify-self: center; }
```

`vw` is 1% of the screen's width; `svh` is 1% of the screen's height with the browser bars showing.

### Make every chapter's visual move once when it arrives

- **Redraw on arrival.** The kolam key draws itself again when you reach it.
- **Run a dial one lap, then hand it to the scroll.** The orbit dot ran one lap lighting each of its five steps; after that, your scroll moved it.

### Put labels that cross a drawing on a pill

Give the label the paper colour as its background and a thin ink outline:

```css
.label { padding: 3px 10px 4px; border-radius: 999px;
  background: var(--paper); box-shadow: 0 0 0 1.4px var(--ink); z-index: 1; }
```

### Pinned visuals: keep them from covering the content

A pinned visual sits on top of the content that scrolls under it, so two things can go wrong: it covers the text, or its own parts slip out of place.

- **Keep the pinned part short.** The TVS dial block is about 250px tall on an 844px phone, so about two-thirds of the screen stays free for reading.
- **Fade its bottom edge.** Give the pinned block the section's background with a mask that fades to clear over the last 15 to 20%, so cards slide softly under it.
  ```css
  .orbit-mini::before{content:"";position:absolute;inset:0;z-index:-1;background:var(--paper);
    mask-image:linear-gradient(#000 82%,transparent)}
  ```
- **Pin it inside its own section only.** Wrap the pinned visual and its list in one container, so it unpins when the list ends and never covers the next chapter.
- **Light the step you are reading.** The step under the dial gets a dark outline and the steps you passed stay bright, so the eye always knows which step the dial is showing.
- **Write a pinned visual's CSS with the child selector `>`.** The TVS bug: the rule `.om-stage svg{position:absolute;inset:0}` was meant for the dial's ring drawing, but it also matched the small icon inside every step circle, so each icon jumped to its circle's top-left corner and sat over the outline. `.om-stage>svg` matches only the ring. Any time a stage holds a drawing plus icons, aim the layout rule at the drawing alone.

### Leave the desktop untouched, and prove it

Screenshot the desktop before and after your patch, then compare each pair. Animations caught at slightly different moments change a few thousand pixels, so on TVS any pair above 20,000 changed pixels was flagged for a look. None were:

```bash
for f in before/*.png; do
  compare -metric AE -fuzz 8% "$f" "after/$(basename "$f")" null: 2>&1; echo " $f"
done
```

`-fuzz 8%` ignores tiny colour differences from anti-aliasing (the soft edge pixels on text and lines). On TVS every pair matched.

## Gotchas

- **A descendant selector catches icons too.** `.stage svg` matches every svg inside the stage, including icons; use `.stage>svg` for the stage's own drawing.
- **`display: contents` draws no box.** The element's children stay, but the element itself has no box, so fade or slide effects on it do nothing. Put the effect on the children.
- **IntersectionObserver never fires for an element hidden with `display: none`.** Good news: a phone-only and a desktop-only copy of a visual can share one script, and only the visible copy plays.
- **The test browser misses what a real phone shows.** Headless Chromium (a browser that runs with no window) differs from a phone in browser bars, font loading and pixel density. Get a real-phone screenshot before you send the link.
- **The viewport tag must be in the `<head>`.** Without it, phones show a tiny zoomed-out page and ignore your media queries (Kevin Powell):
  ```html
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  ```
- **Most phone fixes are size, margins and padding.** Both videos agree. Fix those first.
- **Find breakpoints by testing widths.** A breakpoint is the width where a media query switches the layout. Drag the window narrower until something breaks, and put the breakpoint there. Device sizes change every year.
- **Add a safety net for fast flicks.** A thumb flick can skip past an element before its "play on arrival" fires. On every scroll, reveal anything already on screen or above it, so nothing stays hidden.

## Checklist before sending the link

1. **The viewport tag is in the `<head>`.**
2. **Phone 390 shots show every chapter moving once when it arrives.**
3. **Phone 390 with reduce motion still draws lines and fades blocks in.**
4. **The centrepiece fills about three-quarters of the phone width.**
5. **No label sits on top of a drawing without a pill.**
6. **Pinned visuals leave the text readable, and their icons sit centred (zoom in to check).**
7. **The tablet 768 shots look right.**
8. **Desktop before-and-after `compare` flags no pair above 20,000 changed pixels.**
9. **The test reports no script errors, nothing stuck hidden and no sideways scroll.**
10. **You have real-phone screenshots of the live link.**

## Reuse these

The test scripts live in `docs/mobile-site-tools/`. They need Node and Playwright. Both have a line `executablePath: '/opt/pw-browsers/chromium'`; that is the browser's path in a Claude cloud session. On a laptop, delete that option.

**Shoot every screen** (`shoot.js <html> <outdir> <width> <height> [step] [reduce]`):

```bash
T=/home/user/ash-skills/docs/mobile-site-tools
export NODE_PATH=$(npm root -g)
mkdir -p shots/phone shots/phone-still shots/tablet shots/desk
node $T/shoot.js "$PWD/index.html" shots/phone 390 844
node $T/shoot.js "$PWD/index.html" shots/phone-still 390 844 675 reduce
node $T/shoot.js "$PWD/index.html" shots/tablet 768 1024
node $T/shoot.js "$PWD/index.html" shots/desk 1440 900
```

Each run prints the page height, the number of shots, the page width against the screen width (equal means no sideways scroll) and any script errors.

**Shoot key moments mid-animation and after** (`focus.js <html> <outdir> <width> <height> [reduce]`):

```bash
mkdir -p shots/focus && node $T/focus.js "$PWD/index.html" shots/focus 390 844
```

It reports `stuckHidden` (elements still waiting to appear after the whole scroll; it should be 0), `scrollWidth` and errors. Its selectors (`.key`, `.way`, `#orbit-list` and so on) are the TVS sections; swap in your own page's sections first.

**Make contact sheets:**

```bash
for d in phone phone-still tablet desk; do
  montage shots/$d/*.png -tile 6x -geometry 260x+8+8 shots/$d-sheet.png
done
```

**The patch pattern:**

```python
import sys
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def R(old, new, n=1):
    global s
    c = s.count(old)
    if c != n: sys.exit(f'expected {n}, found {c}: {old[:90]!r}')
    s = s.replace(old, new)

R('old exact text', 'new text')
# ... one R() per change ...
open(p, 'w', encoding='utf-8').write(s); print('patched')
```

The file is written only at the end, after every match has passed.
