import random
from collections import OrderedDict
import collections
import argparse
from mistigri import Tas, Carte, Joueur

parser = argparse.ArgumentParser(
    description='Simulons des parties de Mistigri', 
    epilog="Bonnes parties !"
)
parser.add_argument('-j', '--joueurs', default=3)
parser.add_argument('-p', '--paires', default=20)
parser.add_argument('-f', '--first', help="first player, default=0", default=0)
parser.add_argument('-o', '--outfile', help="out file, default=outfile.csv", default="outfile.csv")
parser.add_argument('--verbose', '-v', action='count', default=0)
args = parser.parse_args()

nb_joueurs = int(args.joueurs)
nb_cartes = int(args.paires)

mistigri = Tas(nb_cartes)
mistigri.creerJeu()

# Préparation du jeu

joueurs = OrderedDict()
listeJoueurs = []

for i in range(nb_joueurs):
    nom = "Joueur" + str(i)
    listeJoueurs.append(nom)
    joueurs[nom]=Joueur(nom)

def distribuerCartes(tas, joueurs):
    items = list(joueurs.items())
    jouCour = 0
    while len(tas.cartes) >0:
        carte = tas.cartes.pop()
        index = items[jouCour]
        joueurs[items[jouCour][0]].jeu.append(carte)
        jouCour += 1
        jouCour = jouCour % len(joueurs)

def eliminerPaires(jeu, verb=1):
    vus = []
    doubles = []
    for carte in jeu:
        if carte.valeur in vus:
            doubles.append(carte.valeur)
        else:
            vus.append(carte.valeur)
    if args.verbose > 1:
        if not doubles:
            print("pas de paires")
        else:
            print("liste des paire(s) :",doubles)
    jeu = [ carte for carte in jeu if carte.valeur not in doubles]
    return jeu

def tirerCarte(destinataire, source):
    if args.verbose > 0:
        print("   ",destinataire.nom, "tire chez",source.nom, source.jeu)
    x = random.randint(0,len(source.jeu)-1)
    if args.verbose > 1:
        print("  avant tirage")
        print(destinataire.nom,destinataire.jeu)
        print(source.nom,source.jeu)
    if args.verbose > 0:
        print("   ",destinataire.nom,"tire",source.jeu[x].valeur)
    destinataire.jeu.append(source.jeu.pop(x))
    if args.verbose > 1:
        print("  après tirage")
        print(destinataire.nom,destinataire.jeu)
        print(source.nom,source.jeu)


if args.verbose > 0:
    print("Distribution...")

distribuerCartes(mistigri, joueurs)

if args.verbose > 0:
    print("après distribution")

for nom,joueur in joueurs.items():
    if args.verbose > 0:
        print("   "+nom, joueur.jeu)
    if args.verbose > 1:
        print("éliminons les paires")
    joueur.jeu = eliminerPaires(joueur.jeu)
    if args.verbose > 0:
        print("   "+nom, joueur.jeu)
        print()

# Déroulement du jeu
if args.verbose > 0:
    print("Début du jeu")

tour = 0
joueurCourant = 0

while True:
    nomJ = listeJoueurs[joueurCourant]
    if args.verbose > 0:
        print("tour de "+nomJ)
        print("   ",joueurs[nomJ].jeu)
    if joueurCourant+1 >= len(listeJoueurs):
        nextJ = listeJoueurs[0]
    else:
        nextJ = listeJoueurs[joueurCourant+1]

    tirerCarte(joueurs[nomJ],joueurs[nextJ])
    joueurs[nomJ].jeu = eliminerPaires(joueurs[nomJ].jeu)
    if args.verbose > 0:
        # print("    après paires")
        print("   ",joueurs[nomJ].jeu)

    if len(joueurs[nomJ].jeu) == 0:
        if args.verbose > 0:
            print(nomJ,"a fini !")
        del joueurs[nomJ]
        listeJoueurs.remove(nomJ)

    if len(joueurs[nextJ].jeu) == 0:
        if args.verbose > 0:
            print(nextJ,"a fini !")
        del joueurs[nextJ]
        listeJoueurs.remove(nextJ)

    if len(joueurs) == 1:
        if args.verbose > 0:
            print()
            print("Reste un seul joueur, fin du jeu")
            joueur = list(joueurs.keys())[0]
            print(joueur,"a perdu\n======\n")
        # print("Tours joués",tour, tour/nb_joueurs)
        print(tour) # seule ligne affichée à la fin
        if args.outfile:
            with open(args.outfile, "w") as file:
                file.write(str(tour))
        break

    joueurCourant += 1
    joueurCourant = joueurCourant % len(joueurs)
    tour += 1
    if args.verbose > 0:
        print()
