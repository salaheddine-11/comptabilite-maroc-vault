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

---

## 🕵️ The Forensic Deduction (Le Signe)

> [!warning] L'anomalie
> Des pertes de change récurrentes (633) sans instruments de couverture documentés (→ [[80 — Couverture des risques financiers (dérivés)]]), des ECA (27/37) provisionnées à minima, ou des ECP (17/47) « oubliés » à la clôture alors que le cours a bougé.

> [!warning] L'intention
> Ignorer le risque de change coûte moins cher à court terme : pas de prime de couverture, pas de provision — et si le cours bouge dans le bon sens, les gains (733) embellissent le résultat sans réalité économique. La direction « gère » le change comme une loterie, pas comme un risque.

> [!warning] Le risque caché
> Le choc de change unique (dévaluation, crise) transforme des pertes latentes en pertes réelles massives ; les ECA non provisionnées sont réintégrées au T22 ; et l'exportateur nu (→ [[42 — Application Souss-Massa]]) voit sa marge disparaître en une seule variation de parité.

> [!danger] Red Flags & Omissions
> 1. Créances ou dettes en devises non réévaluées au dernier cours (la réévaluation est obligatoire à la clôture).
> 2. ECP (17/47) contre-passés « oubliés » ou partiels — le passif latent est sous-estimé.
> 3. Gains de change (733) récurrents sans politique de couverture — la roulette finit toujours par perdre.
> 4. Le silence : aucune information sur l'exposition nette en devises ni sur la politique de couverture dans le rapport de gestion — la direction ne dit pas à quel taux elle dort.

## Sources
CGNC (écarts de conversion) · PCGE (17, 27, 37, 47, 633, 733, 6393) · PCEC (381) · CGI (T22).
