---
statut: ✅ Expliqué (ajouté 09/08/2026)
categorie: Mécanismes
ordre: 46
corpus: NotebookLM 62946d90 (577 sources)
---

# 46 — RRR & emballages (rabais, remises, ristournes)

> [!quote] En une phrase
> Les réductions commerciales s'imputent sur le net commercial quand elles sont sur facture, et passent par 6119/7119 quand elles sont hors facture ; les emballages consignés créent une dette (4425) et une créance (3413) sans TVA… jusqu'au boni/mali.

## Les 3 réductions commerciales

| Type | Définition | Sur facture | Hors facture (avoir) |
| --- | --- | --- | --- |
| **Rabais** | Défaut de qualité, retard de livraison | Non comptabilisé séparément (net commercial) | **Acheteur** : C 6119/6129 · **Vendeur** : D 7119/7129 |
| **Remise** | Volume, fidélité | Idem | Idem |
| **Ristourne** | Périodique globale (fin d'année) | Impossible (calculée a posteriori) | Idem |

**Écriture d'avoir** :
- **Vendeur** : D 7119/7129 (HT) + D 4455 (TVA) / C 3421
- **Acheteur** : D 4411 / C 6119/6129 (HT) + C 34552 (TVA)

## Escomptes (RRR financiers — toujours comptabilisés)

| Opération | Compte | Écriture |
| --- | --- | --- |
| **Escompte accordé** (vendeur) | **6386** (charge financière) | D 6386 + D 4455 / C 3421 |
| **Escompte obtenu** (acheteur) | **7386** (produit financier) | D 4411 / C 7386 + C 34552 |

## Emballages consignés

| Cas | Chez le fournisseur | Chez le client | TVA |
| --- | --- | --- | --- |
| **Consignation** | D 3421 / C **4425** (dettes) | D **3413** (créances) / C 4411 | **Hors champ** |
| **Restitution même prix** | Contrepassation 4425 / 3421 | Contrepassation 4411 / 3413 | Aucune |
| **Reprise < consignation** | D 4425 / C 3421 + **71275** (boni HT) + 4455 | D 4411 + **61317** (mali HT) + 34552 / C 3413 | Boni/mali = **location taxable 20%** |
| **Non-restitution** | D 4425 / C **71278** (vente accessoire HT) + 4455 | D **61231/61232** (HT) + 34552 / C 3413 | **Vente définitive** soumise à TVA |

**3 types d'emballages** : perdus (**61231**, prix intégré au produit) · récupérables identifiables (**2333**, immobilisation) · récupérables non identifiables (**61232**, bouteilles/caisses).

## ⚠️ Les pièges

- Les RRR doivent figurer **distinctement sur la facture** pour réduire la base TVA (remise non mentionnée = non déductible).
- La consignation est **sans TVA** ; mais le boni/mali contient de la TVA → toujours décomposer HT/TVA (ex : boni TTC 60 = 50 HT + 10 TVA).
- **61231 vs 61317** : ne pas confondre — 61231 = achat d'emballages perdus, 61317 = mali sur emballages rendus (vérifié plan officiel).
- Ne jamais passer une réduction sur facture dans 6119 — elle doit rester dans le net commercial.

## Comptable vs Fiscal

- **Comptable** : RRR hors facture = comptes 6119/6129 (diminution de charges) et 7119/7129 (diminution de produits).
- **Fiscal/TVA** : les RRR sur facture réduisent la base imposable (art. 96 CGI) ; un avoir post-facturation régularise la TVA initialement collectée.

## Liens — où ça s'insère dans le fil

- Le cœur des opérations courantes → [[03 — Écritures comptables types]] · la TVA → [[23 — TVA]]
- Les avoirs en fin d'exercice → [[13 — Régularisations de fin d'exercice]]
- Les emballages récupérables stockés → [[22 — Stocks]]

## Sources
NotebookLM 62946d90 (RRR & emballages, 48 sources) · Plan Comptable Marocain officiel (6119/6129/7119/7129, 3413, 4425, 61317, 71275, 71278, 61231/61232, 2333) · CGI art. 96 (base TVA) · cours FSJES (Pr. SABRI).
