# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A study-material repository for the **معلم القرآن (Muallim ul Quran)** course, organised for
students. It is mostly content, not code: ~1 GB of exported slide images plus transcribed
notes (CSV/Markdown) and bilingual question banks (PDF). The only "code" is a few helper
scripts in `tools/`.

## Structure

Everything is organised **by unit** under `units/`:

```
units/unit-NN/
  slides/      slide images — `Unit 0N web slides-NN.jpg` (Unit 03 is `.webp`)
  notes/       vocabulary.csv/.md, grammar.md, ayaat.csv, phrases.csv (U3), exercises.md
  practice/    bilingual question bank: <unit>-questions.md + .pdf
tools/         maintainer scripts (_crop.py, _make_pdf.py, _make_vocab_md.py) + tools/README.md
README.md      student-facing landing page
```

Units 1–3 have notes; Unit 1 also has practice. Units 4–6 currently have `slides/` only.

## Conventions

- **Slide filenames:** `Unit 0N web slides-NN` with zero-padded 2-digit unit and page
  numbers (e.g. `Unit 05 web slides-07.jpg`). Keep page numbers contiguous so sort order
  is correct. Format is per-unit: Unit 03 is `.webp`, the rest `.jpg`.
- **Slides are two-page spreads** (Urdu/Arabic): the **right** page starts the spread and the
  **left** page continues it; page flow runs right→left across spreads.
- **CSV `confidence`** column = certainty of the Arabic transcription (`high`/`med`/`low`);
  `med`/`low` need verification against the slide. See `tools/README.md` for the schema.
- Build artifacts (`*.html` from the PDF step) are git-ignored; commit the `.pdf`, not the HTML.

## Working in this repository

- To read slide *content*, open the image(s) with the Read tool — there is no text source to
  grep. `tools/_crop.py` crops/upscales a region for accurate transcription of dense pages.
- Slide images are large binaries; avoid bulk copying or re-encoding unless asked.
- Regenerate the question PDF with `tools/_make_pdf.py` + headless Chrome (see `tools/README.md`).
