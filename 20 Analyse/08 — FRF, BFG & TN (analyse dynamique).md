---
statut: ✅ Expliqué
categorie: Analyse
ordre: 8
corpus: OUI
---

# 08 — FRF, BFG & TN (analyse dynamique)

> [!quote] En une phrase
> L'équilibre financier en une formule : **TN = FRF − BFG** — le contrôle croisé de cohérence des états de synthèse.

## Les 3 soldes

### Fonds de Roulement Fonctionnel (FRF)
$$\text{FRF} = \text{Financement permanent} − \text{Actif immobilisé}$$
- **FRF > 0** : les ressources longues couvrent les investissements → marge de sécurité pour le cycle d'exploitation.
- **FRF < 0** : une partie des actifs longs financée par du court terme → risque d'équilibre financier.

### Besoin de Financement Global (BFG)
$$\text{BFG} = \text{Actif circulant (hors trésorerie)} − \text{Passif circulant (hors trésorerie)}$$
- **BFG > 0** (normal) : le cycle exige un financement (stocks + délais clients > crédit fournisseurs).
- **BFG < 0** : ressource d'exploitation (crédit fournisseurs ou acomptes clients élevés).

### Trésorerie Nette (TN)
$$\text{TN} = \text{Trésorerie-Actif} − \text{Trésorerie-Passif} = \text{FRF} − \text%BFG$$
$$\Delta\text{TN} = \Delta\text{FRF} − \Delta\text{BFG} \quad \text{(contrôle croisé)}$$

## Le Tableau de Financement CGNC (2 modules)
- **Module I — Synthèse des masses** : variations du FRF, du BFG et de la TN en emplois/ressources.
- **Module II — Emplois et ressources stables** :
  - *Ressources* : autofinancement (CAF − dividendes), cessions d'immobilisations, augmentations de capital, subventions d'investissement, nouveaux emprunts
  - *Emplois* : acquisitions d'immobilisations, remboursements de dettes de financement, de capital, emplois en non-valeurs
  - *Variations globales* : ΔBFG et trésorerie

## La CAF — méthode additive (ESG)
$$\text{CAF} = \text{RN} + \text{dotations stables} − \text{reprises stables} − \text{subventions d'investissement reprises} − \text{produits de cessions} + \text{VNA cédées}$$
- Exclues : toutes dotations/reprises sur actif/passif **circulant** et trésorerie.
- **Autofinancement = CAF − dividendes distribués.**

## Les lectures clés
- **TN négative** = découverts bancaires (5541) : le BFG est financé par du court terme bancaire → fragilité.
- **Couverture des emplois stables** = Classe 1 / Classe 2 ≥ 1 · **Autonomie financière** = 11/14.
- **Délais** : DSO (clients × 360/CA TTC), DPO (fournisseurs × 360/achats TTC), DIO (stocks × 360/coût des ventes) **[standard]**.
- Le BFG normatif dépend du secteur : lourd dans la distribution, léger dans les services.

## Liens — où ça s'insère dans le fil
- Circuit 3 : FRF = capitaux permanents ([[24 — Capitaux propres]], [[18 — Financement]]) − immobilisations (classe 2, [[11 — Non-valeurs]], [[12 — Crédit-bail]])
- Circuit 1 : BFG = cycle ([[22 — Stocks]] + [[16 — Créances]] − dettes fournisseurs) · TN = [[17 — Trésorerie]]
- Le TF → [[04 — États de synthèse (BL, CPC, ESG, TF, ETIC)]] · la CAF → [[09 — Ratios & SIG]]

---

## 🕵️ The Forensic Deduction (Le Signe)

> [!warning] L'anomalie
> Un FRF négatif présenté comme « structurel » ou « acceptable », ou un BFG financé en permanence par découvert bancaire (5541) — la chaîne TN = FRF − BFG qui devient négative sans que le rapport de gestion ne l'explique.

> [!warning] L'intention
> Masquer le déséquilibre structurel : le financement permanent ne couvre plus les emplois durables, mais la direction « gère » au jour le jour avec la banque. Les « améliorations » du FRF obtenues par cessions d'actifs (→ [[19 — Cessions & réévaluation]]) ou par des dettes à court terme reclassées sont des leurres : la structure n'est pas réparée, elle est déguisée.

> [!warning] Le risque caché
> La cessation des paiements (→ [[70 — Restructuration & entreprises en difficulté (Loi 73-17)]]) au premier resserrement bancaire — le déséquilibre structurel ne pardonne pas les accidents conjoncturels.

> [!danger] Red Flags & Omissions
> 1. FRF < 0 récurrent sur plusieurs exercices avec un discours « c'est notre modèle » — aucun modèle ne survit à un FRF négatif permanent.
> 2. BFG/CA en hausse continue — le cycle d'exploitation exige plus de cash chaque année (→ [[09 — Ratios & SIG]]).
> 3. TF (module 2 : variation du FRF) qui ne s'explique pas — le cash dit où est passé l'argent.
> 4. Le silence : aucune information sur la structure de financement des emplois durables (ETIC) — la direction ne dit pas qui paie les immobilisations.

## Sources
CGNC (TF, ESG) · loi 9-88 · PCGE (1-5) · liasse fiscale T6/T7 · guides Upsilon.
