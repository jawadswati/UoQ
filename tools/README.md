# Tools (for maintainers)

Scripts used to transcribe the slide images and build the study material. Students do not
need these — see the top-level [README](../README.md).

```
tools/
  _crop.py          crop + upscale a region of a slide for accurate reading/transcription
  _make_vocab_md.py generate a unit's notes/vocabulary.md from notes/vocabulary.csv
  _make_pdf.py      render a bilingual question-bank .md to print-styled HTML (for PDF)
```

Requires Python 3 with Pillow (for `_crop.py`) and, for PDFs, Google Chrome (headless) plus
the Noto Naskh Arabic and Noto Nastaliq Urdu fonts.

## Data files (in each `units/unit-NN/notes/`)

| File | Columns / contents |
|------|--------------------|
| `vocabulary.csv` | `slide, section, arabic, urdu, notes, confidence` |
| `ayaat.csv` | `slide, [lesson,] topic, arabic, [urdu,] confidence` |
| `phrases.csv` (Unit 3) | `slide, lesson, type, arabic, urdu, confidence` |
| `grammar.md`, `exercises.md` | human-readable notes |

`confidence` = how sure the Arabic transcription is (`high`/`med`/`low`). `med`/`low` should
be verified against the slide. Tags in `notes`: `cognate`, `book-gloss`, `fem-ta`,
`proper-name-no-al`, `sifat`, `singular→plural`, etc.

## Regenerate

```bash
# vocabulary.md from vocabulary.csv
/usr/bin/python3 tools/_make_vocab_md.py \
    units/unit-01/notes/vocabulary.csv units/unit-01/notes/vocabulary.md

# crop a slide region (fractional coords x0 y0 x1 y1, optional scale)
/usr/bin/python3 tools/_crop.py "units/unit-01/slides/Unit 01 web slides-12.jpg" \
    0.62 0.06 1.0 1.0 /tmp/out.jpg 1.0

# question-bank PDF
/usr/bin/python3 tools/_make_pdf.py \
    units/unit-01/practice/unit-01-questions.md /tmp/q.html
google-chrome --headless=new --no-pdf-header-footer \
    --print-to-pdf=units/unit-01/practice/unit-01-questions.pdf /tmp/q.html
```

## Source

Slides are exported from **معلم القرآن — Muallim ul Quran** (arabicpakistan.com). Each slide
image is a two-page spread; being Urdu/Arabic the **right** page starts the spread and the
**left** page continues it. Page flow runs right→left across spreads.
