# Projet 2 - La ferme des 3 chênes

Création d'un site internet pour une exploitation laitière et agricole

## Installation et lancement du projet

### Pour utilisateur de Windows

#### Installation du projet

```
git clone https://github.com/CrevetteGaming/LINFO1002
cd  LINFO1002
cd flask_app
```

#### Installation de flask et de l'environnement virtuel

installation de l'environnement virtuel utile pour le lancement du site

```
py -3 -m venv venv
.\venv\Scripts\activate
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
git clone https://github.com/CrevetteGaming/LINFO1002
cd  LINFO1002
```

#### Installation de Flask

```
pip3 install flask
```

#### Lancement du site

```
cd flask_app
cd flaskr
```

```
flask run
```

#### Rendez vous sur votre navigateur

Introduisez l'url suivant : http://127.0.0.1:5000


## En cas d'erreur

En cas d'erreur lors du lancement du site n'hésitez pas à nous contacter via nos 2 adresses mail : dylan.mainghain@uclouvain.be ou bien nicolas.swinnen@uclouvain.be 

Vous avez dans le répertoire racine du site un fichier explication-screen.pdf qui permet de visualiser le site à l'aide de screenshots et d'explications.

## Arborecense des fichiers
```
LINFO1002-P2
├── README.md
├── readme.txt
├── src // Dossier contenant tout le projet
│   ├── app.py // Fichier principal, le fichier à exécuter pour lancer les sites
│   ├── db // Fichiers liés à la base de données
│   │   ├── 1002-sql-data // Dossier contenant les fichiers d'insertions, les données
│   │   ├── create_db.py // Fichier pour initialiser la base de données, générer les différentes races
│   │   ├── create_db.sql // Script SQL qui crée la base de données
│   │   ├── database.db // Base de données SQL
│   │   ├── db.py // Interface de la base de données
│   │   ├── generate_race.py // Fichier contenant la fonction pour générer la course et la fonction utils pour celle-ci
│   │   ├── __init__.py
│   ├── moon_phase.py // Fichier permettant de calculer la phase de lune pour une date
│   ├── static // Tout les fichiers static du site
│   │   ├── chartjs // Chart js lib
│   │   │   ├── Chart.bundle.min.js
│   │   │   ├── Chart.min.css
│   │   │   └── Chart.min.js
│   │   ├── style.css // Styles pour le site Web
│   │   ├── images
│   │   └── js
│   │       ├── base.js
│   │       └── index.js // Le JS pour la page d'accueil
│       ├── 404.html
│       ├── about.html
│       ├── contact.html
│       ├── bases.html
│       └── index.html
├── tests
│   ├── test_db.py
│   └── test_moon_.py
```

## Auteurs

- Mainghain Dylan
- Swinnen Nicolas
