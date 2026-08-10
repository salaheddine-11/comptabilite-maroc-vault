---
statut: ✅ Expliqué (ajouté 09/08/2026)
categorie: Mécanismes
ordre: 54
corpus: NotebookLM 62946d90 (577 sources) + CGNC
---

# 54 — La logique des écritures comptables (le raisonnement)

> [!quote] En une phrase
> Une écriture n'est pas une formule à mémoriser : c'est un **raisonnement en 5 étapes** — nature du flux → comptes → sens → montants → contrôle. Maîtrisez la logique, et vous retrouverez n'importe quelle écriture du tableau [[53 — Templates d'écritures comptables]].

## 1. Le socle : l'équation et la partie double

> **ACTIF = PASSIF = Capitaux propres + Dettes** (CGNC ; loi 9-88 art. 2)

- **Toute opération** modifie au moins 2 comptes : un débité, un crédité, **d'une somme identique** (partie double).
- L'équation **reste toujours équilibrée** après chaque écriture — c'est le contrôle ultime.
- Le bilan est une **photo** ; le CPC est un **film** ; l'écriture est l'**image élémentaire** du film.

## 2. La règle des sens : le tableau des 6 cas (à connaître par cœur)

| Nature du compte | Classe PCGE | Augmentation | Diminution |
| --- | --- | --- | --- |
| **Actif** (bilan) | 2, 3, 51 | **Débit** | Crédit |
| **Passif** (bilan) | 1, 4, 55 | **Crédit** | Débit |
| **Charge** (CPC) | 6 | **Débit** | Crédit |
| **Produit** (CPC) | 7 | **Crédit** | Débit |
| **Capitaux propres** | 1 (11-13) | **Crédit** | Débit |
| **Classe 8 (résultats)** | 8 | Selon la cascade | — |

> 💡 **L'astuce mnémotechnique** : tout ce qui « entre » ou « coûte » se débite (actif qui augmente, charge qui naît) ; tout ce qui « sort » ou « rapporte » se crédite (dette qui naît, produit qui naît).

## 3. La méthode en 5 étapes (face à N'IMPORTE quelle opération)

### Étape 1 — Identifier la nature du flux
| Type de flux | Exemples | Conséquence |
| --- | --- | --- |
| **Échange** (bien/service contre cash/crédit) | Vente, achat | 2 comptes de bilan/gestion + éventuellement TVA |
| **Transformation** (interne) | Production, consommation de stock | Comptes 6/7 + 3 (stocks) ou 2 (immobilisation produite) |
| **Financement** | Emprunt, apport, subvention | Trésorerie ↔ classe 1/14 |
| **Régularisation** (fin d'exercice) | CCA, PCA, FAE, FNP, provisions | Comptes de régularisation 3491/4491/34271/4417 |
| **Interne à l'entreprise** | Transfert de charge, production immobilisée | 6/7 ↔ 7 (7197) ou 2 (714) |

### Étape 2 — Trouver les comptes concernés
- **Question 1** : l'opération touche-t-elle le **bilan** (classe 1-5) ou le **résultat** (classe 6-7) ?
- **Question 2** : côté actif → immobilisation (2), stock (31), créance (34), trésorerie (51) ? Côté passif → dette (44/14), capitaux propres (11) ?
- **Question 3** : y a-t-il de la **TVA** ? → 4455 (collectée, crédit) ou 3455 (récupérable, débit) — toujours **HT** pour les comptes de classe 6/7.
- ⚠️ **Tiers non compensés** : débiteurs en 34, créditeurs en 44 — jamais de compte mixte.

### Étape 3 — Déterminer le sens (débit/crédit) avec le tableau des 6 cas
- Pour **chaque** compte identifié : augmente-t-il ou diminue-t-il ? → appliquer la règle.
- Le montant inscrit au débit doit toujours **égaler** le total crédité.

### Étape 4 — Vérifier le montant
- **TVA** : le client doit TTC (3421/4411), les comptes 6/7 en HT, la TVA dans 4455/3455.
- **Escompte** : jamais déduit des ventes — 6386 (charge financière) à part.
- **Change** : conversion au cours du jour de l'opération ; écart en 633/733.

### Étape 5 — Contrôler
1. **Équilibre** : total débit = total crédit.
2. **Sens du solde** : un compte d'actif doit avoir un solde débiteur ; un compte de passif, créditeur — sinon erreur d'imputation.
3. **Impact** : l'écriture gonfle-t-elle le résultat (6/7) ou seulement le bilan (1-5) ? *Une charge passée en classe 2 = résultat artificiellement gonflé.*

## 4. Les règles spéciales qui « cassent » le réflexe

| Règle | Logique | Exemple |
| --- | --- | --- |
| **Principe HT** | La TVA n'est ni une charge ni un produit — c'est un tiers (État) | Achat 6121 (HT) + 34552 / 4411 (TTC) |
| **Comptabilité d'engagement** | Le produit naît à la livraison, pas à l'encaissement | Vente à crédit : 3421 / 7111 + 4455 (aucun cash) |
| **CAF additive** | Les reprises circulantes et les cessions (751) sont exclues de la CAF | CAF = RN + dotations stables − reprises stables − 751 + 651 |
| **IS non déductible** | 6701/6705 sont des charges non déductibles → réintégration au T22 | Passage résultat comptable → fiscal ([[26 — Passage résultat comptable → fiscal]]) |
| **Classe 8 cascade** | 81 → 83 → 84 → 85 → 86 → 88 puis transfert 1191/1199 | Le résultat transite par la classe 8, jamais directement en 11 |
| **Classe 9 autonome** | Résultat analytique (98) se réconcilie avec le résultat général (88) | Comptes réfléchis 90 ↔ comptes généraux |
| **Classe 0 hors bilan** | Engagements (cautions, avals, crédit-bail) — pas dans l'équation | 04 engagements donnés / 05 reçus |

## 5. Les comptes de passage (le « sas » entre deux états)

| Compte | Rôle | Exemple d'usage |
| --- | --- | --- |
| **5113** (effets à l'encaissement) | Transitoire entre 3425 et la banque | Remise à l'escompte : 5113 / 3425, puis 5141 / 5113 |
| **3488** (liquidateur) | Regroupe les opérations de liquidation | Dissolution : réalisation de l'actif par le liquidateur |
| **3462/4462** (associés) | Suit la souscription puis la libération du capital | Augmentation : 3462 / 1111, puis 5141 / 3462 |
| **3491/4491** (CCA/PCA) | Isole les charges/produits sur exercices suivants | Extournés au 01/01 |
| **3451X** (subventions à recevoir) | Encaissement différé d'une subvention notifiée | 34512 / 7161, puis 5141 / 34512 |

> 💡 Un compte de passage se **solde toujours à zéro** après l'opération complète — s'il reste un solde, le cycle n'est pas terminé.

## 6. Application guidée — 3 exercices de raisonnement

### Cas 1 : « Nous vendons 10 000 DH HT + TVA 20% à crédit »
1. **Nature** : échange (bien contre créance).
2. **Comptes** : 3421 (client, bilan actif) · 7111 (vente, produit) · 4455 (TVA collectée).
3. **Sens** : 3421 augmente → **débit TTC 12 000** · 7111 produit → **crédit 10 000** · 4455 passif → **crédit 2 000**.
4. **Montants** : TTC au client, HT au produit, TVA à part.
5. **Contrôle** : 12 000 = 10 000 + 2 000 ✅ · 3421 solde débiteur ✅ · résultat +10 000 ✅.

### Cas 2 : « Nous payons 5 000 DH de loyer par chèque, dont 1 000 DH concernent janvier prochain (clôture le 31/12) »
1. **Nature** : échange + régularisation (spécialisation des exercices).
2. **Comptes** : 6131 (location, charge) · 5141 (banque) · 3491 (CCA) à la clôture.
3. **Écriture du paiement** : 6131 (5 000) / 5141 (5 000).
4. **À la clôture** : 1 000 DH concernent N+1 → **3491 (1 000) / 6131 (1 000)**.
5. **Contrôle** : charge N = 4 000 ✅ · 3491 sera extourné au 01/01 ([[49 — Transferts de charges, clôture & réouverture]]) ✅.

### Cas 3 : « Un client nous règle 2 000 DH d'avance pour une prestation non réalisée »
1. **Nature** : encaissement sans produit (engagement → produit différé).
2. **Comptes** : 5141 (banque) · 4421 (clients — avances reçues, passif).
3. **Sens** : banque augmente → **débit 2 000** · dette naît → **crédit 4421 (2 000)**.
4. **À la réalisation** : 4421 (2 000) / 7124 (2 000) — le produit naît à la prestation.
5. **Piège** : si comptabilisé en 7111 directement → résultat gonflé + TVA mal déclarée (la TVA sur avance est exigible à l'encaissement, art. 98 CGI — mais le produit reste différé).

## 7. Les erreurs de logique les plus fréquentes (l'examen les adore)

1. **Passer une charge en classe 2** (immobilisation abusive) → résultat gonflé, amortissements forcés.
2. **Débiter/créditer le mauvais côté** → soldes inversés détectés par la balance (un actif créditeur est un signal d'alarme).
3. **Oublier la TVA** sur une facture → déséquilibre et redressement (art. 117 CGI).
4. **Compenser débiteurs et créditeurs** (3421 vs 4411) → interdit par le CGNC, masque la réalité.
5. **Créditer 7511 au lieu de 7321** pour les dividendes → fausse la CAF (les cessions sont exclues, pas les dividendes).
6. **Utiliser 791 au lieu de 7197** → réflexe français, le PCGE marocain utilise 7197/7397/7597.
7. **Ne pas extourner les régularisations** au 01/01 → double comptabilisation en N+1.

## Liens — où ça s'insère dans le fil

- Le tableau des écritures → [[53 — Templates d'écritures comptables]] (chaque ligne illustre une étape de ce raisonnement)
- La grammaire de base → [[01 — Logique du PCGE & principes]] · le pipeline → [[02 — Cycle comptable quotidien]]
- Les briques du quotidien → [[03 — Écritures comptables types]]
- La clôture applique la logique → [[13 — Régularisations de fin d'exercice]] · [[49 — Transferts de charges, clôture & réouverture]]
- Les cas particuliers → [[44 — Immobilisations financières & titres]] · [[46 — RRR & emballages (rabais, remises, ristournes)]] · [[47 — Opérations sur capital]]

## Sources
CGNC (norme générale, art. 2, 10, 16-17) · loi 9-88 · Plan Comptable Marocain officiel · NotebookLM 62946d90 (577 sources) · cours FSJES (Pr. SABRI, comptabilité générale II).
