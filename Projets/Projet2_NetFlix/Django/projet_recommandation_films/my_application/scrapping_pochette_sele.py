import os
import requests
from PIL import Image
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def get_movie_poster(tconst):
    # Chemin d'accès pour vérifier si l'image existe déjà
    image_path_webp = f'static/images/pochettes/{tconst}.webp'

    # Vérifier si l'image existe déjà
    if os.path.exists(image_path_webp):
        print(f"L'image pour {tconst} existe déjà.")
        return image_path_webp

    print("Démarrage de WebDriver...")
    options = Options()
    options.headless = True  # Exécution en mode sans tête, sans interface utilisateur.
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        base_url = f"https://www.imdb.com/title/{tconst}/mediaviewer/"
        print(f"Accès à l'URL de base : {base_url}")
        driver.get(base_url)

        # Attendre l'élément image en utilisant WebDriverWait
        print("Attente de l'élément image sur la page...")
        wait = WebDriverWait(driver, 10)
        poster_img = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "img[src*='mediaviewer']")))

        # Extraire l'identifiant de l'image et compléter l'URL
        img_id = poster_img.get_attribute("src").split("/")[-2]
        final_url = f"{base_url}{img_id}/"
        print(f"URL finale de l'image : {final_url}")

        # Télécharger l'image
        print("Téléchargement de l'image...")
        response = requests.get(final_url)
        if response.status_code == 200:
            # Convertir l'image en webp et la sauvegarder
            print("Conversion et sauvegarde de l'image en format webp...")
            image = Image.open(BytesIO(response.content))
            image.save(image_path_webp, 'webp')
            print(f"Image sauvegardée : {image_path_webp}")
            return image_path_webp

    except Exception as e:
        print(f"Erreur lors du scrapping de l'image avec Selenium : {e}")
    finally:
        print("Fermeture de WebDriver...")
        driver.quit()  # S'assurer de fermer le pilote pour libérer des ressources

    return None  # Retourner None si aucune image appropriée n'est trouvée ou en cas d'erreur

# Tester la fonction
print(get_movie_poster('tt0084555'))
