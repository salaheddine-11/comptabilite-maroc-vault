---
statut: ✅ Expliqué
categorie: Mécanismes
ordre: 22
corpus: OUI
---

# 22 — Stocks

> [!quote] En une phrase
> Le seul poste du bilan où l'entreprise **s'évalue elle-même** — le terrain de jeu préféré du lissage de résultat. CMUP/FIFO sont les seules méthodes admises.

## Valorisation (règles d'entrée)
- **Acheté** → coût d'acquisition = prix d'achat HT + droits de douane + impôts non récupérables + frais accessoires − RRR rattachables.
- **Produit** → coût de production = matières consommées + charges directes + fraction raisonnable des charges indirectes.
- **Sorties** : **CMUP** et **FIFO** — les seules admises pour les états de synthèse. **LIFO, NIFO et coûts standards interdits au bilan social** (utilisables en analytique avec retraitements).

## Inventaire permanent vs intermittent

| | Permanent | Intermittent |
| --- | --- | --- |
| Principe | Mouvements en continu (classe 9, compte 94) | Aucun mouvement en cours d'exercice |
| Clôture | Écarts avec l'inventaire physique → produits/charges **non courants** | Ajustement global à l'inventaire annuel |
| Usage | Optionnel, industries | Pratique courante des PME |

## Les écritures de fin d'exercice (à connaître par cœur)
1. **Annulation du stock initial** : D 6114 (marchandises) / 6124 (matières) / 713x (produits) — C compte de stock (3111/3121/3151)
2. **Constatation du stock final** : D compte de stock — C 6114/6124/713x
3. **Provision** : annulation provision SI (D 391 / C 7196), puis constitution provision SF (D 6196 / C 391)

**Dans le CPC** : variation = SF − SI. Marchandises/matières : s'ajoute (avec son signe) aux achats. Produits : s'ajoute aux produits (**production stockée**). *Production = ventes + variation de stocks.*

## 🚨 Les 4 messages cachés des stocks
| Message caché | Signe | Vérification |
| --- | --- | --- |
| **Lissage du CPC par stocks gonflés** | Stock final ↑ sans lien avec le CA ; aucune provision sur gammes obsolètes | ETIC C6 ; durée d'écoulement (stock moyen/achats × 360) sur 3-5 ans ; ETIC B5 |
| **Activation opportuniste de charges financières** | Frais financiers incorporés au coût de production sur cycles < 1 an | ETIC A1 (méthodes) ; rapport des CAC |
| **Changement de méthode (CMUP → FIFO) en inflation** | Stock final maximisé, marge embellie | ETIC A3 — traitement rétrospectif obligatoire (RAN) |
| **Inventaire physique ≠ balance** | Ajustements massifs en fin d'exercice | Livre d'inventaire (paraphé par le greffe) vs balance définitive |

## Liens — où ça s'insère dans le fil
- Circuit 1 : variation = SF − SI relie achats et produits du CPC → [[03 — Écritures comptables types]] · DIO → BFG → [[08 — FRF, BFG & TN (analyse dynamique)]]
- Dépréciés par provisions → [[14 — Provisions]] · coûts de production en classe 9 → [[28 — Comptabilité analytique (classe 9)]]

---

## 🕵️ The Forensic Deduction (Le Signe)

> [!warning] L'anomalie
> Des stocks qui croissent plus vite que le chiffre d'affaires (DIO en hausse), ou un inventaire physique qui ne se concilie pas avec la comptabilité — surtout en fin d'exercice.

> [!warning] L'intention
> Le stock est le **réceptacle préféré du résultat** : une variation de stock gonflée (SF surévaluée) augmente le résultat sans aucun flux de trésorerie. À l'inverse, un stock sous-évalué crée des réserves cachées pour les années difficiles. Le choix CMUP/FIFO et la valorisation des encours sont des leviers discrets.

> [!warning] Le risque caché
> La dépréciation massive (391) quand la réalité rattrape l'inventaire — chute brutale du résultat, redressement TVA/IS sur les stocks fictifs, et un BFG (→ [[08 — FRF, BFG & TN (analyse dynamique)]]) qui explose au moment où la banque regarde.

> [!danger] Red Flags & Omissions
> 1. DIO en hausse continue alors que le CA stagne — le stock n'est plus une valeur, c'est un pari.
> 2. Marge brute en baisse avec stocks en hausse — les invendus sont peut-être valorisés au-dessus de leur valeur réelle.
> 3. ETIC C6 (stocks) qui ne se concilie pas avec le bilan, ou « stocks en transit » jamais réceptionnés depuis des mois.
> 4. Le silence : aucune information sur les produits invendables ou démodés — la direction ne dit pas ce que l'inventaire sait.

## Sources
CGNC (stocks) · PCGE (311/312/313/314/315, 6114/6124, 713x, 391) · ETIC C6 · loi 9-88.
