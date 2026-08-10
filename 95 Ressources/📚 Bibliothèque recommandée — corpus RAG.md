---
statut: ✅ Expliqué (ajouté 08/08/2026 — corpus-grounded)
categorie: Ressources
ordre: 97
corpus: Citations du corpus NotebookLM + recommandations
---

# 📚 Bibliothèque recommandée — corpus RAG (livres → BookRAG)

> [!quote] En une phrase
> Les livres **enseignent la logique** de la comptabilité marocaine (mécanismes, méthodes, raisonnement) → ils entrent dans **BookRAG** ; les **faits datés** (taux IS, TVA, barèmes, LF) restent dans **NotebookLM**, recherchés avec la **date du jour**.

> [!important] La règle des deux sources
> | Question | Source | Pourquoi |
> | --- | --- | --- |
> | « Comment se calcule le FRF ? Pourquoi crédit-bail ≠ IFRS 16 ? Quelle est la logique du T22 ? » | 🧠 **Livres (BookRAG)** | La logique ne change pas — c'est le raisonnement qu'on veut te transmettre |
> | « Quel est le taux d'IS 2026 ? La TVA sur l'hôtellerie ? Le plafond des espèces ? » | 📅 **NotebookLM (recherche datée)** | Les faits changent — on cherche avec la date du jour pour du à jour |

---

## 🧠 Livres « logique » → à mettre dans `bookrag/books/`

> ✅ = cité dans ton corpus (vérifié via NotebookLM) · ⭐ = recommandé en plus (non cité mais référence)

### Comptabilité générale & référentiel
| Priorité | Ouvrage                                                        | Auteur / Éditeur                                        | Rôle                                      | Statut                |
| -------- | -------------------------------------------------------------- | ------------------------------------------------------- | ----------------------------------------- | --------------------- |
| 1        | **CGNC + PCGE intégral** (décret 2-89-61 + annexes)            | CNC / BO                                                | 🧠 Le cadre logique de tout               | 🔵 à télécharger      |
| 1        | **Le plan comptable marocain : annoté et commenté** ✅          | M. Abdeladim, A. Talbi (1993)                           | 🧠 Le PCGE expliqué                       | 🟢 / 🔵 à chercher    |
| 2        | **La Comptabilité Générale des Entreprises Marocaines** ✅      | A. Fechtali, B. Fouguig — Éd. Fedala, Casablanca (2000) | 🧠 La logique CGNC en français            | 🟢 / 🔵 selon édition |
| 2        | **Initiation pratique à la comptabilité générale marocaine** ✅ | M. Zeamari — Éd. Maghrébines (2003)                     | 🧠 Pédagogique, exemples marocains        | 🟢 / 🔵               |
| 3        | **Comptabilité générale** ⭐                                    | B. & F. Grandguillot — Dunod                            | 🧠 Le classique français des fondamentaux | 🟢                    |

### Analyse financière & diagnostic (le cœur du PFE)
| Priorité | Ouvrage | Auteur / Éditeur | Rôle | Statut |
| --- | --- | --- | --- | --- |
| 1 | **Finance d'Entreprise T2 : Analyse et diagnostic financiers** ✅ | N. Amine Bouayad — Dar Al Qalam, Rabat (2016) | 🧠 **Le livre marocain de référence** : 100 cas corrigés, QCM | 🟢 / 🔵 à chercher |
| 1 | **Diagnostic Financier de l'Entreprise** ✅ | N. Ibnabdeljalil — Edit-consulting (2006) | 🧠 Diagnostic à la marocaine | 🟢 / 🔵 |
| 2 | **Analyse financière : information financière, diagnostic et évaluation** ✅ | H. de La Bruslerie — Dunod | 🧠 Le plus complet (retraitements, flux, évaluation) | 🟢 |
| 2 | **Finance d'entreprise** ✅ | P. Vernimmen, P. Quiry, Y. Le Fur — Dalloz | 🧠 La bible de la finance | 🔵 **libre sur vernimmen.com** |
| 3 | **Le diagnostic financier** (3e éd.) ✅ | L. Batsch — Economica | 🧠 Diagnostic structuré | 🟢 |
| 3 | **Analyse financière** ✅ | E. Cohen — Economica | 🧠 Méthode complète | 🟢 |
| 3 | **Du bilan comptable au bilan financier** ✅ | F. Bonnet — Economica | 🧠 Les retraitements (→ fiche 10) | 🟢 |
| 3 | **Les ratios qui comptent** ✅ | J. Lochard — Eyrolles | 🧠 Les ratios expliqués | 🟢 |
| 3 | **Analyser et maîtriser la situation financière de son entreprise** ✅ | C. Duplat — Vuibert | 🧠 Approche pratique | 🟢 |
| 4 | **Analyse financière** ⭐ | B. & F. Grandguillot — Dunod | 🧠 Exactement ton cours S4 | 🟢 |
| 4 | **Financial Statement Analysis and Security Valuation** ⭐ | S. Penman | 🧠 Le niveau master : ce que disent les chiffres | 🟢 |
| 4 | **Financial Statement Analysis** ⭐ | K. Subramanyam | 🧠 Ratios, qualité du résultat | 🟢 |

### Finance d'entreprise (le « pourquoi »)
| Priorité | Ouvrage | Auteur / Éditeur | Rôle | Statut |
| --- | --- | --- | --- | --- |
| 2 | **Finance d'entreprise Tome 1** ✅ | R. Belkahia, H. Oudad | 🧠 | 🟢 / 🔵 |
| 3 | **Gestion Financière** ✅ | G. Charreaux — Litec | 🧠 | 🟢 |
| 3 | **Analyse et évaluation financière des entreprises et des groupes** ✅ | C. Hoarau — Vuibert | 🧠 Groupes → consolidation | 🟢 |
| 3 | **Analyse financière et évaluation d'entreprises** ✅ | S. Pariente — Pearson | 🧠 | 🟢 |
| 4 | **Finance** ✅ | Z. Bodie, R. Merton — Pearson | 🧠 Principes | 🟢 |
| 4 | **Fondements de gestion financière** ✅ | A. Corhay, M. Mapapa — Univ. Liège | 🧠 | 🟢 |
| 4 | **Investment Valuation** ⭐ | A. Damodaran | 🧠 Valuation (DCF, décotes) | 🔵 **libre sur son site** |

### IFRS & consolidation
| Priorité | Ouvrage | Auteur / Éditeur | Rôle | Statut |
| --- | --- | --- | --- | --- |
| 3 | **Pratique des normes IFRS** ✅ | R. Obert — Dunod | 🧠 Le référentiel IFRS expliqué | 🟢 |
| 3 | **Guides IFRS annuels PwC/KPMG/Deloitte/EY** ⭐ | Les 4 grands | 🧠 IFRS 15/16, IAS 12 — gratuits | 🔵 **libres (PDF officiels)** |

### Fiscalité & audit
| Priorité | Ouvrage | Auteur / Éditeur | Rôle | Statut |
| --- | --- | --- | --- | --- |
| 3 | **Précis de fiscalité marocaine** ⭐ | Éditions marocaines (dernière édition) | 🧠 La logique du système fiscal (taux → 📅 NotebookLM) | 🟢 / 🔵 |
| 3 | **Thèses ISCAE** ✅ (El Maguiri téléchargée) | ISCAE — groupeiscae.ma | 🧠 Gestion du résultat, audit, normalisation | 🔵 **libres** |
| 3 | **Thèse Elatife — Passage aux IFRS des cotées marocaines** ✅ | Elatife, El Houssaïn (2012) | 🧠 Convergence Maroc/IFRS | 🔵 à chercher |
| 4 | **UE9 Comptabilité** ✅ | Jahier, Lammari, Lépine, Ringuez — Fontaine Picard (2019) | 🧠 Manuel de cours | 🟢 |
| 4 | **Manuel d'audit légal marocain / Arens** ⭐ | OEC Maroc / Arens et al. | 🧠 La logique d'audit | 🟢 |

## 📅 Documents « faits » → restent dans NotebookLM (recherche datée)
> Ceux-là sont déjà dans ton corpus (`96 Documents Réels` + NotebookLM) — **ne pas dupliquer dans BookRAG** (ils changent chaque année) :
- **CGI 2025 + LF 2026 (BO 7470)** ✅ · Circulaires DGI 717/721 ✅ · Décret Charte 2025 ✅
- Taux IS / TVA / CM / CSS / RAS → toujours vérifier avec la date du jour (ex. « taux IS 2026 »)
- Barèmes IR, plafonds (espèces 5 000 DH, véhicules 400 000 DH…), seuils AMMC/BAM

## 🎯 Ordre d'ingestion recommandé (BookRAG)
1. **CGNC + PCGE intégral** (libre) — la logique de base
2. **Amine Bouayad T2 — Analyse et diagnostic financiers** (le livre marocain du PFE)
3. **Vernimmen** (libre) — la finance complète
4. **De La Bruslerie** — l'analyse en profondeur
5. **Fechtali & Fouguig** — la comptabilité marocaine
6. **Guides IFRS** (libres)
7. **Ibnabdeljalil — Diagnostic Financier** (complément marocain)
8. **Précis de fiscalité marocaine** — la logique fiscale
9. **Thèses ISCAE** (libres)
10. **Penman ou Subramanyam** — le niveau master

> 🔵 = légalement libre en PDF · 🟢 = à acheter · ✅ = déjà dans le vault (96 Documents Réels)

## Liens — où ça s'insère dans le fil
- Le service qui va lire ces livres → `C:\Users\salah eddine\bookrag` (README + tests ✅)
- Les faits datés → [[README — Index des documents réels]] · [[21 — Liasse fiscale]] · [[15 — Impôts (IS, IR, CM, CSS)]]
- La logique déjà structurée → [[Le Fil Conducteur]] · [[📖 Lexique — Comprendre les rapports]]
