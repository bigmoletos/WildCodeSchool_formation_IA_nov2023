import requests
import pandas as pd
from bs4 import BeautifulSoup

# Faire une requête GET à l'URL de la page web
url = "https://www.wunderground.com/dashboard/pws/IPROVENC35/table/2023-12-14/2023-12-14/daily"
response = requests.get(url)

# Créer un objet BeautifulSoup à partir du contenu HTML de la réponse
soup = BeautifulSoup(response.content, "html.parser")

# Trouver le tableau qui contient les données météo
table = soup.find(
    "table", class_="history-table desktop-table")

# Convertir le tableau en un objet DataFrame de pandas
df = pd.read_html(str(table))[0]

# Afficher ou sauvegarder le DataFrame
print(df)
# df.to_csv("weather_data.csv")

ptt
