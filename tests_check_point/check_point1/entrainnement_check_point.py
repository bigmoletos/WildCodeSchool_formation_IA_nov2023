# rendre monnaie


def rendre_monnaie(montant_achat, somme_payee):
    monnaie_a_rendre = []
    message = ""

    liste_billets = [500, 200, 100, 50, 20, 10, 5]
    liste_pieces = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    somme_rendre = somme_payee-montant_achat
    print(f"Avec une facture de {montant_achat:.2f} €, si on vous donne {
          somme_payee:.2f} € vous devez rendre {somme_rendre:.2f} €\n")
    if somme_rendre > 0:
        print("Voici combien de billets et de pieces vous devez rendre au client:")
        for billet in liste_billets:
            # message= "billet de: "
            while somme_rendre >= billet:
                monnaie_a_rendre.append(billet)
                somme_rendre -= billet
                message += "billet de: " + str(billet)+"€\n "
        for piece in liste_pieces:
            # message = "pieces de: "
            while somme_rendre >= piece:
                monnaie_a_rendre.append(piece)
                somme_rendre -= piece
                message += "pieces de: " + str(piece) + "€\n "

    # message += message_billet+message_piece+"\n"
    # for monnaie in monnaie_a_rendre:
    #     message += message_billet+message_piece+str(monnaie)+"\n"

    return message


# test fonction
montant_facture = 1250.56
somme_donnee = 2000

print(rendre_monnaie(montant_facture, somme_donnee))


# **Programmation orientée objet**

# Il t'est demandé de créer une nouvelle classe "sentence" qui va hériter de l'ensemble des méthodes de la classe "str" (*les chaines de caractères que tu connais bien en python*).

# Tu devras ajouter une méthode .clean() qui nettoyera les espaces en début et en fin de chaine, mettra en majuscule le premier caractère, et tous les autres caractères en minuscule, et ajoutera un point "." à la fin.

# Tu montreras le résultats en appliquant la méthode à la phrase ci-dessous.
