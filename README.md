# Visualisateur Avancé de la Suite de Fibonacci

## Description

Ce programme propose une interface graphique avancée développée avec Tkinter, permettant de calculer la suite de Fibonacci à l'aide de trois méthodes différentes. L'application fournit une visualisation claire des temps d'exécution, ainsi que des résultats détaillés pour chaque méthode.

## 🖥️ Fonctionnalités Principales

- **Saisie du Numéro de Terme :** Entrez le numéro du terme de Fibonacci que vous souhaitez calculer.
- **Calcul Simultané :** Exécution des trois méthodes (récursive, récursive avec programmation dynamique et itérative) en parallèle.
- **Visualisation Graphique :** Affichage des temps d'exécution sous forme de graphiques attractifs.
- **Tableau des Résultats :** Détails des résultats pour chaque méthode, avec des temps d'exécution clairs.

## 📊 Visualisation

- **Graphique à Barres :** Comparaison visuelle des temps d'exécution des trois méthodes.
- **Étiquettes Précises :** Affichage des temps d'exécution exacts sur chaque barre du graphique.
- **Tableau Récapitulatif :** Présentation des résultats de manière structurée.

## ⚠️ Points Importants

- **Gestion des Erreurs :** Prise en compte des erreurs, notamment le dépassement de pile pour la méthode récursive.
- **Interface Responsive :** Adaptée pour différents formats d'écran, garantissant une utilisation facile.
- **Style Moderne :** Conception esthétique et lisible pour améliorer l'expérience utilisateur.

## Prérequis

Pour exécuter ce script, assurez-vous d'avoir installé :

- **Python 3.x**
- **Bibliothèques :**
  - `tkinter` (inclus avec Python)
  - `matplotlib` (à installer)

Vous pouvez installer `matplotlib` avec la commande suivante :

```bash
pip install matplotlib
```

## Utilisation

1.Lancez le script Python.
2.Entrez un nombre (recommandé : entre 10 et 35).
3.Cliquez sur le bouton "Calculer".

## Limitations

-Pour des valeurs de n supérieures à 35-40, la méthode récursive devient très lente, voire impraticable.
-Les graphiques sont conçus principalement pour illustrer les temps d'exécution.

## 🔍 Modifications Principales de la Version 2

=>Mesures de Temps Améliorées :

  -Utilisation de timeit pour des mesures plus précises.
  -Possibilité de définir le nombre d'exécutions.
  -Calcul du temps moyen par exécution.

=>Visualisation Améliorée :

  -Échelle logarithmique pour mettre en lumière les différences de performance.
  -Coloration des barres dans le graphique pour une meilleure lisibilité.
  -Étiquettes précises sur les temps d'exécution.
  
=>Fonctionnalités Supplémentaires :

  -Champ pour définir le nombre d'exécutions favorisant des analyses plus détaillées.
  -Gestion des méthodes non applicables (notamment pour les cas de la méthode récursive avec des valeurs de n élevées).

## 💡 Conseils d'Utilisation

-Pour des valeurs de n faibles (10-20), envisagez d'augmenter le nombre d'exécutions (1000-10000) pour des mesures plus représentatives.
-Pour des valeurs de n plus élevées (30-35), réduisez le nombre d’exécutions pour éviter des temps d'attente excessifs.

## 🔍 Détails Techniques
-Récursive : Complexité O(2^n), ce qui la rend très lente pour des valeurs élevées.
-Dynamique : Complexité O(n), offrant des performances rapides et efficaces.
-Itératif : Complexité O(n), très rapide avec un faible usage mémoire.
