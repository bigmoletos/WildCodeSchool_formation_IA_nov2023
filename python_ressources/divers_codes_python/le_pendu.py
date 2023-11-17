#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

NBRE_ESSAIS_MAX = 10
mot_mystere = "rouge"

def presentation():
    print ("\n*** Le jeu du pendu *** \n")
    print ("Trouver le mot mystere en", NBRE_ESSAIS_MAX, "coups\n")
 
def entree_utilisateur():
    """ vérifie la validité de la réponse faite par l'utilisateur """
    ok = False
    while ok == False:
        r = raw_input()
        if r.isalpha():
            ok = True
            return r.upper()
 
def is_lettre_in_mot_mystere(lettre, mot_a_trouver):
    """ vérifie si la lettre est reprise dans le mot mystere """
    if lettre in mot_a_trouver.upper():
        return True
    else:
        return False
 
def menu_quitter():
    print ("\n\n1. Continuer...")
    print ("\n2. Quitter...")
    while 1:
        q = raw_input("\nFaites votre choix: ")
        if q.isdigit():
            if q == '2':
                return True
            if q == '1':
                return False
 
def main():
    quitter = False
    while quitter == False:
        compteur = 0
        # titres d'acceuil
        presentation()
        # mot_tmp est la nouvelle chaine
        mot_tmp = len(mot_mystere) * '*'
        # transformation en tableau
        tab = list(mot_tmp)
        # boucle tant qu'on a pas trouvé
        while mot_mystere.upper() != mot_tmp:
            # seulement si le nombre d'essais autorisés n'est pas atteint
            if compteur < NBRE_ESSAIS_MAX:
                # affiche l'évolution de la recherche
                print ("mot mystere: "+ mot_tmp)
                # demande l'entrée de l'utilisateur
                print ("\nEntrez une lettre: ")
                lettre = entree_utilisateur()
                # si la lettre est dans le mot
                if is_lettre_in_mot_mystere(lettre, mot_mystere):
                    # on parcourt tout le mot
                    i = 0
                    for c in mot_mystere.upper():
                        # si il y a correspondance de lettre
                        if c == lettre:
                            # on écris la lettre au bon emplacement dans le tableau
                            tab[i] = lettre
                        i += 1
                    # réinitialisation de la string mot_tmp
                    mot_tmp = ''
                    # on retransforme le tableau en string
                    for c in tab:
                        mot_tmp += c
                else:
                    # la lettre n'est pas dans le mot
                    compteur += 1
                # quand le mot mystère est trouvé
                if mot_mystere.upper() == mot_tmp:
                    print ("\nBravo ! Vous avez trouve le mot mystere !")
                    print ("\nVous avez", compteur, "mauvais essais")
            else:
                print ("Vous n'avez pas trouve le mot mystere en", NBRE_ESSAIS_MAX, "coups")
                break
        # quand on a trouvé le mot ou que le nombre d'essais est atteint
        if menu_quitter():
            print ("\n\nFin du programme. \nMerci pour votre visite\n")
            quitter = True
 
    return 0
 
if __name__ == '__main__': main()
