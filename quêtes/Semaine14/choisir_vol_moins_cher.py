import requests
from datetime import datetime, timedelta

# Définition des variables
date_depart = datetime.today() + timedelta(days=5)
date_retour = date_depart + timedelta(days=7)
heures_depart = {"min": "07:30", "max": "20:00"}
heures_arrivee = {"min": "07:30", "max": "22:00"}
nombre_passagers = 2
budget_par_personne = 60

# Fonction pour formater la date
def formater_date(date):
    return date.strftime("%Y-%m-%d")

# Fonction pour rechercher les vols
def rechercher_vols(origine, destination, date_depart, date_retour, heures_depart, heures_arrivee, nombre_passagers, budget_par_personne):
    url = "https://www.skyscanner.fr/api/v1/flights"
    params = {
        # "apiKey": "YOUR_API_KEY",
        "country": "FR",
        "currency": "EUR",
        "locale": "fr-FR",
        "origin": origine,
        "destination": destination,
        "outboundpartialdate": formater_date(date_depart),
        "inboundpartialdate": formater_date(date_retour),
        "adults": nombre_passagers,
        "children": 0,
        "infants": 0,
        "cabinclass": "economy",
        "rtn": "true",
        "preferdirects": "false",
        "stops": "0",
        "maxprice": budget_par_personne * 2,
        "outbounddeparturetime": heures_depart["min"] + "-" + heures_depart["max"],
        "inboundarrivaltime": heures_arrivee["min"] + "-" + heures_arrivee["max"],
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        try:
            data = response.json()
            # Traiter les données des vols
            for vol in data["results"]:
                print(f"Compagnie aérienne: {vol['airline']}")
                print(f"Départ: {vol['outbound']['departure']['date']} {vol['outbound']['departure']['time']}")
                print(f"Arrivée: {vol['inbound']['arrival']['date']} {vol['inbound']['arrival']['time']}")
                print(f"Durée: {vol['duration']} minutes")
                print(f"Prix: {vol['price']} €")
                print("-" * 20)
        except ValueError:
            print("Erreur : La réponse de l'API n'est pas un JSON valide.")
    else:
        print(f"Une erreur est survenue lors de la recherche des vols. Code d'erreur : {response.status_code}")

# Recherche des vols
rechercher_vols("MRS", "ALC", date_depart, date_retour, heures_depart, heures_arrivee, nombre_passagers, budget_par_personne)




