---
statut: ✅ Expliqué (ajouté 09/08/2026)
categorie: Mécanismes
ordre: 53
corpus: NotebookLM 62946d90 (577 sources) + plan officiel
---

# 53 — Templates d'écritures comptables (tableau de référence)

> [!quote] En une phrase
> Toutes les écritures types du référentiel marocain en un seul tableau — opération → débit → crédit, avec la fiche qui détaille chaque mécanisme. **La méthode pour retrouver ces écritures (et toute autre) : [[54 — La logique des écritures comptables]].**

## 🧱 Opérations courantes (fiches 03 · 23 · 46)

| Opération | Débit | Crédit |
| --- | --- | --- |
| Vente au comptant | 5141/5161 (TTC) | 7111 (HT) · 4455 (TVA) |
| Vente à crédit | 3421 (TTC) | 7111 (HT) · 4455 (TVA) |
| Achat à crédit | 6121/6111 (HT) · 34552 (TVA) | 4411 (TTC) |
| Paiement fournisseur | 4411 | 5141/5161 |
| Encaissement client | 5141/5161 | 3421 |
| Emprunt bancaire | 5141 | 1481 |
| Avoir — RRR vendeur | 7119/7129 (HT) · 4455 | 3421 |
| Avoir — RRR acheteur | 4411 | 6119/6129 (HT) · 34552 |
| Escompte accordé | 6386 · 4455 | 3421 |
| Escompte obtenu | 4411 | 7386 · 34552 |
| Consignation emballage (frs) | 3421 | 4425 |
| Consignation emballage (client) | 3413 | 4411 |
| Restitution même prix | Contrepassation 4425 / 3413 | — |
| Boni reprise emballage (frs) | 4425 | 3421 · 71275 (HT) · 4455 |
| Mali reprise emballage (client) | 4411 · 61317 (HT) · 34552 | 3413 |
| Non-restitution (frs) | 4425 | 71278 (HT) · 4455 |
| Non-restitution (client) | 61231/61232 (HT) · 34552 | 3413 |

## 📋 Clôture & réouverture (fiches 13 · 49)

| Opération | Débit | Crédit |
| --- | --- | --- |
| Charges constatées d'avance (CCA) | 3491 | 61XX |
| Produits constatés d'avance (PCA) | 71XX | 4491 |
| Factures à établir (FAE) | 34271 | 71XX · 4455 |
| Factures non parvenues (FNP) | 61XX · 3455 | 4417 |
| Extourne CCA au 01/01 | 61XX | 3491 |
| Extourne PCA au 01/01 | 4491 | 71XX |
| Extourne FAE au 01/01 | 71XX · 4455 | 34271 |
| Extourne FNP au 01/01 | 4417 | 61XX · 3455 |
| Dotation amortissement | 619x | 28XX |
| Dotation provision | 6194/6392/6596 | 15X/29X/39X/49X |
| Reprise provision | 15X/29X/39X/49X | 7194/7392/7596 |
| Annulation stock initial | 6114/6124 | 31X (compte de stock) |
| Constatation stock final | 31X | 6114/6124 |
| Transfert de charge (avantage en nature) | 6176 | 71976 |
| Transfert de charge (remb. assurance) | 5141 | 71973 (ou 758 si gain) |
| Production immobilisée | 21XX/23XX | **714** (⚠️ pas 7197) |

## 🏗️ Immobilisations & titres (fiches 05 · 19 · 44)

| Opération | Débit | Crédit |
| --- | --- | --- |
| Acquisition immobilisation | 2XXX | 5141 / 4411 (TTC) |
| Achat titres de participation | 2510 | 5141 |
| Dividendes reçus | 5141 | **7321** (⚠️ pas 7511) |
| Cession titres | 5141 (prix) · 6514 (VNA) | 7514 · 2510 (sortie) |
| Dépréciation titres | 6392 | 2951 / 2941 |
| Reprise dépréciation titres | 2951 / 2941 | 7392 |
| Cession immobilisation classique | 5141 (prix) · 651 (VNA) · 28XX (amorts) | 2XXX · 751 (prix) |

## 💳 Effets de commerce (fiche 45)

| Opération | Débit | Crédit |
| --- | --- | --- |
| Acceptation effet (créance → effet) | 3425 | 3421 |
| Remise à l'escompte | 5113 | 3425 |
| Crédit d'escompte obtenu | 5141 (net) · 6311 (agio) · 6147 (frais) | 5520 |
| Encaissement à l'échéance | 5520 | 5113 |
| Impayé / protêt | 3421 · 658X (frais) | 5113 · 5520 (rejet) |
| Recouvrement forcé | 5141 | 3421 |

## 💰 Capitaux propres & subventions (fiches 24 · 47 · 48)

| Opération | Débit | Crédit |
| --- | --- | --- |
| Augmentation capital en numéraire | 3462 (appelé non versé) · 1119 (non appelé) | 1111 · 1121 (prime d'émission) |
| Augmentation capital en nature | 2XXX (apport) | 1111 · 1123 (prime d'apport) |
| Frais d'augmentation | 2113 (non-valeurs) | 5141 |
| Réduction par pertes | 1111 | 1161/1199 |
| Réduction par remboursement | 1111 · 1121 | 4461 (capital à rembourser) |
| Acompte sur dividende | 1191 | 4465 · 44525 (RAS 15%) |
| Affectation du résultat | 1191 (bénéfice) | 1140 (réserve légale 5%) · 1161 (RAN) · 1181 · 4465 |
| Subvention d'exploitation (notification) | 34512 | 7161 |
| Subvention d'équilibre | 34513 | 7561 |
| Subvention d'investissement | 34511 | 1311 |
| Encaissement subvention | 5141 | 3451X |
| Reprise annuelle subv. d'invest. | 1319 | 7577 |

## 👥 Paie (fiche 50)

| Opération | Débit | Crédit |
| --- | --- | --- |
| Constatation de la paie (fin de mois) | 6171 (SBG) · 6174 (charges patronales 21,09% + CIMR) | 4432 (net) · 4441 (CNSS totale) · 44525 (IR) · 4443 (CIMR) |
| Règlement des salaires | 4432 | 5141/5161 |
| Reversement des retenues | 44525 · 4441 · 4443 | 5141 |
| Indemnité de licenciement | 61765 | 4432 (exonérée IR ≤ 1 000 000 DH, art. 57-7°) |

## 🌍 Import/export & dissolution (fiches 51 · 52)

| Opération | Débit | Crédit |
| --- | --- | --- |
| Importation (décompte douanier) | 6111 (CAF) · 61425 (fret/transit HT) · 34552 (TVA 20%) | 4411 (transitaire, TTC) |
| Vente à l'export | 3421 (devises → dirhams) | 7113 (marchandises) / 7122 / 7125 (services) — HT |
| TVA due à reverser | 4455 | 4456 |
| IS constaté | 6701 | 4453 |
| Dissolution — réalisation de l'actif | 3488 (liquidateur) / 5141 | 751 |
| Dissolution — sortie des immobilisations | 651 (VNA) · 28XX | 2XXX |
| Dissolution — apurement du passif | 44XX/14XX | 5141 |
| Boni de liquidation | 1191/1111 | 3488 |
| Mali de liquidation | 3488 | 1199 |
| Répartition du boni aux associés | 1111/1191 | 4465 → 5141 |

## Liens — où ça s'insère dans le fil

- Le tableau de synthèse de tous les mécanismes → chaque ligne pointe vers sa fiche : [[03 — Écritures comptables types]] · [[13 — Régularisations de fin d'exercice]] · [[49 — Transferts de charges, clôture & réouverture]] · [[44 — Immobilisations financières & titres]] · [[45 — Effets de commerce (LCR, BOR, escompte, protêt)]] · [[46 — RRR & emballages (rabais, remises, ristournes)]] · [[47 — Opérations sur capital]] · [[48 — Subventions (exploitation, équilibre, investissement)]] · [[50 — Paie & charges sociales 2026 (CNSS, IR, CIMR)]] · [[51 — TVA à l'importation & exportation]] · [[52 — Dissolution & liquidation]]

## Sources
Plan Comptable Marocain officiel (vérifié compte par compte) · NotebookLM 62946d90 (577 sources) · fiches 01-52 du vault.
