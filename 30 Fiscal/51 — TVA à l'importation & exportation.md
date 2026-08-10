---
statut: ✅ Expliqué (ajouté 09/08/2026 — LF 2026 vérifiée)
categorie: Fiscal
ordre: 51
corpus: NotebookLM 62946d90 (577 sources)
---

# 51 — TVA à l'importation & exportation

> [!quote] En une phrase
> À l'import : TVA 20% sur la valeur CAF majorée des droits de douane (34552) ; à l'export : exonération avec droit à déduction (art. 92) — et entre les deux, les régimes suspensifs de l'art. 94.

## Importation — décompte et écriture

| Étape | Règle | Compte |
| --- | --- | --- |
| **Valeur en douane** | **CAF** (coût, assurance, fret) au cours du change du jour de la **DUM** | Base de calcul |
| **Droits de douane (DAI)** | Ad valorem, taux usuels 2,5% à 40% | Incorporés au coût d'acquisition |
| **TVA à l'importation** | **20%** sur (CAF + DAI + taxes parafiscales + TIC), TVA exclue de sa propre base | D **34552** |
| **Écriture complète** | — | D **6111** (CAF) · D **61425** (fret/transit HT) · D **34552** (TVA) · C **4411** (transitaire, TTC) |
| **Change** | Circulaire 717 : coût réel au taux du jour de la DUM ; gain/perte de change au paiement (633/733) | Déductible/imposable |

## Régimes suspensifs & remboursement (art. 94, 103 CGI)

| Mécanisme | Règles |
| --- | --- |
| **Régimes suspensifs douaniers** | Admission temporaire, entrepôt, perfectionnement actif : suspension des droits + TVA à l'import — TVA exigible si mise à la consommation |
| **Suspension intérieure (art. 94)** | Exportateurs **catégorisés** : achats HT de MP, emballages irrécupérables, services destinés à l'export, dans la limite du **CA export N-1** — exige un **compte matières** |
| **Remboursement (art. 103)** | Cas limitatifs : **exportations**, crédit « butoir » de taux, cessation d'activité, biens d'investissement (36 mois), leasing, ZAI |
| **Délais** | Demande trimestrielle via **SIMPL** ; forclusion **1 an** après le trimestre de naissance du crédit ; instruction 3 mois (cible **90 jours** en 2026) |

## Exportation — exonérations (CGI 2026)

| Aspect | Règle |
| --- | --- |
| **Régime** | Exonération **avec droit à déduction** (art. 92-I-1°) = taux effectif 0% — justifiée par la DUM d'exportation |
| **ZAI** (zones d'accélération industrielle) | Livraisons vers ZAI exonérées avec droit à déduction — assimilées à des exportations |
| **Régularisation TVA d'amont** | Machines/biens meubles : conservation **60 mois** (art. 104-II-2°) sinon reversement au prorata ; immeubles : 10 ans |
| **Comptes de produits** | **7113** (marchandises étranger) · **7122** (biens produits étranger) · **7125** (services étranger) · **7128** (exercices antérieurs) |

⚠️ **LF 2026 TVA** : convergence achevée — plus que **2 taux** (20% normal / 10% réduit) ; facturation électronique obligatoire grandes entreprises au 01/01/2026 (ETI/PME 2026-2027) ; retenue à la source TVA étendue (art. 117 bis) ; amende de **100% de la TVA non retenue** pour le client défaillant.

## Comptable vs Fiscal

- **Comptable** : TVA à l'import en 34552 (récupérable) ; droits de douane dans le coût d'achat/immobilisation ; produits export enregistrés HT en dirhams.
- **Fiscal** : l'exportateur récupère la TVA d'amont par remboursement (mode normal) ou imputation ; le régime suspensif évite l'avance de trésorerie.

## Liens — où ça s'insère dans le fil

- Le mécanisme interne → [[23 — TVA]] · les achats → [[03 — Écritures comptables types]]
- Les opérations en devises → [[25 — Devises & ECA-ECP]] · les zones → [[41 — Incitations fiscales & zones]]
- La trésorerie impactée par le crédit de TVA → [[17 — Trésorerie]]

## Sources
NotebookLM 62946d90 (TVA import/export, 71 sources) · CGI art. 92-I-1°, 94, 96, 99, 103, 104-II-2°, 117 bis · Circulaire 717 · LF 2026 (NEXORA, Upsilon) · douane.gov.ma.
