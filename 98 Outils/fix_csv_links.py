# -*- coding: utf-8 -*-
"""Fix Fiche column in CSV: [N — Name] -> [[N — Name]] wikilinks."""
import re
from pathlib import Path

p = Path(r"C:\Users\salah eddine\Desktop\Reasearch\Reasearch\95 Ressources\Inventaire des Thèmes Comptables Marocains.csv")
lines = p.read_text(encoding="utf-8").splitlines()

fixed = 0
out = []
for line in lines:
    # pattern: ,[44 — Name], -> ,[[44 — Name]],
    new = re.sub(r",\[(\d+) — ([^\]]+)\],", r",[[\1 — \2]],", line)
    if new != line:
        fixed += 1
    out.append(new)

p.write_text("\n".join(out) + "\n", encoding="utf-8")
print(f"fixed {fixed} rows")
# sanity: show new rows
for line in out[-10:]:
    print(line[:110])
