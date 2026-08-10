# -*- coding: utf-8 -*-
"""Check PCGE dépréciations (29x) + list Gemini embedding models available for the key."""
import json
import os
import re
import urllib.request
from pathlib import Path

# 1) PCGE deprecation accounts
txt = Path(r"C:\Users\salah eddine\Desktop\Reasearch\Reasearch\96 Documents Réels\00 Textes officiels\pcm_out.txt").read_text(encoding="utf-8", errors="replace")
print("=== PCGE 29x / dépréciations lines ===")
for i, line in enumerate(txt.splitlines()):
    if re.search(r"29\d{2}|D.pr.ciation", line) and len(line) < 70:
        print(f"{i:4d} | {line}")

# 2) embedding models for the key
key = ""
for p in [Path(r"C:\Users\salah eddine\bookrag\.env")]:
    for line in p.read_text(encoding="utf-8").splitlines():
        if line.startswith("GEMINI_API_KEY="):
            key = line.split("=", 1)[1].strip()
req = urllib.request.Request(f"https://generativelanguage.googleapis.com/v1beta/models?key={key}")
with urllib.request.urlopen(req, timeout=30) as r:
    data = json.loads(r.read().decode("utf-8"))
print("\n=== embedding-capable models (v1beta) ===")
for m in data.get("models", []):
    methods = m.get("supportedGenerationMethods", [])
    name = m["name"]
    if any("embed" in mm.lower() for mm in methods) or "embed" in name.lower():
        print(f"  {name} -> {methods}")
