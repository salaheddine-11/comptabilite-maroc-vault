### Tableau 1 : Transfert de charges (PCGE Maroc — ⚠️ pas de classe 79 !)
| Notion / Cas | Comptes PCGE Maroc | Écritures types (Débit / Crédit) | Spécificités |
| :--- | :--- | :--- | :--- |
| **Définition** | **7197** (Exploitation) · **7397** (Financier) · **7597** (Non courant) | Variable selon l'imputation finale | Technique pour modifier l'imputation initiale d'une charge ou l'annuler provisoirement. ⚠️ Le PCG français utilise 791/796 ; **le PCGE marocain utilise 7197/7397/7597** |
| **1. Avantage en nature** | **6176** (Charges personnel) · **71976** (TCE personnel) | D 6176 / C 71976 | Neutralise la charge initiale (loyer, véhicule) pour l'isoler et l'intégrer en paie |
| **2. Remboursement assurance** | **5141** (Banque) · **71973** (TCE autres charges externes) | D 5141 / C 71973 (ou 758 si gain accessoire) | Compense une charge de réparation de sinistre déjà comptabilisée |
| **3. Production immobilisée** | **Classe 2** · **714** (immob. produites) | D 21XX/23XX / C 714 | **Piège marocain** : INTERDIT d'utiliser 7197 — passe exclusivement par le compte **714** |

### Tableau 2 : Écritures de réouverture (01/01/N+1) — toutes OBLIGATOIRES
| Opération | Comptes | Écriture d'extourne | Rôle |
| :--- | :--- | :--- | :--- |
| **CCA** | **3491** / 61XX | D 61XX / C 3491 | Annule la charge soustraite à l'inventaire (486 en France) |
| **PCA** | **4491** / 71XX | D 4491 / C 71XX | Rapatrie le produit sur le nouvel exercice (487 en France) |
| **FAE** | **34271** / 71XX + 4455 | D 71XX + 4455 / C 34271 | Évite la double comptabilisation à la facture définitive |
| **FNP** | **4417** / 61XX + 3455 | D 4417 / C 61XX + 3455 | Neutralise la charge dès réception de la facture réelle |
| **Bilan d'ouverture** | **Rubrique 01** (011-015) | D 2/3/51 / C 1/4/55 | Soldes de clôture repris via rubrique 01 |
| **Balance après inventaire** | Comptes de situation | — | Base d'édition des états de synthèse |

### Tableau 3 : Correction d'erreurs et pièges
| Cas / Piège | Comptes | Méthode | Impact fiscal |
| :--- | :--- | :--- | :--- |
| **Erreur exercice courant** | Comptes d'origine | Contre-passation ou virement — la correction doit laisser l'écriture initiale **lisible** (négatif admis uniquement pour erreurs) | — |
| **Erreur exercice antérieur** | **6118/6128** (charges ant.) · **7188/7588** (produits ant.) | D 6118/6128 / C 34XX/44XX | Charges d'exercice prescrit non déductibles ; provisions irrégulières réintégrées (art. 10/11 CGI) |
| **Piège 1 : extourne des amortissements/provisions** | 28X/29X/39X/49X | **NE JAMAIS extourner** — reprise explicite (7194/7392/7596) | Art. 10 CGI : régularisation + dotation exercice suivant |
| **Piège 2 : écritures non extournées** | 3491, 4491, 4417 | Contre-passation obligatoire au 01/01 | Double comptabilisation en N+1 → image fidèle faussée + redressement possible |
