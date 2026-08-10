---
statut: ✅ Expliqué
categorie: Mécanismes
ordre: 24
corpus: OUI
---

# 24 — Capitaux propres

> [!quote] En une phrase
> L'argent que les propriétaires ont réellement mis (et laissé) dans l'entreprise — *le haut du bilan raconte qui possède et qui décide*.

## La structure complète (PCGE)

| Rubrique | Compte | Ce que c'est |
| --- | --- | --- |
| **Capital social** | 1111 | Valeur nominale cumulée des actions/parts souscrites |
| **Capital appelé / versé** | 1119 | Fraction souscrite non appelée ou non libérée (en déduction) |
| **Primes** | 1121 émission · 1122 fusion · 1123 apport | Excédent du prix d'émission sur le nominal |
| **Écart de réévaluation** | 1130 | Plus-values latentes de la réévaluation libre — **non distribuable** |
| **Réserve légale** | 1140 | 5 % du bénéfice jusqu'à 10 % du capital (SA/SARL) **[À VÉRIFIER]** |
| **Autres réserves** | 1151 statutaires · 1152 facultatives · 1155 réglementées | Bénéfices affectés durablement |
| **Report à nouveau** | 1161 (créditeur) / 1169 (débiteur) | Bénéfices non affectés / pertes non apurées |
| **Résultat net** | 1191 (bénéfice) / 1199 (perte) | Le solde du CPC, en attente d'affectation |
| **En instance d'affectation** | 1181 / 1189 | Le résultat de N−1 pas encore affecté par l'AGO |
| **Capitaux propres assimilés** | 1311 subventions · 1351 amortissements dérogatoires | Ressources quasi-permanentes (quasi-fonds propres) |

## Le circuit d'affectation du résultat (5 étapes)
1. **Clôture** : D 8100 / C 1191 (ou inverse si perte) — le résultat rejoint le bilan
2. **AGO (sous 6 mois)** : les associés approuvent et décident
3. **Réserve légale** : D 1191 / C 1140 — prélèvement prioritaire
4. **Dividendes** : D 1191 / C 4465 → **retenue à la source** (art. 247-XXXVII-C CGI) — taux en **baisse** : 12,50 % (2025) → **11,25 % (2026)** → 10 % (2027) (LF 2025)
5. **Report à nouveau** : D 1191 / C 1161 — le reliquat reste

## 🚨 Les 4 messages cachés
| Message caché | Signe | Ce que ça révèle |
| --- | --- | --- |
| **Capital non libéré** | Solde important au 1119 | Les associés n'ont pas versé les fonds promis → **intérêts CCA non déductibles** tant que capital non libéré (art. 10-II-A) |
| **Perfusion par les CCA** | 4463 démesuré vs 1111 | Financement par dette court terme remboursable — le retrait des associés peut asphyxier |
| **Politique « sangsue »** | Dividendes > résultat net (prélevés sur réserves) | Décapitalisation — FRF et autofinancement détériorés |
| **Absence de réserves** | 1152 jamais crédité, 1161 vidé | La moindre perte crée un RAN débiteur (1169) |

## Ce que l'analyste en fait
- **ROE = RN / fonds propres moyens** · autonomie financière = 11/14
- **Neutraliser 1130** dans les ratios de solvabilité (pas de cash réel) ; **retraiter 13 + 15 sans objet réel** en quasi-fonds propres
- Comparer **4463 vs 1111** avant de conclure sur la solidité

## Liens — où ça s'insère dans le fil
- Circuit 3 : socle du FRF → [[08 — FRF, BFG & TN (analyse dynamique)]] · accueille la réévaluation → [[19 — Cessions & réévaluation]]
- Dividendes + RAS → [[26 — Passage résultat comptable → fiscal]] · le circuit d'affectation rejoint la trésorerie → [[17 — Trésorerie]]

---

## 🕵️ The Forensic Deduction (Le Signe)

> [!warning] L'anomalie
> Un capital social jamais entièrement libéré (3462 permanent), des comptes courants d'associés (4463) qui dépassent le capital, une réserve légale non constituée (1140 < 5 % du bénéfice), ou un RAN négatif (1169) accompagné d'une distribution (→ [[59 — Politique de financement & dividende]]).

> [!warning] L'intention
> Le circuit des capitaux propres est la **carte d'identité des décisions des associés** : capital non libéré = promesses non tenues ; 4463 énormes = la dette des associés envers la société (ou l'inverse) ; distributions au-delà du résultat distribuable = sortie de cash déguisée. L'écart de réévaluation (1130, non distribuable) distribué est une fraude à la loi.

> [!warning] Le risque caché
> Les quasi-fonds propres illusoires (le capital « annoncé » n'est pas là), la requalification fiscale des intérêts sur CCA non libérés (art. 10-II-A), et l'interdiction de distribution violée — la nullité des décisions et la responsabilité des dirigeants.

> [!danger] Red Flags & Omissions
> 1. 4463 > capital social — les associés financent plus que leur mise ; que se passe-t-il s'ils retirent ?
> 2. Réserve légale non constituée ou plafonnée prématurément — le bénéfice a-t-il été réel ?
> 3. RAN négatif (1169) avec dividende versé — d'où vient l'argent distribué ?
> 4. Le silence : l'ETIC ne détaille pas le tableau de répartition du résultat (→ [[04 — États de synthèse (BL, CPC, ESG, TF, ETIC)]]) — la direction ne dit pas qui a reçu quoi.

## Sources
PCGE (11, 13, 118, 119) · loi 17-95 / 5-96 · CGI art. 10-II-A, 247-XXXVII-C · thèses ISCAE.
