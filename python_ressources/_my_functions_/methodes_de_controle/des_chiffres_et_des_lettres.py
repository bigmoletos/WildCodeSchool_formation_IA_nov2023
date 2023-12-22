"""
Pour cette mission, inspirée d'un jeu télévisé, tu vas essayer de résoudre le problème suivant: Tu dois combiner les variables avec des opérateurs mathématiques (*+-/) pour trouver le résultat 466.
Tu assigneras le résultat à la variable answer.
Attention, pour cette mission, chaque variable n'est utilisable qu'une seule fois.
"""
import itertools

def des_chiffres(nombres,resusltat_attendu):
    # Définir les nombres et les opérations
    # nombres = [12, 20, 15, 3, 30]
    # resultat_attendu=466
    operations = ['+', '-','*','/']
    liste_solutions=[]

    # Générer toutes les permutations possibles des nombres et des opérations
    for nombres_perm in itertools.permutations(nombres):
        for operations_perm in itertools.product(operations, repeat=len(nombres)-1):
            # Construire et évaluer l'expression
            expression = str(nombres_perm[0])
            for i in range(1, len(nombres)):
                expression += operations_perm[i-1] + str(nombres_perm[i])
            if eval(expression) == resultat_attendu:
                liste_solutions.append(expression)
                # print(f"Solution trouvée : {expression} = {resultat_attendu}")
    print(f"Solutions trouvées pour obtenir {resultat_attendu}\n {liste_solutions} ")
    return liste_solutions

# test
nombres = [12, 20, 15, 3, 30]
resultat_attendu=466

des_chiffres(nombres, resultat_attendu)