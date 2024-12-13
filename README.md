# Visualisateur de la Suite de Fibonacci

## Description

Ce projet vise à développer une application en Python qui permet de calculer la suite de Fibonacci en trois versions différentes :
1. Version récursive
2. Version récursive avec programmation dynamique (mémoïsation)
3. Version itérative

L'application mesure également le temps d'exécution de chaque méthode et compare les résultats de manière visuelle à l'aide d'une interface graphique conviviale.

## Objectif

Le programme a pour but de démontrer les différentes approches de calcul de la suite de Fibonacci et de mettre en évidence les différences de performance entre elles. Il permet aux utilisateurs d'entrer un entier `n` et de voir les résultats de chaque méthode ainsi que le temps qu'elles ont mis à exécuter.

## Fonctionnalités Principales

- **Calcul des Valeurs de Fibonacci :**
  - Implémentation de trois méthodes :
    - Récursive
    - Récursive avec programmation dynamique
    - Itérative
- **Mesure du Temps d'Exécution :**
  - Mesure et affichage du temps nécessaire pour chaque méthode.
- **Interface Graphique :**
  - Utilisation de `Tkinter` ou `PyQt` pour une interface utilisateur attrayante.
  - Champs de saisie pour entrer le numéro du terme de Fibonacci.
  - Boutons pour lancer le calcul pour chaque méthode.
  - Affichage des résultats et des temps d'exécution.
- **Comparaison des Résultats :**
  - Présentation des résultats sous forme de tableaux ou de listes.
  - Visualisation des temps d'exécution via des graphiques (optionnellement avec `matplotlib`).
- **Gestion des Erreurs :**
  - Validation des entrées utilisateur pour s'assurer qu'elles sont des entiers non négatifs.

## Technologies Utilisées

- **Langage :** Python
- **Bibliothèques :**
  - `Tkinter` ou `PyQt` pour l’interface graphique.
  - `time` pour mesurer le temps d’exécution.
  - `matplotlib` (optionnel) pour la visualisation des temps d’exécution sous forme de graphique.

## Installation

Pour exécuter ce projet, assurez-vous d'avoir Python installé sur votre machine. Ensuite, clonez le dépôt et installez les bibliothèques nécessaires :

```bash
git clone <URL_DU_DEPOT>
cd <NOM_DU_DOSSIER>
pip install -r requirements.txt
