
quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre.", "    encore des espaces   ", "HELLO KSS"
]

characters = [
    "alvin et les Chipmunks", 
    "Babar", 
    "betty boop", 
    "calimero", 
    "casper", 
    "le chat potté", 
    "Kirikou"
]
user_answer=user_answer = input('Tapez entrée pour découvrir une autre citation ou D pour quitter le programme:')

if user_answer == "B":
    print("B...")
elif user_answer == "C":
    print("C pas la bonne réponse ! Et G pas d’humour, je C...")
elif user_answer == "D":
    pass
else:
    print("si c'est ni C ni B, ben alors c'est quoi?")

def get_random_item_in(my_list):
    # TODO: get a random number
    item = my_list[0] # get a quote from a list
    print(item) # show the quote in the interpreter
    return "program is over" # returned value


while user_answer != "D":
    print(get_random_item_in(quotes))
    user_answer = "D"

for quotes in quotes:
    quotes.capitalize()
    quotes[2].strip()
    quotes[0].upper()
    quotes[3].lower()
    print(quotes)    

"{character} a dit : {quote}".format(character="franck", quote="Tout n'est pas cirrhose dans la vie, comme dit l'alcoolique")

qote=[0, 1, 2, 3, 4, 5, 6]
type(qote)
print(qote[2])
qote.index(6)
print(qote)
qote.append(7)
print(qote)
qote.insert(3,0)
print(qote)
qote[8]="huit"
print(qote)

qote.pop(8)
print(qote)


qote.remove(4)
print(qote)

len(quotes)

import turtle
# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()

