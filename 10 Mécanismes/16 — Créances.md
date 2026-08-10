---
statut: ✅ Expliqué (complété 08/08/2026)
categorie: Mécanismes
ordre: 16
corpus: OUI + deep research
---

# 16 — Créances

> [!quote] En une phrase
> Le crédit que l'entreprise accorde à ses clients : 3421 → 3424 (douteux) → provisions — avec deux outils de mobilisation : les **effets de commerce** et l'**affacturage**.

## Le circuit de la créance client

| Étape | Écriture | Comptes |
| --- | --- | --- |
| **Vente à crédit** | Débit Clients (TTC) / Crédit Produits (HT) + TVA | 3421 · 71211 · 4455 |
| **Effet de commerce** (traite acceptée) | Débit Effets à recevoir / Crédit Clients | **3425** · 3421 |
| **Client douteux ou litigieux** | Débit Clients douteux / Crédit Clients | **3424** · 3421 |
| **Provision** | Dotation / Crédit provision (net des sûretés) | 61964 · **3942** |
| **Perte définitive** | Débit pertes sur créances irrécouvrables / Crédit Clients | 6182 / 6585 · 3421/3424 |

## Les effets de commerce et l'escompte
- **Remise à l'escompte** : D 5141 (Banque) + 6311 (intérêts) / C **5520** (crédit d'escompte) — à l'échéance : D 5520 / C 3425.
- **Côté banque (PCEC)** : 2211 escompte du papier commercial · 2213 effets à l'encaissement pris à crédit immédiat · 2215 mobilisation des créances professionnelles (art. 529-536 Code de Commerce) · 2217 valeurs impayées · 2221 mobilisation créances sur l'étranger.
- **Escompte ≠ affacturage** : l'escompte mobilise un effet (financement court terme, le client reste débiteur) ; l'[[30 — Affacturage]] transfère la créance (facture) au factor — avec ou sans recours.
- ⚠️ L'escompte sans recours ou la cession « à titre de garantie » restent suivis en **hors bilan** (PCEC 8768) — le risque n'est pas toujours sorti.

## La classification BAM des créances en souffrance (établissements de crédit)
- **Pré-douteuses → douteuses → compromises** (retards ≥ 360 jours) : provisionnement **20 % / 50 % / 100 %** (net des sûretés) — circulaire 19/G/2002. L'analyste transpose cette grille aux créances 3424 des entreprises.

## 🚨 Les messages cachés
- **Créances > 6 mois non provisionnées** = refus de la prudence pour éviter les dotations (6196) → vérifier ETIC B6 (créances) + existence de poursuites.
- **Glissement 3421 → 3424** = signal de dégradation du crédit client (lire net des provisions 3942).
- **DSO** (délai d'encaissement = clients × 360 / CA TTC) : l'allongement gonfle le BFG → [[08 — FRF, BFG & TN (analyse dynamique)]].
- **Fiscal** : la provision n'est déductible que si individualisée + recours judiciaire dans les 12 mois → réintégration T22 sinon ([[14 — Provisions]]).
- **Affacturage/cession** : sortie comptable des 3421 mais risque conservé si cession avec recours.

## Liens — où ça s'insère dans le fil
- Circuit 1 : nées des ventes → [[03 — Écritures comptables types]] · financées par l'affacturage → [[30 — Affacturage]] · DSO → BFG → [[08 — FRF, BFG & TN (analyse dynamique)]]
- Dépréciées par provisions → [[14 — Provisions]] · FAE à la clôture → [[13 — Régularisations de fin d'exercice]]

## Sources
PCGE (3421, 3424, 3425, 3481, 3942, 5520, 6182/6585) · PCEC (2211-2228, 8768) · Code de Commerce 529-536 · circulaire BAM 19/G/2002 · deep research NotebookLM (08/08/2026).
