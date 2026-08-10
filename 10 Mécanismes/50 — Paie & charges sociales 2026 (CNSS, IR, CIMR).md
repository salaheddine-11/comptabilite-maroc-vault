---
statut: ✅ Expliqué (ajouté 09/08/2026 — taux LF 2026 vérifiés)
categorie: Mécanismes
ordre: 50
corpus: NotebookLM 62946d90 (577 sources)
---

# 50 — Paie & charges sociales 2026 (CNSS, IR, CIMR)

> [!quote] En une phrase
> La paie est un mini-circuit fiscal : brut → CNSS salarié (6,74%) → IR retenu (barème 2026, seuil 40 000 DH) → net, le tout enregistré en 6171/6174 avec les dettes 4432/4441/44525.

## Cotisations CNSS 2026 (total 27,83% : 21,09% employeur + 6,74% salarié)

| Branche | Employeur | Salarié | Base 2026 |
| --- | --- | --- | --- |
| Allocations familiales | 6,40% | — | Brut total (sans plafond) |
| Prestations sociales court terme | 1,05% | 0,52% | Plafonnée **6 000 DH/mois** |
| Prestations sociales long terme | 7,93% | 3,96% | Plafonnée **6 000 DH/mois** |
| AMO | 4,11% | 2,26% | Brut total (sans plafond) |
| Taxe formation professionnelle | 1,60% | — | Brut total (sans plafond) |

**SMIG 2026** : **17,92 DH/h** (≈ 3 422,72 DH brut/mois, 191,33 h) — décret 2.25.983 · **SMAG 2026** : **97,44 DH/jour** (≈ 2 533,44 DH/mois, 26 jours).

## Mécanique du bulletin de paie (IR 2026)

1. **SBG** = base + heures sup + primes + indemnités + avantages
2. **SBI** = SBG − exonérations (transport urbain 500 DH, repas ~40 DH/j, kilométrique 3 DH/km, indemnité de caisse 190 DH…)
3. **SNI** = SBI − (CNSS salarié + CIMR salarié + **frais professionnels 25%**, plafond 2 916,67 DH/mois)
4. **IR brut** = (SNI × taux) − somme à déduire · **seuil d'exonération 40 000 DH/an**
5. **IR net** = IR brut − réduction charges de famille (**600 DH/an par personne**, LF 2026, max 6)
6. **Net à payer** = SBG − (CNSS + CIMR + IR net + oppositions)

**Barème IR 2026 (annuel)** : 0–40 000 : **0%** · 40 001–60 000 : 10% · 60 001–80 000 : 20% · 80 001–100 000 : 30% · 100 001–180 000 : 34% · >180 000 : 37%

⚠️ **CIMR** (part salarié) entièrement **déductible de l'IR** · oppositions via 4136 (avis tiers détenteurs, saisie-arrêt, cession de créance).

## Comptabilisation (écriture mensuelle)

| Compte | Intitulé | Débit | Crédit |
| --- | --- | --- | --- |
| **6171** | Rémunération du personnel | **SBG** | |
| **6174** | Charges sociales patronales | **21,09% + CIMR patronale** | |
| **4432** | Rémunérations dues au personnel | | Net à payer |
| **4441** | CNSS | | Total (salariale + patronale) |
| **44525** | État — IR retenu | | IR net |
| **4443** | Caisses de retraite (CIMR) | | Total CIMR |

**Indemnités de licenciement** (61765) : **exonérées d'IR** dans la limite de **1 000 000 MAD** (art. 57-7° CGI) ; indemnités légales exonérées de CNSS (art. 53 Code du travail). Depuis le 01/01/2026, les pensions de base (CNSS, CMR, RCAR) et CIMR sont **totalement exonérées d'IR**.

## Comptable vs Fiscal

- **Comptable** : constatation des dettes et charges en fin de mois (6171/6174), règlement du net début mois suivant, reversement des retenues fin de mois.
- **Fiscal** : charges de personnel déductibles (art. 10 CGI) sauf excédents non justifiés ; déclaration annuelle des salaires (état 9421) ; la taxe de formation professionnelle figure sur les états CNSS.

## Liens — où ça s'insère dans le fil

- L'écriture de base → [[03 — Écritures comptables types]]
- L'IR retenu à la source → [[15 — Impôts (IS, IR, CM, CSS)]] · la liasse → [[21 — Liasse fiscale]]
- Les dettes sociales réduisent le BFG → [[08 — FRF, BFG & TN (analyse dynamique)]]

## Sources
NotebookLM 62946d90 (paie 2026, 75 sources) · Upsilon Consulting (CNSS 2026, SMIG/SMAG) · CGI art. 57-7°, art. 73-I, art. 74-I (LF 2026) · Plan Comptable Marocain officiel (6171, 6174, 4432, 4441, 4443, 44525) · Code du travail art. 53.
