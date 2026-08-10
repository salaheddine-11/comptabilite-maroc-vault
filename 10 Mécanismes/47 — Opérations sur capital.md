---
statut: ✅ Expliqué (ajouté 09/08/2026)
categorie: Mécanismes
ordre: 47
corpus: NotebookLM 62946d90 (577 sources)
---

# 47 — Opérations sur capital (augmentation, réduction, apports)

> [!quote] En une phrase
> Le capital est la clé de voûte juridique de la société — son augmentation (numéraire, nature), sa réduction et les apports obéissent à des règles strictes de la loi 17-95 et à des écritures PCGE spécifiques.

## Augmentation de capital

| Opération | Débit | Crédit | Règles |
| --- | --- | --- | --- |
| **En numéraire** | **3462** (associés, capital appelé non versé) · **1119** (capital non appelé) | **1111** (capital social) + **1121** (prime d'émission) | Appel progressif possible ; transit par **4462** (versements reçus) ; droits d'enregistrement 0,5% (min 1 000 DH) |
| **Frais d'augmentation** | **2113** (non-valeurs) | 5141 | Soit activés en non-valeurs (amortis ≤ 5 ans), soit imputés sur les primes (1121) |
| **En nature** | Comptes d'actif (2231 fonds commercial, 2321 bâtiment, 2510 titres…) | 1111 + **1123** (prime d'apport) | **Libération intégrale obligatoire** ; **commissaire aux apports (CAA)** obligatoire en SA, et en SARL sauf dispense sous seuils |

## Réduction de capital

| Opération | Débit | Crédit | Règles |
| --- | --- | --- | --- |
| **Par pertes** | 1111 | 1161/1199 (absorbe les pertes) | Réduction motivée par des pertes — pas d'imposition |
| **Par remboursement aux associés** | 1111 + 1121 (primes) | 4461 (associés, capital à rembourser) | Rachat d'actions possible (loi 17-95 art. 291+) ; protection des créanciers (délai d'opposition) |
| **Apport en industrie** | — | — | **Interdit** en SA ; en SARL, ne compte pas dans le capital (droits de parts) — loi 17-95 |

## Acomptes sur dividendes & affectation

| Opération | Débit | Crédit |
| --- | --- | --- |
| **Acompte sur dividende** (AGO) | 1191 (résultat à affecter) | **4465** (dividendes à payer) + **44525** (RAS 15% si personnes physiques) |
| **Affectation du résultat** | 1191 (bénéfice) | **1140** (réserve légale 5% jusqu'à 10% du capital) · 1161 (report à nouveau) · 1181 (résultat en instance) · 4465 (dividendes) |

## ⚠️ Les pièges

- **Réserve légale** : dotation annuelle de **5%** du bénéfice jusqu'à **10% du capital** (loi 17-95 art. 332) — obligation d'ordre public.
- **Acomptes sur dividendes** : autorisés si bilan certifié par le CAC et bénéfice réalisé (art. 346 loi 17-95) ; le régime mère-fille s'applique aussi aux acomptes.
- **Frais d'augmentation** : choix comptable (activation 2113 vs imputation sur prime) — le choix fiscal est aligné (non-valeurs déductibles sur 5 ans).
- **Apport en nature** : sans rapport du CAA, l'apport est réputé fictif → responsabilité solidaire des associés pendant 5 ans.

## Comptable vs Fiscal

- **Comptable** : augmentation par apports → 1111/1121 ; frais activés en non-valeurs.
- **Fiscal** : droits d'enregistrement 0,5% sur les apports en numéraire (min 1 000 DH) ; 1% sur les apports en nature (immobilier) ; les primes d'émission ne sont pas distribuables sans imposition (RAS 15% sur les dividendes, art. 14 CGI).

## Liens — où ça s'insère dans le fil

- Le capital fait partie des capitaux propres → [[24 — Capitaux propres]]
- Les non-valeurs (2113) → [[11 — Non-valeurs]] · la prime d'émission → [[24 — Capitaux propres]]
- La réduction par pertes rejoint le passage fiscal → [[26 — Passage résultat comptable → fiscal]]
- La vie de la société → [[39 — Fusions & scissions]] · [[52 — Dissolution & liquidation]]

## Sources
Loi 17-95 (art. 332, 346, 356, 357) · NotebookLM 62946d90 (opérations sur capital, 83 sources) · CGI (droits d'enregistrement, RAS art. 14) · Plan Comptable Marocain officiel (1111, 1119, 1121, 1123, 2113, 3462, 4461/4462, 4465).
