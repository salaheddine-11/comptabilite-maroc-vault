---
statut: ✅ Expliqué
categorie: Finance d'Entreprise
ordre: 55
corpus: NON
---

# 55 — Choix d'investissement : VAN, TRI, Payback

> [!quote] En une phrase
> Un investissement n'est pas un achat : c'est un **pari sur l'avenir**. Le TRI est le taux de mensonge préféré des directions — l'analyste doit savoir où il ment.

## 1. De quoi parle-t-on vraiment
- **Comptablement**, un investissement = une immobilisation (classe 2) qui s'amortit (→ [[05 — Amortissements]]) et se cède (→ [[19 — Cessions & réévaluation]]).
- **Économiquement**, un investissement = **un décaissement aujourd'hui contre des encaissements incertains demain**. La frontière est plus large que la classe 2 : une campagne marketing, une formation, un système d'information, une augmentation du BFG (→ [[08 — FRF, BFG & TN (analyse dynamique)]]) sont des investissements économiques.
- **Le découplage** : le résultat comptable enregistre l'investissement *après coup* (dotation annuelle 619x) ; la décision économique se prend *avant* (flux actualisés). Une entreprise peut afficher un bénéfice comptable et détruire de la valeur — et l'inverse.

## 2. Les critères de décision

| Critère | Définition | Règle | Piège principal |
| --- | --- | --- | --- |
| **VAN** [standard] | Σ FNTt / (1+k)^t − I0, flux actualisés au CMPC (→ [[57 — Structure de capital & CMPC (WACC)]]) | VAN > 0 → création de valeur | Le taux k décide de tout : un CMPC manipulé rend tout projet rentable |
| **TRI** [standard] | Taux qui annule la VAN | TRI > k → accepter | 3 pièges : TRI multiples (flux de signes alternés), TRI vs VAN (projets mutuellement exclusifs), réinvestissement implicite des flux au TRI |
| **Payback** [standard] | Délai de récupération du capital investi | Le plus court, sous contrainte de liquidité | Ignore les flux APRÈS la récupération — un projet lent mais très rentable est éliminé à tort |
| **Indice de profitabilité** [standard] | VAN / I0 | Classement quand le capital est rationné | Dépend du taux ; favorise les petits projets |

**La règle d'or** : la VAN est le critère roi (elle mesure la *création de valeur* en dirhams). Le TRI est un taux — il ne dit pas *combien* de valeur. Le Payback est un filtre de liquidité, pas un critère de rentabilité.

## 3. La construction des flux — le vrai travail
> Toute la valeur d'un chiffrage tient dans les flux, pas dans la formule. *Garbage in, garbage out.*

1. **FNT = résultat d'exploitation après IS + dotations − investissement − ΔBFG** [standard]
2. **Le piège du BFG** : une croissance des ventes augmente créances + stocks + (fournisseurs). Si ΔBFG > 0, le cash est *détruit* même quand le résultat progresse — le lien direct avec [[08 — FRF, BFG & TN (analyse dynamique)]] : l'entreprise qui « croît » sans financer son BFG s'asphyxie.
3. **Flux incrémentaux** : ne compter que ce qui *change* si le projet est fait. Exclure les coûts irrécupérables (déjà payés), inclure le coût d'opportunité (loyer perdu, temps de la direction).
4. **L'IS** : le taux marginal s'applique aux flux après dotations (→ [[15 — Impôts (IS, IR, CM, CSS)]]). Les dotations ne sont pas des cash-flows mais créent un **bouclier fiscal** : IS payé = IS théorique − IS économisé.
5. **La cession finale** : valeur résiduelle nette de l'IS sur plus-value (→ [[19 — Cessions & réévaluation]], 751/651) + **récupération du BFG** en fin de projet (le BFG se *libère* — souvent oublié).
6. **Crédit-bail vs achat** (→ [[12 — Crédit-bail]]) : deux structures de flux différentes (loyers vs amortissement + intérêts) ; on compare en *coût après IS*, jamais en cash brut.

## 4. Le contexte marocain
- **Taux sans risque** : obligations du Trésor / courbe BAM [À VÉRIFIER valeur courante] ; le taux d'actualisation doit intégrer la prime de risque pays Maroc (marché émergent) [standard].
- **TVA récupérable** (→ [[23 — TVA]]) : l'investissement se chiffre **hors TVA** quand elle est déductible — une erreur classique gonfle I0 de 20 %.
- **Subventions d'investissement** (→ [[48 — Subventions (exploitation, équilibre, investissement)]]) : à *déduire* du décaissement initial (ou traiter comme flux) — la décision réelle est celle de l'entreprise *après* subvention.
- **Incitations** (→ [[41 — Incitations fiscales & zones]]) : amortissement accéléré en zone (ZAI, CFC) = bouclier fiscal plus rapide → TRI amélioré sans changer le risque économique.
- **Financements participatifs** (→ [[33 — Financements participatifs]]) : Ijara/Mourabaha = structure de flux différente (marge au lieu d'intérêt), même logique de comparaison après IS.

## 5. Après la décision — le post-audit
La plupart des directions ne reviennent jamais sur leurs investissements : biais de confirmation, bonus déjà versés, « on a déjà dépensé ». **Le post-audit** (comparer FNT prévus vs réels, 2-3 ans après) est le seul correctif — et son absence est un signal sur la culture de décision de l'entreprise.

## 6. Le pont avec les états financiers
- **Bilan** : la classe 2 grossit (et le FRF se dégrade si l'investissement est financé à court terme, → [[08 — FRF, BFG & TN (analyse dynamique)]])
- **CPC** : les dotations 619x réduisent le résultat *annuel* — mais le TRI était déjà décidé avant
- **TF** : le décaissement apparaît au module « investissement » ; le flux de trésorerie disponible est la vérité comptable du projet
- **ROI comptable ≠ TRI** : résultat / actif moyen ignore la valeur temps — on ne compare que des pommes avec des pommes.

> [!warning] The Forensic Deduction (Le Signe)
> **L'anomalie** : des investissements (capex) qui croissent plus vite que le chiffre d'affaires *sans* hausse de capacité (CA par m², CA par employé, production stables) — ou des « investissements de modernisation » dont le montant égale exactement les amortissements annuels.
> **L'intention** : présenter du *remplacement* (dépense de maintien) comme de la *croissance* — pour le conseil, les banques, ou pour *gonfler la base d'actifs* avant une cession et justifier un prix (→ [[56 — Valorisation d'entreprise (ANR, multiples, DCF)]]). À l'inverse, une direction qui *réduit* les capex de maintien gonfle l'EBITDA court terme — elle emprunte à l'avenir.
> **Le risque caché** : obsolescence brutale, perte de compétitivité, et à terme une dépréciation massive (29/391, → [[14 — Provisions]]) qui tombe en une seule fois — le « mur d'amortissements » que l'analyse des ratios ne voit pas venir.

> [!danger] Red Flags & Omissions
> 1. Des TRI annoncés **sans ΔBFG** dans les flux — la croissance du projet détruit du cash non chiffré.
> 2. Un taux d'actualisation unique pour tous les projets (le risque pays n'est pas le risque projet).
> 3. Des investissements « stratégiques » dont le **post-audit n'existe pas** — personne ne vérifie, donc personne n'apprend.
> 4. Le silence de l'ETIC : les engagements d'investissement (classe 0, → [[27 — Engagements hors bilan (classe 0)]]) et les immobilisations en cours (233) jamais commentés — la direction ne dit pas ce qu'elle a promis d'acheter.

## Liens — où ça s'insère dans le fil
- Circuit 3 : décide de l'emploi des capitaux → [[18 — Financement]] · [[24 — Capitaux propres]] · [[57 — Structure de capital & CMPC (WACC)]]
- Analyse : les flux du projet → [[08 — FRF, BFG & TN (analyse dynamique)]] · la rentabilité comptable → [[09 — Ratios & SIG]]
- Fiscal : bouclier fiscal et incitations → [[15 — Impôts (IS, IR, CM, CSS)]] · [[41 — Incitations fiscales & zones]]
- Alternatives de financement → [[12 — Crédit-bail]] · [[33 — Financements participatifs]]

## Sources
Théorie financière standard (VAN, TRI, Payback) [standard] · CGI art. 10 (déductibilité des intérêts) · circulaires DGI [À VÉRIFIER] · documents de référence AMMC (section investissements des émetteurs).
