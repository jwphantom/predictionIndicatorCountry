# Outils décisionnel - Application de prédiction des indicateurs d'un pays

Bienvenue dans l'application d'outils décisionnel, une application web Flask conçue pour prédire certains indicateurs clés d'un pays notamment des indicateurs comme l'espérance de vie, taux de mortalité adulte, infantile etc...

## Structure du projet

Le projet est organisé de la manière suivante :

    app/
        init.py
        ###autres fichiers

        routes/
            init.py
            ###autres fichiers
        
        models/
            init.py
            ###autres fichiers

        templates/
            ###fichiers de vue

        utils/
            ### fichier de fonction

        error.py

    run.py



- Le dossier `app` contient le code de l'application Flask.
- Le sous-dossier `routes` contient les fichiers de routage de l'application.
- Le sous-dossier `models` contient les modèles de prédiction.
- Le sous-dossier `templates` contient les vues des routes.
- Le sous-dossier `utils` contient des fonctions statique.
- `error.py` contient la gestion des erreurs web.
- `run.py` est le point d'entrée de l'application.


## Installation des dépendances

Avant de lancer l'application, assurez-vous d'installer les dépendances nécessaires en utilisant `pip` et le fichier `requirements.txt`. Exécutez la commande suivante à la racine de votre projet :

```shell
pip install -r requirements.txt
```

## Lancement de l'application

```shell
flask --app run run 
```

## Usage

L'application vous permet de faire ressortir les indicateurs d'un pays à partir des données reçus. Utilisez l'interface utilisateur pour interagir avec l'application et effectuer des prédictions.


## Usage
- James Olongo (https://github.com/jwphantom)


## Licence

Ce projet est sous licence MIT
