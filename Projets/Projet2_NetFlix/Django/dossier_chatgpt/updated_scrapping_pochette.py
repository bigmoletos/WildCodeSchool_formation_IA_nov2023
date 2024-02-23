import requests
from bs4 import BeautifulSoup

# Utiliser un dictionnaire pour le cache des URLs des images
image_cache = {}

def get_movie_poster(tconst):
    # Vérifier si l'image est déjà en cache
    if tconst in image_cache:
        return image_cache[tconst]

    url = f"https://www.imdb.com/title/{tconst}/"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lèvera une exception pour les réponses non réussies
        soup = BeautifulSoup(response.text, 'html.parser')

        # Trouver l'image de la pochette du film
        movie_poster_div = soup.find('div', class_='ipc-media ipc-media--poster-27x40 ipc-image-media-ratio--poster-27x40 ipc-media--baseAlt ipc-media--poster-l ipc-poster__poster-image ipc-media__img')
        if not movie_poster_div:
            return None

        movie_poster_img = movie_poster_div.find('img')
        if not movie_poster_img:
            return None

        image_url = movie_poster_img['src']

        # Ajouter l'URL de l'image au cache
        image_cache[tconst] = image_url

        return image_url
    except Exception as e:
        print(f"Une erreur est survenue lors du scrapping de l'image: {e}")
        return None