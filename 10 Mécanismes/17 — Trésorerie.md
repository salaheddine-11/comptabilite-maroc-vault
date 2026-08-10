---
statut: ✅ Expliqué (complété 08/08/2026)
categorie: Mécanismes
ordre: 17
corpus: OUI + deep research
---

# 17 — Trésorerie

> [!quote] En une phrase
> Le cash, enfin : banques et caisse à l'actif (51), découverts au passif (55) — le CGNC les présente séparément, et leur différence est le **solde de tout le système** : TN = FRF − BFG.

## La structure (classe 5)

| Rubrique | Comptes | Rôle |
| --- | --- | --- |
| **51 — Trésorerie-Actif** | 5111 chèques à encaisser · 5113 effets à encaisser · 5115 virements de fonds (passage) · **5141** banques (débiteur) · 5143 Trésorerie Générale · 5146 chèques postaux · **5161** caisses · 5165 régies d'avances | Tous les encaissements |
| **55 — Trésorerie-Passif** | **5520** crédits d'escompte · **5530** crédits de trésorerie (warrants, crédits à l'exportation, facilités de caisse) · **5541** banques créditrices (découvert) | Concours bancaires courants |
| **59** | 5900 provisions pour dépréciation des comptes de trésorerie (devises bloquées, comptes gelés) | |

## Le rapprochement bancaire (l'outil de contrôle n°1)
Explique l'écart entre le solde du compte **5141** et le relevé bancaire :
- **Chèques émis non présentés** (déjà débités dans les livres, pas encore au banquier) ;
- **Agios et frais bancaires non enregistrés** (6147 services bancaires) ;
- **Intérêts créditeurs** (7381) et **virements non saisis** ;
- Régularisations passées en conséquence — des écarts persistants = erreurs ou anomalies à creuser.

## Les écritures types
| Opération | Débit | Crédit |
| --- | --- | --- |
| Encaissement chèque client | 5111 (puis 5141) | 3421 |
| Découvert bancaire | (au bilan : 55) | 5541 |
| Escompte d'effet | 5141 + 6311 | 5520 |
| Retrait banque → caisse | 5161 | 5141 (via 5115) |

## 🚨 Les messages cachés
- **Découverts récurrents (5541)** = le BFG est financé par du court terme bancaire → fragilité structurelle (TN négative) : « liquidité sous perfusion ».
- **Crédit de TVA permanent (3456)** = achats qu'on ne voit pas → factures de complaisance ([[23 — TVA]]).
- **Caisse physique** : le compte 5161 doit coller au comptage — les écarts de caisse non expliqués sont un signal de contrôle interne défaillant.
- **Banques créditrices (5541) vs crédits de trésorerie (5530)** : le découvert est un financement *forcé*, le crédit de trésorerie un financement *négocié* — l'analyse de la composition de 55 révèle la qualité de la relation bancaire.

## Ce que l'analyste en fait
- **TN = 51 − 55 = FRF − BFG** (bouclage) ; ΔTN = ΔFRF − ΔBFG (contrôle croisé des états).
- Liquidité immédiate = 51 / exigible à court terme **[standard]**.
- Les découverts (55) s'ajoutent aux dettes financières pour la capacité de remboursement.

## Liens — où ça s'insère dans le fil
- Circuit 1 : TN = FRF − BFG → [[08 — FRF, BFG & TN (analyse dynamique)]] · découvert = financement forcé → [[18 — Financement]] · crédit de TVA → [[23 — TVA]]
- Rapprochement = zone de contrôle → [[07 — Messages cachés (lecture entre les lignes)]] · effets et escompte → [[16 — Créances]]

---

## 🕵️ The Forensic Deduction (Le Signe)

> [!warning] L'anomalie
> Une trésorerie nette positive au bilan mais des découverts (5541) récurrents en cours de mois — ou un résultat positif accompagné d'une TN structurellement négative (→ [[08 — FRF, BFG & TN (analyse dynamique)]]).

> [!warning] L'intention
> Le **window dressing** de fin de mois : encaissements accélérés, reports de décaissements, cessions de créances temporaires (→ [[82 — Financements structurés & titrisation]]) pour présenter un solde bancaire présentable à la banque. La direction photographie le bilan au meilleur moment — le relevé du 31 ne raconte pas le mois.

> [!warning] Le risque caché
> La dépendance bancaire totale (découvert permanent = le BFG est financé par du court terme), les frais financiers cachés (agios), et au premier refus de la banque : la cessation des paiements (→ [[70 — Restructuration & entreprises en difficulté (Loi 73-17)]]).

> [!danger] Red Flags & Omissions
> 1. TF (tableau de flux) qui ne se concilie pas avec la variation de trésorerie du bilan — le cash raconte une autre histoire.
> 2. Découvert permanent (5541) présenté comme « saisonnier » depuis plusieurs exercices.
> 3. Cessions de créances ou affacturage (→ [[30 — Affacturage]]) concentrés en fin de mois.
> 4. Le silence : les conventions de découvert (plafonds, garanties — classe 0) jamais mentionnées — la direction ne dit pas à quel fil elle est suspendue.

## Sources
PCGE (51, 55, 59) · PCEC (2211/2213, 5520/5530) · guides de travaux de fin d'exercice · corpus NotebookLM.
