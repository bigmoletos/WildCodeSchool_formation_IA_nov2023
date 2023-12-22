"""module fournissant des fonctions sur les dates"""
from datetime import datetime
import locale


def date_du_jour_long():
    """donne la date du jour au format long"""
    # Définir la locale sur le français
    locale.setlocale(locale.LC_TIME, 'french')

    # Obtenir la date et l'heure actuelles
    maintenant = datetime.now()

    # Formater la date et l'heure
    date_formatee = maintenant.strftime('%A %d %B %Y à %Hh%M')

    return date_formatee


def date_du_jour_court():
    """donne la date du jour au format court"""
    # Obtenir la date actuelle
    maintenant = datetime.now()

    # Formater la date
    date_formatee = maintenant.strftime('%d-%m-%Y')

    return date_formatee


print(date_du_jour_court())


def intervalle_entre_dates(date1, date2):
    """calcul l'intevalle entre 2 dates"""
    # Convertir les chaînes de caractères en dates
    date1 = datetime.strptime(date1, '%d-%m-%Y')
    date2 = datetime.strptime(date2, '%d-%m-%Y')

    # Calculer l'intervalle
    intervalle = date2 - date1

    return intervalle.days


# Exemple d'utilisation :
jours = intervalle_entre_dates('13-10-2023', '20-10-2023')
print("Il y a ", jours, " jours entre ces deux dates.")


def intervalle_entre_heures(heure1, heure2):
    """calcul l'intervalle entre 2 heures"""
    # Format de l'heure
    format_heure = '%H:%M:%S.%f'

    try:
        # Convertir les chaînes de caractères en heures
        heure1 = datetime.strptime(heure1, format_heure)
        heure2 = datetime.strptime(heure2, format_heure)

        # Calculer l'intervalle
        intervalle = abs(heure2 - heure1)

        # Extraire les années, mois, jours, heures, minutes, secondes et millisecondes
        annees = intervalle.days // 365
        mois = (intervalle.days % 365) // 30
        jours = (intervalle.days % 365) % 30
        heures = intervalle.seconds // 3600
        minutes = (intervalle.seconds % 3600) // 60
        secondes = (intervalle.seconds % 3600) % 60
        millisecondes = intervalle.microseconds // 1000

        # Formater l'intervalle
        intervalle_formate = f"{annees} années {mois} mois {jours} jours {heures} heures {
            minutes} minutes {secondes} secondes {millisecondes} millisecondes"

        return intervalle_formate

    except ValueError:
        return "Erreur : le format de l'heure doit être 'HH:MM:SS.ssssss'"


# Exemple d'utilisation :
print(intervalle_entre_heures('12:34:56.789012', '13:14:15.161718'))
