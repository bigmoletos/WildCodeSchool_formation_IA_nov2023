

# """
# Help for statisticians!
# Your fellow statisticians need you. They want to learn
# how to program in Python and have tons of calculations to do.

# Very kindly, you agree to help them. Complete the missions below.

# For all functions below, please add an extra cell where you
# actually call the function on at least two different inputs
# and displays the returned value (if the function doesn't
# already display stuff).
# """

# # Mission 9: Create a function that takes a day as a parameter and returns the next day (i.e. for Sunday it would return Monday).
# # You can use lists or dictionaries to solve this.

# def get_next_day(your_day):
#     list_days=["monday","thuesday","wednesday","thursday","friday","saturday","sunday"]
#     next_days=""
#     french_langage=False
#     english_days,french_days=traduire_jour(your_day)
#     # print("french:",french_days)
#     # print("english:",english_days)
#     if your_day.lower() in list_days: #si jour en anglais
#         index_day = list_days.index(your_day.lower())
#     elif english_days in list_days: #si jour en francais
#         index_day = list_days.index(english_days)
#         french_langage=True
#         # print("index_day:",index_day)
#         # nextday = (nextday + 1) % 7  #autre solution avec le modulo7 si on arrive à 6-> 6+1=7 7%7=0
#     # print("index_next_day:",index_nextday)
#     else :
#         print("Votre saisie ne correspond pas à un jour de la semaine ")
#         return

#     index_nextday =(index_day + 1) if not (index_day + 1)==7 else 0
#     if french_langage:
#         next_days=list_days[index_nextday]
#         english_days,french_days=traduire_jour(next_days)
#         next_days=french_days
#         # print("nextdays french",next_days)
#     else:
#         next_days=list_days[index_nextday]
#         # print("nextdays gb",next_days)


#     return next_days


# def traduire_jour(jour):
#     jours = {
#         "lundi": "monday",
#         "mardi": "tuesday",
#         "mercredi": "wednesday",
#         "jeudi": "thursday",
#         "vendredi": "friday",
#         "samedi": "saturday",
#         "dimanche": "sunday"
#     }

#     jours_inverse = {v: k for k, v in jours.items()}  # Crée un dictionnaire inversé
#     # print("traduire 1  :        ",jours.get(jour.lower()))
#     # print("traduire 2  :        ",jours_inverse.get("sunday"))
#     english_days=jours.get(jour.lower())
#     french_days=jours_inverse.get(jour.lower())
#     return english_days,french_days

# #  autre possibilité avec une table de correspondance
# def get_next_day2(your_day):
#     days = {
#         "lundi": "mardi",
#         "mardi": "mercredi",
#         "mercredi": "jeudi",
#         "jeudi": "vendredi",
#         "vendredi": "samedi",
#         "samedi": "dimanche",
#         "dimanche": "lundi",
#         "monday": "tuesday",
#         "tuesday": "wednesday",
#         "wednesday": "thursday",
#         "thursday": "friday",
#         "friday": "saturday",
#         "saturday": "sunday",
#         "sunday": "monday"
#     }
#     return days.get(your_day.lower())
###########################
# # test de la fonction
# if __name__ == '__main__':
#     your_day1="dimanche"
#     your_day2="monday"
#     print("the next days is: ", get_next_day(your_day1))
#     print("the next days is: ", get_next_day(your_day2))

###############################################################################
"""
Mission 10: Create a function that fills an empty list with values (words) from the following string :

# "After twelve soft showers are the arch-duchess' socks dry, arch-dry?"
"""

# def transform_sentence_in_words_list(sentence):
#     list_words=[]
#     # list_words = re.sub(r'[^\w\s]', '', sentence).split() # autre solution on ne garde que les lettres
#     # Ou utilisation de translate et maketrans pour remplacer la ponctuation par des espaces vides
#     table = str.maketrans(",", " ", "'?!.:")
#     list_words =sentence.translate(table).split()
#     # list_words=sentence.replace(",", "").replace("'", "").replace("?", "").split(" ")
#     return list_words


###########################
# # test de la fonction
# if __name__ == '__main__':
#     my_sentence="After twelve soft showers are the arch-duchess' socks dry, arch-dry?"
#     name_function=transform_sentence_in_words_list( my_sentence)
#     message=f"Resultat fonction "
#     print(message,name_function)

###############################################################################


"""
    # Mission 11: Create a function that that takes a string as input, converts all characters to lowercase, and returns a new string where
# every vowel at an even index is capitalized, keeping all other characters unchanged.
# Example: antithetical -> AntithEtIcAl
# Example: marvelously -> marvElOuslY
"""
def change_vowels(your_word):
    # list_vowels=[]
    voyelles = 'aeiouyéèêëàâôûùïîüÿ'
    your_word=list(your_word.lower())
    for index,letter in enumerate(your_word):
        if index%2 ==0 and letter in voyelles:
            your_word[index]=letter.upper()
    your_word="".join(your_word)
    return your_word

###########################
# test de la fonction
if __name__ == '__main__':
    your_word="antithetical"
    your_word2="marvelously"

    name_function=change_vowels( your_word)
    name_function2=change_vowels( your_word2)
    message=f"Resultat fonction "

    print(message,name_function)
    print(message,name_function2)

###############################################################################

"""
    # Mission 12: Create a function that takes a number n as parameter, and then returns a list containing n lists, each containing n empty lists.
"""
def create_list(size_of_list):
    
    return
###########################
# test de la fonction
if __name__ == '__main__':
    size_of_list=4
    size_of_list2=5

    name_function=create_list(size_of_list)
    name_function2=create_list(size_of_list2)
    message=f"Resultat fonction "

    print(message,name_function)
    print(message,name_function2)
###############################################################################
"""
    # Mission 13: Create a function that takes two inputs, their year of birth and first name.
# Convert the year of birth into an int and subtract it from the current year (you can do it using a certain module :-P).
# Then display the message: Hello [first name], today you are (or you will be this year) [age] years old.
# When testing the function, ask the user for the parameters!

"""


###########################
# test de la fonction
if __name__ == '__main__':
    your_word="antithetical"
    your_word2="marvelously"

    name_function=change_vowels( your_word)
    name_function2=change_vowels( your_word2)
    message=f"Resultat fonction "

    print(message,name_function)
    print(message,name_function2)
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################




# def next_day(day):
#     days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#     try:
#         current_day_index = days_of_week.index(day)
#         next_day_index = (current_day_index + 1) % 7
#         return days_of_week[next_day_index]
#     except ValueError:
#         return "Invalid day. Please enter a valid day of the week."

# # Test the function
# print(next_day('Sunday'))  # Output: Monday
