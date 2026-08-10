---
statut: ✅ Expliqué
categorie: Finance d'Entreprise
ordre: 56
corpus: NON
---

# 56 — Valorisation d'entreprise : ANR, multiples, DCF

> [!quote] En une phrase
> La valeur est une **fourchette**, le prix est une **décision**. L'analyste construit la fourchette ; le négociateur assume la décision — la comptabilité fournit les faits, jamais le prix.

## 1. Pourquoi valoriser
Cession/acquisition, OPA-OPE (règles AMMC), transmission familiale, apport partiel d'actifs, sortie d'associé, litige entre actionnaires, garantie d'actif et de passif (GAP), fiscalité (droits d'enregistrement). Chaque contexte impose une méthode dominante : un banquier regarde l'ANR, un industriel le DCF, un comparateur les multiples — la bonne pratique est de **croiser au moins deux approches**.

## 2. L'approche patrimoniale — ce que vaut la « matière »
- **ANR (actif net réel)** = capitaux propres retraités — la traduction directe de [[10 — Retraitements (valeur comptable → valeur actuelle)]] : éliminer les non-valeurs (→ [[11 — Non-valeurs]]), réintégrer les provisions réglementées (→ [[14 — Provisions]]), reclasser les quasi-fonds propres.
- **ANCC (actif net comptable corrigé)** = ANR + plus-values latentes nettes d'impôt sur les immobilisations (→ [[19 — Cessions & réévaluation]]).
- **La limite** : l'approche patrimoniale regarde le *passé* (coûts historiques) et ignore la rentabilité future. Une entreprise rentable avec un ANR faible vaut plus que son ANR ; une entreprise en perte vaut moins.
- **Qui l'utilise** : holdings (actif = portefeuille de titres, → [[44 — Immobilisations financières & titres]]), immobilier (valeur de marché du foncier), sociétés en liquidation (→ [[52 — Dissolution & liquidation]]).

## 3. L'approche comparative — ce que le marché paie
- **Multiples** : VE/EBITDA (le plus utilisé), PER, VE/CA, VE/BE pour les banques [standard]. Le **VE (valeur d'entreprise)** = valeur des fonds propres + dette nette − trésorerie : on compare des entreprises *indépendamment de leur structure de capital* (lien → [[57 — Structure de capital & CMPC (WACC)]]).
- **Le jeu des comparables** : pairs cotés au MASI, transactions récentes publiées (AMMC), primes/décotes.
- **Les pièges marocains** : peu de comparables purs (secteurs concentrés : banques, ciment, télécoms), décote de holding, décote de liquidité (titres non cotés), prime de contrôle dans les OPA [standard].
- **L'EBITDA lui-même** : retraiter le crédit-bail (→ [[12 — Crédit-bail]]), les produits non récurrents, les subventions (→ [[48 — Subventions (exploitation, équilibre, investissement)]]), la rémunération excessive de la direction (entreprises familiales).
- **L'éternel biais** : le vendeur choisit le multiple le plus flatteur, l'acheteur le plus sévère — la négociation commence par *la définition* de l'EBITDA.

## 4. L'approche DCF — ce que l'avenir rapporte
1. **Flux** : FCF = EBE − IS théorique − capex de maintien − ΔBFG [standard] — les trois derniers termes sont les plus manipulables (cf. [[55 — Choix d'investissement (VAN, TRI, Payback)]]).
2. **Prévisions** : 3 à 5 ans explicites, puis **valeur terminale** (formule de Gordon : FCFn+1 / (WACC − g)) [standard].
3. **Le piège de la croissance perpétuelle** : g doit rester ≤ croissance long terme de l'économie marocaine (≈ 3-4 %) [standard] — une g à 6 % éternelle est un mensonge mathématique.
4. **La valeur terminale représente souvent 60 à 80 % de la valeur totale** : c'est là que se joue la négociation, pas dans les trois premières années.
5. **Actualisation au CMPC** (→ [[57 — Structure de capital & CMPC (WACC)]]), avec prime de taille/liquidité pour les PME [standard].
6. **De l'entreprise aux fonds propres** : VE − dette nette = valeur des fonds propres. La dette nette se retraite : crédit-bail (→ [[12 — Crédit-bail]]), quasi-fonds propres (comptes courants 4463), provisions durables sans objet (→ [[14 — Provisions]]), trésorerie excédentaire.

## 5. Les cas particuliers marocains

| Type | Méthode dominante | Pourquoi |
| --- | --- | --- |
| **Banques / assurances** | ANR + méthode des dividendes (excess capital) | L'actif est monétaire, le DCF sur EBE ne s'applique pas (→ [[32 — Plans comptables sectoriels]], [[44 — Immobilisations financières & titres]]) |
| **Holding** | ANR par composantes + décote holding | La valeur = somme des titres, moins la décote |
| **Immobilier** | ANR réévalué | Le foncier domine ; le DCF sert de contrôle |
| **PME familiale** | Multiple de résultat normalisé + décote de taille | Le résultat publié est sous-estimé (rémunérations, frais personnels) |
| **Startups (CFC)** | DCF avec scénarios / comparables de transactions | Pas d'historique — tout est dans les hypothèses (→ [[41 — Incitations fiscales & zones]]) |

## 6. Pourquoi la comptabilité ne suffit pas
Le résultat CGNC est construit sur le **coût historique** et la **prudence** : provisions lissées (→ [[14 — Provisions]]), amortissements choisis (→ [[05 — Amortissements]]), non-valeurs activées (→ [[11 — Non-valeurs]]). La valeur économique exige de *défaire* ces choix — c'est exactement l'objet des retraitements (→ [[10 — Retraitements (valeur comptable → valeur actuelle)]]). **Une valorisation qui reprend le résultat publié sans retraitement n'est pas une valorisation : c'est une opinion.**

> [!warning] The Forensic Deduction (Le Signe)
> **L'anomalie** : une fourchette de valorisation *étroite* (ex. 95-105) présentée par le vendeur, ou un DCF dont la valeur terminale représente > 80 % de la valeur totale avec une croissance g proche du WACC.
> **L'intention** : présenter comme « objective » une valeur qui dépend de deux hypothèses invisibles (g et WACC) — le rapport de valorisation devient un argument de négociation déguisé en mathématiques. Le vendeur « oublie » le BFG normatif ; l'acheteur découvre un besoin de capex de maintien sous-estimé.
> **Le risque caché** : payer le prix d'un scénario central optimiste. En cas de litige (actionnaire sortant, GAP, contrôle fiscal de la valeur vénale), le juge ou l'inspecteur retiendra la méthode la plus défendable — celle qui repose sur des faits comptables vérifiables, pas sur des hypothèses.

> [!danger] Red Flags & Omissions
> 1. Un EBITDA « ajusté » qui réintègre tout (frais de direction, pertes ponctuelles) mais n'exclut jamais les produits exceptionnels.
> 2. Un BFG normatif absent ou calculé sur un historique « purgé » des années de croissance.
> 3. Des comparables choisis pour leur multiple élevé, sans ajustement de taille ni de liquidité.
> 4. Le silence : aucune mention des engagements hors bilan (cautions, retraites, crédit-bail — → [[27 — Engagements hors bilan (classe 0)]]) dans le rapport de valorisation ; aucun scénario dégradé chiffré.

## Liens — où ça s'insère dans le fil
- Les faits de base → [[04 — États de synthèse (BL, CPC, ESG, TF, ETIC)]] · [[10 — Retraitements (valeur comptable → valeur actuelle)]]
- Les leviers comptables à défaire → [[14 — Provisions]] · [[05 — Amortissements]] · [[11 — Non-valeurs]] · [[19 — Cessions & réévaluation]]
- Le taux → [[57 — Structure de capital & CMPC (WACC)]] · le flux → [[55 — Choix d'investissement (VAN, TRI, Payback)]]
- Le cadre juridique des transactions → [[39 — Fusions & scissions]] · [[52 — Dissolution & liquidation]]

## Sources
Théorie financière standard (ANR, multiples, DCF) [standard] · règlements AMMC (OPA/OPE, information financière) · pratiques de place (rapports d'évaluation, banques d'affaires) · CGI (droits d'enregistrement, valeur vénale) [À VÉRIFIER].
