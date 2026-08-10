#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Canvas-only generator: reuses build_graph helpers, emits only Concept Graph.canvas."""
import os, re
from build_graph import VAULT, parse_frontmatter, emit_canvas

nodes, by_id = [], {}
for root, dirs, files in os.walk(VAULT):
    dirs[:] = [d for d in dirs if not d.startswith(".") and d != "synth"]
    for f in files:
        if not f.endswith(".md"):
            continue
        path = os.path.join(root, f)
        # skip tooling/work folders — they are not knowledge themes
        rel = os.path.relpath(path, VAULT)
        if rel.startswith("98 Outils"):
            continue
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        node_id = f[:-3]
        fm = parse_frontmatter(text)
        cat = fm.get("categorie", "Ressources")
        if node_id in ("🏠 Accueil", "Le Fil Conducteur"):
            cat = "hub"
        if node_id.startswith("📖 Lexique"):
            cat = "hub"
        nodes.append({"id": node_id, "cat": cat, "file": rel})
        by_id[node_id] = True

links, seen = [], set()
for root, dirs, files in os.walk(VAULT):
    dirs[:] = [d for d in dirs if not d.startswith(".") and d != "synth"]
    for f in files:
        if not f.endswith(".md"):
            continue
        path = os.path.join(root, f)
        rel = os.path.relpath(path, VAULT)
        if rel.startswith("98 Outils"):
            continue
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        src = f[:-3]
        if src not in by_id:
            continue
        for m in re.finditer(r"\[\[([^\]\|#]+)(?:\|[^\]]+)?\]\]", text):
            tgt = m.group(1).strip()
            if tgt in by_id and tgt != src:
                key = (src, tgt) if src < tgt else (tgt, src)
                if key not in seen:
                    seen.add(key)
                    links.append({"source": src, "target": tgt})

emit_canvas({"nodes": nodes, "links": links})
