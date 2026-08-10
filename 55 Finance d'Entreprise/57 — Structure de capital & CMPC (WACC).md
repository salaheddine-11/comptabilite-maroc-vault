---
statut: ✅ Expliqué
categorie: Finance d'Entreprise
ordre: 57
corpus: NON
---

# 57 — Structure de capital & CMPC (WACC)

> [!quote] En une phrase
> Le CMPC est la **ligne de flottaison** : en dessous, chaque projet détruit de la valeur. Un CMPC manipulé rend n'importe quel projet rentable — c'est le levier préféré des directions qui veulent un « oui ».

## 1. Le CMPC — le coût du capital
**CMPC = (E/V) × kE + (D/V) × kD × (1 − t)** [standard]
- **kE** (coût des fonds propres) : MEDAF — kE = Rf + β × (E(Rm) − Rf) [standard]
- **kD** (coût de la dette) : taux d'intérêt moyen **après impôt** — le bouclier fiscal (1 − t) : la dette coûte moins cher parce que les intérêts sont déductibles (→ [[15 — Impôts (IS, IR, CM, CSS)]])
- **Pondérations** : à la **valeur de marché** (pas comptable) — sinon on compare des pommes et des poires [standard]
- **β** : bêta sectoriel *désendetté* puis ré-endetté à la structure cible : βE = βU × (1 + (1−t) × D/E) [standard]

## 2. Les composantes au Maroc
- **Rf** : taux des obligations du Trésor (courbe BAM) [À VÉRIFIER valeur courante]
- **Prime de risque marché** : prime de risque actions Maroc (pays émergent) [standard]
- **Prime de taille / liquidité** : indispensable pour les PME non cotées [standard]
- **kD effectif** : les plafonds du CGI limitent la déductibilité — intérêts déductibles seulement si capital entièrement libéré, base ≤ capital, taux ≤ taux BAM (art. 10-II-A CGI) → au-delà, le coût réel de la dette augmente (intérêts non déductibles réintégrés au T22, → [[26 — Passage résultat comptable → fiscal]])
- **Le sous-capitalisation** : des comptes courants d'associés (4463) massifs = dette déguisée en fonds propres — l'inspecteur regarde le taux et la base (→ [[18 — Financement]])

## 3. L'effet de levier — l'amplificateur
**RCP = ROCE + (ROCE − kD) × (1 − t) × D/CP** [standard]
- Si **ROCE > kD** : la dette *amplifie* la rentabilité des capitaux propres (effet de levier positif)
- Si **ROCE < kD** : le levier joue en sens inverse — chaque dirham de dette détruit de la valeur (effet de massue)
- **Le risque caché** : le levier n'est pas un choix de rentabilité, c'est un choix de *volatilité* — la banque marocaine le sait : provisionnement des créances en souffrance 20/50/100 % (circulaire BAM 19/G/2002) et exigences de covenants (→ [[08 — FRF, BFG & TN (analyse dynamique)]])

## 4. Les arbitrages de structure au Maroc

| Source | Coût avant IS | Particularité marocaine |
| --- | --- | --- |
| **Dette bancaire** | kD (taux BAM + marge) | Dominante ; garanties personnelles des dirigeants |
| **Obligations (1410)** | kD publique | Réservé aux grandes entreprises notées ; marché BAM |
| **Crédit-bail** (→ [[12 — Crédit-bail]]) | loyer implicite | Hors bilan social — retraité en dette par l'analyste |
| **Comptes courants (4463)** | quasi kD | Déductibilité plafonnée (art. 10-II-A) — souvent *non* libérés |
| **Financements participatifs** (→ [[33 — Financements participatifs]]) | marge Mourabaha/Ijara | Sans intérêt *nominal* — déductibilité de la marge à vérifier [À VÉRIFIER doctrine] |
| **Fonds propres** | kE | Le plus cher économiquement, le seul sans covenant |

**Le pecking order marocain** [standard] : autofinancement (CAF − dividendes) → dette bancaire → augmentation de capital. Les PME familiales évitent l'ouverture du capital (perte de contrôle) ; les groupes cotés arbitrent entre dette obligataire et augmentation de capital selon les fenêtres de marché.

## 5. De la structure au taux — l'usage du CMPC
1. Le CMPC est le **taux d'actualisation** des projets (→ [[55 — Choix d'investissement (VAN, TRI, Payback)]]) et des valorisations (→ [[56 — Valorisation d'entreprise (ANR, multiples, DCF)]])
2. Chaque projet a son **propre risque** : un projet export (→ [[25 — Devises & ECA-ECP]]) porte un risque de change que le CMPC groupe ne reflète pas
3. La **capacité d'endettement** : la dette supportable = celle que le cash-flow peut servir sans violer les covenants — la banque calcule le *debt service coverage* (→ [[09 — Ratios & SIG]])
4. **L'effet de signal** : une augmentation de capital dit « l'action est chère », un rachat d'actions dit « nous n'avons pas de projets » (Myers-Majluf) [standard]

## 6. Le pont avec le bilan CGNC
- La structure de capital est lisible *directement* au passif : 11/13 (fonds propres + quasi), 14-15 (dettes de financement), 44/45 (dettes d'exploitation)
- Les retraitements de l'analyste (→ [[10 — Retraitements (valeur comptable → valeur actuelle)]]) reconstruisent la structure *économique* : crédit-bail réintégré (→ [[12 — Crédit-bail]]), provisions réglementées en quasi-fonds propres (→ [[14 — Provisions]]), non-valeurs éliminées (→ [[11 — Non-valeurs]])
- Le FRF (→ [[08 — FRF, BFG & TN (analyse dynamique)]]) est la traduction bilan de la structure : financement permanent vs emplois durables

> [!warning] The Forensic Deduction (Le Signe)
> **L'anomalie** : un CMPC *constant* d'année en année alors que la structure de capital, le risque de change ou les taux BAM ont bougé — ou un CMPC calculé avec un β *non désendetté* sur une cible plus endettée que l'émetteur.
> **L'intention** : *baisser artificiellement le taux* pour faire passer la VAN d'un projet stratégique (ou d'une acquisition) au-dessus de zéro — la décision est prise d'abord, le chiffrage s'adapte. La dette hors bilan (crédit-bail, → [[27 — Engagements hors bilan (classe 0)]]) maintient un levier apparent faible et un kE sous-estimé.
> **Le risque caché** : accepter des projets qui détruisent réellement de la valeur ; sous-estimer le risque de structure (covenants, concentration bancaire, refinancement) ; et au moment du refinancement, le « mur » de la dette qui arrive à échéance en même temps que la conjoncture se retourne.

> [!danger] Red Flags & Omissions
> 1. Un CMPC **sans prime de taille** pour une PME — le taux d'un grand groupe appliqué à une petite structure.
> 2. Un β emprunté à un secteur coté **sans désendettement** — le risque de l'émetteur n'est pas celui du secteur.
> 3. Des intérêts non déductibles (dépassement des plafonds art. 10-II-A) jamais mentionnés dans les notes — le coût réel de la dette est supérieur au nominal.
> 4. Le silence : aucune information sur les échéanciers de dette (ETIC B7/B8) ni sur les garanties données (classe 0) — la structure de capital réelle inclut des engagements que le bilan ne montre pas.

## Liens — où ça s'insère dans le fil
- La structure au bilan → [[24 — Capitaux propres]] · [[18 — Financement]] · [[08 — FRF, BFG & TN (analyse dynamique)]]
- Le coût fiscal de la dette → [[15 — Impôts (IS, IR, CM, CSS)]] · [[26 — Passage résultat comptable → fiscal]] · [[18 — Financement]]
- Les alternatives → [[12 — Crédit-bail]] · [[33 — Financements participatifs]] · [[41 — Incitations fiscales & zones]]
- L'usage du taux → [[55 — Choix d'investissement (VAN, TRI, Payback)]] · [[56 — Valorisation d'entreprise (ANR, multiples, DCF)]]

## Sources
Théorie financière standard (MEDAF, Modigliani-Miller, pecking order) [standard] · CGI art. 10-II-A (déductibilité des intérêts) · circulaires BAM (créances en souffrance, marché obligataire) · pratiques AMMC [À VÉRIFIER].
