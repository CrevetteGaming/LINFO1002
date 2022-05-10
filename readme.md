# Projet 2 - La ferme des 3 chênes

Création d'un site internet pour une exploitation laitière et agricole

## Installation et lancement du projet

### Pour utilisateur de Windows

#### Installation du projet

```
git clone https://github.com/CrevetteGaming/LINFO1002_P2_MATTHIEU_08
cd  LINFO1002

cd flask_app
```

#### Installation de flask et lancement de l'environnement virtuel

lancement de l'environnement virtuel utile pour le lancement du site

```
.\env\Scripts\activate
```

installation de Flask

```
pip install Flask
```

#### Lancement du site

```
flask run
```

#### Rendez vous sur votre navigateur

Introduisez l'url suivant : http://127.0.0.1:5000


### Pour utilisateur POSIX (Mac et Linux)

#### Installation du projet

Commencons par cloner le dépo et allons dans le dossier du projet

```
git clone https://github.com/CrevetteGaming/LINFO1002_P2_MATTHIEU_08
cd  LINFO1002
```

#### Installation de Flask

```
pip3 install flask
```

#### Lancement du site

```
cd flask_app
```

```
flask run
```

#### Rendez vous sur votre navigateur

Introduisez l'url suivant : http://127.0.0.1:5000


## En cas d'erreur

En cas d'erreur lors du lancement du site n'hésitez pas à nous contacter via nos 2 adresses mail : nicolas.swinnen@student.uclouvain.be 

Vous avez dans le répertoire racine du site un fichier explication-screen.pdf qui permet de visualiser le site à l'aide de screenshots et d'explications.

## Arborecense des fichiers
```
LINFO1002-P2
├── README.md
├── LICENCE
├── flask_app // Dossier contenant tout le projet
│   ├── database // Fichiers liés à la base de données
│   │   ├── 1002-sql-data // Dossier contenant les fichiers d'insertions, les données
│   │   │   |   ├── insert_animaux.sql
│   │   │   |   ├── insert_animaux_types.sql
│   │   │   |   ├── insert_animaux_velages.sql
│   │   │   |   ├── insert_complications.sql
│   │   │   |   ├── insert_familles.sql
│   │   │   |   ├── insert_types.sql
│   │   │   |   ├── insert_velages.sql
│   │   │   |   └── insert_velages_complications.sql
│   │   ├── create_db.py // Fichier pour initialiser la base de données, générer les différentes races
│   │   ├── inginious.sql // Script SQL qui crée la base de données
│   │   ├── database.sqlite base de données 
│   │   ├── info // Fichiers contenant les fonctions utiles pour créer les différents graphiques
│   ├── static // Tout les fichiers static du site
│   │   │   └── css 
│   │   │   |   └── style.css // Styles pour le site Web
│   │   │   └── images
│   │   │   |   ├── farm-logo-3.ico
│   │   │   |   ├── farm-logo-2.png
│   │   │   |   ├── troischenes1.jpg
│   │   │   |   ├── troischenes1.jpg
│   │   │   |   ├── troischenes2.jpg
│   │   │   |   └── troischenes3.jpg
│   ├── templates
│   |   ├── bases.html
│   |   ├── index.html
│   |   ├── about.html
│   |   └── contact.html
|   ├── tests
│   |   └── test.py
│   ├── Explication-Screen.pdf
│   │── __init__.py // Fichier principal, le fichier à exécuter pour lancer les sites
│   ├── app.py 
|   ├── readme.txt

```

## Auteurs

- Mainghain Dylan
- Swinnen Nicolas
