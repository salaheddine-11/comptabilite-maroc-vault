# -*- coding: utf-8 -*-
"""Check gemini-3.6-flash availability + quick generate test."""
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

print("=== all 3.x flash models ===")
for m in data.get("models", []):
    if "3." in m["name"] and "flash" in m["name"]:
        methods = m.get("supportedGenerationMethods", [])
        print(f"  {m['name']} -> gen={'generateContent' in methods}")

for cand in ["models/gemini-3.6-flash", "models/gemini-3.6-flash-lite"]:
    url = f"https://generativelanguage.googleapis.com/v1beta/{cand}:generateContent?key={key}"
    body = json.dumps({"contents": [{"parts": [{"text": "Dis ok"}]}]}).encode()
    req2 = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req2, timeout=30) as r2:
            out = json.loads(r2.read().decode())
        print(f"{cand}: OK -> {out['candidates'][0]['content']['parts'][0]['text'][:40]}")
    except Exception as e:
        print(f"{cand}: FAIL -> {e}")
