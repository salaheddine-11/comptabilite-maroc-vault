### Tableau 1 : Nomenclature et fonctionnement des deux instruments (Loi 15-95)
| Caractéristique / Compte | Lettre de Change Relevée (LCR) | Billet à Ordre Relevé (BOR) |
| :--- | :--- | :--- |
| **Rôle & Création** | Créée par le vendeur (tireur) qui ordonne à son client (tiré) de payer [1-3]. | Émis par le client (souscripteur) qui s'engage à payer son créancier [3-6]. |
| **Acceptation & Échéance** | Requiert l'acceptation expresse (signature au recto) du tiré [7, 8]. Échéance à court terme [9, 10]. | Pas d'acceptation requise (le souscripteur est déjà engagé) [11]. Échéance < 3 mois [12, 13]. |
| **Compte 3425 (Actif)** | **Clients - effets à recevoir** : Portefeuille d'actifs pour suivre les traites acceptées [14-16]. | Utilisé de la même façon pour enregistrer les billets à ordre reçus des clients [14, 16]. |
| **Compte 4415 (Passif)** | **Fournisseurs - effets à payer** : Enregistre les dettes d'effets acceptées chez le client [17-19]. | Enregistre l'engagement direct de paiement signé par le client [17-19]. |
| **Comptes d'attente (5113)** | **Effets à l'encaissement** (Transitoire) : Reçoit les effets remis en banque avant crédit final [20-22]. | Le PCGE n'a pas de compte 3450 pour l'encaissement (345 est l'État [23], 5113 gère les effets [20, 21]). |

### Tableau 2 : Cycle comptable complet chez le vendeur (PCGE Maroc)
| Étape du cycle | Débit | Crédit | Observations & Justifications PCGE |
| :--- | :--- | :--- | :--- |
| **1. Création de l'effet** | **3425** (Effets à recevoir) | **3421** (Clients) | Matérialise la créance ordinaire en effet négociable [14, 24]. |
| **2. Remise à l'escompte** | **5141** (Banque - net) <br>**63115** (Intérêts d'escompte HT) <br>**61472** (Commissions HT) <br>**34552** (TVA récup. 10%) | **5520** (Crédits d'escompte) | Le compte **5520** enregistre le nominal total [25-27]. L'effet reste maintenu en **3425** à l'actif [15, 16, 28]. |
| **3. Dénouement escompte** | **5520** (Crédit d'escompte) | **3425** (Effets à recevoir) | Écriture passée à la date d'échéance pour solder les comptes miroirs [29-31]. |
| **4. Endossement** | **4411** (Fournisseurs) | **3425** (Effets à recevoir) | Transmission de propriété à un tiers pour règlement de dette [32, 33]. |
| **5. Aval (Garantie tiers)** | **0411** / **0451** (Engagements) | **0419** / **0459** (Contreparties) | Enregistrement extra-comptable (Hors-bilan) obligatoire [34-36]. |
| **6. Encaissement direct** | **5113** (Effets à encaisser) <br>puis **5141** (Banque) & **6147** | **3425** (Effets à recevoir) <br>puis **5113** (Effets à encaisser) | Transit par **5113** puis prélèvement des commissions de service (TVA 10%) [21, 22]. |
| **7. Impayé à l'échéance** | **3421** (Clients - nominal + frais) <br>**6147** (Frais de rejet HT) <br>**34552** (TVA 10%) | **5141** (Banque - si escompté) <br>**3425** (Effets à recevoir) | Si escompté, la banque se rembourse sur le compte courant [37, 38]. Le client est débité [37, 39]. |
| **8. Recouvrement final** | **5141** (Banque) | **3421** (Clients) | Solde définitif après règlement amiable ou poursuites [40, 41]. |

### Tableau 3 : Les 3 pièges fondamentaux à éviter au Maroc
| Piège comptable ou fiscal | Règle du Référentiel Français (PCG) | Règle Impérative PCGE Maroc / Loi 15-95 |
| :--- | :--- | :--- |
| **1. Maintien en 3425 vs Dé-comptabilisation** | En France, les effets escomptés peuvent être retirés de l'actif (dé-comptabilisation sous conditions de transfert de risques). | **Maintien obligatoire à l'actif** en **3425** jusqu'à l'échéance réelle de l'effet [15, 16, 28], contre-passé par le passif **5520** [26, 42]. |
| **2. LCR magnétique vs LCR papier** | La LCR dématérialisée française permet une simplification comptable et l'escompte direct sans effet papier. | **Pas de LCR magnétique cambiaire** : L'escompte magnétique est traité comme un crédit de trésorerie classique [43]. Les créances restent en **3421** [44]. |
| **3. Rigueur Cambiaire & Délais** | Des délais de grâce peuvent être accordés par le juge. Recours moins formalistes. | **Interdiction des jours de grâce** (Art. 231 du Code de Commerce) [45, 46]. Recours prescrits par **3 ans** contre le tiré [47] et **1 an** contre l'endosseur [47]. |