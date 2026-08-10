#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract financial statements from Auto Hall document de référence 2025."""
import os, re

PDF = r"C:\Users\salah eddine\Desktop\Reasearch\Reasearch\96 Documents Réels\01 Documents de référence AMMC\Auto Hall — Document de Référence 2025.pdf"
OUT = r"C:\Users\salah eddine\Desktop\Reasearch\Reasearch\98 Outils\extracted"
os.makedirs(OUT, exist_ok=True)

try:
    import pymupdf
except ImportError:
    import fitz as pymupdf

doc = pymupdf.open(PDF)
print(f"PAGES: {len(doc)}")

# locate key sections
keywords = ["BILAN", "Compte de produits et charges", "Tableau de financement",
            "ETIC", "Etat des informations complémentaires", "Etats financiers",
            "États financiers", "Rapport général", "Rapport du commissaire",
            "Certification"]
hits = {}
for i, page in enumerate(doc):
    text = page.get_text()
    for kw in keywords:
        if kw.lower() in text.lower():
            hits.setdefault(kw, []).append(i + 1)

for kw, pages in sorted(hits.items()):
    print(f"{kw}: pages {pages[:12]}")

# dump the financial statements pages to text files (search bilan actif/passif + CPC)
def dump_range(a, b, name):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as fh:
        for i in range(a - 1, min(b, len(doc))):
            fh.write(f"\n===== PAGE {i+1} =====\n")
            fh.write(doc[i].get_text())

bilan_pages = hits.get("BILAN", [])
# real financial statements block = pages 138-166 (Rapports CAC + analyse) ; tables later
dump_range(138, 166, "bilan.txt")
dump_range(170, 212, "tables.txt")
cpc_pages = hits.get("Compte de produits et charges", [])
if cpc_pages:
    dump_range(cpc_pages[0], cpc_pages[0] + 4, "cpc.txt")
tf_pages = hits.get("Tableau de financement", [])
if tf_pages:
    dump_range(tf_pages[0], tf_pages[0] + 3, "tf.txt")
print("DONE")
