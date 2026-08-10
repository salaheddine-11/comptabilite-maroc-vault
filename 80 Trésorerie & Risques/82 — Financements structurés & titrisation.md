---
statut: ✅ Expliqué
categorie: Trésorerie & Risques
ordre: 82
corpus: NON
---

# 82 — Financements structurés & titrisation

> [!quote] En une phrase
> Le financement structuré est l'art de **transformer des actifs dormants en liquidité** — et parfois des risques en engagements invisibles. Ce qui sort du bilan n'a pas disparu : il a changé de propriétaire, et souvent de lecteur.

## 1. Le principe
Financer sur les **flux futurs** (créances, loyers, royalties, recettes d'infrastructure) plutôt que sur le bilan de l'entreprise : le prêteur regarde la qualité du flux, pas la santé de l'emprunteur. Les structures typiques : **titrisation de créances**, **project finance** (financement de projets sans recours), **sale & lease-back** (→ [[12 — Crédit-bail]]), **financement d'acquisition** (LBO).

## 2. La titrisation — le mécanisme
- **Le véhicule (FCT — fonds de titrisation de créances, loi 33-06)** [À VÉRIFIER] : une société cède ses créances à un fonds, qui émet des parts (titres) financées par des investisseurs — l'entreprise reçoit la liquidité immédiatement ; le fonds encaisse les créances à terme.
- **L'impact comptable** : les créances **sortent du bilan** (cession, → [[16 — Créances]]) — le BFG diminue (→ [[08 — FRF, BFG & TN (analyse dynamique)]]), la trésorerie augmente (→ [[17 — Trésorerie]]) : *le bilan paraît immédiatement plus sain, sans dette nouvelle*.
- **Le cousin proche** : l'**affacturage** (→ [[30 — Affacturage]]) — la différence : l'affacturage est une cession simple à un factor ; la titrisation est un marché (parts négociables) supervisé par l'AMMC.
- **Le piège du recours** : si la cession comporte un **recours** (l'entreprise garantit le recouvrement), ce n'est plus une cession — c'est un **emprunt déguisé** (le risque reste, la dette est cachée).

## 3. Le project finance — sans recours
- Un **SPV (société de projet)** porte l'actif et la dette ; les prêteurs n'ont de recours que sur les flux du projet (péages, loyers, contrats d'achat) — *la dette du projet ne pèse pas sur le bilan de la maison mère* (sauf consolidation, → [[20 — Consolidation]]).
- **Les garanties** : contrats de construction, assurances, comptes séquestres — le montage est une machine à répartir les risques (→ [[27 — Engagements hors bilan (classe 0)]]).
- **Le cas marocain** : infrastructures (autoroutes, énergies renouvelables — le solaire de Ouarzazate), immobilier, hôtellerie — les grands projets marocains sont des montages SPV.

## 4. Le sale & lease-back
Vendre un actif (immobilier, équipement) à une société de leasing pour le louer ensuite : la liquidité immédiate, l'usage conservé, le risque de propriété transféré (→ [[12 — Crédit-bail]]) — *l'analyste retraite : le sale & lease-back est un financement, pas une cession* (→ [[10 — Retraitements (valeur comptable → valeur actuelle)]]).

## 5. Le hors bilan économique — la lecture de l'analyste
| Structure | Ce que le bilan montre | Ce que l'analyste doit voir |
| --- | --- | --- |
| Titrisation sans recours | Créances sorties, cash reçu | La qualité du portefeuille cédé — les créances douteuses ont-elles été triées ? |
| Titrisation avec recours | Idem | Dette cachée + risque conservé → retraiter en dette |
| SPV non consolidé | Rien au bilan de la mère | Les engagements (garanties, cautions, → [[27 — Engagements hors bilan (classe 0)]]) et la consolidation (→ [[20 — Consolidation]]) |
| Sale & lease-back | Produit de cession (751) | C'est un financement — le retraiter en dette et en charge de loyer |

## 6. Les risques
- **La sélection adverse** : la titrisation qui sort les créances douteuses du bilan (le « tri » du portefeuille) — le bilan s'améliore, le risque part chez les investisseurs du fonds… qui l'avaient peut-être mal évalué.
- **Les véhicules non consolidés** : le SPV qui n'est pas consolidé (périmètre, → [[20 — Consolidation]]) cache la dette — la crise financière de 2008 a appris au monde que « hors bilan » veut dire « invisible », pas « absent ».
- **La complexité** : chaque montage a ses propres règles fiscales (droits d'enregistrement, TVA sur les cessions de créances [À VÉRIFIER]) et comptables — la documentation est le premier risque.

> [!warning] The Forensic Deduction (Le Signe)
> **L'anomalie** : des cessions de créances massives (ou un SPV) qui apparaissent alors que la qualité du portefeuille clients se dégrade — ou des cessions « sans recours » dont la documentation révèle des garanties cachées (recours partiel, indemnités de première perte).
> **L'intention** : embellir le bilan avant une échéance (covenant bancaire, émission obligataire, valorisation — → [[56 — Valorisation d'entreprise (ANR, multiples, DCF)]]) : les créances douteuses sortent, la trésorerie rentre, le BFG se comprime — *la photo est belle, le risque a seulement changé de poche*.
> **Le risque caché** : quand le recours existe mais n'est pas comptabilisé, la défaillance des débiteurs cédés ramène la charge au bilan — en une fois, avec les pénalités de la banque en plus. Les SPV non consolidés peuvent cacher des pertes qui n'apparaîtront qu'à la consolidation ou à la faillite.

> [!danger] Red Flags & Omissions
> 1. Des cessions de créances qui augmentent alors que le DSO se dégrade — pourquoi céder ce qui se paie bien ?
> 2. Une titrisation « sans recours » dont les notes ne précisent ni le périmètre cédé ni les garanties résiduelles.
> 3. Des SPV ou véhicules ad hoc absents du périmètre de consolidation sans explication (→ [[20 — Consolidation]]).
> 4. Le silence : la politique de titrisation (montants, recours, engagements résiduels) jamais décrite dans les notes — la direction ne dit pas ce qu'elle a sorti du bilan.

## Liens — où ça s'insère dans le fil
- Les actifs cédés → [[16 — Créances]] · [[30 — Affacturage]] · [[12 — Crédit-bail]] · [[22 — Stocks]]
- Le hors bilan → [[27 — Engagements hors bilan (classe 0)]] · la consolidation → [[20 — Consolidation]] · les retraitements → [[10 — Retraitements (valeur comptable → valeur actuelle)]]
- Le cadre → [[18 — Financement]] · [[57 — Structure de capital & CMPC (WACC)]] · la crise → [[71 — Diagnostic de défaillance & scoring]]

## Sources
Loi 33-06 (titrisation de créances, FCT) [À VÉRIFIER] · réglementation AMMC (OPCVM/fonds) · CGI (droits d'enregistrement, TVA sur cessions) [À VÉRIFIER] · IFRS (décomptabilisation, consolidation) [standard] · pratiques des banques d'affaires marocaines (montages SPV).
