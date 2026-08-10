# -*- coding: utf-8 -*-
"""List available generateContent-capable models for the key."""
import json
import urllib.request
from pathlib import Path

key = ""
for line in Path(r"C:\Users\salah eddine\bookrag\.env").read_text(encoding="utf-8").splitlines():
    if line.startswith("GEMINI_API_KEY="):
        key = line.split("=", 1)[1].strip()

req = urllib.request.Request(f"https://generativelanguage.googleapis.com/v1beta/models?key={key}")
with urllib.request.urlopen(req, timeout=30) as r:
    data = json.loads(r.read().decode("utf-8"))

print("=== models supporting generateContent ===")
for m in data.get("models", []):
    methods = m.get("supportedGenerationMethods", [])
    if "generateContent" in methods:
        print(f"  {m['name']}")
