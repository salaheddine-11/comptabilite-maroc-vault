---
statut: ✅ Expliqué (ajouté 09/08/2026)
categorie: Mécanismes
ordre: 49
corpus: NotebookLM 62946d90 (577 sources)
---

# 49 — Transferts de charges, clôture & réouverture

> [!quote] En une phrase
> Le transfert de charge change l'imputation d'une charge (7197/7397/7597 — pas 791 !), la clôture régularise (CCA, PCA, FAE, FNP), et la réouverture contre-passe tout au 01/01 — sauf amortissements et provisions.

## Transferts de charges (⚠️ comptes marocains 7197/7397/7597)

| Cas | Débit | Crédit | Règle |
| --- | --- | --- | --- |
| **Avantage en nature au personnel** | 6176 (charges personnel) | **71976** (TCE personnel) | Neutralise la charge initiale (loyer, véhicule) pour l'intégrer en paie |
| **Remboursement d'assurance** | 5141 | **71973** (TCE autres charges externes) — ou 758 si gain accessoire | Compense la charge de sinistre déjà comptabilisée |
| **Production immobilisée** | 21XX/23XX | **714** (immobilisations produites) | **INTERDIT** d'utiliser 7197 — passage exclusif par 714 |

⚠️ **Piège majeur** : le PCG français utilise 791/796 ; **le PCGE marocain utilise 7197 (exploitation), 7397 (financier), 7597 (non courant)** — vérifié dans le plan officiel.

## Clôture & réouverture — toutes les extournes sont OBLIGATOIRES

| Écriture | À la clôture (31/12/N) | Réouverture (01/01/N+1) |
| --- | --- | --- |
| **CCA** | D 3491 / C 61XX | D 61XX / C 3491 |
| **PCA** | D 71XX / C 4491 | D 4491 / C 71XX |
| **FAE** | D 34271 / C 71XX + 4455 | D 71XX + 4455 / C 34271 |
| **FNP** | D 61XX + 3455 / C 4417 | D 4417 / C 61XX + 3455 |
| **Bilan d'ouverture** | — | Rubrique **01** (011-015) : D 2/3/51 / C 1/4/55 |

⚠️ **NE JAMAIS extourner** : amortissements (28X), provisions (15X, 29X, 39X, 49X) — ils se soldent par **reprise** (7194/7392/7596) ou dotation, jamais par contre-passation. L'IS constaté en N ne s'extourne pas non plus (dette certaine).

## Correction d'erreurs

| Cas | Méthode | Comptes |
| --- | --- | --- |
| **Erreur de l'exercice courant** | Contre-passation ou virement — l'écriture initiale doit rester **lisible** (négatif admis uniquement pour erreurs) | Comptes d'origine |
| **Erreur d'exercice antérieur** | Constatation directe dans les comptes d'exercices antérieurs | **6118/6128** (charges ant.) · **7188/7588** (produits ant.) |

## ⚠️ Les pièges

- **Extourne oubliée** : double comptabilisation de la charge/produit en N+1 → résultat faussé + redressement possible (spécialisation des exercices, CGNC art. 17).
- **Balance après inventaire** : seuls les comptes de situation y figurent — base d'édition des états de synthèse.
- **Charges d'exercice prescrit** : non déductibles (art. 10/11 CGI) ; provisions irrégulières réintégrées.
- Les régularisations se passent **HT** (la TVA n'est pas une charge pour l'entreprise).

## Comptable vs Fiscal

- **Comptable** : spécialisation des exercices (CGNC) — rattacher chaque charge/produit à son exercice.
- **Fiscal** : une charge non rattachée à l'exercice concerné est réintégrée ; la correction doit respecter l'art. 10 CGI (régularisation + dotation l'exercice suivant).

## Liens — où ça s'insère dans le fil

- La clôture complète → [[13 — Régularisations de fin d'exercice]] · [[02 — Cycle comptable quotidien]]
- La production immobilisée (714) → [[22 — Stocks]] · [[05 — Amortissements]]
- Les reprises (7194/7392) → [[14 — Provisions]]

## Sources
NotebookLM 62946d90 (transferts/réouverture, 49 sources) · Plan Comptable Marocain officiel (7197x, 7397, 7597, 714, 3491, 4491, 34271, 4417, 6118/6128, rubrique 01) · CGI art. 10-11 · CGNC art. 17.
