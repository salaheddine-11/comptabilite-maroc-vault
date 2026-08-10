---
tags: [fil-conducteur, moc, systeme, vue-ensemble]
---

# 🧭 Le Fil Conducteur — 71 thèmes, un seul système

> [!abstract] Pourquoi ce document existe
> Les 71 thèmes du vault ne sont pas une liste à cocher : ce sont les **pièces d'une seule machine**. Ce document raconte comment elles s'emboîtent — le *flow* complet, de la facture du jour au rapport de l'analyste, en passant par l'impôt et le groupe.
>
> **La règle d'or :** tout thème est un *organe* (compte), un *flux* (écriture), un *état* (sortie) ou un *contrôle* (audit/fiscal). Trouvez le circuit, vous trouvez le rôle.

---

## 0. La carte générale : une machine à 4 circuits + 2 miroirs + 3 sorties

```
                        ┌────────────────────────────────────────────────────┐
                        │            CIRCUIT 3 — LE FINANCEMENT              │
                        │   (24 Capitaux propres · 18 Financement ·          │
                        │    12 Crédit-bail · 05 Amortissements · 08 FRF)    │
                        └──────────────────────────┬─────────────────────────┘
                                                   │ porte la structure
                                                   ▼
┌────────────────────────────────────────────────────────────────────────────────────┐
│              CIRCUIT 1 — L'EXPLOITATION (le cœur qui tourne chaque jour)            │
│                                                                                    │
│   01 PCGE ─→ 02 Cycle ─→ 03 Écritures ─→ 22 Stocks ─→ 16 Créances ─→ 17 Trésorerie │
│   (grammaire)  (pipeline)   (briques)     (valeur)    (crédit client)   (cash)     │
│                                                                                    │
│   ▲ chaque jour : acheter → stocker → vendre → encaisser — c'est ici que naît le BFG│
└────────────────────────────────────────────────────────────────────────────────────┘
                        │
                        ▼  une fois par an : tout se recoupe
┌────────────────────────────────────────────────────────────────────────────────────┐
│              CIRCUIT 2 — LA CLÔTURE (la vérité annuelle)                            │
│                                                                                    │
│   13 Régularisations → 14 Provisions → 05 Amortissements → 04 États de synthèse     │
│   (rattacher N)          (prudence)       (étaler)         (BL·CPC·ESG·TF·ETIC)     │
│        │                                                                           │
│        └──→ 23 TVA → 15 Impôts (IS/CM/CSS) → 21 Liasse fiscale → 26 Passage fiscal │
│            (détecteur)      (l'impôt)           (23 tableaux)      (T22 : la vérité)│
└────────────────────────────────────────────────────────────────────────────────────┘
                        │
                        ▼  quand l'entreprise grandit
┌────────────────────────────────────────────────────────────────────────────────────┐
│              CIRCUIT 4 — LE GROUPE & L'INTERNATIONAL                               │
│   31 Comptes de liaison → 20 Consolidation → 29 IFRS · 25 Devises · 27 Hors bilan  │
└────────────────────────────────────────────────────────────────────────────────────┘

MIROIRS PARALLÈLES :  28 Comptabilité analytique (classe 9, interne) · 30 Affacturage · 32-34 Sectoriel
SORTIES D'ANALYSE :   07 Messages cachés · 09 Ratios & SIG · 08 FRF/BFG/TN · 10 Retraitements
SORTIES DE VALEUR :   55 Choix d'investissement · 56 Valorisation · 57 Structure de capital (CMPC)
```

---

## 1. Circuit 1 — L'exploitation : le cœur qui tourne chaque jour

> **La question du circuit :** comment l'argent entre dans l'entreprise, se transforme, et ressort.

**[[01 — Logique du PCGE & principes]]** est la grammaire : 10 classes (1-5 bilan, 6-8 gestion, 9 analytique, 0 spéciaux), partie double, 7 principes (coût historique, prudence, image fidèle…). Sans cette carte, aucune écriture ne fait sens. **[[02 — Cycle comptable quotidien]]** est le pipeline qui applique la grammaire : *pièce justificative → journal → grand-livre → balance → inventaire → clôture → états* (loi 9-88 art. 1-9).

Les **[[03 — Écritures comptables types]]** sont les briques du quotidien : vente comptant/crédit (3421/7111/4455), achat (6121/3455/4411), paie (6171/4432/4441/44525), emprunt (5141/1481). **Le message caché du circuit :** la vente à crédit crée un produit SANS cash — c'est la **comptabilité d'engagement** (loi 9-88 art. 10), et c'est exactement ici que naît le **BFG** ([[08 — FRF, BFG & TN (analyse dynamique)]]). Les **[[46 — RRR & emballages (rabais, remises, ristournes)]]** affinent la facture : réductions sur facture = net commercial, hors facture = 6119/7119, emballages consignés = 3413/4425 (sans TVA, jusqu'au boni/mali). La **[[50 — Paie & charges sociales 2026 (CNSS, IR, CIMR)]]** détaille le mini-circuit fiscal mensuel : CNSS 21,09%+6,74%, IR barème 2026 (seuil 40 000 DH), CIMR déductible — le tout en 6171/6174.

- **[[22 — Stocks]]** : la valeur qui attend. CMUP/FIFO (seuls admis), variation SF − SI qui rejoint les achats (6114/6124) ou la production (713x). *Un stock qui gonfle sans lien avec le CA = résultat gonflé.*
- **[[16 — Créances]]** : le crédit accordé aux clients. 3421 → 3424 (douteux) → provisions 3942. Le glissement 3421→3424 est le premier signal de dégradation. Les **effets de commerce ([[45 — Effets de commerce (LCR, BOR, escompte, protêt)]], 3425/4415)** et l'**affacturage ([[30 — Affacturage]])** sont les deux façons de transformer le crédit client en cash — le cycle complet : acceptation → remise à l'escompte (5520) → encaissement (5113) → protêt si impayé (loi 15-95).
- **[[17 — Trésorerie]]** : le cash enfin. 51 à l'actif, **55 au passif (découverts)** — le CGNC les présente séparément. Un découvert récurrent (5541) dit : *le BFG est financé par du court terme bancaire* → fragilité.

> 🔗 **Bouclage du circuit 1 :** TN = FRF − BFG ([[08 — FRF, BFG & TN (analyse dynamique)]]) — la trésorerie est le *solde* de tout le système, pas une ligne isolée. ΔTN = ΔFRF − ΔBFG : le contrôle croisé des états.

---

## 2. Circuit 2 — La clôture : la vérité annuelle

> **La question du circuit :** comment le résultat de l'exercice se construit… et se vérifie. C'est la **zone n°1 de l'auditeur**.

1. **[[13 — Régularisations de fin d'exercice]]** — spécialisation des exercices (art. 17) : CCA (3491), PCA (4491), charges à payer, produits à recevoir (3493), **FAE (34271)**, **FNP (44171)** + contre-passation au 01/01. *Ce sont des calculs internes, sans flux de trésorerie — le réceptacle préféré de la gestion du résultat.* **[[49 — Transferts de charges, clôture & réouverture]]** complète la mécanique : transferts en 7197/7397/7597 (⚠️ pas 791), production immobilisée par 714, extournes obligatoires des CCA/PCA/FAE/FNP — mais jamais des amortissements ni provisions.
2. **[[14 — Provisions]]** — prudence (art. 16) : dépréciation stocks (391), créances (394), immobilisations (29), risques et charges (15), réglementées (135). *Le thermomètre de l'honnêteté : reprises massives (719x) = lissage qui se libère.*
3. **[[05 — Amortissements]]** — étaler le coût sur la durée d'usage (619x/28xx). *La date de départ et la durée sont des choix → levier de résultat n°1 (thèses ISCAE).*
4. **[[04 — États de synthèse (BL, CPC, ESG, TF, ETIC)]]** — le « tout indissociable » (loi 9-88 art. 9) : BL (photo), CPC (film), ESG (cascade MB→VA→EBE→RN + CAF), TF (explication du cash), ETIC (**le procès-verbal des décisions**).
5. **[[23 — TVA]]** — le détecteur de mensonges : 3455/4455, solde 4456 ou 3456, tableau T21. *CA déclaré en TVA ≠ CA du CPC = l'un des deux ment.*
6. **[[15 — Impôts (IS, IR, CM, CSS)]]** — 20/35/40 % (2026), CM 0,25 % (min 3 000 DH), CSS 1,5-5 % (BNF ≥ 1 M DH). **[[21 — Liasse fiscale]]** : les 23 tableaux T1-T23 que voit l'inspecteur. **[[26 — Passage résultat comptable → fiscal]]** : le tableau T22/B12 — réintégrations/déductions — **l'écart entre l'image fidèle et l'assiette fiscale est souvent la vérité**.

> 🔗 **Bouclage du circuit 2 :** les régularisations (13) nourrissent le CPC ; les provisions (14) et amortissements (5) le résultat ET le bilan ; le T22 (26) transforme le résultat comptable en base IS ; la liasse (21) est la version « fiscale » du dossier complet. **L'ETIC est le ciment : c'est lui qui dit quelles décisions ont été prises (A1 dérogations, A2 changements, B1-B10 tableaux).**

---

## 3. Circuit 3 — Le financement : la structure qui porte tout

> **La question du circuit :** d'où vient l'argent long qui finance les emplois durables ? Sans ce circuit, le circuit 1 ne peut pas tourner.

- **[[24 — Capitaux propres]]** : 1111 capital, primes (112x), réserve légale (1140), RAN (1161/1169), résultat (1191/1199), écart de réévaluation (1130 — **non distribuable**). Le circuit d'affectation en 5 étapes (clôture → AGO → réserve légale → dividendes 4465 → RAN). *Capital non libéré + CCA énormes (4463) = des associés qui peuvent retirer leur argent demain.* **[[47 — Opérations sur capital]]** : augmentation en numéraire (3462/1119/1121), en nature (CAA obligatoire, 1123 prime d'apport), réduction par pertes ou rachat — l'apport en industrie est interdit en SA.
- **[[44 — Immobilisations financières & titres]]** : le portefeuille durable — 2510 titres de participation, 258 autres titres, 248 créances financières, dépréciations 2951/2941. Dividendes en 7321 (pas 7511), cession 7514/6514, régime mère-fille : abattement 100% (art. 6-I-C-1°).
- **[[48 — Subventions (exploitation, équilibre, investissement)]]** : 7161 (courant), 7561 (non courant), 1311/1319 (capitaux propres assimilés) — reprise 7577 au rythme de l'amortissement, terrain sur 10 ans (art. 9-II CGI).
- **[[18 — Financement]]** : 1481 emprunts bancaires, 1410 obligataires, subventions d'investissement (1311 — capitaux propres assimilés), **CCA 4463 + intérêts (63114)** — déductibles seulement si capital libéré, base ≤ capital, taux ≤ taux BAM (art. 10-II-A CGI).
- **[[12 — Crédit-bail]]** : hors bilan social (061 + ETIC B10), **réintégré par l'analyste** en dette financière — sinon la dette réelle est sous-estimée.
- **[[11 — Non-valeurs]]** : actif FICTIF (211x, amorti ≤ 5 ans) — éliminé de l'actif net réel.
- **[[19 — Cessions & réévaluation]]** : 751/651 (VNA), écart 1130, quasi-fonds propres (13 + 15 sans objet réel).
- **[[08 — FRF, BFG & TN (analyse dynamique)]]** : FRF = Financement permanent − Actif immobilisé ≥ 0 = la marge de sécurité de long terme. Le TF (2 modules) explique POURQUOI le FRF a bougé.

> 🔗 **Bouclage du circuit 3 :** le financement (18) achète les immobilisations (classe 2), qui s'amortissent (05), ce qui détruit du FRF (08)… que la CAF reconstruit. **L'autofinancement = CAF − dividendes : c'est le carburant du renouvellement.**

---

## 4. Circuit 4 — Le groupe & l'international : quand l'entreprise grandit

> **La question du circuit :** le même PCGE, appliqué à plusieurs entités et plusieurs monnaies.

- **[[31 — Comptes de liaison siège_succursales]]** : rubrique 16 (1601/1605) — les opérations internes au réseau d'une même personne morale (⚠️ en France la rubrique 16 = emprunts ; au Maroc = liaison).
- **[[20 — Consolidation]]** : périmètre (loi 17-95 art. 356), 3 méthodes (IG, IP, MEE), survaleur (amortie 10 ans max CGNC vs test de dépréciation IFRS), intérêts minoritaires, éliminations intra-groupe.
- **[[29 — IFRS vs CGNC]]** : coût historique vs juste valeur, IFRS 16 (crédit-bail), impôts différés — les cotées, banques et assurances publient en IFRS depuis 2008.
- **[[25 — Devises & ECA-ECP]]** : réévaluation au dernier cours, ECA (27/37, provisionnées 6393) vs ECP (17/47, contre-passés), 633/733. *Vital pour les exportateurs (agrumes, conserveries — Agadir).*
- **[[27 — Engagements hors bilan (classe 0)]]** : 041 cautions, 043 retraites, 061 crédit-bail — *les bombes à retardement* : un bilan équilibré peut cacher des cautions croisées qui inversent un diagnostic de solvabilité.
- **[[51 — TVA à l'importation & exportation]]** : à l'import, TVA 20% sur CAF + DAI (34552) ; à l'export, exonération avec droit à déduction (art. 92) ; entre les deux, les régimes suspensifs (art. 94) et le remboursement du crédit (art. 103, SIMPL, cible 90 jours).
- **[[52 — Dissolution & liquidation]]** : le terminus du système — dissolution (AGE, art. 356-357 : situation nette < 1/4 du capital), liquidation (réalisation 751/651, boni/mali, 3488), IS de cessation sous 45 jours, RAS sur le boni.

---

## 5. Les miroirs et les sorties — les thèmes qui éclairent les 4 circuits

| Thème | Rôle dans le système | Alimente |
| --- | --- | --- |
| [[28 — Comptabilité analytique (classe 9)]] | Miroir interne de la comptabilité générale (comptes réfléchis 90) ; coûts d'achat/production/revient | Valorisation des stocks, contrôle budgétaire — se réconcilie avec le résultat général (98 ↔ 88) |
| [[30 — Affacturage]] | Transforme les créances (11) en trésorerie (12) — finance le circuit 1 | Réduit le BFG (08) ; opération bancaire (sectoriel) |
| [[33 — Financements participatifs]] | Variante du circuit 3 : Mourabaha, Ijara, Moucharaka, Salam, Sukuk | Finance les immobilisations et le cycle — comptes PCEC |
| [[32 — Plans comptables sectoriels]] | Adaptations du PCGE : PCEC (banques), assurances, immobilier, agricole, associations, OPCVM/OPCI | Benchmarking sectoriel (04) |
| [[34 — Normes comptables de l'État]] | Règles du secteur public (deniers publics) — hors PCGE | Périmètre public |
| [[10 — Retraitements (valeur comptable → valeur actuelle)]] | Reconstruit la réalité économique : bilan comptable → bilan financier (14 retraitements) | ANC/ANR, DCF, consolidations, décotes |
| [[07 — Messages cachés (lecture entre les lignes)]] | Synthèse de tout : les 13 signaux d'alerte | Chaque signal pointe un poste précis |
| [[09 — Ratios & SIG]] | La lecture chiffrée : MB → VA → EBE → CAF + ratios (seuils du cours) | DSO↔créances, DIO↔stocks, DPO↔fournisseurs, ROE, capacité de remboursement |

## 5bis. Les compléments 2026 — l'actualité du référentiel

| Thème | Pourquoi il complète le système |
| --- | --- |
| [[35 — Réforme comptable marocaine (convergence IFRS)]] | Le chantier CNC/OEC : le CGNC converge vers l'IFRS — l'avenir de tous les circuits |
| [[36 — Facturation électronique]] | La DGI généralise la e-facture (2026) : pièces, TVA et liasse se dématérialisent |
| [[37 — Loi 32-10 (délais de paiement)]] | Contrôlée par le CAC — et ses indemnités sont **déductibles** (exception art. 11-I) |
| [[38 — Impôts différés]] | Le pont fiscal CGNC (1351) ↔ IAS 12 en consolidation |
| [[39 — Fusions & scissions]] | La restructuration : capital 1111, primes 1122/1123, art. 161 vs 162 |
| [[40 — Flux de trésorerie (IFRS vs TF CGNC)]] | Deux récits du cash : équilibre fonctionnel vs liquidité réelle |
| [[41 — Incitations fiscales & zones]] | ZAI/CFC/startups : IS 0 % 5 ans puis 20 % — à retraiter dans l'analyse |
| [[42 — Application Souss-Massa]] | Agro-export, tourisme, pêche, immobilier : le système appliqué au terrain |

## 5ter. Les compléments 09/08/2026 — les rouages manquants de la comptabilité générale

| Thème | Pourquoi il complète le système |
| --- | --- |
| [[44 — Immobilisations financières & titres]] | Circuit 3 : le portefeuille durable (2510/2581/2487) et le régime mère-fille 100% |
| [[45 — Effets de commerce (LCR, BOR, escompte, protêt)]] | Circuit 1 : transformer le crédit client en cash — cycle complet loi 15-95 |
| [[46 — RRR & emballages (rabais, remises, ristournes)]] | Circuit 1 : la facture dans tous ses états — net commercial, avoirs, consignation |
| [[47 — Opérations sur capital]] | Circuit 3 : augmenter/réduire le capital, apports, réserve légale |
| [[48 — Subventions (exploitation, équilibre, investissement)]] | Circuits 2-3 : 7161/7561 produits, 1311 + 7577 étalement (terrain 10 ans) |
| [[49 — Transferts de charges, clôture & réouverture]] | Circuit 2 : 7197/7397/7597, 714, extournes — le passage d'un exercice à l'autre |
| [[50 — Paie & charges sociales 2026 (CNSS, IR, CIMR)]] | Circuit 1 : le bulletin de paie 2026 — CNSS 27,83%, IR seuil 40 000, CIMR |
| [[51 — TVA à l'importation & exportation]] | Circuit 4 : CAF+DAI, régimes suspensifs, remboursement SIMPL 90 jours |
| [[52 — Dissolution & liquidation]] | Le terminus : fin de vie de l'entreprise, boni/mali, IS de cessation |
| [[53 — Templates d'écritures comptables]] | La table de référence : toutes les écritures types du système en un seul tableau, avec la fiche-source de chaque ligne |
| [[54 — La logique des écritures comptables]] | La méthode : équation, tableau des 6 cas, raisonnement en 5 étapes — comment retrouver n'importe quelle écriture |

## 5quater. La finance d'entreprise — la création de valeur (10/08/2026)

> La sortie ultime de la machine : les 4 circuits produisent des états (04) et des ratios (09) — la finance d'entreprise les transforme en **décisions** : investir, valoriser, financer. C'est le pont entre le *passé comptable* et l'*avenir économique*.

| Thème | Pourquoi il complète le système |
| --- | --- |
| [[55 — Choix d'investissement (VAN, TRI, Payback)]] | La décision d'emploi des capitaux du circuit 3 : flux actualisés, piège du BFG, bouclier fiscal |
| [[56 — Valorisation d'entreprise (ANR, multiples, DCF)]] | Le prix des 4 circuits : retraitements (10) → ANR, comparables MASI, DCF |
| [[57 — Structure de capital & CMPC (WACC)]] | Le taux d'exigence des apporteurs de capitaux : le CMPC actualise 55 et 56 — la ligne de flottaison de la création de valeur |
| [[58 — Fusions & acquisitions (M&A)]] | L'acquisition : prime de contrôle, due diligence, survaleur (écart d'acquisition) — payer le juste prix d'un pari |
| [[59 — Politique de financement & dividende]] | Le retour aux actionnaires : taux de distribution, RAS, signaux — la politique de dividende comme message |

## 5quinquies. Le pilotage — le pont vers l'avenir (10/08/2026)

> Les 4 circuits racontent le passé ; le pilotage projette la machine dans l'avenir. Le budget promet, l'écart mesure l'honnêteté de la promesse, le KPI déclenche la décision.

| Thème | Pourquoi il complète le système |
| --- | --- |
| [[65 — Budget & contrôle budgétaire (écarts)]] | La projection des circuits 1-2 : budget de trésorerie = la survie ; écarts = la vérité de l'exécution |
| [[66 — Tableaux de bord & KPIs (pilotage)]] | Les 5-7 indicateurs qui pilotent : DSO/DIO/DPO, CAF, cash forecast — chaque KPI est une décision attachée |
| [[67 — Le prévisionnel financier & le business plan]] | Le budget projeté à 3-5 ans : bilan prévisionnel, plan de financement, scénarios — le pont vers la valorisation (56) |

## 5sexies. Le cycle de vie extrême — la restructuration (10/08/2026)

> Quand la machine casse : l'échelle de secours de la loi 73-17, du mandat ad hoc confidentiel à la liquidation judiciaire publique — et l'art de lire la défaillance deux ans avant le tribunal.

| Thème | Pourquoi il complète le système |
| --- | --- |
| [[70 — Restructuration & entreprises en difficulté (Loi 73-17)]] | Les 4 dispositifs légaux + la comptabilité de la crise (continuité d'exploitation, provisions) |
| [[71 — Diagnostic de défaillance & scoring]] | Le radar FRF → BFG → TN + les signaux externes (protêts, incidents BAM) + le plan de redressement |
| [[73 — Droit des sociétés marocain (formes & gouvernance légale)]] | Le squelette juridique : SNC/SCS/SARL/SA, conventions réglementées, seuils — la transparence varie avec la forme |

## 5septies. La modernité — ESG, gouvernance, digitalisation (10/08/2026)

> La machine s'ouvre au monde : le reporting extra-financier (AMMC) liste les passifs que le bilan n'a pas provisionnés ; la gouvernance est le système immunitaire ; la facturation électronique (36) numérise la piste d'audit.

| Thème | Pourquoi il complète le système |
| --- | --- |
| [[75 — ESG & reporting extra-financier (AMMC)]] | Le E/S/G comme indicateur avancé du passif — provisions environnementales, coût du capital, greenwashing |
| [[76 — Gouvernance d'entreprise & contrôle interne]] | Conseil, comités, conventions réglementées, séparation des fonctions — le contrôle de tous les circuits |
| [[79 — Fraude financière & cybersécurité]] | Le triangle de la fraude, les faux états, la détection forensique — le contrôle interne comme vaccin, le cyber comme nouveau champ |

## 5octies. La couverture — trésorerie avancée & risques (10/08/2026)

> La machine face à l'incertitude : dérivés pour couvrir le change et les taux (80), mutualisation de la trésorerie du groupe (81), ingénierie des financements hors bilan (82) — et la lecture forensique de ce que le bilan ne montre pas.

| Thème | Pourquoi il complète le système |
| --- | --- |
| [[80 — Couverture des risques financiers (dérivés)]] | Forwards/options/swaps : la couverture de l'exposition (25) — et le hors bilan qui peut cacher la spéculation |
| [[81 — Cash pooling & trésorerie de groupe]] | La centralisation des soldes : frais financiers réduits, mais contagion et tunneling inversé (31, 20) |
| [[82 — Financements structurés & titrisation]] | FCT, SPV, sale & lease-back : la liquidité sur flux futurs — et les recours cachés que l'analyste retraite |

---

## 6. Les 3 fils transversaux (présents dans chaque circuit)

### 6.1 La règle des deux traitements (comptable vs fiscal)
Partout où le CGNC et le CGI divergent, le vault le signale explicitement :
- **Provisions** : comptable = prudence (14) ; fiscal = déductibles seulement si individualisées + recours judiciaire 12 mois (10-I-F-2° CGI) → réintégration au T22.
- **Amortissements** : comptable = durée d'usage ; fiscal = dégressif optionnel (art. 10-III-C-1°), plafond véhicules 400 000 DH TTC (LF 2025).
- **Subventions d'investissement** : comptable = capitaux propres assimilés (1311) ; fiscal = étalement au rythme de l'amortissement.
- **Dividendes reçus** : abattement fiscal 100 % (art. 6-I-C-1°) à déduire au tableau de passage ; RAS à la distribution (art. 247-XXXVII-C).

### 6.2 Les 12 pièges du référentiel marocain (détail dans [[01 — Logique du PCGE & principes]])
Analyse fonctionnelle (pas par échéance) · non-valeurs = actif fictif · 13 = quasi-fonds propres · rubrique 16 = liaison (pas emprunts) · tiers non compensés · 51/55 séparés · escomptes en 6386, pas de 78/79 · CAF additive · IS/CSS non déductibles · classe 8 en cascade · classe 0 hors bilan · classe 9 à réconcilier.

### 6.3 Les 13 messages cachés (détail dans [[07 — Messages cachés (lecture entre les lignes)]])
Actif fictif · stocks gonflés · pertes clients masquées (3424) · asphyxie fournisseurs · résultat non pérenne (courant vs non courant) · lissage par provisions · CCA/PCA anormaux · usure « arrangée » (amortissements) · CCA 4463 + risque fiscal · liquidité sous perfusion (55) · désinvestissement dissimulé (751/651) · redressement fiscal provisions clients · fiscalité contre image fidèle (1130/1351).

---

## 7. La boucle complète — l'histoire en 10 lignes

> Une entreprise marocaine **naît** avec des capitaux propres (16) et des dettes de financement (18) — le circuit 3. Elle **achète** des immobilisations qui s'amortissent (05) et un stock qui se vend (15) : chaque vente crée une créance (11) qui devient du cash (12) — le circuit 1, qui dégage un BFG financé par le FRF (08). Chaque année, la **clôture** rattache, provisionne, amortit (13-14-05), produit les 5 états (04), déclare la TVA (23) et l'impôt (15) à travers la liasse (21) et le tableau de passage (26) — le circuit 2, où l'auditeur vérifie tout. Si elle grandit, elle consolide (20), se couvre en devises (17), surveille ses engagements (27) et compare à l'IFRS (29). Et à chaque instant, l'analyste retraite (10), calcule (09)… et **lit entre les lignes** (07).

**Un poste du bilan = une décision passée. Un choix comptable = une intention. Le fil conducteur vous donne la carte — les fiches vous donnent le détail — les rapports vous donnent la profondeur.**

---

*Document maître du vault — généré le 08/08/2026, mis à jour le 10/08/2026. Les liens pointent vers les 71 fiches thématiques et les 6 rapports fondateurs.*
