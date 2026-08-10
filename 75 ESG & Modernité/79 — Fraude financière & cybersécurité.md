---
statut: ✅ Expliqué
categorie: ESG & Modernité
ordre: 79
corpus: NON
---

# 79 — Fraude financière & cybersécurité

> [!quote] En une phrase
> La fraude prospère là où trois conditions se rencontrent : la **pression**, l'**opportunité** et la **rationalisation**. Le contrôle interne (→ [[76 — Gouvernance d'entreprise & contrôle interne]]) supprime l'opportunité — l'analyste, lui, doit voir la pression et entendre la rationalisation.

## 1. Le triangle de la fraude [standard]
| Angle | Contenu | Où l'analyste le voit |
| --- | --- | --- |
| **Pression** | Bonus liés au résultat, covenants à respecter, besoin de cash personnel | Résultats « trop parfaits », objectifs ambitieux non atteints |
| **Opportunité** | Absence de séparation des fonctions, contrôle interne faible, direction omnipotente | Concentration des pouvoirs, absence de comités, CAC complaisant |
| **Rationalisation** | « Tout le monde le fait », « je rembourserai », « c'est pour sauver l'entreprise » | Le discours de la direction — l'audace des justifications |

## 2. Les fraudes comptables — les classiques marocains
- **Fausses factures** : fournisseurs fictifs (612x), sous-traitance fantôme — *la piste d'audit (→ [[02 — Cycle comptable quotidien]]) est le rempart ; l'absence de pièces est l'aveu*.
- **Détournement d'encaissements** : ventes au comptant non enregistrées, caisses parallèles — la TVA (→ [[23 — TVA]]) comme détecteur : *CA déclaré en TVA ≠ CA du CPC*.
- **Stocks fictifs** : inventaire physique vs comptable (→ [[22 — Stocks]]) — *l'inventaire annuel est le seul test qui ne ment pas*.
- **Gestion du résultat** : amortissements choisis (→ [[05 — Amortissements]]), provisions lissées (→ [[14 — Provisions]]), régularisations déplacées (→ [[13 — Régularisations de fin d'exercice]]) — *pas toujours illégale, toujours trompeuse*.
- **Faux états** : comptes infidèles, double comptabilité — l'infraction la plus grave (présentation de comptes infidèles, loi 17-95).

## 3. La fraude aux états — la frontière floue
Entre l'optimisation (légale) et la fraude (pénale), il y a la **matérialité** : un lissage qui change la lecture des comptes est une fraude, même si chaque écriture est « régulière ». Les signaux : résultats qui battent les objectifs de très peu chaque année, variations de provisions sans événement, changements de méthodes (→ [[04 — États de synthèse (BL, CPC, ESG, TF, ETIC)]], ETIC A2).

## 4. Le rôle des garde-fous
- **Le CAC** : certification, rapport spécial, circularisation (→ [[04 — États de synthèse (BL, CPC, ESG, TF, ETIC)]]) — *la circularisation des banques et des clients est l'arme absolue contre les soldes fictifs*.
- **L'audit interne** : indépendant de la direction, rattaché au comité d'audit — son absence est un signal (→ [[76 — Gouvernance d'entreprise & contrôle interne]]).
- **La séparation des fonctions** : celui qui encaisse n'enregistre pas, celui qui paie n'autorise pas — *les plus grandes fraudes marocaines ont toutes un point commun : une seule personne contrôlait le cycle complet*.
- **Le whistleblowing** : le dispositif d'alerte interne — son existence est un indicateur de maturité.

## 5. La cybersécurité — le nouveau champ de bataille
- **La fraude au président** (fake president) : des virements ordonnés par un « dirigeant » usurpé (deepfake, email piraté) — des millions partis en une journée.
- **Le ransomware** : la paralysie des systèmes (comptabilité, paie, facturation) — la rançon ou l'arrêt.
- **La facturation électronique** (→ [[36 — Facturation électronique]]) : double visage — *la traçabilité DGI renforce la piste d'audit (chaque facture est horodatée et signée), mais la dépendance numérique crée une surface d'attaque*.
- **Les données personnelles** : la loi 09-08 (protection des données) [À VÉRIFIER] impose la sécurisation — une fuite de données clients est un risque de réputation, de sanctions et de contentieux.
- **L'impact comptable** : pertes de fraude (6585), provisions pour litiges (15/45), assurance cyber — et surtout la **fiabilité des états** : un système compromis peut avoir enregistré des écritures falsifiées.

## 6. La détection forensique — les tests de cohérence
| Test | Anomalie révélatrice |
| --- | --- |
| TVA déclarée vs CA comptable (→ [[23 — TVA]]) | CA sous-déclaré ou ventes fantômes |
| Inventaire physique vs stock comptable (→ [[22 — Stocks]]) | Stocks fictifs ou détournés |
| Circularisation des clients/fournisseurs (→ [[04 — États de synthèse (BL, CPC, ESG, TF, ETIC)]]) | Soldes non confirmés, adresses suspectes |
| Charges par rapport à l'effectif (→ [[50 — Paie & charges sociales 2026 (CNSS, IR, CIMR)]]) | Sous-traitance fictive, salariés fantômes |
| Fournisseurs : cohérence des adresses/RIB | Fausses factures (un RIB = un fournisseur) |
| Rythme des écritures en fin d'exercice (→ [[13 — Régularisations de fin d'exercice]]) | Régularisations massives = tentative de déplacer le résultat |

> [!warning] The Forensic Deduction (Le Signe)
> **L'anomalie** : une seule personne cumulant la signature, la comptabilité et l'accès aux fonds ; des résultats qui battent les objectifs de très peu pendant des années ; des fournisseurs dont les adresses ou RIB se ressemblent ; une fraude au président rendue possible par l'absence de double validation des virements.
> **L'intention** : la fraude n'est jamais un accident — c'est une décision rendue possible par l'organisation. La direction qui refuse d'investir dans le contrôle interne (ou qui garde la comptabilité « en famille ») choisit l'opportunité ; la rationalisation viendra après (« je rembourserai », « c'était pour l'entreprise »).
> **Le risque caché** : la fraude se découvre toujours — par l'inventaire, la circularisation, le contrôle fiscal, un lanceur d'alerte ou la banque. Quand elle se découvre : pertes directes, redressement fiscal (fausses charges réintégrées + majorations), perte de certification des comptes, responsabilité pénale des dirigeants — et l'entreprise que l'analyse croyait rentable était un trou.

> [!danger] Red Flags & Omissions
> 1. Absence totale de séparation des fonctions documentée — une seule personne fait tout le cycle (achat → paiement, encaissement → enregistrement).
> 2. Des écarts récurrents entre la TVA déclarée et le CA comptable, jamais expliqués (→ [[23 — TVA]]).
> 3. Des fournisseurs ou clients dont la circularisation revient avec des réponses évasives ou des adresses douteuses.
> 4. Le silence : aucune information sur les procédures de sécurité informatique ni les incidents (phishing, tentatives de fraude) dans le rapport de gestion — la direction ne dit pas ce qu'elle craint.

## Liens — où ça s'insère dans le fil
- Le rempart → [[76 — Gouvernance d'entreprise & contrôle interne]] · [[02 — Cycle comptable quotidien]] · [[04 — États de synthèse (BL, CPC, ESG, TF, ETIC)]]
- Les détecteurs → [[23 — TVA]] · [[22 — Stocks]] · [[13 — Régularisations de fin d'exercice]] · [[09 — Ratios & SIG]]
- La modernité → [[36 — Facturation électronique]] · [[75 — ESG & reporting extra-financier (AMMC)]] · la sanction → [[26 — Passage résultat comptable → fiscal]]

## Sources
Théorie de la fraude (triangle de Cressey) [standard] · loi 17-95 (présentation de comptes infidèles) · loi 09-08 (protection des données) [À VÉRIFIER] · circulaires DGI (facturation électronique) · pratiques des cabinets d'audit forensique (tests de cohérence) [standard].
