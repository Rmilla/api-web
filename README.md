# Projet api web

Ce projet, développé dans le cadre de notre formation chez Diginamic, consiste en la création d'une API web compacte et efficace. Utilisant des technologies de pointe telles que SQLAlchemy, FastAPI et Uvicorn, cette API a été conçue pour offrir une expérience utilisateur fluide et des performances optimales. SQLAlchemy nous a permis de gérer la base de données avec une approche orientée objet, tandis que FastAPI a apporté sa rapidité et sa simplicité pour la création d'interfaces API modernes. Finalement, Uvicorn, en tant que serveur ASGI, a assuré une connexion rapide et fiable. Ce projet représente une synthèse pratique de notre apprentissage chez Diginamic, démontrant notre capacité à intégrer ces technologies avancées dans une solution concrète.

## Fonctionalités

- Gestion de Requêtes et Réponses Asynchrones : Utilisation de FastAPI pour gérer les requêtes et réponses de manière asynchrone, améliorant ainsi les performances et l'efficacité du serveur.

- Opérations CRUD sur la Base de Données : Implémentation complète des opérations Create, Read, Update, Delete (CRUD) via SQLAlchemy, permettant une manipulation facile et efficace des données.

- Gestion des Erreurs : Système robuste de gestion des erreurs pour fournir des réponses claires et précises en cas de problèmes.

- Performances Optimisées avec Uvicorn : Utilisation d'Uvicorn, un serveur ASGI léger et rapide, pour des performances accrues, particulièrement dans les environnements asynchrones.

- Routes API Personnalisables : Création de routes API personnalisées et intuitives, rendant l'API facile à utiliser et à intégrer.

- Tests Unitaires : Mise en œuvre de tests unitaires pour assurer la fiabilité et la robustesse du code, facilitant ainsi la maintenance et les mises à jour futures.

## Architechture du projet

Voici l'architecture du projet pour l'api web

```
nom_projet/
    |- README.md
    |- requirements.txt
    |- .gitignore
    |- projet/
        |- __init__.py
        |- main.py
        |- config/
            |- __init__.py
            |- db.py
            |- ...
        |- controllers/
            |- __init__.py
            |- ...
        |- models/
            |- __init__.py
            |- ...
        |- routes/
            |- __init__.py
            |- ...
        |- schemas/
            |- __init__.py
            |- ...
    |- tests/
        |- __init__.py
        |- ...
   
```
- README.md : Fournit une vue d'ensemble, des instructions d'installation et d'utilisation.
- requirements.txt : Liste toutes les bibliothèques Python nécessaires.
- .gitignore : Empêche certains fichiers/dossiers d'être suivis par Git.
- main.py : Fichier principal lancé pour démarrer l'application FastAPI.
- Dossier config : Contient les configurations, notamment la connexion à la base de données.
- Dossier controllers : Gère la logique métier et le traitement des données.
- Dossier models : Définit les structures de données pour la base de données.
- Dossier routes : Définit les points de terminaison de l'API et leur logique associée.
- Dossier schemas : Schémas Pydantic pour la validation et la sérialisation des données.

