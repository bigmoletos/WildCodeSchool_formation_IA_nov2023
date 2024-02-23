import random


def verifier_num_securite_sociale(numero):
    # Supprimer les espaces
    numero = numero.replace(" ", "")

    # Vérifier la longueur du numéro
    if len(numero) != 15:
        return False

    # Extraire la clé et le numéro sans la clé
    cle = int(numero[-2:])
    numero_sans_cle = numero[:-2]

    # Calculer la clé
    cle_calculee = 97 - (int(numero_sans_cle) % 97)
    # print(f"\nnumero_sans_cle :\n{numero_sans_cle} \n")
    # print(f"\ncle_calculee :\n{cle_calculee} \n")

    # Vérifier si la clé calculée correspond à la clé du numéro
    return cle == cle_calculee


# Test
# numero = "1 66 04 75 014 008 50"
# numero = "2 62 10 62 381 157 36"
numero = "1 66 04 38 40 04 22 16"
print(verifier_num_securite_sociale(numero))  # Doit afficher True ou False


def generer_numero_securite_sociale():
    # Générer un numéro sans la clé
    numero_sans_cle = "16604" + \
        "".join([str(random.randint(0, 9)) for _ in range(8)])

    # Calculer la clé
    cle = 97 - (int(numero_sans_cle) % 97)

    # Retourner le numéro complet
    return numero_sans_cle + str(cle)


# Générer une liste de numéros de sécurité sociale
liste_numeros = [generer_numero_securite_sociale() for _ in range(10)]

# Afficher la liste
for numero in liste_numeros:
    print(numero)
