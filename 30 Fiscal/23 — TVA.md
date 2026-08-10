---
statut: ✅ Expliqué
categorie: Fiscal
ordre: 23
corpus: OUI
---

# 23 — TVA

> [!quote] En une phrase
> Le **détecteur de mensonges** de la comptabilité marocaine : l'entreprise déclare sa TVA chaque mois à la DGI — si le CA déclaré en TVA ne colle pas au CPC, l'un des deux ment.

## Le mécanisme complet
- **TVA collectée (facturée)** : crédit du compte **4455** à chaque vente ou livraison à soi-même.
- **TVA récupérable** : débit du compte **3455** (34551 immobilisations, 34552 charges).
- **Principe HT** : la TVA collectée n'est pas un produit ; la TVA récupérable n'est pas une charge.
- **TVA non récupérable** : intégrée au coût d'achat ou de production du bien/service.
- **Solde** : collectée > récupérable → **4456 TVA due** ; récupérable > collectée → **3456 crédit de TVA**.
- **Déclaration** : détail par taux au **tableau T21** de la liasse.
- **Régime des encaissements (droit commun)** : la taxe n'est due qu'au paiement effectif → comptes transitoires **4458 / 3458**.
- **Taux 2026 (cours Fiscalité + LF)** : **20 %** taux normal par défaut · **10 %** taux réduit (hôtellerie, restauration, banques, riz, pâtes…) · **0 %** exonérations avec droit à déduction (EAD) · **convergence LF** (art. 247-XXXXI) : électricité **18→20 %**, location compteurs **15→20 %**, transport voyageurs/marchandises **18→20 %**, transport urbain et routier **12→10 %**, sucre raffiné **9→10 %** (2025→2026) — l'ancien 14 % a convergé vers 20 % **[À VÉRIFIER : cas particuliers restants]**.
- **Assiette (art. 96 CGI)** : prix de vente + recettes accessoires + transport + emballage perdu + intérêts de règlement − réductions commerciales/financières.
- **Créances douteuses** : en régime des encaissements (droit commun), la TVA n'est due que si elle est **encaissée** — une créance impayée ne génère pas de TVA due **[modalités de régularisation : À VÉRIFIER]**. La TVA non récupérable sur factures non conformes (art. 203) reste une réintégration.

## 🚨 Les 3 messages cachés de la TVA
| Message caché | Signe | Ce que ça révèle | Vérification |
| --- | --- | --- | --- |
| **Discordance de marge** | CA déclaré en TVA ≠ CA HT du CPC | Ventes au comptant dissimulées ou cut-off défaillant | Rapprocher T21 du CPC |
| **Crédit de TVA permanent suspect** | 3456 débiteur structurel sans investissements lourds récents | **Factures de complaisance** : achats fictifs pour gonfler la TVA récupérable et réduire l'IS | ETIC B2 + état des règlements de classe 6 |
| **TVA non récupérée** | Charges comptabilisées TTC sans isoler la TVA déductible | Factures non conformes (CGI art. 203) ou négligence | Sondage sur les pièces du grand-livre |

## Traitement comptable vs fiscal
- **Comptable** : HT toujours ; le crédit de TVA (3456) est une créance d'État, pas de la trésorerie disponible.
- **Fiscal** : la TVA non récupérable non justifiée est une **réintégration** au T22 ; la livraison à soi-même est taxable (4455).
- **Analyse** : dans la CAF additive, la TVA est neutre (hors flux retraités) ; dans les ratios de rotation, DSO/DPO se calculent **TTC** (créances et achats incluent la TVA).

## Liens — où ça s'insère dans le fil
- Circuit 1 : dans chaque vente/achat → [[03 — Écritures comptables types]] · solde → dette d'État (4456) ou créance (3456) → [[17 — Trésorerie]]
- Circuit 2 : T21 → [[21 — Liasse fiscale]] · cohérence avec le CA du CPC → [[07 — Messages cachés (lecture entre les lignes)]]

## Sources
CGI (TVA, art. 203) · PCGE (3455/3456, 4455/4456, 4458/3458) · liasse fiscale T21 · guides DGI.
