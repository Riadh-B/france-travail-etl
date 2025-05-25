# France Travail - Récupération des offres d'emploi CDI (Département 07)

Ce projet permet de récupérer automatiquement les **offres d’emploi en CDI** dans le **département 07 (Ardèche)** depuis l’API publique de **France Travail**.  
Les données sont exportées dans 3 fichiers CSV distincts : `offres.csv`, `entreprises.csv`, `competences.csv`.

---

## 🚀 Fonctionnalités

- Authentification OAuth2 via identifiants API
- Requête de l’API France Travail paginée (toutes les offres disponibles)
- Extraction des données utiles
- Séparation des offres, des entreprises et des compétences
- Sauvegarde des résultats au format CSV

---

## 🗂️ Structure du projet
```bash
├── api.py # Authentification + récupération des offres
├── parser.py # Extraction des données brutes en 3 structures
├── utils.py # Export vers fichiers CSV
├── main.py # Point d’entrée principal
├── .env # Identifiants API (non versionné)
├── .gitignore # Fichiers à ne pas versionner
└── README.md # Ce fichier
```

---

## 🛠️ Prérequis

- Python 3.7+
- Clé API France Travail (inscription gratuite sur [francetravail.io](https://www.francetravail.io/))

---

## 🧪 Installation

1. **Clone du projet**
   ```bash
   git clone https://github.com/<ton_utilisateur>/france-travail-etl.git
   cd france-travail-etl
   ```

2. **Création du fichier .env** 
```bash
CLIENT_ID=xxxxxxxxxxxx
CLIENT_SECRET=xxxxxxxxxxxx
TOKEN_URL=https://entreprise.francetravail.fr/connexion/oauth2/access_token?realm=/partenaire
API_SCOPE=api_offresdemploiv2 o2dsoffre
URL_API=https://api.francetravail.io/partenaire/offresdemploi/v2/offres/search
```

2. **Installation des dépendances** 
Installation des dépendances
```bash
requests
pandas
python-dotenv
```

3. **Lancer le script**
```bash
python main.py
```

Les fichiers suivants seront créés dans le dossier courant :

offres.csv

entreprises.csv

competences.csv

