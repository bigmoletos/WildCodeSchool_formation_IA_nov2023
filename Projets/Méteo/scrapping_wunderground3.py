import requests
from bs4 import BeautifulSoup

url = "https://www.wunderground.com/dashboard/pws/IPROVENC35/table/2023-12-14/2023-12-14/daily"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Trouver le tableau avec les données météo
table = soup.find(
    "table", class_="history-table desktop-table")

# Afficher le tableau
print(table)
