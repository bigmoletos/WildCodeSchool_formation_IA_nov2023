import re


class Sentence:
    """
    Il t'est demandé de créer une nouvelle classe "sentence" qui va hériter de l'ensemble des méthodes de la classe "str" (*les chaines de caractères que tu connais bien en python*).
    Tu devras ajouter une méthode .clean() qui nettoyera les espaces en début et en fin de chaine, mettra en majuscule le premier caractère, et tous les autres caractères en minuscule, et ajoutera un point "." à la fin.

    Tu montreras le résultats en appliquant la méthode à la phrase ci-dessous.
"""

    def __init__(self, sentence):
        self.sentence = sentence

    def supprime_espace(self):
        # supprimes les espaces consecutifs supérieurs à 2
        self.sentence = re.sub(' +', ' ', self.sentence)
        # print(self.sentence)

    def clean(self):
        self.supprime_espace()
        sentence_clean = self.sentence

        liste_ponctuation = ["?", "!", ";", ".", ",", ":"]
        for ponctuation in liste_ponctuation:
            sentence_clean = sentence_clean.replace(ponctuation, "")
        # if sentence_clean[-1] != '.':
            # return sentence_clean + '.'
        sentence_clean = sentence_clean.strip().capitalize()
        sentence_clean += '.'
        return sentence_clean


# test de la fonction
def main():
    # numbers = [1, 2, 3]
    # création d'une liste de chiffres aleatoires
    # numbers = [random.randint(-5, 5) for _ in range(5)]
    # your_sentence = "   Hello world c'eSt Pas encore la fin du monDe    "
    your_sentence2 = "   Hello,   world    c'eSt!    Pas :  ?encore la fin du monDe    .   "
    instance_sentence = Sentence(your_sentence2)
    print(instance_sentence.clean())


if __name__ == '__main__':
    main()
