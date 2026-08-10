# -*- coding: utf-8 -*-
"""Dump the full rubrique 24/25 (immobilisations financières) section of the PCGE."""
from pathlib import Path

txt = Path(r"C:\Users\salah eddine\Desktop\Reasearch\Reasearch\96 Documents Réels\00 Textes officiels\pcm_out.txt").read_text(encoding="utf-8", errors="replace")
lines = txt.splitlines()

# find section start and end
start = end = None
for i, line in enumerate(lines):
    if "24/25 IMMOBILSATIONS FINANCIERES" in line.upper():
        start = i
    if start is not None and i > start and "AMORTISSEMENTS" in line.upper() and "28" in line:
        # stop before amortissements section for classe 2 (2812x appears at 237)
        if i > start + 3:
            end = i
            break
# fallback end: the "35 TITRES" line
if end is None:
    for i, line in enumerate(lines):
        if start and i > start and "35 TITRES" in line.upper():
            end = i
            break
if end is None:
    end = start + 80

print(f"Section {start}..{end}")
for j in range(start, min(end, len(lines))):
    print(f"{j:4d} | {lines[j]}")
