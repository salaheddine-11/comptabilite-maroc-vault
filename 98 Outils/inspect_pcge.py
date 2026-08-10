# -*- coding: utf-8 -*-
"""Inspect rubriques 24-26 of the official Plan Comptable Marocain text."""
import re
from pathlib import Path

txt = Path(r"C:\Users\salah eddine\Desktop\Reasearch\Reasearch\96 Documents Réels\00 Textes officiels\pcm_out.txt").read_text(encoding="utf-8", errors="replace")

lines = txt.splitlines()
print("=== lines mentioning 'Immobilisations financières' or rubrique 24/25 ===")
for i, line in enumerate(lines):
    if re.search(r"24\s|25\s|26\s|Immobilisations financi", line) and len(line) < 80:
        print(f"{i:4d} | {line}")

print("\n=== context around 251 (titres de participation) ===")
for i, line in enumerate(lines):
    if "Titres de participation" in line or "titres de participation" in line:
        lo = max(0, i - 6)
        hi = min(len(lines), i + 6)
        for j in range(lo, hi):
            print(f"{j:4d} | {lines[j]}")
        print("---")
