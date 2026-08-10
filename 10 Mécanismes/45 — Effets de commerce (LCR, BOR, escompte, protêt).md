---
statut: ✅ Expliqué (ajouté 09/08/2026)
categorie: Mécanismes
ordre: 45
corpus: NotebookLM 62946d90 (577 sources)
---

# 45 — Effets de commerce (LCR, BOR, escompte, protêt)

> [!quote] En une phrase
> La lettre de change et le billet à ordre transforment une créance en instrument négociable — le cycle complet va de l'acceptation à l'escompte, au protêt et au recouvrement (loi 15-95, Code de Commerce art. 159+).

## Les 2 instruments (loi 15-95)

| Caractéristique | Lettre de Change Relevée (LCR) | Billet à Ordre Relevé (BOR) |
| --- | --- | --- |
| **Création** | Par le vendeur (tireur) qui ordonne au client (tiré) de payer | Émis par le client (souscripteur) qui s'engage à payer |
| **Acceptation** | Requiert l'acceptation expresse (signature au recto) du tiré | Pas d'acceptation (le souscripteur est déjà engagé) |
| **Échéance** | Court terme | < 3 mois en pratique |
| **Comptes** | 3425 Clients-effets à recevoir · 4415 Fournisseurs-effets à payer | Idem |

## Le cycle complet chez le vendeur

| Étape | Débit | Crédit |
| --- | --- | --- |
| **1. Acceptation** (créance → effet) | 3425 (effets à recevoir) | 3421 (clients) |
| **2. Remise à l'escompte** | **5113** (effets à l'encaissement, transitoire) — ou 5520 directement | 3425 |
| **3. Crédit d'escompte accordé** | 5141 (net) + **6311** (intérêts/agio) + **6147** (frais) | **5520** (crédits d'escompte) |
| **4. Encaissement à l'échéance** | 5520 | 5113 |
| **5. Impayé / protêt** | 3421 (clients) + **658x** (frais de protêt) | 5113 + 5520 (rejet) |
| **6. Recouvrement forcé** | 5141 | 3421 |

⚠️ Le PCGE n'a **pas de compte 3450** pour les effets (345 = État) — l'encaissement passe par **5113**.

## ⚠️ Les pièges

- **Escompte sans recours vs avec recours** : avec recours, l'effet revient en 3425 si impayé (endossement non libératoire) ; sans recours, la banque supporte le risque.
- **Endossement** : transfert de propriété de l'effet à un tiers (fournisseur ou banque) — écriture 3425 → 3425 (nouveau bénéficiaire) ou 4415 chez l'endosseur.
- **Aval** : garantie donnée par un tiers (avaliste) — engagement hors bilan à suivre en classe 0 (04 engagements donnés).
- **Protêt** : acte authentique constatant le refus de paiement — obligatoire pour conserver les recours cambiaires (art. 159-260 Code de Commerce).
- **TVA** : la remise à l'escompte ne déclenche pas de TVA ; seuls les agios/frais sont soumis.

## Comptable vs Fiscal

- **Comptable** : l'effet est une créance de même nature que 3421 — mêmes règles de dépréciation (3424 clients douteux après impayé).
- **Fiscal** : la perte sur effet impayé est déductible si justifiée (protêt + poursuites) ; les frais de protêt sont déductibles (art. 11 CGI).

## Liens — où ça s'insère dans le fil

- Complète la gestion des créances → [[16 — Créances]] · la trésorerie → [[17 — Trésorerie]]
- L'escompte est un financement à court terme → [[18 — Financement]] · [[30 — Affacturage]] (alternative)
- Les engagements d'aval → [[27 — Engagements hors bilan (classe 0)]]

## Sources
Loi 15-95 (Code de Commerce) art. 159-260 · NotebookLM 62946d90 (effets de commerce, 55 sources) · Plan Comptable Marocain officiel (5113, 5520, 3425, 4415) · plancomptable.ma.
