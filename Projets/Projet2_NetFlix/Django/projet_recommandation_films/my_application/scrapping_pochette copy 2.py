import os
import requests
from PIL import Image
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def get_movie_poster(tconst):
    options = Options()
    options.headless = True  # Run in headless mode, without a UI.
    driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    # Define the path to check if the image already exists
    image_path_webp = f'/static/images/pochettes/{tconst}.webp'
    # Si l'image est déja stockée inutile de la telecharger
    if os.path.exists(image_path_webp):
        print(f"Image for {tconst} already exists.")
        return image_path_webp
    try:
        url = f"https://www.imdb.com/title/{tconst}/mediaviewer/"
        driver.get(url)
        # Wait for the page to load, you can use WebDriverWait here to wait for a specific element to ensure the page has loaded
        driver.implicitly_wait(10) # This is not the best practice, it's better to use WebDriverWait
        # Find the image with 'mediaviewer' in the src attribute
        poster_imgs = driver.find_elements(By.CSS_SELECTOR, "img[src*='mediaviewer']")
        # Filter out any that start with the Amazon URL
        poster_img = next((img for img in poster_imgs if not img.get_attribute('src').startswith('https://m.media-amazon.com')), None)
        if poster_img:
            src = poster_img.get_attribute('src')
            # Download the image
            response = requests.get(src)
            if response.status_code == 200:
                # Convert the image to webp and save it
                image = Image.open(BytesIO(response.content))
                image.save(image_path_webp, 'webp')
                return image_path_webp


    except Exception as e:
        print(f"Erreur lors du scrapping de l'image avec Selenium: {e}")
    finally:
        driver.quit()  # Make sure to quit the driver to free up resources

    return None  # Return None if no proper poster is found or an error occurred


print(get_movie_poster_with_selenium('tt0084555'))
