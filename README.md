# Jeu Scrabble en Python avec Tkinter

Ce projet est un jeu de Scrabble simplifié développé en Python utilisant la bibliothèque Tkinter pour l'interface graphique.

## Fonctionnalités

- Affichage de 7 lettres aléatoires pour former un mot.
- Validation du mot formé avec un correcteur orthographique en français (module `pyspellchecker`).
- Calcul du score en fonction des lettres utilisées.
- Timer de 60 secondes pour chaque partie.
- Boutons pour ajouter des lettres, valider le mot, effacer la dernière lettre, et rejouer.

## Programmation Orientée Objet (POO)

Ce projet utilise la programmation orientée objet (POO) pour organiser le code de manière claire et modulaire.

- **Classe principale `ScrabbleGame`** :  
  Cette classe contient tous les attributs et méthodes nécessaires pour gérer le jeu, comme l’affichage des lettres, la gestion des actions de l’utilisateur, la validation du mot, le calcul du score, et le timer.

- **Encapsulation** :  
  Toutes les variables d’état du jeu (lettres sélectionnées, score, temps restant, etc.) sont encapsulées dans l’objet `ScrabbleGame`. Cela permet de maintenir un état cohérent et de simplifier la maintenance.

- **Méthodes de classe** :  
  Les fonctionnalités du jeu (ajouter une lettre, valider le mot, démarrer un nouveau jeu, etc.) sont implémentées sous forme de méthodes, ce qui permet de réutiliser et organiser le code efficacement.

- **Instanciation** :  
  Le jeu est représenté par une instance de la classe `ScrabbleGame`. Cela permet de créer et manipuler plusieurs parties indépendantes si besoin.

L’utilisation de la POO rend le code plus modulaire, maintenable, et facilite l’extension future du projet.

## Prérequis

- Python 3.x
- Modules Python nécessaires :
  - `tkinter` (inclus par défaut dans Python)
  - `pyspellchecker`
  - `unicodedata` (module standard Python)

Pour installer `pyspellchecker` :

```bash
pip install pyspellchecker
