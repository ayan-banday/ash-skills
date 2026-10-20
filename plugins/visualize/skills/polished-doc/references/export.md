# Export

The skill writes the content once, as HTML from `assets/template.html`, and exports it to the format the user asked for. **PDF is the default.** The words, order, palette, and visuals are the same in every format.

## Contents
- PDF
- Word (.docx)
- Google Docs
- HTML
- Setup and troubleshooting

## PDF

```bash
python scripts/build_pdf.py doc.html doc.pdf --seed 9 --footer "Onboarding plan · draft" --save-html final.html
python scripts/check_pages.py doc.pdf --sheets shots/     # --allow 1 when page 1 is a cover
```

- `--seed` applies a palette; leave it off to keep the palette already in the file.
- `--harmony` and `--hue` fix the harmony type or base hue for the seed.
- `--save-html` writes the palette-applied HTML (the HTML deliverable); the working file keeps the template palette.
- `--size Letter` for US readers.
- `--allow 1` exempts the cover. Add other page numbers only for deliberate short pages.
- Open the sheets in `shots/` and look at every page before handing over.

## Word (.docx)

Use when the user asks for Word, wants to edit the result in Word, or must submit a .docx. Read the docx skill for docx-js mechanics if it is available.

1. Build and check the PDF first; it is the visual reference.
2. Export the visuals as images: `python scripts/figures.py doc.html figs/`. It writes `fig-01.png` and onward plus `sizes.txt` with each image's pixel size.
3. Write a small Node script that requires `scripts/docx_helpers.js`, passes the palette hex values (without `#`), and rebuilds the content in order: `eyebrow`, `title`, `lede`, `h1`, `h2`, `para`, `bullet`, `step`, `callback`, `table`, `image`, `decision`. Bold uses `**double asterisks**` inside strings. Run `node scripts/docx_helpers.js` once to see a working sample.
4. Image size: width 560 px or less, height = width × h / w from `sizes.txt`.
5. Verify: open the .docx in Word and export to PDF (on Windows, Word COM via PowerShell; elsewhere LibreOffice `soffice --headless --convert-to pdf`), render pages, and look. Check that each figure sits with its heading (`keepNext` is set on headings) and nothing is orphaned.

Word cannot run the HTML layout, so expect small differences: chips become comma lists or a two-column table, sketches become images, the decision box is a one-cell shaded table.

## Google Docs

- If a Google Docs connector or docs skill is available, use it and follow its instructions; carry over headings, bold, lists, tables, and images.
- Otherwise build the .docx and tell the user to upload it to Drive and open it with Google Docs. Formatting survives well; fonts may fall back.

## HTML

The built HTML (with the palette applied) works as a page in its own right. For a screen-first, scrolling page with animation, the brief-page skill is the better tool; this skill's HTML is print-shaped.

## Setup and troubleshooting

| Problem | Fix |
|---|---|
| `playwright` missing | `pip install playwright` then `python -m playwright install chromium`. The scripts fall back to installed Microsoft Edge. |
| `pypdfium2` missing (checker) | `pip install pypdfium2 pillow` |
| `docx` npm package missing | `npm install docx` in a temp folder and run the Node script from there |
| Fonts look like Georgia and Segoe | Google Fonts did not load (offline). The fallbacks are fine; mention it in the hand-off. |
| Chrome or Python says file not found for a file that exists | Windows path over 260 characters. Build in a short folder (for example `%TEMP%\cd`) and copy the result. |
| A bash heredoc with mixed quotes fails | Write the script with the file tool instead of a heredoc. |
