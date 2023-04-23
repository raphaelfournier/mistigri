# Mistigri

Le mistigri est un jeu de cartes, qui a de nombreux noms, comme le
[Pouilleux](https://fr.wikipedia.org/wiki/Pouilleux). Dans sa variante pour
enfants, il se joue avec 41 cartes (20 paires et une carte seule). On peut y
jouer avec un jeu classique de 52 cartes, le valet de trèfle étant écarté.

Ce programme propose de dérouler ce jeu et d'examiner le nombre de tours
nécessaires pour qu'une partie se termine.

## Aide 

    python jeu.py --help
    
Variables :

- joueurs : nombre de joueurs
- paires : nombre de cartes (50 pour un jeu traditionnel et jouer avec 51 cartes, 20 par défaut)
- first : pour que le premier joueur ne soit pas le joueur 0
- outfile : fichier de sortie
- verbosité : -v pour dérouler les étapes du jeu.

## Notebook

Un notebook exécute `N` parties et affiche la distribution des nombres de tours
joués. Il serait intéressant de faire un calcul formel de cette espérance, il
semble y avoir une gaussienne…

## Autres ressources

Il y a sur [ce
site](http://lostmathlessons.blogspot.com/2016/12/old-maid.html?m=1) des calculs
mathématiques autour du jeu (mais pas forcément sur la durée de la partie).
