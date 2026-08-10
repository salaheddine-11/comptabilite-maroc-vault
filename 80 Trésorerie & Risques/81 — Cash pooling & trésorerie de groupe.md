---
statut: ✅ Expliqué
categorie: Trésorerie & Risques
ordre: 81
corpus: NON
---

# 81 — Cash pooling & trésorerie de groupe

> [!quote] En une phrase
> Le cash pooling est la **mutualisation des excédents et des besoins** : chaque filiale qui dort avec son trésor, c'est le groupe qui se prive de son arme. Mais une trésorerie centralisée est aussi une épée — celle que les créanciers d'une filiale peuvent retourner contre tout le groupe.

## 1. Le principe
- Dans un groupe, certaines filiales ont des excédents (trésorerie dormante), d'autres des besoins (découverts payants). Le pooling **compense** : l'excédent d'une filiale finance le besoin d'une autre — le groupe ne paie des intérêts que sur le solde net.
- **Bénéfices** : réduction des frais financiers, taux négociés globalement (le groupe parle à la banque avec un seul chiffre), visibilité consolidée (le cash forecast du groupe, → [[66 — Tableaux de bord & KPIs (pilotage)]]).

## 2. Les formes
| Forme | Mécanique | Comptabilité |
| --- | --- | --- |
| **Cash pooling physique (sweeping)** | Virements réels des comptes des filiales vers le compte central (zéro balancing) | Créances/dettes intra-groupe au bilan de chaque filiale |
| **Notional pooling** | Compensation des intérêts sans mouvement de fonds | Aucun mouvement — seule la convention change le calcul des intérêts |
| **Comptes miroirs** | La banque maintient des sous-comptes pour le reporting | Le reporting par filiale reste possible |

## 3. La comptabilité marocaine
- **Les comptes de liaison** (1601/1605) pour les succursales d'une même personne morale (→ [[31 — Comptes de liaison siège_succursales]]) — le pooling entre sociétés **distinctes** passe par des comptes courants :
  - **Comptes courants d'associés** (4463) pour les personnes physiques — avec le plafond de déductibilité des intérêts (art. 10-II-A, → [[18 — Financement]])
  - **Avances et prêts entre sociétés du groupe** : comptes 148x (emprunts auprès des associés/entreprises liées) et 248x (créances sur entreprises liées) [À VÉRIFIER numéros exacts]
- **La convention de trésorerie** : taux d'intérêt, échéances, conditions de remboursement — le document qui transforme des avances informelles en dette organisée.

## 4. Le cadre fiscal — ce que la DGI regarde
- **Les prix de transfert** : le taux d'intérêt intra-groupe doit être un **taux de marché** — un taux trop bas est un transfert de richesse (et de base taxable) vers la filiale bénéficiaire ; la DGI peut redresser (→ [[26 — Passage résultat comptable → fiscal]]).
- **La déductibilité** : les intérêts versés à la maison mère ou aux associés sont plafonnés (capital libéré, base, taux BAM — art. 10-II-A) — au-delà, réintégration au T22.
- **La TVA** : les prestations de trésorerie intra-groupe (intérêts, frais de gestion) peuvent être soumises à TVA selon la nature [À VÉRIFIER] — la convention doit le prévoir.

## 5. Les risques — l'épée du pooling
- **La contagion** : la convention de trésorerie crée des créances croisées — si une filiale fait faillite (→ [[70 — Restructuration & entreprises en difficulté (Loi 73-17)]]), les avances qu'elle a reçues deviennent des créances douteuses pour les autres (provisions 394/248, → [[14 — Provisions]]), et ses dettes envers le pool doivent être provisionnées par le groupe.
- **La requalification** : des avances permanentes sans convention ni échéance peuvent être requalifiées en **apport déguisé** (fiscalement) ou en **dette subordonnée** (par les tribunaux) — l'ambiguïté se paie.
- **Le tunneling inversé** : le pool qui siphonne la trésorerie d'une filiale saine pour financer la maison mère en perte — les minoritaires et les créanciers de la filiale sont les victimes (→ [[59 — Politique de financement & dividende]]).
- **Le risque bancaire** : le découvert d'une filiale couvert par le pool masque sa fragilité propre — l'analyste qui ne regarde que le consolidé ne voit pas la filiale en difficulté.

> [!warning] The Forensic Deduction (Le Signe)
> **L'anomalie** : des filiales qui « prêtent » en permanence à la maison mère sans échéance ni intérêt de marché — ou une filiale saine dont la trésorerie est systématiquement balayée vers le pool pendant que la maison mère accumule les pertes.
> **L'intention** : le tunneling inversé — le pool n'est plus une mutualisation, c'est une pompe. Les taux intra-groupe hors marché transfèrent le résultat là où l'impôt est le plus faible (prix de transfert) ; l'absence de convention maintient l'ambiguïté qui protège tout le monde… jusqu'au tribunal.
> **Le risque caché** : à la première difficulté d'une filiale, les créances du pool sont douteuses ; à la faillite de la maison mère, les avances reçues par les filiales sont exigibles immédiatement (clause de déchéance du terme) — la contagion emporte tout le groupe, et l'analyse consolidée (→ [[20 — Consolidation]]) avait masqué la répartition réelle du risque.

> [!danger] Red Flags & Omissions
> 1. Des comptes courants intra-groupe (4463/148x/248x) qui enflent sans convention de trésorerie ni taux documenté.
> 2. Des intérêts intra-groupe au taux zéro ou hors marché — le transfert de valeur est fiscalement redressable.
> 3. Une filiale au découvert permanent « couvert par le pool » — sa fragilité propre est masquée par le groupe.
> 4. Le silence : l'ETIC et les notes ne décrivent pas la convention de trésorerie (taux, échéances, subordination) — la direction ne dit pas qui doit quoi à qui.

## Liens — où ça s'insère dans le fil
- La mécanique intra-groupe → [[31 — Comptes de liaison siège_succursales]] · [[20 — Consolidation]] · [[44 — Immobilisations financières & titres]]
- Le cadre → [[18 — Financement]] (déductibilité) · [[26 — Passage résultat comptable → fiscal]] · [[57 — Structure de capital & CMPC (WACC)]]
- Les risques → [[70 — Restructuration & entreprises en difficulté (Loi 73-17)]] · [[14 — Provisions]] · [[59 — Politique de financement & dividende]] · la couverture → [[80 — Couverture des risques financiers (dérivés)]]

## Sources
CGNC (comptes courants, liaison) · CGI (art. 10-II-A déductibilité, prix de transfert) · circulaires DGI (prix de transfert) [À VÉRIFIER] · pratiques bancaires marocaines (conventions de trésorerie des groupes) · doctrine (requalification des avances) [À VÉRIFIER].
