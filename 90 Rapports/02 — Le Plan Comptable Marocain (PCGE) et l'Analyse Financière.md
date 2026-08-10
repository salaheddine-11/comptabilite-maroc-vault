# Le Plan Comptable Marocain (PCGE/CGNC) et son Articulation avec l'Analyse Financière (1)

**Périmètre** : Explication de chaque classe de comptes du Plan Comptable Général des Entreprises marocain (PCGE, issu du CGNC et de la loi 9-88) : ce que contient chaque classe, à quoi elle sert, quand on l'utilise, et comment elle alimente l'analyse financière (états de synthèse, FRF/BFG/TN, ratios).

**Statut des informations** : contenu fondé sur le corpus de 308 sources NotebookLM (CGNC officiel, plans comptables sectoriels, documents de travail CRMEF, guides Upsilon, liasse fiscale DGI) **et vérifié compte par compte contre le « Plan Comptable Marocain » officiel (document PDF fourni par l'utilisateur, 1 307 lignes de nomenclature)**. Les éléments absents des sources sont signalés **[standard]** (pratique classique d'analyse) ou **[À VÉRIFIER]** (à confirmer sur texte officiel).

---

## 1. Logique générale du PCGE : une codification décimale hiérarchique

Le PCGE marocain organise la comptabilité selon une **codification décimale à 5 niveaux** :

| Niveau | Nombre de chiffres | Exemple |
| --- | --- | --- |
| Classe | 1 | **1** — Financement permanent |
| Rubrique | 2 | **11** — Capitaux propres |
| Poste | 3 | **111** — Capital social ou personnel |
| Compte principal | 4 | **1111** — Capital social |
| Compte divisionnaire | 5+ | **11111** — Actions ordinaires |

Le cadre comptable comporte **dix classes codifiées de 1 à 0**, réparties en trois familles :

| Catégorie | Classe | Intitulé | Rôle économique | État de synthèse alimenté |
| --- | --- | --- | --- | --- |
| **Comptes de bilan (situation)** | 1 | Financement permanent | Ressources stables (> 1 an) : capitaux propres et dettes de financement | Passif du bilan (haut de bilan) |
|  | 2 | Actif immobilisé | Emplois durables : non-valeurs, incorporelles, corporelles, financières | Actif du bilan (actif stable) |
|  | 3 | Actif circulant (hors trésorerie) | Stocks, créances, titres et valeurs de placement | Actif du bilan (bas de bilan) |
|  | 4 | Passif circulant (hors trésorerie) | Dettes fournisseurs, fiscales, sociales et autres dettes à court terme | Passif du bilan (bas de bilan) |
|  | 5 | Trésorerie | Disponibilités (banques, caisse) et concours bancaires | Actif ou passif du bilan (trésorerie brute) |
| **Comptes de gestion (résultat)** | 6 | Charges | Consommations de ressources (exploitation, financières, non courantes) | Débit du CPC |
|  | 7 | Produits | Revenus générés (ventes, produits financiers, non courants) | Crédit du CPC |
|  | 8 | Résultats | Résultats intermédiaires en cascade et résultat net | Transition vers le bilan et le CPC |
| **Comptes spéciaux** | 9 | Comptes de produits et charges réfléchis | Comptabilité analytique d'exploitation (coûts, contrôle de gestion) | Hors états de synthèse légaux |
|  | 0 | Comptes spéciaux | Engagements hors bilan, bilan d'ouverture/clôture, comptes d'ordre | Notes ETIC, suivi hors bilan |

**Deux principes structurants du CGNC** :

1. **Approche fonctionnelle** : les créances et dettes sont classées selon leur *fonction économique* (exploitation, financement, investissement) et **non selon leur échéance** — les créances/dettes nées à plus d'un an restent dans leur masse d'origine jusqu'à règlement final. C'est ce qui rend possible l'analyse fonctionnelle (FRF/BFG/TN).
2. **Non-compensation** : les comptes de tiers débiteurs (classe 3, rubrique 34) et créditeurs (classe 4, rubrique 44) sont séparés pour mesurer l'impact réel de chaque fonction sur la trésorerie.

---

## 2. Classe 1 — Financement permanent (les ressources stables)

**Rôle** : regrouper les ressources d'une durée supérieure à un an : capitaux propres (et assimilés), dettes de financement, provisions durables.

| Rubrique | Comptes principaux | Utilité / Quand l'utiliser |
| --- | --- | --- |
| **11 — Capitaux propres** | **1111** Capital social ; **1112** Fonds de dotation ; **1117** Capital personnel ; **1121** Primes d'émission ; **1122** Primes de fusion ; **1123** Primes d'apport ; **1130** Écart de réévaluation ; **1140** Réserve légale ; **1151** Réserves statutaires ; **1152** Réserves facultatives ; **1155** Réserves réglementées ; **1161** Report à nouveau (créditeur) / **1169** (débiteur) ; **1181/1189** Résultats nets en instance d'affectation ; **1191** Résultat net (créditeur) / **1199** (débiteur) | Constitution/augmentation de capital ; dotation à la réserve légale ; réévaluation libre (1130) ; clôture de l'exercice (1191/1199) ; affectation du résultat en AGO (118 puis 1140/1161/4465) |
| **13 — Capitaux propres assimilés** | **1311** Subventions d'investissement reçues ; **1319** Subventions inscrites au CPC ; **1351** Provisions pour amortissements dérogatoires ; **1352** Provisions pour plus-values en instance d'imposition ; **1354** Provisions pour investissements ; **1355** Provisions pour reconstitution des gisements ; **1356** Provisions pour logements ; **1358** Autres provisions réglementées | Encaissement de subventions publiques d'équipement ; étalement au rythme de l'amortissement du bien financé ; amortissements accélérés fiscaux |
| **14 — Dettes de financement** | **1410** Emprunts obligataires ; **1481** Emprunts auprès des établissements de crédit ; **1482** Avances de l'État ; **1483** Dettes rattachées à des participations ; **1484** Billets de fonds ; **1485** Avances reçues et comptes courants bloqués ; **1486** Fournisseurs d'immobilisation ; **1487** Dépôts et cautionnements reçus ; **1488** Autres dettes de financement | Encaissement d'un emprunt bancaire MLT ou émission d'un emprunt obligataire (appel public à l'épargne) |
| **15 — Provisions durables pour risques et charges** | **1511** Provisions pour litiges ; **1512** Garanties données aux clients ; **1513** Provisions pour propre assureur ; **1514** Pertes sur marchés à terme ; **1515** Amendes, doubles droits, pénalités ; **1516** Pertes de change ; **1551** Provisions pour impôts ; **1552** Pensions de retraite ; **1555** Charges à répartir sur plusieurs exercices | Clôture : litiges, garanties, retraites — risques dont l'échéance dépasse 12 mois |
| **16 — Comptes de liaison des établissements et succursales** | **1601** Comptes de liaison du siège ; **1605** Comptes de liaison des établissements | Transferts de trésorerie/actifs entre sites d'une même personne morale |
| **17 — Écarts de conversion — passif (éléments stables)** | **1710** Augmentation des créances immobilisées ; **1720** Diminution des dettes de financement | Inventaire : gains de change latents sur éléments stables en devises (contre-passés à l'ouverture) |

> ⚠️ **Particularités marocaines** (vérifiées sur le plan officiel) :
> 

> - Le **report à nouveau** est en **116** (1161 créditeur / 1169 débiteur) *à l'intérieur* de la rubrique 11 — et non dans une rubrique 16 ;
> 

> - La **rubrique 16** est réservée aux **comptes de liaison des établissements et succursales** (et non aux emprunts comme dans le PCG français) ;
> 

> - Les **résultats en instance d'affectation** ont leur propre poste : **118** (1181/1189) ;
> 

> - Les subventions d'investissement et provisions réglementées sont logées dans les **capitaux propres assimilés (13)**, en dépit de la dette d'impôt latent qu'elles incorporent.
> 

**Lien avec l'analyse financière** :

- **FRF** = Financement permanent (Classe 1) − Actif immobilisé (Classe 2). Classe 1 > Classe 2 → marge de sécurité de long terme ; Classe 1 < Classe 2 → déséquilibre structurel (immobilisations financées par du court terme).
- **Autonomie financière** = Capitaux propres (11) / Dettes de financement (14). Ratio > 1 = indépendance vis-à-vis des créanciers financiers.
- **Quasi-fonds propres** : les provisions réglementées (135) et provisions durables sans objet réel (15) sont retraitées comme quasi-fonds propres par l'analyste (pas de décaissement) ; les provisions à échéance < 1 an sont reclassées en passif circulant.
- La réévaluation libre (1130) améliore instantanément les ratios de solvabilité perçus par les banques.

---

## 3. Classe 2 — Actif immobilisé (les emplois durables)

**Rôle** : enregistrer les biens, créances et droits conservés durablement pour l'activité (l'« appareil productif »).

| Rubrique | Comptes principaux | Utilité / Quand l'utiliser | Amortissement typique |
| --- | --- | --- | --- |
| **21 — Non-valeurs** | **2111** Frais de constitution ; **2112** Frais préalables au démarrage ; **2113** Frais d'augmentation du capital ; **2114** Frais de fusions-scissions ; **2116** Frais de prospection ; **2117** Frais de publicité ; **2121** Frais d'acquisition d'immobilisations ; **2125** Frais d'émission d'emprunts ; **2128** Autres charges à répartir ; **2130** Primes de remboursement d'obligations | Étaler des charges d'établissement profitant aux exercices futurs | **Linéaire, ≤ 5 exercices** (pas de prorata la 1ʳᵉ année) |
| **22 — Incorporelles** | **2210** R&D ; **2220** Brevets, marques, droits ; **2230** Fonds commercial ; **2285** Incorporelles en cours | Capitaliser la R&D interne, acheter brevets/fonds de commerce (clientèle, droit au bail) | R&D et brevets amortissables ; **fonds commercial non amorti** (provision si dépréciation) |
| **23 — Corporelles** | **2311** Terrains nus ; **2314** Terrains de gisement ; **2321** Bâtiments ; **2331** Installations techniques ; **2332** Matériel et outillage ; **2340** Matériel de transport ; **2351** Mobilier ; **2355** Matériel informatique ; **2392-2398** Corporelles en cours + avances | Achat d'actifs physiques au coût d'acquisition/production ; avancement de chantiers | Terrains non amortissables (sauf gisements : épuisement) ; autres amortissables |
| **24/25 — Financières** | **2411** Prêts au personnel ; **2415** Prêts aux associés ; **2416** Billets de fonds ; **2481** Titres immobilisés ; **2486** Dépôts et cautionnements ; **2510** Titres de participation ; **2581** Actions ; **2588** Titres divers | Prêts > 1 an non liés à l'exploitation ; participations stratégiques | **Non amortissables** ; provisions pour dépréciation (294/295) |
| **27 — Écarts de conversion — actif (stables)** | **2710** Diminution des créances immobilisées ; **2720** Augmentation des dettes de financement | Inventaire : pertes de change latentes sur éléments stables | Contre-passation à l'ouverture |
| **28 — Amortissements** | **281** Non-valeurs (2811-2813) ; **282** Incorporelles (2821-2828) ; **283** Corporelles (2831-2838) | Dotation annuelle par le débit du **619** (dotations d'exploitation) | Diminue la valeur brute → **VNC** |
| **29 — Provisions pour dépréciation** | **2920** Incorporelles ; **2930** Corporelles ; **2941/2948** Prêts/créances financières ; **2951** Titres de participation ; **2958** Autres titres immobilisés | Moins-value réversible (terrains, marques, fonds commercial, titres) | Reprise en produits (classe 7) si remontée de valeur |

**Lien avec l'analyse financière** :

- **VNC** = valeur brute (21-27) − amortissements (28) − provisions (29). L'analyste substitue aux VNC les **valeurs actuelles** (ANR) pour les terrains/constructions ; il **élimine les non-valeurs (21)** de l'actif net réel (actif fictif).
- **Ratio de couverture des emplois stables** = Financement permanent / Actif immobilisé net ≥ 1.
- **Tableau de financement (module II)** : acquisitions d'immobilisations = emplois stables ; cessions = ressources stables ; le croisement investissements bruts/dotations indique si l'entreprise renouvelle son outil productif.

---

## 4. Classe 3 — Actif circulant (hors trésorerie) : stocks, créances, titres

**Rôle** : éléments à court terme du patrimoine participant au cycle d'exploitation.

| Rubrique | Comptes principaux | Utilité / Quand l'utiliser |
| --- | --- | --- |
| **31 — Stocks** | **311** Marchandises (3111/3112) ; **312** Matières et fournitures consommables (**3121** matières premières, **3122** consommables, **3123** emballages) ; **313** Produits en cours (3131 biens, 3134 services) ; **314** Produits intermédiaires et résiduels ; **315** Produits finis | À la clôture : le stock initial est crédité par le débit de **6114** (variation de stocks de marchandises) ou **6124** (variation de stocks de matières) ; le stock final est débité par le crédit du même compte |
| **34 — Créances de l'actif circulant** | **3411** Fournisseurs — avances versées ; **3417** RRR à obtenir ; **3421** Clients ; **3423** Retenues de garantie ; **3424** Clients douteux ou litigieux ; **3425** Clients — effets à recevoir ; **34271** Clients — factures à établir ; **3431** Avances au personnel ; **3451** Subventions à recevoir ; **3453** Acomptes sur IS ; **3455** État — TVA récupérable ; **3456** État — crédit de TVA ; **3461** Associés — apports ; **3462** Capital souscrit non versé ; **3463** Comptes courants débiteurs ; **3481** Créances sur cessions d'immobilisations ; **3491** Charges constatées d'avance ; **3493** Intérêts courus à percevoir ; **3497** Comptes transitoires débiteurs | Facturation d'une vente (débit 3421, crédit classe 7 + 4455 TVA facturée) ; transfert en 3424 dès que le risque d'impayé est caractérisé ; rattachement des produits à la clôture (34271) |
| **35 — Titres et valeurs de placement** | **350** TVP (3501 actions, 3504 obligations, 3506 bons de caisse/trésor) | Placements financiers court terme (liquidité) |
| **37 — Écarts de conversion — actif (circulants)** | **370** (3701 diminution des créances circulantes, 3702 augmentation des dettes circulantes) | Inventaire (contre-passation à l'ouverture) |
| **39 — Provisions pour dépréciation de l'actif circulant** | **391** Stocks (3911-3915) ; **394** Créances (**3942** clients, 3941-3948) ; **3950** TVP | Dépréciation probable et réversible ; dotation par le **61961/61964** (exploitation) ou **65963** (non courant) |

**Lien avec l'analyse financière** : la classe 3 est le moteur du **BFG** : stocks (31) + créances d'exploitation (34) créent des besoins ; les délais clients (3421, 3425) gonflent le BFG ; le glissement 3421 → 3424 signale une dégradation du crédit client (à lire net des provisions 3942). L'analyste mesure les **délais d'encaissement (DSO)** sur le compte 3421 **[standard]**.

---

## 5. Classe 4 — Passif circulant (hors trésorerie) : dettes à court terme

**Rôle** : dettes d'exploitation et hors exploitation à court terme (ressources gratuites du cycle d'exploitation).

| Rubrique | Comptes principaux | Utilité / Quand l'utiliser |
| --- | --- | --- |
| **44 — Dettes du passif circulant** | **4411** Fournisseurs ; **4413** Retenues de garantie ; **4415** Fournisseurs — effets à payer ; **4417** Fournisseurs — factures non parvenues ; **4421** Clients — avances et acomptes reçus ; **4425** Clients — dettes pour emballages consignés ; **4432** Rémunérations dues au personnel ; **4433** Dépôts du personnel ; **4437** Charges du personnel à payer (congés payés) ; **4441** CNSS ; **4443** Caisses de retraite ; **4445** Mutuelles ; **4447** Charges sociales à payer ; **4452** État — impôts et taxes ; **4453** État — impôts sur les résultats (IS) ; **4455** État — TVA facturée ; **4456** État — TVA due ; **4461** Associés — capital à rembourser ; **4463** Comptes courants d'associés créditeurs ; **4465** Associés — dividendes à payer ; **4481** Dettes sur acquisitions d'immobilisations ; **4491** Produits constatés d'avance ; **4493** Intérêts courus à payer ; **4497** Comptes transitoires créditeurs | Réception de facture d'achat (crédit 4411, débit classe 6 + 3455) ; acceptation d'effets (4415) ; FNP à la clôture (spécialisation des exercices) ; liquidation de la paie (4432) ; IS liquidé (4453 par le débit de 6701) ; dividendes votés en AGO (4465 par le débit de 1191) |
| **45 — Autres provisions pour risques et charges (court terme)** | **450** (4501 litiges, 4502 garanties, 4505 amendes, 4506 pertes de change, 4507 impôts) | Risques exigibles à court terme |
| **47 — Écarts de conversion — passif (circulants)** | **470** (4701, 4702) | Gains de change latents sur éléments circulants |

**Lien avec l'analyse financière** : les comptes 4411 (fournisseurs), 4432 (personnel), 4441 (CNSS), 4491 (PCA) constituent des **ressources d'exploitation gratuites** qui réduisent le BFG :

**BFG = (31 + 34) − 44**. Plus le **délai de règlement fournisseurs (DPO)** est élevé, plus le besoin de trésorerie est allégé **[standard — formule]** ; au Maroc, le respect des délais légaux de paiement est un point contrôlé par le commissaire aux comptes.

---

## 6. Classe 5 — Trésorerie : liquidités et concours bancaires

**Rôle** : suivre la liquidité quotidienne. Le CGNC sépare **Trésorerie-Actif (51)** et **Trésorerie-Passif (55)** — caisse et banques réunies à l'actif, découverts isolés au passif (contrairement au PCG français).

| Rubrique | Comptes principaux | Utilité / Quand l'utiliser |
| --- | --- | --- |
| **51 — Trésorerie — actif** | **5111** Chèques à encaisser ; **5113** Effets à encaisser ; **5115** Virements de fonds (compte de passage) ; **5141** Banques (soldes débiteurs) ; **5143** Trésorerie Générale ; **5146** Chèques postaux ; **5161** Caisses ; **5165** Régies d'avances et accréditifs | Tout encaissement : réception d'un chèque client (débit 5111, crédit 3421) puis crédit bancaire ; retrait banque → caisse via 5115 |
| **55 — Trésorerie — passif** | **5520** Crédits d'escompte ; **5530** Crédits de trésorerie ; **5541** Banques (soldes créditeurs) | Découverts autorisés, escompte et concours bancaires courants à la clôture |
| **59 — Provisions pour dépréciation des comptes de trésorerie** | **5900** | Devises bloquées, comptes gelés |

**Outil de contrôle — le rapprochement bancaire** : explique l'écart entre le solde du compte 5141 et le relevé bancaire (chèques émis non présentés, agios non enregistrés, virements non saisis) ; des régularisations sont passées (charges bancaires en 6147, intérêts financiers en 738).

**Lien avec l'analyse financière** :

- **Trésorerie Nette (TN)** = Trésorerie-Actif (51) − Trésorerie-Passif (55) = **FRF − BFG** (solde de bouclage de l'équilibre financier).
- **Liquidité immédiate** = 51 / dettes exigibles à court terme **[standard]** (le CGNC ne fixe pas de ratios réglementaires).

---

## 7. Classe 6 — Charges (débit du CPC)

**Rôle** : enregistrer les consommations de ressources, **hors taxes récupérables**, rattachées à l'exercice (comptabilité d'engagement). Structure marocaine en **3 niveaux + impôts** (exploitation, financier, non courant).

| Rubrique | Comptes principaux | Utilité / Quand l'utiliser |
| --- | --- | --- |
| **61 — Charges d'exploitation** | **611** Achats revendus de marchandises (**6111/6112** achats, **6114** variation de stocks, **6119** RRR obtenus) ; **612** Achats consommés de matières et fournitures (**6121** matières premières, **6122** consommables, **6123** emballages, **6124** variation, **6125** achats non stockés, **6126** travaux-études-prestations, **6129** RRR) ; **613/614** Autres charges externes (**6131** locations, **6132** redevances de crédit-bail, **6133** entretien, **6134** assurances, **6135** personnel extérieur, **6136** intermédiaires et honoraires, **6137** redevances brevets, **6141** études, **6142** transports, **6143** déplacements, **6144** publicité, **6145** frais postaux et télécoms, **6146** cotisations et dons, **6147** services bancaires) ; **616** Impôts et taxes (**6161** taxe urbaine, patente, taxes locales ; **6167** droits d'enregistrement, taxes sur véhicules) ; **617** Charges de personnel (**6171** rémunérations, **6174** charges sociales, **6176** autres charges sociales, **6177** rémunération de l'exploitant) ; **618** Autres charges d'exploitation (**6181** jetons de présence, **6182** pertes sur créances irrécouvrables) ; **619** Dotations d'exploitation (**6191-6193** amortissements, **6194-6196** provisions dont **61964** créances, **6198** exercices antérieurs) | Enregistrement des achats à réception de facture ; dotation annuelle aux amortissements et provisions ; liquidation de la paie (617) |
| **63 — Charges financières** | **631** Charges d'intérêts (**6311** intérêts des emprunts et dettes, **63114** intérêts des comptes courants) ; **633** Pertes de change ; **638** Autres charges financières (**6386** escomptes accordés, **6385** charges nettes sur cessions de TVP) ; **639** Dotations financières (**6391** amortissement des primes de remboursement, **6392-6394** provisions) | Intérêts courus (crédit de 4493) ; pertes de change ; escomptes de règlement accordés |
| **65 — Charges non courantes** | **651** VNA des immobilisations cédées (6512-6518) ; **656** Subventions accordées ; **658** Autres charges non courantes (**6581** pénalités sur marchés et dédits, **6583** pénalités et amendes fiscales, **6585** créances devenues irrécouvrables, **6586** dons et libéralités) ; **659** Dotations non courantes (**6591** amortissements exceptionnels, **6594** provisions réglementées dont **65941** amortissements dérogatoires, **6595** risques et charges, **65962/65963** dépréciations) | Événements anormaux et fortuits ; cessions d'immobilisations |
| **67 — Impôts sur les résultats** | **6701** Impôts sur les bénéfices (IS) ; **6705** Imposition minimale annuelle (cotisation minimale) ; **6708** Rappels et dégrèvements | Liquidation de l'IS et de la CM (débit 6701, crédit 4453) |

**Lien avec l'analyse financière** : la classe 6 alimente le CPC et l'ESG — les achats (611-614) entrent dans la **marge brute** et la **valeur ajoutée** ; les charges de personnel (617) et impôts et taxes (616) permettent le passage de la VA à l'**EBE** ; les dotations (619) et charges financières (6311) distinguent la performance économique de la performance financière. Côté fiscal, la classe 6 est la base des **réintégrations** (charges non déductibles : amendes 6583, véhicules de tourisme > 400 000 DH, dépenses en espèces > 5 000 DH/jour, intérêts CCA non conformes...).

---

## 8. Classe 7 — Produits (crédit du CPC)

**Rôle** : enregistrer les revenus générés, **hors TVA collectée**, rattachés à l'exercice. Le classement suit la **cascade des soldes de gestion**.

| Rubrique | Comptes principaux | Utilité / Articulation avec les SIG |
| --- | --- | --- |
| **71 — Produits d'exploitation** | **711** Ventes de marchandises (**7111** Maroc, **7113** étranger, **7118** exercices antérieurs, **7119** RRR accordés) ; **712** Ventes de biens et services produits (**7121** biens produits au Maroc — 71211 produits finis, 71212 intermédiaires, 71217 résiduels —, **7122** biens produits à l'étranger, **7124/7125** services produits, **7126** redevances brevets, **7127** ventes et produits accessoires, **7129** RRR) ; **713** Variation des stocks de produits (**7131** en cours, **7132** biens produits, **7134** services en cours) ; **714** Immobilisations produites pour elle-même (7141-7143) ; **716** Subventions d'exploitation ; **718** Autres produits d'exploitation (**7181** jetons de présence reçus, **7182** revenus des immeubles non affectés) ; **719** Reprises d'exploitation et transferts de charges (**7191-7193** reprises sur amortissements, **7194** provisions immobilisations, **7195** risques et charges, **7196** actif circulant, **7197** transferts, **7198** exercices antérieurs) | 711 → **Marge brute** (711 − 611) ; 712+713+714 → **Production de l'exercice** → **Valeur ajoutée** (MB + Production − consommations 612/613/614) ; 716 → **EBE** (VA + 716 − 616 − 617) |
| **73 — Produits financiers** | **732** Produits des titres de participation et titres immobilisés (**7321** revenus des participations) ; **733** Gains de change ; **738** Intérêts et autres produits financiers (**7381** intérêts des prêts, **7384** revenus des TVP, **7385** produits nets sur cessions de TVP, **7386** escomptes obtenus) ; **739** Reprises financières, transferts de charges (7391-7398) | **Résultat financier** = produits financiers (73) − charges financières (63) |
| **75 — Produits non courants** | **751** Produits des cessions d'immobilisations (7512-7518) ; **756** Subventions d'équilibre ; **757** Reprises sur subventions d'investissement ; **758** Autres produits non courants (**7581** pénalités et dédits reçus, **7582** dégrèvements d'impôts, **7585** rentrées sur créances soldées, **7586** dons et libéralités) ; **759** Reprises non courantes (**7591** amortissements exceptionnels, **7594** provisions réglementées, **7595** risques et charges, **7596** dépréciations, **7597** transferts) | **Résultat non courant** ; les produits de cession (751) sont **déduits** du résultat net dans le calcul de la CAF additive |

> ⚠️ **Particularités marocaines** : pas de rubrique globale 78/79 — les reprises et transferts sont ventilés par niveau (719 exploitation, 739 financier, 759 non courant) ; les escomptes de règlement accordés sont débités en **charges financières** (6386) et non déduits des ventes ; les escomptes obtenus sont crédités en **produits financiers** (7386).
> 

**Lien avec l'analyse financière** : la classe 7 alimente CPC et ESG ; seules les **reprises sur éléments stables** (actif immobilisé, financement permanent) sont intégrées à la **CAF additive** — les reprises sur circulants (7194-7196) en sont exclues.

---

## 9. Classe 8 — Résultats : la cascade du résultat net

**Rôle** : classe de transition qui fait apparaître les **résultats intermédiaires en cascade** du CPC et de l'ESG. Le plan officiel distingue **six niveaux** de résultats :

| Rubrique | Comptes principaux | Rôle |
| --- | --- | --- |
| **81 — Résultat d'exploitation** | **810** Résultat d'exploitation (8100) ; **811** Marge brute (8110) ; **814** Valeur ajoutée (8140) ; **817** Excédent brut d'exploitation (**8171** créditeur / **8179** insuffisance brute d'exploitation) | Performance opérationnelle brute avant choix financiers et impôts |
| **83 — Résultat financier** | **8300** | Produits financiers (73) − charges financières (63) |
| **84 — Résultat courant** | **8400** | Résultat d'exploitation + résultat financier (élément cyclique, se prête à la prévision) |
| **85 — Résultat non courant** | **8500** | Opérations anormales et fortuites |
| **86 — Résultat avant impôts** | **8600** | Résultat courant + résultat non courant |
| **88 — Résultat après impôts** | **8800** | Bénéfice ou perte nette finale après IS ; solde transféré au bilan : **1191** (bénéfice) ou **1199** (perte) en classe 1 |

**Affectation du résultat (AGO)** : une fois les comptes approuvés, l'assemblée vote l'affectation — **réserve légale** (dotation annuelle, usuellement 5 % du bénéfice dans la limite de 10 % du capital pour SA/SARL **[À VÉRIFIER selon textes]**, compte 1140), **dividendes** (4465 ; retenue à la source art. 247-XXXVII-C CGI), **report à nouveau** (1161). La distribution est débitée du compte 1191 ; le résultat non encore affecté transite par **1181/1189**.

**Lien avec l'analyse financière** : les soldes 8110/8140/8171 sont la base des ratios de marge (marge brute, taux de VA, taux d'EBE) ; le résultat net (1191/1199) alimente la **CAF** (méthode additive), le **ROE** et la politique de distribution.

---

## 10. Classe 9 — Comptes de produits et charges réfléchis (comptabilité analytique)

**Rôle** : outil interne de **contrôle de gestion** — calcul des coûts, des centres d'analyse, des écarts — fonctionnant de manière autonome par rapport à la comptabilité générale via les **comptes réfléchis** (miroir des comptes généraux).

| Rubrique | Contenu | Utilisation |
| --- | --- | --- |
| **90 — Comptes de produits et charges réfléchis** | **903** Stocks réfléchis (9031/9039) ; **906** Charges réfléchies (**9061** exploitation, **9063** financières, **9065** non courantes, **9067** IS) ; **907** Produits réfléchis (9071/9073/9075) ; **908** Résultats réfléchis (9081-9088) | Miroir de la comptabilité générale pour alimenter la CAE sans interférer avec les comptes légaux |
| **91 — Comptes de reclassement et d'analyse** | Ouverts et attribués selon les nécessités de l'entreprise | Retraiter/reclasser les charges selon les besoins d'analyse |
| **92 — Sections analytiques** | **921** Sections générales ; **923** Approvisionnement ; **925** Production ; **927** Distribution ; **928** Autres | Regrouper les charges indirectes par centres d'activité (répartition primaire et secondaire, unités d'œuvre) |
| **93 — Coûts d'achat ou de production** | **933** Coûts d'achat (9331 marchandises, 9335 matières) ; **935** Coûts de production (9351/9352) ; **938** Autres (9381 coûts de production des immobilisations) | Valoriser les stocks et les produits au coût complet |
| **94 — Inventaire permanent des stocks** | **941-945** Inventaire permanent (marchandises, matières, en-cours, produits) ; **949** Provisions sur stocks | Suivi continu des stocks en quantités et en valeur |
| **95 — Coûts de revient** | **953** Marchandises ; **955** Produits ; **958** Autres | Coût complet unitaire par produit/commande/chantier |
| **96 — Écarts sur coûts préétablis** | **962** Écarts sur sections (quantités, coûts) ; **964** Écarts sur inventaire permanent | Contrôle budgétaire : écarts entre réalisations et prévisions |
| **97 — Différences d'incorporation** | **971** Charges non incorporables ; **972** Charges supplétives incorporées ; **973** Produits non incorporés ; **974/975** Différences sur charges/produits incorporables ; **976** Différences d'inventaire ; **977** Différences sur niveau d'activité ; **978** Autres | Rapprocher le coût d'analyse (avec charges supplétives) du coût comptable |
| **98 — Résultats analytiques** | **981-983** Résultats par catégorie ; **986** Reports des écarts sur coûts préétablis ; **987** Reports des différences d'incorporation | Réconciliation du résultat analytique global avec le résultat net de la comptabilité générale |
| **99 — Comptes de liaison interne** | **991** Liaisons internes d'un même établissement ; **995** Cessions entre établissements (9951 fournies, 9955 reçues) | Transferts internes de charges et produits entre établissements |

**Quand l'utiliser** : détermination des coûts complets (méthode des sections homogènes), analyse de rentabilité par produit, contrôle budgétaire (écarts sur coûts préétablis), pilotage opérationnel — hors états de synthèse légaux.

---

## 11. Classe 0 — Comptes spéciaux (bilan d'ouverture, comptes d'ordre et engagements hors bilan)

**Rôle** : opérations techniques de fin/début d'exercice et suivi des engagements hors bilan.

| Rubrique | Contenu | Utilisation |
| --- | --- | --- |
| **01 — Bilan d'ouverture** | **011-015** Réouverture des comptes de financement permanent, d'actif immobilisé, d'actif/passif circulant et de trésorerie | Réouverture des comptes en début d'exercice |
| **02 — Clôture du bilan** | **021-025** Clôture des comptes des mêmes masses | Clôture des comptes en fin d'exercice |
| **03 — Comptes d'ordre** | **031/033** Opérations en instance de dénouement ; **035/036** Opérations en devises (contre-valeur) ; **038** Données statistiques | Suivi des opérations transitoires et statistiques |
| **04 — Engagements donnés** | **041** Avals, cautions et garanties donnés ; **043** Engagements de pensions de retraite ; **045** Effets circulant sous endos ; **046** Prêts consentis non versés ; **048** Autres | Engagements hors bilan donnés (dettes potentielles pour l'analyste !) |
| **05 — Engagements reçus** | **051** Avals, cautions et garanties reçus ; **055** Biens détenus en garantie ; **056** Emprunts non encore encaissés ; **057** Découverts non utilisés et plafonds d'escompte ; **058** Autres | Engagements hors bilan reçus (ressources potentielles) |
| **06 — Engagements de crédit-bail** | **061** Redevances de crédit-bail restant à courir ; **065** Engagements reçus pour utilisation en crédit-bail | Suivi des engagements de location-financement |
| **08 — Autres comptes spéciaux** | **081** | Divers |

**Lien avec l'analyse financière** : les engagements hors bilan (04/05/06) sont repris dans l'**ETIC** — élément clé pour l'analyste : les cautions données (041), les engagements de retraite (043) et les redevances de crédit-bail (061) peuvent cacher des **dettes potentielles** qui pèsent sur la solvabilité réelle (retraitement en dette financière du crédit-bail, par exemple).

---

## 12. Articulation des comptes avec les états de synthèse et l'analyse financière

| État de synthèse | Classes d'alimentation | Rôle de l'état |
| --- | --- | --- |
| **Bilan (BL)** | Classes **1 à 5** | Photographie patrimoniale, lecture fonctionnelle en masses (FRF, BFG, TN) |
| **CPC** | Classes **6 et 7** | Performance en cascade : résultat d'exploitation (81) + financier (83) = résultat courant (84) ; + non courant (85) = résultat avant impôts (86) ; − IS (67) = résultat après impôts (88) |
| **ESG** | Classes **6, 7, 8** | TFR (MB 811, VA 814, EBE 817, résultats) + tableau de détermination de la **CAF** et de l'autofinancement |
| **Tableau de Financement (TF)** | Classes **1 à 5**  • autofinancement | Flux entre deux bilans : CAF, emplois/ressources stables, variations du FRF, BFG, TN |
| **ETIC** | Notes + classes 2-4 et 0 (tableaux immobilisations, provisions, créances/dettes, engagements hors bilan) | Méthodes, dérogations, engagements hors bilan, échéanciers |

**Tableau de correspondance comptes → indicateurs d'analyse** :

| Indicateur | Formule fonctionnelle | Comptes d'origine |
| --- | --- | --- |
| **FRF** | Financement permanent − Actif immobilisé | Classe 1 − Classe 2 |
| **BFG** | Actif circulant (hors trésorerie) − Passif circulant (hors trésorerie) | (31 + 34 + 35) − (44 + 45) |
| **TN** | Trésorerie-Actif − Trésorerie-Passif = FRF − BFG | 51 − 55 |
| **Marge brute** | Ventes de marchandises − Achats revendus | 711 − 611 |
| **Valeur ajoutée** | MB + Production − Consommations externes | (711-714) − (612/613/614) |
| **EBE** | VA + Subventions d'exploitation − Impôts et taxes − Charges de personnel | VA + 716 − 616 − 617 |
| **Résultat courant** | Résultat d'exploitation + Résultat financier | 81 + 83 (84) |
| **CAF (additive)** | RN + dotations stables − reprises stables − produits de cessions + VNA cédées | 88 + 619/639/659 (stables) − 719/739/759 (stables) − 751 + 651 |
| **IS / CM** | 6701 / 6705 (via 4453) | Passage RC → RF (liasse fiscale) |

---

## 13. Pièges et particularités du référentiel marocain à retenir

1. **Analyse fonctionnelle, pas liquidité** : créances et dettes classées par fonction économique, quelle que soit leur échéance — le bilan marocain se lit en FRF/BFG/TN.
2. **Non-valeurs (21)** = actif fictif : à éliminer de l'actif net réel et des capitaux propres.
3. **Capitaux propres assimilés (13)** : subventions d'investissement et provisions réglementées comptées en capitaux propres malgré la dette d'impôt latent — retraitement en quasi-fonds propres.
4. **Rubrique 16 = comptes de liaison** (et non les emprunts comme en France) ; le **report à nouveau est en 116** (rubrique 11) ; les **résultats en instance d'affectation en 118** ; les dettes financières sont en **14**.
5. **Tiers non compensés** : débiteurs en 34, créditeurs en 44 (jamais de solde net).
6. **Trésorerie positive (51) et négative (55) présentées séparément** au bilan.
7. **Escomptes accordés en charges financières (6386)** ; pas de rubriques globales 78/79 (reprises/transferts ventilés : 719/739/759).
8. **CAF additive** : exclut les dotations/reprises sur actif circulant et trésorerie ; exclut les produits de cession (751) et réintègre les VNA (651).
9. **IS dans le CPC** via 6701/6705 ; **IS non déductible** et **CSS non déductible** (réintégrations) ; les pénalités et amendes fiscales (6583) sont non déductibles.
10. **Classe 8 en cascade** : 81 (résultat d'exploitation + soldes intermédiaires 811/814/817) → 83 (financier) → 84 (courant) → 85 (non courant) → 86 (avant impôts) → 88 (après impôts) → transfert en 1191/1199 au passif.
11. **Engagements hors bilan (classe 0)** : cautions, retraites, crédit-bail — à retraiter dans l'analyse de solvabilité.
12. **Classe 9 autonome** : comptes réfléchis (90), sections (92), coûts (93-95), écarts (96), différences d'incorporation (97) — le résultat analytique (98) doit se réconcilier avec le résultat général.

---

## 14. Limites et points à vérifier

| Élément | Statut |
| --- | --- |
| Formules chiffrées des ratios de rentabilité (ROE/ROA) dans le référentiel CGNC | **[standard]** — non définies par le CGNC (l'AMMC et les documents de référence les calculent : ROE = RN/fonds propres moyens) |
| DSO / DPO en jours | **[standard]** — formules classiques |
| Réserve légale : 5 % du bénéfice, plafond 10 % du capital | **[À VÉRIFIER]** — pratique usuelle SA/SARL (loi 17-95 / 5-96) |
| Durées d'amortissement précises par catégorie (bâtiments 20 ans, matériel 10 ans, transport 5 ans...) | **[standard]** — le plan comptable ne les chiffre pas ; usages fiscaux (CGI) et professionnels |
| Comptes 56/57/58 de la classe 5 | Absents du PCGE d'entreprise (spécifiques PCEC bancaire) |
| Coquille « 2441 » pour les prêts au personnel dans le document PDF source | Probablement **2411** (cohérent avec 2415/2416/2418) — **[À VÉRIFIER]** sur le CGNC officiel |

---

## 15. Sources principales

- **Plan Comptable Marocain (PCGE)** — nomenclature officielle des classes 1 à 0 (document PDF fourni, vérifié compte par compte)
- CGNC — Code Général de Normalisation Comptable (Conseil National de la Comptabilité) : cadre comptable, terminologie, modalités de fonctionnement des comptes
- Loi n° 9-88 (obligations comptables des commerçants) et loi 44-03
- Plan comptable du secteur immobilier (classes 1 à 9 détaillées) ; plan comptable des établissements de crédit (PCEC) — comparaison
- Liasse fiscale DGI (23 tableaux, T5/T6/T7 : ESG-CAF, TF) ; guide arrêté des comptes (revue par classe 1-5)
- Upsilon Consulting (PCGE, états de synthèse, réévaluation) ; CRMEF (référentiel comptable marocain) ; Master GCFF (loi 9-88)
- Documents de référence AMMC (FEC, CDG Capital, Wafasalaf, CFG Bank)

---

*Rapport généré le 04/08/2026 — NotebookLM (308 sources) + vérification contre le Plan Comptable Marocain officiel (PDF fourni). Les éléments marqués [standard] et [À VÉRIFIER] doivent être confirmés dans les référentiels de cours et les textes officiels.*

**Périmètre** : Explication de chaque classe de comptes du Plan Comptable Général des Entreprises marocain (PCGE, issu du CGNC et de la loi 9-88) : ce que contient chaque classe, à quoi elle sert, quand on l'utilise, et comment elle alimente l'analyse financière (états de synthèse, FRF/BFG/TN, ratios).

**Statut des informations** : contenu fondé sur le corpus de 308 sources NotebookLM (CGNC officiel, plans comptables sectoriels, documents de travail CRMEF, guides Upsilon, liasse fiscale DGI) **et vérifié compte par compte contre le « Plan Comptable Marocain » officiel (document PDF fourni par l'utilisateur, 1 307 lignes de nomenclature)**. Les éléments absents des sources sont signalés **[standard]** (pratique classique d'analyse) ou **[À VÉRIFIER]** (à confirmer sur texte officiel).

---

## 1. Logique générale du PCGE : une codification décimale hiérarchique

Le PCGE marocain organise la comptabilité selon une **codification décimale à 5 niveaux** :

| Niveau | Nombre de chiffres | Exemple |
| --- | --- | --- |
| Classe | 1 | **1** — Financement permanent |
| Rubrique | 2 | **11** — Capitaux propres |
| Poste | 3 | **111** — Capital social ou personnel |
| Compte principal | 4 | **1111** — Capital social |
| Compte divisionnaire | 5+ | **11111** — Actions ordinaires |

Le cadre comptable comporte **dix classes codifiées de 1 à 0**, réparties en trois familles :

| Catégorie | Classe | Intitulé | Rôle économique | État de synthèse alimenté |
| --- | --- | --- | --- | --- |
| **Comptes de bilan (situation)** | 1 | Financement permanent | Ressources stables (> 1 an) : capitaux propres et dettes de financement | Passif du bilan (haut de bilan) |
|  | 2 | Actif immobilisé | Emplois durables : non-valeurs, incorporelles, corporelles, financières | Actif du bilan (actif stable) |
|  | 3 | Actif circulant (hors trésorerie) | Stocks, créances, titres et valeurs de placement | Actif du bilan (bas de bilan) |
|  | 4 | Passif circulant (hors trésorerie) | Dettes fournisseurs, fiscales, sociales et autres dettes à court terme | Passif du bilan (bas de bilan) |
|  | 5 | Trésorerie | Disponibilités (banques, caisse) et concours bancaires | Actif ou passif du bilan (trésorerie brute) |
| **Comptes de gestion (résultat)** | 6 | Charges | Consommations de ressources (exploitation, financières, non courantes) | Débit du CPC |
|  | 7 | Produits | Revenus générés (ventes, produits financiers, non courants) | Crédit du CPC |
|  | 8 | Résultats | Résultats intermédiaires en cascade et résultat net | Transition vers le bilan et le CPC |
| **Comptes spéciaux** | 9 | Comptes de produits et charges réfléchis | Comptabilité analytique d'exploitation (coûts, contrôle de gestion) | Hors états de synthèse légaux |
|  | 0 | Comptes spéciaux | Engagements hors bilan, bilan d'ouverture/clôture, comptes d'ordre | Notes ETIC, suivi hors bilan |

**Deux principes structurants du CGNC** :

1. **Approche fonctionnelle** : les créances et dettes sont classées selon leur *fonction économique* (exploitation, financement, investissement) et **non selon leur échéance** — les créances/dettes nées à plus d'un an restent dans leur masse d'origine jusqu'à règlement final. C'est ce qui rend possible l'analyse fonctionnelle (FRF/BFG/TN).
2. **Non-compensation** : les comptes de tiers débiteurs (classe 3, rubrique 34) et créditeurs (classe 4, rubrique 44) sont séparés pour mesurer l'impact réel de chaque fonction sur la trésorerie.

---

## 2. Classe 1 — Financement permanent (les ressources stables)

**Rôle** : regrouper les ressources d'une durée supérieure à un an : capitaux propres (et assimilés), dettes de financement, provisions durables.

| Rubrique | Comptes principaux | Utilité / Quand l'utiliser |
| --- | --- | --- |
| **11 — Capitaux propres** | **1111** Capital social ; **1112** Fonds de dotation ; **1117** Capital personnel ; **1121** Primes d'émission ; **1122** Primes de fusion ; **1123** Primes d'apport ; **1130** Écart de réévaluation ; **1140** Réserve légale ; **1151** Réserves statutaires ; **1152** Réserves facultatives ; **1155** Réserves réglementées ; **1161** Report à nouveau (créditeur) / **1169** (débiteur) ; **1181/1189** Résultats nets en instance d'affectation ; **1191** Résultat net (créditeur) / **1199** (débiteur) | Constitution/augmentation de capital ; dotation à la réserve légale ; réévaluation libre (1130) ; clôture de l'exercice (1191/1199) ; affectation du résultat en AGO (118 puis 1140/1161/4465) |
| **13 — Capitaux propres assimilés** | **1311** Subventions d'investissement reçues ; **1319** Subventions inscrites au CPC ; **1351** Provisions pour amortissements dérogatoires ; **1352** Provisions pour plus-values en instance d'imposition ; **1354** Provisions pour investissements ; **1355** Provisions pour reconstitution des gisements ; **1356** Provisions pour logements ; **1358** Autres provisions réglementées | Encaissement de subventions publiques d'équipement ; étalement au rythme de l'amortissement du bien financé ; amortissements accélérés fiscaux |
| **14 — Dettes de financement** | **1410** Emprunts obligataires ; **1481** Emprunts auprès des établissements de crédit ; **1482** Avances de l'État ; **1483** Dettes rattachées à des participations ; **1484** Billets de fonds ; **1485** Avances reçues et comptes courants bloqués ; **1486** Fournisseurs d'immobilisation ; **1487** Dépôts et cautionnements reçus ; **1488** Autres dettes de financement | Encaissement d'un emprunt bancaire MLT ou émission d'un emprunt obligataire (appel public à l'épargne) |
| **15 — Provisions durables pour risques et charges** | **1511** Provisions pour litiges ; **1512** Garanties données aux clients ; **1513** Provisions pour propre assureur ; **1514** Pertes sur marchés à terme ; **1515** Amendes, doubles droits, pénalités ; **1516** Pertes de change ; **1551** Provisions pour impôts ; **1552** Pensions de retraite ; **1555** Charges à répartir sur plusieurs exercices | Clôture : litiges, garanties, retraites — risques dont l'échéance dépasse 12 mois |
| **16 — Comptes de liaison des établissements et succursales** | **1601** Comptes de liaison du siège ; **1605** Comptes de liaison des établissements | Transferts de trésorerie/actifs entre sites d'une même personne morale |
| **17 — Écarts de conversion — passif (éléments stables)** | **1710** Augmentation des créances immobilisées ; **1720** Diminution des dettes de financement | Inventaire : gains de change latents sur éléments stables en devises (contre-passés à l'ouverture) |

> ⚠️ **Particularités marocaines** (vérifiées sur le plan officiel) :
> 

> - Le **report à nouveau** est en **116** (1161 créditeur / 1169 débiteur) *à l'intérieur* de la rubrique 11 — et non dans une rubrique 16 ;
> 

> - La **rubrique 16** est réservée aux **comptes de liaison des établissements et succursales** (et non aux emprunts comme dans le PCG français) ;
> 

> - Les **résultats en instance d'affectation** ont leur propre poste : **118** (1181/1189) ;
> 

> - Les subventions d'investissement et provisions réglementées sont logées dans les **capitaux propres assimilés (13)**, en dépit de la dette d'impôt latent qu'elles incorporent.
> 

**Lien avec l'analyse financière** :

- **FRF** = Financement permanent (Classe 1) − Actif immobilisé (Classe 2). Classe 1 > Classe 2 → marge de sécurité de long terme ; Classe 1 < Classe 2 → déséquilibre structurel (immobilisations financées par du court terme).
- **Autonomie financière** = Capitaux propres (11) / Dettes de financement (14). Ratio > 1 = indépendance vis-à-vis des créanciers financiers.
- **Quasi-fonds propres** : les provisions réglementées (135) et provisions durables sans objet réel (15) sont retraitées comme quasi-fonds propres par l'analyste (pas de décaissement) ; les provisions à échéance < 1 an sont reclassées en passif circulant.
- La réévaluation libre (1130) améliore instantanément les ratios de solvabilité perçus par les banques.

---

## 3. Classe 2 — Actif immobilisé (les emplois durables)

**Rôle** : enregistrer les biens, créances et droits conservés durablement pour l'activité (l'« appareil productif »).

| Rubrique | Comptes principaux | Utilité / Quand l'utiliser | Amortissement typique |
| --- | --- | --- | --- |
| **21 — Non-valeurs** | **2111** Frais de constitution ; **2112** Frais préalables au démarrage ; **2113** Frais d'augmentation du capital ; **2114** Frais de fusions-scissions ; **2116** Frais de prospection ; **2117** Frais de publicité ; **2121** Frais d'acquisition d'immobilisations ; **2125** Frais d'émission d'emprunts ; **2128** Autres charges à répartir ; **2130** Primes de remboursement d'obligations | Étaler des charges d'établissement profitant aux exercices futurs | **Linéaire, ≤ 5 exercices** (pas de prorata la 1ʳᵉ année) |
| **22 — Incorporelles** | **2210** R&D ; **2220** Brevets, marques, droits ; **2230** Fonds commercial ; **2285** Incorporelles en cours | Capitaliser la R&D interne, acheter brevets/fonds de commerce (clientèle, droit au bail) | R&D et brevets amortissables ; **fonds commercial non amorti** (provision si dépréciation) |
| **23 — Corporelles** | **2311** Terrains nus ; **2314** Terrains de gisement ; **2321** Bâtiments ; **2331** Installations techniques ; **2332** Matériel et outillage ; **2340** Matériel de transport ; **2351** Mobilier ; **2355** Matériel informatique ; **2392-2398** Corporelles en cours + avances | Achat d'actifs physiques au coût d'acquisition/production ; avancement de chantiers | Terrains non amortissables (sauf gisements : épuisement) ; autres amortissables |
| **24/25 — Financières** | **2411** Prêts au personnel ; **2415** Prêts aux associés ; **2416** Billets de fonds ; **2481** Titres immobilisés ; **2486** Dépôts et cautionnements ; **2510** Titres de participation ; **2581** Actions ; **2588** Titres divers | Prêts > 1 an non liés à l'exploitation ; participations stratégiques | **Non amortissables** ; provisions pour dépréciation (294/295) |
| **27 — Écarts de conversion — actif (stables)** | **2710** Diminution des créances immobilisées ; **2720** Augmentation des dettes de financement | Inventaire : pertes de change latentes sur éléments stables | Contre-passation à l'ouverture |
| **28 — Amortissements** | **281** Non-valeurs (2811-2813) ; **282** Incorporelles (2821-2828) ; **283** Corporelles (2831-2838) | Dotation annuelle par le débit du **619** (dotations d'exploitation) | Diminue la valeur brute → **VNC** |
| **29 — Provisions pour dépréciation** | **2920** Incorporelles ; **2930** Corporelles ; **2941/2948** Prêts/créances financières ; **2951** Titres de participation ; **2958** Autres titres immobilisés | Moins-value réversible (terrains, marques, fonds commercial, titres) | Reprise en produits (classe 7) si remontée de valeur |

**Lien avec l'analyse financière** :

- **VNC** = valeur brute (21-27) − amortissements (28) − provisions (29). L'analyste substitue aux VNC les **valeurs actuelles** (ANR) pour les terrains/constructions ; il **élimine les non-valeurs (21)** de l'actif net réel (actif fictif).
- **Ratio de couverture des emplois stables** = Financement permanent / Actif immobilisé net ≥ 1.
- **Tableau de financement (module II)** : acquisitions d'immobilisations = emplois stables ; cessions = ressources stables ; le croisement investissements bruts/dotations indique si l'entreprise renouvelle son outil productif.

---

## 4. Classe 3 — Actif circulant (hors trésorerie) : stocks, créances, titres

**Rôle** : éléments à court terme du patrimoine participant au cycle d'exploitation.

| Rubrique | Comptes principaux | Utilité / Quand l'utiliser |
| --- | --- | --- |
| **31 — Stocks** | **311** Marchandises (3111/3112) ; **312** Matières et fournitures consommables (**3121** matières premières, **3122** consommables, **3123** emballages) ; **313** Produits en cours (3131 biens, 3134 services) ; **314** Produits intermédiaires et résiduels ; **315** Produits finis | À la clôture : le stock initial est crédité par le débit de **6114** (variation de stocks de marchandises) ou **6124** (variation de stocks de matières) ; le stock final est débité par le crédit du même compte |
| **34 — Créances de l'actif circulant** | **3411** Fournisseurs — avances versées ; **3417** RRR à obtenir ; **3421** Clients ; **3423** Retenues de garantie ; **3424** Clients douteux ou litigieux ; **3425** Clients — effets à recevoir ; **34271** Clients — factures à établir ; **3431** Avances au personnel ; **3451** Subventions à recevoir ; **3453** Acomptes sur IS ; **3455** État — TVA récupérable ; **3456** État — crédit de TVA ; **3461** Associés — apports ; **3462** Capital souscrit non versé ; **3463** Comptes courants débiteurs ; **3481** Créances sur cessions d'immobilisations ; **3491** Charges constatées d'avance ; **3493** Intérêts courus à percevoir ; **3497** Comptes transitoires débiteurs | Facturation d'une vente (débit 3421, crédit classe 7 + 4455 TVA facturée) ; transfert en 3424 dès que le risque d'impayé est caractérisé ; rattachement des produits à la clôture (34271) |
| **35 — Titres et valeurs de placement** | **350** TVP (3501 actions, 3504 obligations, 3506 bons de caisse/trésor) | Placements financiers court terme (liquidité) |
| **37 — Écarts de conversion — actif (circulants)** | **370** (3701 diminution des créances circulantes, 3702 augmentation des dettes circulantes) | Inventaire (contre-passation à l'ouverture) |
| **39 — Provisions pour dépréciation de l'actif circulant** | **391** Stocks (3911-3915) ; **394** Créances (**3942** clients, 3941-3948) ; **3950** TVP | Dépréciation probable et réversible ; dotation par le **61961/61964** (exploitation) ou **65963** (non courant) |

**Lien avec l'analyse financière** : la classe 3 est le moteur du **BFG** : stocks (31) + créances d'exploitation (34) créent des besoins ; les délais clients (3421, 3425) gonflent le BFG ; le glissement 3421 → 3424 signale une dégradation du crédit client (à lire net des provisions 3942). L'analyste mesure les **délais d'encaissement (DSO)** sur le compte 3421 **[standard]**.

---

## 5. Classe 4 — Passif circulant (hors trésorerie) : dettes à court terme

**Rôle** : dettes d'exploitation et hors exploitation à court terme (ressources gratuites du cycle d'exploitation).

| Rubrique | Comptes principaux | Utilité / Quand l'utiliser |
| --- | --- | --- |
| **44 — Dettes du passif circulant** | **4411** Fournisseurs ; **4413** Retenues de garantie ; **4415** Fournisseurs — effets à payer ; **4417** Fournisseurs — factures non parvenues ; **4421** Clients — avances et acomptes reçus ; **4425** Clients — dettes pour emballages consignés ; **4432** Rémunérations dues au personnel ; **4433** Dépôts du personnel ; **4437** Charges du personnel à payer (congés payés) ; **4441** CNSS ; **4443** Caisses de retraite ; **4445** Mutuelles ; **4447** Charges sociales à payer ; **4452** État — impôts et taxes ; **4453** État — impôts sur les résultats (IS) ; **4455** État — TVA facturée ; **4456** État — TVA due ; **4461** Associés — capital à rembourser ; **4463** Comptes courants d'associés créditeurs ; **4465** Associés — dividendes à payer ; **4481** Dettes sur acquisitions d'immobilisations ; **4491** Produits constatés d'avance ; **4493** Intérêts courus à payer ; **4497** Comptes transitoires créditeurs | Réception de facture d'achat (crédit 4411, débit classe 6 + 3455) ; acceptation d'effets (4415) ; FNP à la clôture (spécialisation des exercices) ; liquidation de la paie (4432) ; IS liquidé (4453 par le débit de 6701) ; dividendes votés en AGO (4465 par le débit de 1191) |
| **45 — Autres provisions pour risques et charges (court terme)** | **450** (4501 litiges, 4502 garanties, 4505 amendes, 4506 pertes de change, 4507 impôts) | Risques exigibles à court terme |
| **47 — Écarts de conversion — passif (circulants)** | **470** (4701, 4702) | Gains de change latents sur éléments circulants |

**Lien avec l'analyse financière** : les comptes 4411 (fournisseurs), 4432 (personnel), 4441 (CNSS), 4491 (PCA) constituent des **ressources d'exploitation gratuites** qui réduisent le BFG :

**BFG = (31 + 34) − 44**. Plus le **délai de règlement fournisseurs (DPO)** est élevé, plus le besoin de trésorerie est allégé **[standard — formule]** ; au Maroc, le respect des délais légaux de paiement est un point contrôlé par le commissaire aux comptes.

---

## 6. Classe 5 — Trésorerie : liquidités et concours bancaires

**Rôle** : suivre la liquidité quotidienne. Le CGNC sépare **Trésorerie-Actif (51)** et **Trésorerie-Passif (55)** — caisse et banques réunies à l'actif, découverts isolés au passif (contrairement au PCG français).

| Rubrique | Comptes principaux | Utilité / Quand l'utiliser |
| --- | --- | --- |
| **51 — Trésorerie — actif** | **5111** Chèques à encaisser ; **5113** Effets à encaisser ; **5115** Virements de fonds (compte de passage) ; **5141** Banques (soldes débiteurs) ; **5143** Trésorerie Générale ; **5146** Chèques postaux ; **5161** Caisses ; **5165** Régies d'avances et accréditifs | Tout encaissement : réception d'un chèque client (débit 5111, crédit 3421) puis crédit bancaire ; retrait banque → caisse via 5115 |
| **55 — Trésorerie — passif** | **5520** Crédits d'escompte ; **5530** Crédits de trésorerie ; **5541** Banques (soldes créditeurs) | Découverts autorisés, escompte et concours bancaires courants à la clôture |
| **59 — Provisions pour dépréciation des comptes de trésorerie** | **5900** | Devises bloquées, comptes gelés |

**Outil de contrôle — le rapprochement bancaire** : explique l'écart entre le solde du compte 5141 et le relevé bancaire (chèques émis non présentés, agios non enregistrés, virements non saisis) ; des régularisations sont passées (charges bancaires en 6147, intérêts financiers en 738).

**Lien avec l'analyse financière** :

- **Trésorerie Nette (TN)** = Trésorerie-Actif (51) − Trésorerie-Passif (55) = **FRF − BFG** (solde de bouclage de l'équilibre financier).
- **Liquidité immédiate** = 51 / dettes exigibles à court terme **[standard]** (le CGNC ne fixe pas de ratios réglementaires).

---

## 7. Classe 6 — Charges (débit du CPC)

**Rôle** : enregistrer les consommations de ressources, **hors taxes récupérables**, rattachées à l'exercice (comptabilité d'engagement). Structure marocaine en **3 niveaux + impôts** (exploitation, financier, non courant).

| Rubrique | Comptes principaux | Utilité / Quand l'utiliser |
| --- | --- | --- |
| **61 — Charges d'exploitation** | **611** Achats revendus de marchandises (**6111/6112** achats, **6114** variation de stocks, **6119** RRR obtenus) ; **612** Achats consommés de matières et fournitures (**6121** matières premières, **6122** consommables, **6123** emballages, **6124** variation, **6125** achats non stockés, **6126** travaux-études-prestations, **6129** RRR) ; **613/614** Autres charges externes (**6131** locations, **6132** redevances de crédit-bail, **6133** entretien, **6134** assurances, **6135** personnel extérieur, **6136** intermédiaires et honoraires, **6137** redevances brevets, **6141** études, **6142** transports, **6143** déplacements, **6144** publicité, **6145** frais postaux et télécoms, **6146** cotisations et dons, **6147** services bancaires) ; **616** Impôts et taxes (**6161** taxe urbaine, patente, taxes locales ; **6167** droits d'enregistrement, taxes sur véhicules) ; **617** Charges de personnel (**6171** rémunérations, **6174** charges sociales, **6176** autres charges sociales, **6177** rémunération de l'exploitant) ; **618** Autres charges d'exploitation (**6181** jetons de présence, **6182** pertes sur créances irrécouvrables) ; **619** Dotations d'exploitation (**6191-6193** amortissements, **6194-6196** provisions dont **61964** créances, **6198** exercices antérieurs) | Enregistrement des achats à réception de facture ; dotation annuelle aux amortissements et provisions ; liquidation de la paie (617) |
| **63 — Charges financières** | **631** Charges d'intérêts (**6311** intérêts des emprunts et dettes, **63114** intérêts des comptes courants) ; **633** Pertes de change ; **638** Autres charges financières (**6386** escomptes accordés, **6385** charges nettes sur cessions de TVP) ; **639** Dotations financières (**6391** amortissement des primes de remboursement, **6392-6394** provisions) | Intérêts courus (crédit de 4493) ; pertes de change ; escomptes de règlement accordés |
| **65 — Charges non courantes** | **651** VNA des immobilisations cédées (6512-6518) ; **656** Subventions accordées ; **658** Autres charges non courantes (**6581** pénalités sur marchés et dédits, **6583** pénalités et amendes fiscales, **6585** créances devenues irrécouvrables, **6586** dons et libéralités) ; **659** Dotations non courantes (**6591** amortissements exceptionnels, **6594** provisions réglementées dont **65941** amortissements dérogatoires, **6595** risques et charges, **65962/65963** dépréciations) | Événements anormaux et fortuits ; cessions d'immobilisations |
| **67 — Impôts sur les résultats** | **6701** Impôts sur les bénéfices (IS) ; **6705** Imposition minimale annuelle (cotisation minimale) ; **6708** Rappels et dégrèvements | Liquidation de l'IS et de la CM (débit 6701, crédit 4453) |

**Lien avec l'analyse financière** : la classe 6 alimente le CPC et l'ESG — les achats (611-614) entrent dans la **marge brute** et la **valeur ajoutée** ; les charges de personnel (617) et impôts et taxes (616) permettent le passage de la VA à l'**EBE** ; les dotations (619) et charges financières (6311) distinguent la performance économique de la performance financière. Côté fiscal, la classe 6 est la base des **réintégrations** (charges non déductibles : amendes 6583, véhicules de tourisme > 400 000 DH, dépenses en espèces > 5 000 DH/jour, intérêts CCA non conformes...).

---

## 8. Classe 7 — Produits (crédit du CPC)

**Rôle** : enregistrer les revenus générés, **hors TVA collectée**, rattachés à l'exercice. Le classement suit la **cascade des soldes de gestion**.

| Rubrique | Comptes principaux | Utilité / Articulation avec les SIG |
| --- | --- | --- |
| **71 — Produits d'exploitation** | **711** Ventes de marchandises (**7111** Maroc, **7113** étranger, **7118** exercices antérieurs, **7119** RRR accordés) ; **712** Ventes de biens et services produits (**7121** biens produits au Maroc — 71211 produits finis, 71212 intermédiaires, 71217 résiduels —, **7122** biens produits à l'étranger, **7124/7125** services produits, **7126** redevances brevets, **7127** ventes et produits accessoires, **7129** RRR) ; **713** Variation des stocks de produits (**7131** en cours, **7132** biens produits, **7134** services en cours) ; **714** Immobilisations produites pour elle-même (7141-7143) ; **716** Subventions d'exploitation ; **718** Autres produits d'exploitation (**7181** jetons de présence reçus, **7182** revenus des immeubles non affectés) ; **719** Reprises d'exploitation et transferts de charges (**7191-7193** reprises sur amortissements, **7194** provisions immobilisations, **7195** risques et charges, **7196** actif circulant, **7197** transferts, **7198** exercices antérieurs) | 711 → **Marge brute** (711 − 611) ; 712+713+714 → **Production de l'exercice** → **Valeur ajoutée** (MB + Production − consommations 612/613/614) ; 716 → **EBE** (VA + 716 − 616 − 617) |
| **73 — Produits financiers** | **732** Produits des titres de participation et titres immobilisés (**7321** revenus des participations) ; **733** Gains de change ; **738** Intérêts et autres produits financiers (**7381** intérêts des prêts, **7384** revenus des TVP, **7385** produits nets sur cessions de TVP, **7386** escomptes obtenus) ; **739** Reprises financières, transferts de charges (7391-7398) | **Résultat financier** = produits financiers (73) − charges financières (63) |
| **75 — Produits non courants** | **751** Produits des cessions d'immobilisations (7512-7518) ; **756** Subventions d'équilibre ; **757** Reprises sur subventions d'investissement ; **758** Autres produits non courants (**7581** pénalités et dédits reçus, **7582** dégrèvements d'impôts, **7585** rentrées sur créances soldées, **7586** dons et libéralités) ; **759** Reprises non courantes (**7591** amortissements exceptionnels, **7594** provisions réglementées, **7595** risques et charges, **7596** dépréciations, **7597** transferts) | **Résultat non courant** ; les produits de cession (751) sont **déduits** du résultat net dans le calcul de la CAF additive |

> ⚠️ **Particularités marocaines** : pas de rubrique globale 78/79 — les reprises et transferts sont ventilés par niveau (719 exploitation, 739 financier, 759 non courant) ; les escomptes de règlement accordés sont débités en **charges financières** (6386) et non déduits des ventes ; les escomptes obtenus sont crédités en **produits financiers** (7386).
> 

**Lien avec l'analyse financière** : la classe 7 alimente CPC et ESG ; seules les **reprises sur éléments stables** (actif immobilisé, financement permanent) sont intégrées à la **CAF additive** — les reprises sur circulants (7194-7196) en sont exclues.

---

## 9. Classe 8 — Résultats : la cascade du résultat net

**Rôle** : classe de transition qui fait apparaître les **résultats intermédiaires en cascade** du CPC et de l'ESG. Le plan officiel distingue **six niveaux** de résultats :

| Rubrique | Comptes principaux | Rôle |
| --- | --- | --- |
| **81 — Résultat d'exploitation** | **810** Résultat d'exploitation (8100) ; **811** Marge brute (8110) ; **814** Valeur ajoutée (8140) ; **817** Excédent brut d'exploitation (**8171** créditeur / **8179** insuffisance brute d'exploitation) | Performance opérationnelle brute avant choix financiers et impôts |
| **83 — Résultat financier** | **8300** | Produits financiers (73) − charges financières (63) |
| **84 — Résultat courant** | **8400** | Résultat d'exploitation + résultat financier (élément cyclique, se prête à la prévision) |
| **85 — Résultat non courant** | **8500** | Opérations anormales et fortuites |
| **86 — Résultat avant impôts** | **8600** | Résultat courant + résultat non courant |
| **88 — Résultat après impôts** | **8800** | Bénéfice ou perte nette finale après IS ; solde transféré au bilan : **1191** (bénéfice) ou **1199** (perte) en classe 1 |

**Affectation du résultat (AGO)** : une fois les comptes approuvés, l'assemblée vote l'affectation — **réserve légale** (dotation annuelle, usuellement 5 % du bénéfice dans la limite de 10 % du capital pour SA/SARL **[À VÉRIFIER selon textes]**, compte 1140), **dividendes** (4465 ; retenue à la source art. 247-XXXVII-C CGI), **report à nouveau** (1161). La distribution est débitée du compte 1191 ; le résultat non encore affecté transite par **1181/1189**.

**Lien avec l'analyse financière** : les soldes 8110/8140/8171 sont la base des ratios de marge (marge brute, taux de VA, taux d'EBE) ; le résultat net (1191/1199) alimente la **CAF** (méthode additive), le **ROE** et la politique de distribution.

---

## 10. Classe 9 — Comptes de produits et charges réfléchis (comptabilité analytique)

**Rôle** : outil interne de **contrôle de gestion** — calcul des coûts, des centres d'analyse, des écarts — fonctionnant de manière autonome par rapport à la comptabilité générale via les **comptes réfléchis** (miroir des comptes généraux).

| Rubrique | Contenu | Utilisation |
| --- | --- | --- |
| **90 — Comptes de produits et charges réfléchis** | **903** Stocks réfléchis (9031/9039) ; **906** Charges réfléchies (**9061** exploitation, **9063** financières, **9065** non courantes, **9067** IS) ; **907** Produits réfléchis (9071/9073/9075) ; **908** Résultats réfléchis (9081-9088) | Miroir de la comptabilité générale pour alimenter la CAE sans interférer avec les comptes légaux |
| **91 — Comptes de reclassement et d'analyse** | Ouverts et attribués selon les nécessités de l'entreprise | Retraiter/reclasser les charges selon les besoins d'analyse |
| **92 — Sections analytiques** | **921** Sections générales ; **923** Approvisionnement ; **925** Production ; **927** Distribution ; **928** Autres | Regrouper les charges indirectes par centres d'activité (répartition primaire et secondaire, unités d'œuvre) |
| **93 — Coûts d'achat ou de production** | **933** Coûts d'achat (9331 marchandises, 9335 matières) ; **935** Coûts de production (9351/9352) ; **938** Autres (9381 coûts de production des immobilisations) | Valoriser les stocks et les produits au coût complet |
| **94 — Inventaire permanent des stocks** | **941-945** Inventaire permanent (marchandises, matières, en-cours, produits) ; **949** Provisions sur stocks | Suivi continu des stocks en quantités et en valeur |
| **95 — Coûts de revient** | **953** Marchandises ; **955** Produits ; **958** Autres | Coût complet unitaire par produit/commande/chantier |
| **96 — Écarts sur coûts préétablis** | **962** Écarts sur sections (quantités, coûts) ; **964** Écarts sur inventaire permanent | Contrôle budgétaire : écarts entre réalisations et prévisions |
| **97 — Différences d'incorporation** | **971** Charges non incorporables ; **972** Charges supplétives incorporées ; **973** Produits non incorporés ; **974/975** Différences sur charges/produits incorporables ; **976** Différences d'inventaire ; **977** Différences sur niveau d'activité ; **978** Autres | Rapprocher le coût d'analyse (avec charges supplétives) du coût comptable |
| **98 — Résultats analytiques** | **981-983** Résultats par catégorie ; **986** Reports des écarts sur coûts préétablis ; **987** Reports des différences d'incorporation | Réconciliation du résultat analytique global avec le résultat net de la comptabilité générale |
| **99 — Comptes de liaison interne** | **991** Liaisons internes d'un même établissement ; **995** Cessions entre établissements (9951 fournies, 9955 reçues) | Transferts internes de charges et produits entre établissements |

**Quand l'utiliser** : détermination des coûts complets (méthode des sections homogènes), analyse de rentabilité par produit, contrôle budgétaire (écarts sur coûts préétablis), pilotage opérationnel — hors états de synthèse légaux.

---

## 11. Classe 0 — Comptes spéciaux (bilan d'ouverture, comptes d'ordre et engagements hors bilan)

**Rôle** : opérations techniques de fin/début d'exercice et suivi des engagements hors bilan.

| Rubrique | Contenu | Utilisation |
| --- | --- | --- |
| **01 — Bilan d'ouverture** | **011-015** Réouverture des comptes de financement permanent, d'actif immobilisé, d'actif/passif circulant et de trésorerie | Réouverture des comptes en début d'exercice |
| **02 — Clôture du bilan** | **021-025** Clôture des comptes des mêmes masses | Clôture des comptes en fin d'exercice |
| **03 — Comptes d'ordre** | **031/033** Opérations en instance de dénouement ; **035/036** Opérations en devises (contre-valeur) ; **038** Données statistiques | Suivi des opérations transitoires et statistiques |
| **04 — Engagements donnés** | **041** Avals, cautions et garanties donnés ; **043** Engagements de pensions de retraite ; **045** Effets circulant sous endos ; **046** Prêts consentis non versés ; **048** Autres | Engagements hors bilan donnés (dettes potentielles pour l'analyste !) |
| **05 — Engagements reçus** | **051** Avals, cautions et garanties reçus ; **055** Biens détenus en garantie ; **056** Emprunts non encore encaissés ; **057** Découverts non utilisés et plafonds d'escompte ; **058** Autres | Engagements hors bilan reçus (ressources potentielles) |
| **06 — Engagements de crédit-bail** | **061** Redevances de crédit-bail restant à courir ; **065** Engagements reçus pour utilisation en crédit-bail | Suivi des engagements de location-financement |
| **08 — Autres comptes spéciaux** | **081** | Divers |

**Lien avec l'analyse financière** : les engagements hors bilan (04/05/06) sont repris dans l'**ETIC** — élément clé pour l'analyste : les cautions données (041), les engagements de retraite (043) et les redevances de crédit-bail (061) peuvent cacher des **dettes potentielles** qui pèsent sur la solvabilité réelle (retraitement en dette financière du crédit-bail, par exemple).

---

## 12. Articulation des comptes avec les états de synthèse et l'analyse financière

| État de synthèse | Classes d'alimentation | Rôle de l'état |
| --- | --- | --- |
| **Bilan (BL)** | Classes **1 à 5** | Photographie patrimoniale, lecture fonctionnelle en masses (FRF, BFG, TN) |
| **CPC** | Classes **6 et 7** | Performance en cascade : résultat d'exploitation (81) + financier (83) = résultat courant (84) ; + non courant (85) = résultat avant impôts (86) ; − IS (67) = résultat après impôts (88) |
| **ESG** | Classes **6, 7, 8** | TFR (MB 811, VA 814, EBE 817, résultats) + tableau de détermination de la **CAF** et de l'autofinancement |
| **Tableau de Financement (TF)** | Classes **1 à 5**  • autofinancement | Flux entre deux bilans : CAF, emplois/ressources stables, variations du FRF, BFG, TN |
| **ETIC** | Notes + classes 2-4 et 0 (tableaux immobilisations, provisions, créances/dettes, engagements hors bilan) | Méthodes, dérogations, engagements hors bilan, échéanciers |

**Tableau de correspondance comptes → indicateurs d'analyse** :

| Indicateur | Formule fonctionnelle | Comptes d'origine |
| --- | --- | --- |
| **FRF** | Financement permanent − Actif immobilisé | Classe 1 − Classe 2 |
| **BFG** | Actif circulant (hors trésorerie) − Passif circulant (hors trésorerie) | (31 + 34 + 35) − (44 + 45) |
| **TN** | Trésorerie-Actif − Trésorerie-Passif = FRF − BFG | 51 − 55 |
| **Marge brute** | Ventes de marchandises − Achats revendus | 711 − 611 |
| **Valeur ajoutée** | MB + Production − Consommations externes | (711-714) − (612/613/614) |
| **EBE** | VA + Subventions d'exploitation − Impôts et taxes − Charges de personnel | VA + 716 − 616 − 617 |
| **Résultat courant** | Résultat d'exploitation + Résultat financier | 81 + 83 (84) |
| **CAF (additive)** | RN + dotations stables − reprises stables − produits de cessions + VNA cédées | 88 + 619/639/659 (stables) − 719/739/759 (stables) − 751 + 651 |
| **IS / CM** | 6701 / 6705 (via 4453) | Passage RC → RF (liasse fiscale) |

---

## 13. Pièges et particularités du référentiel marocain à retenir

1. **Analyse fonctionnelle, pas liquidité** : créances et dettes classées par fonction économique, quelle que soit leur échéance — le bilan marocain se lit en FRF/BFG/TN.
2. **Non-valeurs (21)** = actif fictif : à éliminer de l'actif net réel et des capitaux propres.
3. **Capitaux propres assimilés (13)** : subventions d'investissement et provisions réglementées comptées en capitaux propres malgré la dette d'impôt latent — retraitement en quasi-fonds propres.
4. **Rubrique 16 = comptes de liaison** (et non les emprunts comme en France) ; le **report à nouveau est en 116** (rubrique 11) ; les **résultats en instance d'affectation en 118** ; les dettes financières sont en **14**.
5. **Tiers non compensés** : débiteurs en 34, créditeurs en 44 (jamais de solde net).
6. **Trésorerie positive (51) et négative (55) présentées séparément** au bilan.
7. **Escomptes accordés en charges financières (6386)** ; pas de rubriques globales 78/79 (reprises/transferts ventilés : 719/739/759).
8. **CAF additive** : exclut les dotations/reprises sur actif circulant et trésorerie ; exclut les produits de cession (751) et réintègre les VNA (651).
9. **IS dans le CPC** via 6701/6705 ; **IS non déductible** et **CSS non déductible** (réintégrations) ; les pénalités et amendes fiscales (6583) sont non déductibles.
10. **Classe 8 en cascade** : 81 (résultat d'exploitation + soldes intermédiaires 811/814/817) → 83 (financier) → 84 (courant) → 85 (non courant) → 86 (avant impôts) → 88 (après impôts) → transfert en 1191/1199 au passif.
11. **Engagements hors bilan (classe 0)** : cautions, retraites, crédit-bail — à retraiter dans l'analyse de solvabilité.
12. **Classe 9 autonome** : comptes réfléchis (90), sections (92), coûts (93-95), écarts (96), différences d'incorporation (97) — le résultat analytique (98) doit se réconcilier avec le résultat général.

---

## 14. Limites et points à vérifier

| Élément | Statut |
| --- | --- |
| Formules chiffrées des ratios de rentabilité (ROE/ROA) dans le référentiel CGNC | **[standard]** — non définies par le CGNC (l'AMMC et les documents de référence les calculent : ROE = RN/fonds propres moyens) |
| DSO / DPO en jours | **[standard]** — formules classiques |
| Réserve légale : 5 % du bénéfice, plafond 10 % du capital | **[À VÉRIFIER]** — pratique usuelle SA/SARL (loi 17-95 / 5-96) |
| Durées d'amortissement précises par catégorie (bâtiments 20 ans, matériel 10 ans, transport 5 ans...) | **[standard]** — le plan comptable ne les chiffre pas ; usages fiscaux (CGI) et professionnels |
| Comptes 56/57/58 de la classe 5 | Absents du PCGE d'entreprise (spécifiques PCEC bancaire) |
| Coquille « 2441 » pour les prêts au personnel dans le document PDF source | Probablement **2411** (cohérent avec 2415/2416/2418) — **[À VÉRIFIER]** sur le CGNC officiel |

---

## 15. Sources principales

- **Plan Comptable Marocain (PCGE)** — nomenclature officielle des classes 1 à 0 (document PDF fourni, vérifié compte par compte)
- CGNC — Code Général de Normalisation Comptable (Conseil National de la Comptabilité) : cadre comptable, terminologie, modalités de fonctionnement des comptes
- Loi n° 9-88 (obligations comptables des commerçants) et loi 44-03
- Plan comptable du secteur immobilier (classes 1 à 9 détaillées) ; plan comptable des établissements de crédit (PCEC) — comparaison
- Liasse fiscale DGI (23 tableaux, T5/T6/T7 : ESG-CAF, TF) ; guide arrêté des comptes (revue par classe 1-5)
- Upsilon Consulting (PCGE, états de synthèse, réévaluation) ; CRMEF (référentiel comptable marocain) ; Master GCFF (loi 9-88)
- Documents de référence AMMC (FEC, CDG Capital, Wafasalaf, CFG Bank)

---

*Rapport généré le 04/08/2026 — NotebookLM (308 sources) + vérification contre le Plan Comptable Marocain officiel (PDF fourni). Les éléments marqués [standard] et [À VÉRIFIER] doivent être confirmés dans les référentiels de cours et les textes officiels.*