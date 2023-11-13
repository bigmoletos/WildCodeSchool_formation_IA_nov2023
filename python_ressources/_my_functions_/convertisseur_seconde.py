# ecrire un programme qui transforme les secondes en années mois jour heure minutes seconde
# input en seconde
nombre_seconde = int(input("veuillez saisir un chiffre entier de secondes:  "))
initial = nombre_seconde
# 1 mois = 30,416j, 1 années=365 j, 1jour 24h, 1heure 60minute 1 minute 60s
minute = 60
heure = 60*minute
jour = 24*heure
mois = 30*jour
annee = 12*mois

# calcul du qutotient entier des années par //
year_in_nombre = nombre_seconde//annee
# on prend le reste des secondes avec le modulo %
nombre_seconde %= annee
# calcul du qutotient entier des mois par //
month_in_nombre = nombre_seconde//mois
# on prend le reste des secondes avec le modulo %
nombre_seconde %= mois
# calcul du qutotient entier des jour par //
days_in_nombre = nombre_seconde//jour
# on prend le reste des secondes avec le modulo %
nombre_seconde %= jour
# calcul du qutotient entier des heure par //
heures_in_nombre = nombre_seconde//heure
# on prend le reste des secondes avec le modulo %
nombre_seconde %= heure
# calcul du qutotient entier des minutes par //
minutes_in_nombre = nombre_seconde//minute
# on prend le reste des secondes avec le modulo %
nombre_seconde %= minute
# on arrondit les secondes restantes à 2 chiffres
nombre_seconde = round(nombre_seconde, 2)
seconde_in_nombre = nombre_seconde
# econdes_in_nombre=nombre_seconde//

print(f" avec  {initial} secondes on obtient {year_in_nombre} années {month_in_nombre} mois {
      heures_in_nombre} jour {minutes_in_nombre} minutes {seconde_in_nombre} secondes")


# autre possibilité avec les boucles
while True:
    while True:
        if (nombre_seconde -60)>0:
            nombre_seconde=nombre_seconde -60
            minute+=1
        else:
            break
    while True:
        if (minute -60)>0:
            minute=minute -60
            heure+=1
        else:
            break
    while True:
        if (heure -24)>0:
            heure=heure - 24
            jour+=1
        else:
            break
    break


print(f" il y a {heure} heure , {minute} min  , {nombre_seconde} seconde")