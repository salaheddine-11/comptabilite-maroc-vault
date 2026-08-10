# -*- coding: utf-8 -*-
"""Render Concept Graph.canvas to an SVG preview (scaled) for visual verification."""
import json
import xml.sax.saxutils as sax
from pathlib import Path

CANVAS = Path(r"C:\Users\salah eddine\Desktop\Reasearch\Reasearch\Concept Graph.canvas")
OUT = Path(r"C:\Users\salah eddine\Desktop\Reasearch\Reasearch\98 Outils\canvas_preview.svg")

data = json.loads(CANVAS.read_text(encoding="utf-8"))
nodes = [n for n in data["nodes"] if n["type"] == "file"]
edges = data.get("edges", [])

# bounds
min_x = min(n["x"] for n in nodes)
min_y = min(n["y"] for n in nodes)
max_x = max(n["x"] + n["width"] for n in nodes)
max_y = max(n["y"] + n["height"] for n in nodes)
W, H = max_x - min_x, max_y - min_y
SCALE = 0.5  # shrink for viewing
pad = 20

nid2node = {n["id"]: n for n in nodes}
COLORS = {"1": "#ef4444", "2": "#f97316", "3": "#eab308", "4": "#22c55e", "5": "#06b6d4", "6": "#a855f7", None: "#94a3b8"}

parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W*SCALE+pad*2:.0f}" height="{H*SCALE+pad*2:.0f}" '
         f'viewBox="{-pad} {-pad} {W*SCALE+pad*2} {H*SCALE+pad*2}" font-family="Segoe UI, sans-serif">']
parts.append(f'<rect x="{-pad}" y="{-pad}" width="{W*SCALE+pad*2:.0f}" height="{H*SCALE+pad*2:.0f}" fill="#0f172a"/>')

def tx(x): return (x - min_x) * SCALE
def ty(y): return (y - min_y) * SCALE

# edges first
for e in edges:
    a, b = nid2node.get(e["fromNode"]), nid2node.get(e["toNode"])
    if not a or not b:
        continue
    ax, ay = tx(a["x"] + a["width"] / 2), ty(a["y"] + a["height"] / 2)
    bx, by = tx(b["x"] + b["width"] / 2), ty(b["y"] + b["height"] / 2)
    parts.append(f'<line x1="{ax:.1f}" y1="{ay:.1f}" x2="{bx:.1f}" y2="{by:.1f}" stroke="#64748b" stroke-opacity="0.25" stroke-width="1"/>')

# nodes
for n in nodes:
    x, y = tx(n["x"]), ty(n["y"])
    w, h = n["width"] * SCALE, n["height"] * SCALE
    col = COLORS.get(n.get("color"), "#94a3b8")
    label = Path(n["file"]).stem
    # shorten label: keep after "— " if present
    short = label.split("— ")[-1] if "— " in label else label
    short = sax.escape(short)
    parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="6" fill="{col}" fill-opacity="0.18" stroke="{col}" stroke-width="1.5"/>')
    parts.append(f'<text x="{x+w/2:.1f}" y="{y+h/2:.1f}" fill="#e2e8f0" font-size="9" text-anchor="middle" dominant-baseline="middle">{short[:38]}</text>')

parts.append("</svg>")
OUT.write_text("\n".join(parts), encoding="utf-8")
print(f"SVG preview: {OUT}  ({len(nodes)} cards, {len(edges)} edges, {W:.0f}x{H:.0f} canvas)")
