#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Builds the interactive concept graph for the Obsidian vault 'Comptabilité Maroc'.
Parses all .md files (frontmatter + wikilinks) and emits a self-contained HTML
file with an embedded force-directed graph (vanilla JS, no CDN, fully offline).
"""
import json, os, re, html

VAULT = r"C:\Users\salah eddine\Desktop\Reasearch\Reasearch"
OUT_HTML = os.path.join(VAULT, "Concept Graph Interactif.html")
OUT_JSON = os.path.join(VAULT, "95 Ressources", "graph-data.json")

CAT_COLORS = {
    "Fondations":       "#3b82f6",   # blue
    "Mécanismes":       "#10b981",   # green
    "Analyse":          "#f59e0b",   # amber
    "Fiscal":           "#ef4444",   # red
    "Avancé":           "#8b5cf6",   # violet
    "Sectoriel":        "#14b8a6",   # teal
    "Compléments 2026": "#ec4899",   # pink
    "Rapports":         "#64748b",   # slate
    "Ressources":       "#94a3b8",   # gray
    "hub":              "#eab308",   # gold
}
DEFAULT_COLOR = "#9ca3af"

def parse_frontmatter(text):
    fm = {}
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip().strip('"')
    return fm

def force_layout(nodes, links, W=3200, H=2200, iters=700):
    """Python re-implementation of the JS force layout (repulsion/spring/gravity)."""
    import math, random
    random.seed(42)
    pos = {n["id"]: [random.random() * W, random.random() * H, 0.0, 0.0] for n in nodes}
    ids = list(pos.keys())
    adj = {i: [] for i in ids}
    for l in links:
        adj[l["source"]].append(l["target"])
        adj[l["target"]].append(l["source"])
    REP, SPRING, REST, GRAV, DAMP = 2600.0, 0.015, 260.0, 0.004, 0.82
    for _ in range(iters):
        for a in range(len(ids)):
            for b in range(a + 1, len(ids)):
                x1, y1 = pos[ids[a]][0], pos[ids[a]][1]
                x2, y2 = pos[ids[b]][0], pos[ids[b]][1]
                dx, dy = x1 - x2, y1 - y2
                d2 = dx * dx + dy * dy
                if d2 < 1: d2 = 1
                d = math.sqrt(d2)
                f = REP / d2
                pos[ids[a]][2] += dx / d * f; pos[ids[a]][3] += dy / d * f
                pos[ids[b]][2] -= dx / d * f; pos[ids[b]][3] -= dy / d * f
        for l in links:
            a, b = pos[l["source"]], pos[l["target"]]
            dx, dy = b[0] - a[0], b[1] - a[1]
            d = math.sqrt(dx * dx + dy * dy) or 1
            f = (d - REST) * SPRING
            a[2] += dx / d * f; a[3] += dy / d * f
            b[2] -= dx / d * f; b[3] -= dy / d * f
        for p in pos.values():
            p[2] += (W / 2 - p[0]) * GRAV; p[3] += (H / 2 - p[1]) * GRAV
            p[2] *= DAMP; p[3] *= DAMP
            p[0] += p[2]; p[1] += p[3]
    return {i: (p[0], p[1]) for i, p in pos.items()}


def grid_layout(nodes):
    """Structured layout for the Canvas: one column per category, nodes stacked
    vertically sorted by ordre. Tall categories wrap into sub-columns (max 14 rows)
    so no column becomes unreadably long. Returns {id: (x, y)} centers."""
    CAT_ORDER = [
        "hub", "Fondations", "Mécanismes", "Analyse", "Fiscal", "Avancé",
        "Sectoriel", "Compléments 2026", "Cas pratiques", "Rapports",
        "Ressources", "Documents Réels",
    ]
    groups = {}
    for n in nodes:
        groups.setdefault(n["cat"], []).append(n)
    for g in groups:
        groups[g].sort(key=lambda n: (int(str(n.get("ordre", "99")) or 99), n["id"]))

    COL_W, ROW_H, MAX_ROWS = 420, 165, 14
    X0, Y0 = 60, 60
    pos, x = {}, X0
    for cat in CAT_ORDER:
        if cat not in groups:
            continue
        items = groups[cat]
        chunks = [items[i:i + MAX_ROWS] for i in range(0, len(items), MAX_ROWS)]
        for chunk in chunks:
            y = Y0
            for n in chunk:
                pos[n["id"]] = (x, y)
                y += ROW_H
            x += COL_W
    # any category missing from CAT_ORDER
    for cat in groups:
        if cat not in CAT_ORDER:
            items = groups[cat]
            chunks = [items[i:i + MAX_ROWS] for i in range(0, len(items), MAX_ROWS)]
            for chunk in chunks:
                y = Y0
                for n in chunk:
                    pos[n["id"]] = (x, y)
                    y += ROW_H
                x += COL_W
    return pos


# Obsidian canvas node colors: 1=red 2=orange 3=yellow 4=green 5=cyan 6=purple
CANVAS_COLORS = {
    "hub": "6",
    "Fondations": "4",
    "Mécanismes": "1",
    "Analyse": "5",
    "Fiscal": "2",
    "Avancé": "3",
    "Sectoriel": "4",
    "Compléments 2026": "2",
    "Cas pratiques": "3",
    "Rapports": "5",
    "Ressources": "3",
    "Documents Réels": "1",
    "Outils": "6",
}


def emit_canvas(data):
    """Emit an Obsidian Canvas (.canvas JSON) with file cards + edges."""
    import uuid
    pos = grid_layout(data["nodes"])
    canvas_nodes, canvas_edges = [], []
    for n in data["nodes"]:
        x, y = pos[n["id"]]
        w = 320 if n["cat"] == "hub" else 260
        node = {
            "id": str(uuid.uuid4()),
            "type": "file",
            "file": n["file"].replace("\\", "/"),
            "x": round(x - w / 2, 1),
            "y": round(y - 75, 1),
            "width": w,
            "height": 150 if n["cat"] == "hub" else 130,
        }
        col = CANVAS_COLORS.get(n["cat"])
        if col:
            node["color"] = col
        canvas_nodes.append(node)
    nid = {n["id"]: cn["id"] for n, cn in zip(data["nodes"], canvas_nodes)}
    for l in data["links"]:
        a, b = pos[l["source"]], pos[l["target"]]
        side_a, side_b = ("right", "left") if a[0] < b[0] else ("bottom", "top")
        canvas_edges.append({
            "id": str(uuid.uuid4()),
            "fromNode": nid[l["source"]],
            "fromSide": side_a,
            "toNode": nid[l["target"]],
            "toSide": side_b,
        })
    canvas = {"nodes": canvas_nodes, "edges": canvas_edges}
    path = os.path.join(VAULT, "Concept Graph.canvas")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(canvas, fh, ensure_ascii=False)
    print(f"OK: canvas -> {path} ({len(canvas_nodes)} cards, {len(canvas_edges)} edges)")


def main():
    nodes, by_id = [], {}
    for root, dirs, files in os.walk(VAULT):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for f in files:
            if not f.endswith(".md"):
                continue
            path = os.path.join(root, f)
            with open(path, encoding="utf-8") as fh:
                text = fh.read()
            node_id = f[:-3]
            fm = parse_frontmatter(text)
            cat = fm.get("categorie", "Ressources")
            if node_id == "🏠 Accueil":
                cat = "hub"
            if node_id == "Le Fil Conducteur":
                cat = "hub"
            rel = os.path.relpath(path, VAULT)
            nodes.append({
                "id": node_id,
                "label": node_id,
                "cat": cat,
                "ordre": fm.get("ordre", ""),
                "statut": fm.get("statut", ""),
                "file": rel,
            })
            by_id[node_id] = len(nodes) - 1

    links = []
    link_set = set()
    for root, dirs, files in os.walk(VAULT):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for f in files:
            if not f.endswith(".md"):
                continue
            path = os.path.join(root, f)
            with open(path, encoding="utf-8") as fh:
                text = fh.read()
            src = f[:-3]
            if src not in by_id:
                continue
            for m in re.finditer(r"\[\[([^\]\|#]+)(?:\|[^\]]+)?\]\]", text):
                tgt = m.group(1).strip()
                if tgt in by_id and tgt != src:
                    key = (src, tgt) if src < tgt else (tgt, src)
                    if key not in link_set:
                        link_set.add(key)
                        links.append({"source": src, "target": tgt})

    data = {"nodes": nodes, "links": links}
    with open(OUT_JSON, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=1)

    # colors per category
    cats = sorted({n["cat"] for n in nodes})
    palette = {c: CAT_COLORS.get(c, DEFAULT_COLOR) for c in cats}

    template = HTML_TEMPLATE.replace("__GRAPH_DATA__", json.dumps(data, ensure_ascii=False))
    template = template.replace("__PALETTE__", json.dumps(palette, ensure_ascii=False))
    with open(OUT_HTML, "w", encoding="utf-8") as fh:
        fh.write(template)

    emit_canvas(data)

    print(f"OK: {len(nodes)} nodes, {len(links)} links -> {OUT_HTML}")

HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>📊 Concept Graph — Comptabilité Maroc (42 thèmes)</title>
<style>
  :root { --bg:#0f172a; --panel:#1e293b; --border:#334155; --text:#e2e8f0; --dim:#94a3b8; }
  * { box-sizing:border-box; margin:0; padding:0; }
  body { background:var(--bg); color:var(--text); font-family:'Segoe UI',system-ui,sans-serif; overflow:hidden; height:100vh; }
  #header { position:fixed; top:0; left:0; right:0; z-index:20; display:flex; align-items:center; gap:14px;
            padding:10px 16px; background:rgba(15,23,42,.92); border-bottom:1px solid var(--border); backdrop-filter:blur(6px); }
  #header h1 { font-size:15px; font-weight:600; white-space:nowrap; }
  #header h1 span { color:var(--dim); font-weight:400; }
  #search { flex:1; max-width:340px; padding:7px 12px; border-radius:8px; border:1px solid var(--border);
            background:#0b1220; color:var(--text); font-size:13px; outline:none; }
  #search:focus { border-color:#3b82f6; }
  #stats { font-size:12px; color:var(--dim); white-space:nowrap; }
  #reset { padding:6px 12px; border-radius:8px; border:1px solid var(--border); background:#0b1220; color:var(--text);
           cursor:pointer; font-size:12px; }
  #reset:hover { border-color:#3b82f6; }
  #legend { position:fixed; top:60px; left:16px; z-index:15; background:rgba(30,41,59,.9); border:1px solid var(--border);
            border-radius:10px; padding:10px 12px; font-size:11px; max-width:230px; }
  #legend .row { display:flex; align-items:center; gap:7px; padding:2px 0; }
  #legend .dot { width:10px; height:10px; border-radius:50%; flex-shrink:0; }
  #panel { position:fixed; top:60px; right:16px; z-index:15; width:300px; max-height:calc(100vh - 90px); overflow-y:auto;
           background:rgba(30,41,59,.95); border:1px solid var(--border); border-radius:10px; padding:14px; display:none; font-size:13px; }
  #panel h2 { font-size:14px; margin-bottom:8px; }
  #panel .meta { color:var(--dim); font-size:12px; margin-bottom:8px; }
  #panel .tag { display:inline-block; padding:2px 8px; border-radius:20px; font-size:11px; margin:2px 4px 2px 0; }
  #panel ul { list-style:none; }
  #panel li { padding:3px 0; }
  #panel li a { color:#60a5fa; text-decoration:none; cursor:pointer; }
  #panel li a:hover { text-decoration:underline; }
  #panel .file { font-family:Consolas,monospace; font-size:11px; color:var(--dim); word-break:break-all; margin-top:8px; }
  #closePanel { float:right; cursor:pointer; color:var(--dim); font-size:16px; }
  #svgWrap { position:fixed; inset:0; }
  svg { width:100%; height:100%; display:block; cursor:grab; }
  svg.dragging { cursor:grabbing; }
  .link { stroke:var(--dim); stroke-opacity:.25; }
  .link.hot { stroke-opacity:.85; }
  .node { cursor:pointer; }
  .node circle { stroke:#0f172a; stroke-width:1.5; }
  .node.dim { opacity:.15; }
  .node text { fill:var(--text); font-size:10px; paint-order:stroke; stroke:#0f172a; stroke-width:2.5px;
               stroke-linejoin:round; pointer-events:none; }
  .node.searchHit circle { stroke:#fbbf24; stroke-width:3; }
  .hint { position:fixed; bottom:10px; left:16px; z-index:15; color:var(--dim); font-size:11px; }
</style>
</head>
<body>
<div id="header">
  <h1>📊 Concept Graph <span>— Comptabilité Maroc · 42 thèmes, un seul système</span></h1>
  <input id="search" type="text" placeholder="🔍 Rechercher un thème… (ex: TVA, consolidation, stocks)">
  <div id="stats"></div>
  <button id="reset">⟲ Réinitialiser</button>
</div>
<div id="legend"></div>
<div id="panel">
  <span id="closePanel">✕</span>
  <h2 id="pTitle"></h2>
  <div class="meta" id="pMeta"></div>
  <div id="pTags"></div>
  <div id="pBody"></div>
  <div class="file" id="pFile"></div>
</div>
<div id="svgWrap"><svg id="svg"></svg></div>
<div class="hint">🖱 glisser = déplacer un nœud · molette = zoom · fond glissable = panoramique · cliquer un nœud = détail · survoler = voisins</div>

<script>
"use strict";
const DATA = __GRAPH_DATA__;
const PALETTE = __PALETTE__;

const W = 1600, H = 1050;
const svg = document.getElementById('svg');
const NS = 'http://www.w3.org/2000/svg';
const gLinks = document.createElementNS(NS,'g');
const gNodes = document.createElementNS(NS,'g');
svg.appendChild(gLinks); svg.appendChild(gNodes);
const view = {x:0, y:0, k:1};

// ---------- force layout (velocity Verlet, no CDN) ----------
const nodes = DATA.nodes.map(n => ({
  ...n, x: Math.random()*W, y: Math.random()*H, vx:0, vy:0, r: 5 + (n.cat==='hub'?7:0) + (n.ordre? Math.min(3, parseInt(n.ordre)/20):0)
}));
const idx = {}; nodes.forEach((n,i)=>idx[n.id]=i);
const links = DATA.links.map(l => ({s: idx[l.source], t: idx[l.target]}));
const adj = nodes.map(()=>[]);
links.forEach(l => { adj[l.s].push(l.t); adj[l.t].push(l.s); });

const REP = 900, SPRING = 0.02, GRAV = 0.002, DAMP = 0.85;
function tick() {
  for (let i=0;i<nodes.length;i++){
    const a=nodes[i];
    for (let j=i+1;j<nodes.length;j++){
      const b=nodes[j]; let dx=a.x-b.x, dy=a.y-b.y;
      let d2=dx*dx+dy*dy; if(d2<1) d2=1;
      const f=REP/d2; const d=Math.sqrt(d2);
      dx/=d; dy/=d;
      a.vx+=dx*f; a.vy+=dy*f; b.vx-=dx*f; b.vy-=dy*f;
    }
  }
  for (const l of links){
    const a=nodes[l.s], b=nodes[l.t];
    const dx=b.x-a.x, dy=b.y-a.y, d=Math.sqrt(dx*dx+dy*dy)||1;
    const f=(d-130)*SPRING;
    a.vx+=dx/d*f; a.vy+=dy/d*f; b.vx-=dx/d*f; b.vy-=dy/d*f;
  }
  for (const n of nodes){
    n.vx += (W/2 - n.x)*GRAV; n.vy += (H/2 - n.y)*GRAV;
    n.vx*=DAMP; n.vy*=DAMP;
    n.x+=n.vx; n.y+=n.vy;
  }
}
let running = true;
function loop(){
  if (running) { for(let i=0;i<6;i++) tick(); draw(); }
  requestAnimationFrame(loop);
}

const linkEls = links.map(l=>{
  const el=document.createElementNS(NS,'line'); el.setAttribute('class','link'); gLinks.appendChild(el); return el;
});
const nodeEls = nodes.map(n=>{
  const g=document.createElementNS(NS,'g'); g.setAttribute('class','node');
  const c=document.createElementNS(NS,'circle'); c.setAttribute('r',n.r);
  c.setAttribute('fill', PALETTE[n.cat]||'#9ca3af');
  const t=document.createElementNS(NS,'text'); t.textContent=n.label; t.setAttribute('dy',n.r+11);
  g.appendChild(c); g.appendChild(t); gNodes.appendChild(g); return g;
});

function draw(){
  const tx = view.x, ty = view.y, k = view.k;
  for (let i=0;i<linkEls.length;i++){
    const a=nodes[links[i].s], b=nodes[links[i].t];
    linkEls[i].setAttribute('x1', a.x*k+tx); linkEls[i].setAttribute('y1', a.y*k+ty);
    linkEls[i].setAttribute('x2', b.x*k+tx); linkEls[i].setAttribute('y2', b.y*k+ty);
  }
  for (let i=0;i<nodeEls.length;i++){
    const n=nodes[i];
    nodeEls[i].setAttribute('transform', `translate(${n.x*k+tx},${n.y*k+ty}) scale(${k})`);
  }
}

// ---------- interactions ----------
let hovered = -1, selected = -1, dragging = -1, panning = false, panStart = null, panView = null;
function setHover(i){
  if (hovered===i) return;
  hovered=i;
  const hot = new Set();
  if (i>=0){ hot.add(i); adj[i].forEach(j=>hot.add(j)); }
  nodeEls.forEach((el,j)=>{ el.classList.toggle('dim', i>=0 && !hot.has(j)); });
  linkEls.forEach((el,j)=>{ el.classList.toggle('hot', i>=0 && (links[j].s===i||links[j].t===i)); });
}
function showPanel(i){
  selected=i;
  const n=nodes[i];
  const p=document.getElementById('panel');
  document.getElementById('pTitle').textContent = n.label;
  document.getElementById('pMeta').textContent = `Catégorie : ${n.cat} · Ordre : ${n.ordre||'—'} · Statut : ${n.statut||'—'}`;
  const tags=document.getElementById('pTags'); tags.innerHTML='';
  const t=document.createElement('span'); t.className='tag';
  t.style.background=PALETTE[n.cat]||'#64748b'; t.textContent=n.cat; tags.appendChild(t);
  const body=document.getElementById('pBody');
  const neigh = [...new Set(adj[i])];
  if (neigh.length){
    const ul=document.createElement('ul');
    const cap={hub:'🏠 Accueil'};
    for (const j of neigh.slice(0,40)){
      const li=document.createElement('li'); const a=document.createElement('a');
      a.textContent='→ '+(cap[nodes[j].label]||nodes[j].label);
      a.addEventListener('click',()=>showPanel(j));
      li.appendChild(a); ul.appendChild(li);
    }
    body.innerHTML='<b>Liens dans le système ('+neigh.length+') :</b>'; body.appendChild(ul);
  } else body.innerHTML='<i>Aucun lien — nœud isolé.</i>';
  document.getElementById('pFile').textContent = n.file||'';
  p.style.display='block';
}
document.getElementById('closePanel').addEventListener('click',()=>{ document.getElementById('panel').style.display='none'; selected=-1; });

svg.addEventListener('pointerdown', e=>{
  const el = e.target.closest('.node');
  if (el){
    const i = nodeEls.indexOf(el);
    dragging=i; running=false;
    const n=nodes[i]; const rect=svg.getBoundingClientRect();
    const px=(e.clientX-rect.left-view.x)/view.k, py=(e.clientY-rect.top-view.y)/view.k;
    n._ox=px-n.x; n._oy=py-n.y;
    el.setPointerCapture(e.pointerId);
  } else {
    panning=true; panStart={x:e.clientX,y:e.clientY}; panView={x:view.x,y:view.y};
  }
});
svg.addEventListener('pointermove', e=>{
  if (dragging>=0){
    const n=nodes[dragging]; const rect=svg.getBoundingClientRect();
    n.x=(e.clientX-rect.left-view.x)/view.k - n._ox;
    n.y=(e.clientY-rect.top-view.y)/view.k - n._oy;
    draw();
  } else if (panning){
    view.x = panView.x + (e.clientX-panStart.x);
    view.y = panView.y + (e.clientY-panStart.y);
    draw();
  }
});
svg.addEventListener('pointerup', e=>{
  if (dragging>=0){
    const i=dragging; dragging=-1; running=true;
    if (i===hovered || e.target.closest('.node')) showPanel(i);
  } else if (panning){ panning=false; }
});
svg.addEventListener('wheel', e=>{
  e.preventDefault();
  const rect=svg.getBoundingClientRect();
  const mx=e.clientX-rect.left, my=e.clientY-rect.top;
  const f = e.deltaY<0 ? 1.12 : 0.89;
  view.x = mx - (mx-view.x)*f; view.y = my - (my-view.y)*f; view.k*=f;
  draw();
},{passive:false});
nodeEls.forEach((el,i)=>{
  el.addEventListener('pointerenter', ()=>setHover(i));
  el.addEventListener('pointerleave', ()=>{ if(hovered===i) setHover(-1); });
});

// ---------- search ----------
const q = document.getElementById('search');
function doSearch(){
  const s=q.value.trim().toLowerCase();
  nodeEls.forEach((el,i)=>{
    const hit = !s || nodes[i].label.toLowerCase().includes(s);
    el.classList.toggle('searchHit', !!s && hit);
    el.style.display = hit?'':'none';
  });
  linkEls.forEach(el=>el.style.display = s?'none':'');
  if (s){
    const i = nodes.findIndex(n=>n.label.toLowerCase().includes(s));
    if (i>=0) showPanel(i);
  }
}
q.addEventListener('input', doSearch);

// ---------- legend & stats ----------
const legend=document.getElementById('legend');
Object.entries(PALETTE).forEach(([cat,col])=>{
  const row=document.createElement('div'); row.className='row';
  const dot=document.createElement('span'); dot.className='dot'; dot.style.background=col;
  row.appendChild(dot); row.appendChild(document.createTextNode(cat));
  legend.appendChild(row);
});
document.getElementById('stats').textContent = DATA.nodes.length+' thèmes · '+DATA.links.length+' connexions';
document.getElementById('reset').addEventListener('click',()=>{ view.x=0; view.y=0; view.k=1; });
loop();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    main()
