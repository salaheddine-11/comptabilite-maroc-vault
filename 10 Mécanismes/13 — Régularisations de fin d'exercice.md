---
statut: ✅ Expliqué
categorie: Mécanismes
ordre: 13
corpus: OUI
---

# 13 — Régularisations de fin d'exercice

> [!quote] En une phrase
> Rattacher chaque charge et chaque produit au **bon exercice** (spécialisation, loi 9-88 art. 17) — *la zone de contrôle n°1 de l'auditeur*, car ces écritures ne découlent d'aucun flux de trésorerie.

## Les 6 familles (+ la contre-passation)

| Compte | Type | Ce qu'il enregistre | Exemple chiffré |
| --- | --- | --- | --- |
| **CCA (3491)** | Actif | Charges payées en N concernant N+1 | Assurance 12 000 DH payée le 01/12/N pour 12 mois → part N+1 = 11 000 : D 3491 / C 6168 |
| **PCA (4491)** | Passif | Produits encaissés en N, réalisés en N+1 | Vente 50 000 DH facturée le 25/12/N, livrée en janvier : D 7111 / C 4491 |
| **Charges à payer** (ICNE 1487, 4493) | Passif | Charges de N sans facture reçue | Emprunt, intérêts 6 000 DH payables le 31/03/N+1, courus 9 mois = 4 500 : D 6311 / C 1487 |
| **Produits à recevoir** (ICNP 3493) | Actif | Produits acquis en N sans pièce | Intérêts à recevoir 2 000 DH : D 3493 / C 7381 |
| **FAE (34271)** | Actif (clients) | CA livré en N, facture non émise | Livraison 30 000 HT le 30/12/N, TVA 20 % : D 34271 (36 000) / C 7111 + C 4458 |
| **FNP (44171)** | Passif (fournisseurs) | Biens reçus en N, facture non reçue | Achat 15 000 HT reçu le 28/12/N, TVA 20 % : D 6121 + D 3458 / C 44171 (18 000) |
| **Contre-passation** (01/01/N+1) | Extourne | Annulation stricte des régularisations | FAE extournée : D 7111 + D 4458 / C 34271 |

## 🚨 Les 5 leviers de manipulation à surveiller

| Levier | Signe à observer | Ce que ça révèle |
| --- | --- | --- |
| Arbitrage des **CCA** | 3491 en hausse brutale, décorrélé des années passées | Report de charges vers N+1 pour surévaluer le résultat |
| Minoration des **FNP** | Écart entre bons de réception et FNP comptabilisées | Dissimulation d'achats consommés → MB et EBE embellis |
| Gonflement des **FAE** | Annulations massives au 01/01/N+1, avoirs en début d'année | Ventes fictives anticipées au 31/12 |
| Lissage par les **PCA** | Hausse injustifiée de 4491 | Stockage de revenus pour soutenir les résultats futurs |
| Sous-évaluation des **ICNE** | Absence d'intérêts courus sur emprunts et CCA | Minoration des charges financières → rentabilité gonflée |

## Ce que fait l'analyste
Premier réflexe devant un bilan : ouvrir l'ETIC et regarder les comptes **3491, 4491, 34271, 44171** — *un solde de CCA qui double sans raison = une intention*.

## Liens — où ça s'insère dans le fil
- Circuit 2 : ajustent le cycle → [[02 — Cycle comptable quotidien]] · FAE ↔ créances → [[16 — Créances]] · FNP ↔ fournisseurs → [[17 — Trésorerie]]
- Impactent le résultat → [[09 — Ratios & SIG]] · zone de l'audit → [[07 — Messages cachés (lecture entre les lignes)]]

## Sources
CGNC · loi 9-88 art. 17 · guides de travaux de fin d'exercice · PCGE (3491, 4491, 34271, 44171, 4458/3458).
