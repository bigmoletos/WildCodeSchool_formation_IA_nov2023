#quiz
#https://openclassrooms.com/fr/courses/4262331-demarrez-votre-projet-avec-python/4263931-rangez-des-donnees-dans-des-listes
#documentation
#https://docs.python.org/3.5/tutorial/datastructures.html
characters=["titi","gros minet","peggy",'Mowgli','ratz']
print (characters)
characters.remove("peggy")
print (characters)
characters.append("fleche bleue")
print (characters)
characters=[x if x=='Mowgli' else x=='balou' for x in characters]
#characters[4] = "Balou"
print (characters)
def replace_(characters,old,new):
    for idx, i in enumerate(characters):
             if i == old:
                     characters[idx] = new
replace_(characters, 'Mowgli', 'balou')
print (characters)

characters=["mowgli", "titi", "superman","goldorak",'spiderman']
print(characters)
characters.remove("spiderman")
print(characters)
characters.insert(2,"rahan")
print(characters)
characters.append("blanche")
print(characters)
characters.pop(4)
print(characters)
print(characters)
characters.count("titi")
print(characters)
characters.sort()
print(characters)
print(len(characters))
print(characters)
characters.reverse()
print(characters)
["balou" for x in characters if x =="titi"]
print(characters)
print("ligne 22",["baloou" if x =="titi" else x for x in characters ])
characters=["baloou" if x =="titi" else x for x in characters ]
print(characters)
#characters=["mowgli", "titi", "superman","goldorak",'spiderman']
print(characters)
del characters[2:4]
print(characters)
characters.insert(2,"mowgli")
print(characters)
#utilisation de set
a = set('abracadabra')
b=set('almagtr')
print("a-b:" ,a-b)
print("a^b:" ,a^b)
print("a|b:" ,a|b)
print("a&b:" ,a&b)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# What is your name?  It is lancelot.
# What is your quest?  It is the holy grail.
# What is your favorite color?  It is blue

a = {x for x in 'abracadabra' if x not in 'abc'}
print ("trie les lettres ne sont pas (abc) daans le dictionnaire 'abracadabra",a)

print("{} a dit : {}".format("Babar", "Tout n'est pas cirrhose dans la vie, comme dit l'alcoolique."))