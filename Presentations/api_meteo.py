import requests
import json
from config import keys as k

"""
    créer une API  météorologiques en temps réel
    données météorologiques en temps réel:
    Météo-France
    OpenWeatherMap
    MeteoGroup

    formatage des données en  JSON ou XML.
    définition des paramètres de l'API, tels que les données qui seront accessibles et les méthodes HTTP qui seront utilisées pour les récupérer.

"""
api_key = k.get('API_KEY_OPEN_WEATHER_MAP1')
print("my key:", api_key)


def get_weather_data_API(ville, latitude, longitude, api_key):
    """
    Récupère les données météorologiques en temps réel pour une latitude et une longitude données.

    Args:
        latitude: La latitude du point d'intérêt.
        longitude: La longitude du point d'intérêt.

    Returns:
        Les données météorologiques en temps réel au format JSON.
    """
    # type d'extraction:
    type_extract = f"weather?lat={latitude}&lon={longitude}"
    type_extract = f"weather?q={ville}"
    type_extract = f"aggregated/year?q={ville}"

    # url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"
    url = f"https://api.openweathermap.org/data/2.5/{
        type_extract}&APPID={api_key}"
    # url = "https://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=a06c3654b45696b6e76c91f8825a9cad"
    # url = f"https://api.openweathermap.org/data/2.5/weather?q={
    #     ville}&APPID={api_key}"
    url = f"https://bulk.openweathermap.org/snapshot/hourly1h_zip_eu.csv.gz?appid={
        api_key}"
    url = f"https://bulk.openweathermap.org/snapshot/hourly1h_zip_eu.json.gz?appid={
        api_key}"
    print(url)
    # url = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(
    #     latitude, longitude, api_key
    # )
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data, indent=4))  # Affiche les données JSON formatées
        return data
    else:
        return None


if __name__ == "__main__":
    # Marseille
    my_ville = "marseille,fr"
    my_latitude = 43.3333
    my_longitude = 5.5
    # my_latitude = 43.2970
    # my_longitude = 5.3811
    # latitude = 43
    # longitude = 5
    api_key = "981a147a34913f83a580f46c324b97c7"  # api_key_stat_owm
    # api_key = "a06c3654b45696b6e76c91f8825a9cad"  # default
    weather_data = get_weather_data_API(
        my_ville, my_latitude, my_longitude, api_key)
    print(weather_data)
