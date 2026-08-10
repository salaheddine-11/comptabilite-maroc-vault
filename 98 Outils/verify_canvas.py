# -*- coding: utf-8 -*-
"""Verify canvas layout: group nodes by column x, list colors, check y ordering."""
import json
from pathlib import Path

c = json.loads(Path(r"C:\Users\salah eddine\Desktop\Reasearch\Reasearch\Concept Graph.canvas").read_text(encoding="utf-8"))
nodes = [n for n in c["nodes"] if n["type"] == "file"]
print(f"nodes: {len(nodes)}  edges: {len(c.get('edges', []))}")

# group by rounded column x
cols = {}
for n in nodes:
    col = round(n["x"] / 400)
    cols.setdefault(col, []).append(n)

print(f"\n=== columns ({len(cols)}) ===")
for col in sorted(cols):
    items = sorted(cols[col], key=lambda n: n["y"])
    cats = {}
    for n in items:
        cats.setdefault(n.get("color", "?"), 0)
        cats[n.get("color", "?")] += 1
    first = items[0]["file"].split("/")[0]
    print(f"col x~{col*400:>4}: {len(items):>2} cards | first file: {first} | colors: {cats}")

# color counts
import collections
cc = collections.Counter(n.get("color", "none") for n in nodes)
print(f"\ncolor distribution: {dict(cc)}")
print(f"cards with color: {sum(1 for n in nodes if 'color' in n)}/{len(nodes)}")
