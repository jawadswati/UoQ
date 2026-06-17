#!/usr/bin/env python3
"""Generate a grouped, human-readable vocabulary.md from vocabulary.csv."""
import csv, sys
from collections import OrderedDict

csv_path, md_path = sys.argv[1], sys.argv[2]

SECTION_TITLES = {
    "bahut-aasaan": "Slide 1 — قرآن کریم کے چند بہت آسان الفاظ (Very easy words)",
    "mazeed-alfaaz": "Slide 2 — قرآن کریم کے چند مزید الفاظ (A few more words)",
    "mazeed-aasaan": "Slide 3 — قرآن کریم کے چند مزید آسان الفاظ (More easy words)",
    "mashhoor": "Slide 4 — قرآن کریم کے چند مشہور الفاظ (Famous words)",
    "mazeed-alfaaz-2": "Slide 5 — قرآن کریم کے چند مزید الفاظ (More words)",
    "mazeed-aasaan-qurani": "Slide 6 — چند مزید آسان قرآنی الفاظ (More easy Quranic words)",
    "aasaan-mashhoor": "Slide 7 — مزید آسان اور مشہور قرآنی الفاظ (More easy & famous words)",
    "chand-aasaan": "Slide 8 — قرآن کریم کے چند آسان الفاظ (A few easy words)",
    "sifaat-allah": "Slide 9 — اللہ تعالیٰ کی چند مشہور صفات (Well-known attributes of Allah)",
    "jamaa-plurals": "Slide 10 — جمع کے چند آسان قرآنی الفاظ (Easy Quranic plurals)",
    "jamaa-aat": "Slide 11 — جمع کے مزید آسان قرآنی الفاظ (More plurals, ـات pattern)",
}

rows = list(csv.DictReader(open(csv_path, encoding="utf-8")))
groups = OrderedDict()
for r in rows:
    groups.setdefault(r["section"], []).append(r)

out = ["# Unit 01 — Vocabulary", "",
       f"Total entries: **{len(rows)}**. Source: slide images in `Unit 01/`. "
       "Confidence refers to the Arabic transcription (see `../README.md`).",
       "Entries marked `book-gloss` carry the Urdu meaning printed in the book; "
       "others use a standard concise meaning.", ""]

for sec, items in groups.items():
    out.append("## " + SECTION_TITLES.get(sec, sec))
    out.append("")
    out.append("| # | Arabic | Urdu meaning | Notes | Conf |")
    out.append("|---|--------|--------------|-------|------|")
    for i, r in enumerate(items, 1):
        conf = r["confidence"]
        flag = " [?]" if conf in ("med", "low") else ""
        out.append(f"| {i} | {r['arabic']}{flag} | {r['urdu']} | {r['notes']} | {conf} |")
    out.append("")

open(md_path, "w", encoding="utf-8").write("\n".join(out))
print("wrote", md_path, "with", len(rows), "rows in", len(groups), "sections")
