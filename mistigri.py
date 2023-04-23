import random

class Carte:
    """ carte du jeu"""

    def __init__(self, valeur):
        self.valeur = valeur

    def __str__(self):
        return self.valeur

    def __repr__(self):
        return str(self.valeur)

class Joueur:
    """joueur TODO"""

    def __init__(self, nom):
        self.nom = nom
        self.jeu = []

class Tas:
    """toutes les cartes du Mistigri"""

    def __init__(self, nbcartes):
        self.cartes = []
        self.nbcartes = nbcartes

    def eliminerPaires(jeu, verb=1):
        vus = []
        doubles = []
        for carte in jeu:
            if carte.valeur in vus:
                doubles.append(carte.valeur)
            else:
                vus.append(carte.valeur)
        # if not doubles:
        # print("pas de paires")
        # else:
        # print("paire(s)",doubles)
        jeu = [ carte for carte in jeu if carte.valeur not in doubles]
        return jeu

    def creerJeu(self):
        for i in range(self.nbcartes):
            self.cartes.append(Carte(i))
            self.cartes.append(Carte(i))
        self.cartes.append(Carte(self.nbcartes))
        random.shuffle(self.cartes)

    def distribuerCartes(self, joueurs):
        items = list(joueurs.items())
        jouCour = 0
        while len(self.cartes) >0:
            carte = self.cartes.pop()
            index = items[jouCour]
            joueurs[items[jouCour][0]].jeu.append(carte)
            jouCour += 1
            jouCour = jouCour % len(joueurs)

