# Ising Model - README

**LPHYS1201 : Informatique et méthodes numériques**

Auteurs : Solal Lemoine, Étienne Roger

Date de création : Décembre 2023

## Description du projet

Ce projet en python porte sur la simulation du modèle d'Ising en 2D via un algorithme de Metropolis. \
Il s'agit d'un modèle simple mais important en physique statistique qui sert à étudier les propriétés ferromagnétiques de matériaux.

## Fichiers

Le dossier comporte 4 modules et 3 programmes à exécuter directement:

* *Metropolis.py*
* *Initialize.py*
* *Fixed_temp.py*
* *Range_temp.py*

* ***Ising_main.py***
* *Fix_demo.py*
* *Range_demo.py*

### Modules de fonctions "outils"

* *Metropolis.py* : implémentation de l'algorithme de Metropolis ainsi que quelques autres fonctions utiles.
* *Initialize.py* : fonctions qui initialisent une simulation càd qui demandent à l'utilisateur les paramètres de la simulation souhaitée.

### Modules de fonctions "simulation"

* *Fixed_temp.py* : simulation pour une température fixe, \
représentation visuelle de la grille, graphes de l'énergie et de la magnétisation au cours du temps.
* *Range_temp.py* : simulation pour une série de températures \
  et graphes des énergies et magnétisations finales selon la température.

### Programmes à exécuter directement

* **Ising_main.py**: programme de simulation du modèle d'Ising, laissant l'utilisateur choisir les paramètres de simulation.
* *Fix_demo.py* : programme "démo" pour une simulation Fixed_temp particulière avec paramètres prédéfinis.
* *Range_demo.py* : programme "démo" pour une simulation Range_temp particulière avec paramètres prédéfinis.

## Packages utilisés

Dans ce projet, les packages suivants sont utilisés :

* *numpy* : pour la facilitation des opérations sur les matrices et le générateur pseudo-aléatoire 
* *matplotlib* : pour toutes les représentations graphiques
* *tqdm* : pour afficher une barre de progression de la simulation

Ceux-ci doivent donc être installés si ce n'est déjà fait \
dans l'ordinateur de l'utilisateur pour qu'il puisse correctement exécuter les programmes.

## Exécution

Le fichier principal du projet est Ising_main.py .\
Lancé simplement par un "python Ising_main.py" dans le terminal,
il permet à l'utilisateur de choisir exactement chaque paramètre et configuration de\
la simulation souhaitée du modèle d'Ising.

Les fichiers Fix_demo.py et Range_demo.py eux sont des programmes sans input et\
peuvent donc être exécuter sans interaction de la part de l'utilisateur. \
Chacun simule un cas intéressant des modèles à température respectivement fixe et variable.

Notons que ces 3 fonctions produisent toutes des graphiques, sauvegardés automatiquement :\
Ising_main.py dans le cas d'une simulation à T fixe (model = "f") et Fix_demo.py produisent\
 <FixT_energy_magnet.png> et <lattice_evolution.png>.
Ising_main.py dans le cas d'une simulation à T variable (model = "r") et Range_demo.py produisent <RangeT_energy_magnet.png>.

Attention, l'utilisateur doit fermer les fenêtres des graphes pour que le programme prenne fin.

### Paramètres initiaux intéressants

Voici quelques paramètres à utiliser dans Ising_main.py pour obtenir \
des graphiques de simulations physiquement intéressantes :

* B nul : N=100, matrix type = r, J= 1, B = 0 , model = f, T = 0.5, edge = c
* B fort : N = 100, matrix type = r, J = 1, B = 1, model = f , T = 0.5, edge = c
* J nul : N = 100, matrix type = d, J = 0, B = 1, model = r, edge = t
* J fort : N = 100, matrix type = u, J = 2, B = 0, model = r, edge = c

### Lien du dépôt github

[(https://github.com/lemoine-py/Ising-model.git)]
