from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd

# Créer une nouvelle instance de navigateur
driver = webdriver.Firefox()  # ou webdriver.Chrome(), selon votre navigateur

# Aller à la page web
url = "https://www.wunderground.com/dashboard/pws/IPROVENC35/table/2023-12-14/2023-12-14/daily"
driver.get(url)

# Attendre que la page soit complètement chargée
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'table')))

# Récupérer le tableau avec les données météo
table = driver.find_element_by_tag_name('table')

# Utiliser pandas pour lire le tableau HTML
df = pd.read_html(table.get_attribute('outerHTML'))[0]

# Afficher le DataFrame
print(df)

# Fermer le navigateur
driver.quit()
