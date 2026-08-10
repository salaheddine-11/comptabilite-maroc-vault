---
statut: ✅ Expliqué
categorie: Mécanismes
ordre: 25
corpus: OUI
---

# 25 — Devises & ECA-ECP

> [!quote] En une phrase
> Si l'entreprise a des créances/dettes en devises, sa valeur en dirhams change chaque jour — à la clôture, on réévalue au dernier cours, et la différence devient un **écart de conversion**.

## Le mécanisme (CGNC)

| Question | Réponse |
| --- | --- |
| **Évaluation à la clôture** | Créances/dettes en devises converties au **dernier cours connu** à la date d'inventaire |
| **Perte latente → ECA** | Diminution de créances / augmentation de dettes → **27** (stables : 2710, 2720) et **37** (circulants : 3701, 3702) — ACTIF |
| **Gain latent → ECP** | Augmentation de créances / diminution de dettes → **17** (1710, 1720) et **47** (4701, 4702) — PASSIF |
| **Pertes réalisées** | **633** (6331 exercice, 6338 antérieurs) — y compris écarts négatifs sur trésorerie devises |
| **Gains réalisés** | **733** — gains latents sur créances/dettes **non** comptabilisés (prudence) |
| **Provision obligatoire** | Toute perte latente (ECA) : D 6393 / C 1516 (durable) ou 4506 (court terme) |
| **Contre-passation** | Les écritures d'ajustement sont contre-passées au 01/01/N+1 |
| **Banques (PCEC)** | Comptes de concordance dirhams/devises (381) et positions de change |

## 🚨 Les 3 messages cachés
| Message caché | Signe | Ce que ça révèle |
| --- | --- | --- |
| **Résultat gonflé sans provision** | ECA élevé au bilan, aucune dotation 6393 | Refus délibéré de la prudence — vérifier ETIC B5 |
| **Résultat financier sous perfusion** | Gains de change (733) portant le résultat financier, EBE en baisse | Performance fragile, dépendante des fluctuations — retraiter le courant |
| **Risque de change non couvert** | ECA/ECP volatils, quote-part significative des CP | Import-export sans couverture à terme — vérifier ETIC A1 + engagements devises |

> 💡 **Crucial pour Agadir** : toute entreprise exportatrice (agrumes, primeurs, conserveries, poisson) vit avec le risque de change — un résultat peut être gonflé ou sous-estimé de plusieurs points selon le dirham.

## Traitement fiscal
- **Gains de change latents** (écarts de conversion actif) : **réintégrés** au résultat fiscal (T22) — le fisc ne reconnaît que le réalisé ; les profits latents de change de N−1 réalisés en N sont déduits en N.
- Pertes de change latentes : provisions déductibles sous conditions.

## Liens — où ça s'insère dans le fil
- Circuit 4 : créances/dettes en devises (34/44) → [[16 — Créances]] · ECA/ECP → résultats et provisions → [[14 — Provisions]]
- Exportateurs : couverture → [[27 — Engagements hors bilan (classe 0)]] · retraitement → [[10 — Retraitements (valeur comptable → valeur actuelle)]]

## Sources
CGNC (écarts de conversion) · PCGE (17, 27, 37, 47, 633, 733, 6393) · PCEC (381) · CGI (T22).
