# Ising Model - README -

LPHYS1201 : Informatique et méthodes numériques \
Auteurs : Solal Lemoine, Etienne Roger \
Date de création : Décembre 2023 

## Description du projet
Ce projet en python porte sur la simulation du modèle d'Ising en 2D via un algorithme de Metropolis. \
Il s'agit d'un modèle simple mais important en physique statistique qui sert à étudier les propriétés ferromagnétiques de matériaux.

## Fichiers
Le dossier comporte 4 modules et 2 programmes exécutables. 
* Metropolis.py 
* Initialize.py 
* Fixed_temp.py 
* Range_temp.py
* Ising_main.py 
* Demonstration.py 
### Modules de fonctions "outils"
* Metropolis.py : implémentation de l'algorithme de Metropolis ainsi que quelques autres fonctions utiles.
* Initialize.py : fonctions qui initialisent une simulation càd qui demandent à l'utilisateur les paramètres de la simulation souhaitée.
### Modules de fonctions "simulation"
* Fixed_temp.py : simulation pour une température fixe, \
représentation visuelle de la grille, graphes de l'énergie et de la magnétisation au cours du temps.
* Range_temp.py : simulation pour une série de températures \
  et graphes des énergies et magnétisations finales selon la température.
### Programmes exécutables
* Ising_main.py : programme de simulation du modèle d'Ising, laissant l'utilisateur choisir les paramètres de simulation.
* Demonstration.py : programme "démo" pour une simulation particulière avec paramètres prédéfinis.

## Packages utilisés

Dans ce projet, les packages suivants sont utilisés :
* numpy
* matplotlib
* tqdm
Ceux-ci doivent donc être installés si ce n'est déjà fait \
dans l'ordinateur de l'utilisateur pour qu'il puisse correctement exécuter les programmes.

## Exécution 

Le fichier principal du projet est Ising_main.py . \ 
Lancé simplement par un "python Ising_main.py" dans le terminal,
il permet à l'utilisateur de choisir exactement chaque paramètre et configuration de \
la simulation souhaitée du modèle d'Ising. \

### Paramètres initiaux intéressants


## Lien du dépôt github

[https://github.com/Duckoder/Ising-model.git]