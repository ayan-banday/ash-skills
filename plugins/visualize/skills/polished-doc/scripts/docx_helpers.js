// Helpers for building the Word version of a Clear Documents file with docx-js.
// Require this from your build script:  const H = require('<skill>/scripts/docx_helpers.js')
// Needs the `docx` npm package (npm install docx in a temp folder if require fails).
//
// The Word version carries the same words, headings, and order as the PDF. Visuals come in
// as PNGs from figures.py. Colours come from the same palette (pass hex without '#').
//
// Example at the bottom runs with:  node docx_helpers.js  (writes sample.docx)

const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, ImageRun, Table, TableRow, TableCell,
  WidthType, BorderStyle, ShadingType, LevelFormat, AlignmentType,
} = require('docx');

function make(pal) {
  const P = Object.assign({ ink: '1A2428', muted: '4C585D', line: 'D4DCDE', primary: '376979', accent: 'B07829' }, pal || {});
  const none = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' };

  // "**bold** plain" -> runs
  const runs = (s, o = {}) => s.split(/(\*\*[^*]+\*\*)/).filter(Boolean).map(t =>
    t.startsWith('**') ? new TextRun({ text: t.slice(2, -2), bold: true, ...o }) : new TextRun({ text: t, ...o }));

  const para = (s, o = {}) => new Paragraph({ children: runs(s, o.run || {}), spacing: { after: 140, line: 288 }, ...(o.p || {}) });
  const lede = s => para(s, { run: { size: 25, color: P.muted } });
  const eyebrow = (s, rule = true) => new Paragraph({
    keepNext: true, spacing: { before: rule ? 300 : 0, after: 80 },
    border: rule ? { top: { style: BorderStyle.SINGLE, size: 12, color: P.primary, space: 12 } } : undefined,
    children: [new TextRun({ text: s.toUpperCase(), bold: true, size: 16, color: P.muted, characterSpacing: 30 })],
  });
  const title = s => new Paragraph({ heading: HeadingLevel.TITLE, children: [new TextRun(s)] });
  const h1 = s => new Paragraph({ heading: HeadingLevel.HEADING_1, keepNext: true, children: [new TextRun(s)] });
  const h2 = s => new Paragraph({ heading: HeadingLevel.HEADING_2, keepNext: true, children: [new TextRun(s)] });
  const bullet = s => new Paragraph({ numbering: { reference: 'bullets', level: 0 }, children: runs(s), spacing: { after: 80, line: 288 } });
  const step = s => new Paragraph({ numbering: { reference: 'steps', level: 0 }, children: runs(s), spacing: { after: 80, line: 288 } });
  const callback = s => para(s, { p: { border: { left: { style: BorderStyle.SINGLE, size: 18, color: P.primary, space: 12 } }, indent: { left: 240 } } });

  // widthPx <= 600 keeps it inside A4 margins; height keeps the PNG's aspect ratio
  const image = (file, w, h, widthPx = 560) => new Paragraph({
    keepLines: true, spacing: { before: 120, after: 200 },
    children: [new ImageRun({ type: 'png', data: fs.readFileSync(file), transformation: { width: widthPx, height: Math.round(widthPx * h / w) } })],
  });

  // rows: array of arrays of strings; first row is the header. widths in DXA, summing to the table width
  const table = (rows, widths) => {
    const total = widths.reduce((a, b) => a + b, 0);
    const cell = (t, w, head) => new TableCell({
      width: { size: w, type: WidthType.DXA }, margins: { top: 80, bottom: 80, left: 120, right: 120 },
      borders: { top: none, left: none, right: none, bottom: { style: BorderStyle.SINGLE, size: head ? 12 : 4, color: head ? P.primary : P.line } },
      children: [new Paragraph({ children: head
        ? [new TextRun({ text: t.toUpperCase(), bold: true, size: 16, color: P.muted, characterSpacing: 20 })]
        : runs(t, { size: 21 }) })],
    });
    return new Table({
      width: { size: total, type: WidthType.DXA }, columnWidths: widths,
      rows: rows.map((r, i) => new TableRow({ tableHeader: i === 0, cantSplit: true, children: r.map((t, j) => cell(t, widths[j], i === 0)) })),
    });
  };

  // the one action at the end: a filled single-cell table
  const decision = (head, body, width = 9000) => new Table({
    width: { size: width, type: WidthType.DXA }, columnWidths: [width],
    rows: [new TableRow({ cantSplit: true, children: [new TableCell({
      width: { size: width, type: WidthType.DXA }, shading: { type: ShadingType.CLEAR, color: 'auto', fill: P.primary },
      margins: { top: 300, bottom: 300, left: 360, right: 360 }, borders: { top: none, bottom: none, left: none, right: none },
      children: [
        new Paragraph({ spacing: { after: 140 }, children: [new TextRun({ text: head, bold: true, size: 30, color: 'FFFFFF', font: 'Georgia' })] }),
        new Paragraph({ spacing: { line: 300 }, children: [new TextRun({ text: body, color: 'FFFFFF' })] }),
      ] })] })],
  });

  const doc = children => new Document({
    styles: {
      default: { document: { run: { font: 'Calibri', size: 22, color: P.ink } } },
      paragraphStyles: [
        { id: 'Title', name: 'Title', basedOn: 'Normal', run: { font: 'Georgia', size: 48, bold: true, color: P.ink }, paragraph: { spacing: { after: 200 } } },
        { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: 'Georgia', size: 34, bold: true, color: P.ink }, paragraph: { spacing: { before: 80, after: 160 }, outlineLevel: 0 } },
        { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: 'Georgia', size: 26, bold: true, color: P.primary }, paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 1 } },
      ],
    },
    numbering: { config: [
      { reference: 'bullets', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 420, hanging: 260 } } } }] },
      { reference: 'steps', levels: [{ level: 0, format: LevelFormat.DECIMAL, text: '%1.', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 420, hanging: 360 } }, run: { bold: true, color: P.primary } } }] },
    ] },
    sections: [{ properties: { page: { margin: { top: 1000, bottom: 1000, left: 1300, right: 1300 } } }, children }],
  });

  const save = (d, path) => Packer.toBuffer(d).then(b => { fs.writeFileSync(path, b); console.log('wrote', path); });

  return { runs, para, lede, eyebrow, title, h1, h2, bullet, step, callback, image, table, decision, doc, save,
    spacer: () => new Paragraph({ spacing: { after: 120 }, children: [] }) };
}

module.exports = make;

if (require.main === module) {
  const H = make({ primary: '376979' });
  const d = H.doc([
    H.eyebrow('Proposal · sales team', false),
    H.title('Reply to every new lead within one hour'),
    H.lede('Last month our first reply took **19 hours** on average.'),
    H.eyebrow('1 · Where the time goes'),
    H.h1('Leads wait for the morning sort before anyone owns them'),
    H.para('Every lead lands in a shared inbox, and **nobody owns it until 9:30 the next morning**.'),
    H.step('The form sends each lead **straight to the person on duty**.'),
    H.step('They reply within one hour.'),
    H.spacer(),
    H.table([['Day', 'On duty'], ['Monday', 'Ankit'], ['Tuesday', 'Sara']], [2000, 3200]),
    H.spacer(),
    H.decision('Approve the rota by Friday 23 October', 'If you approve, lead duty starts on Monday.'),
  ]);
  H.save(d, 'sample.docx');
}
