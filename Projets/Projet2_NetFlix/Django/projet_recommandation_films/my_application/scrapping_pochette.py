# pylint: disable=missing-module-docstring
import requests
from bs4 import BeautifulSoup

def get_movie_poster(tconst, default_image_url='url_of_default_image'):
    url = f"https://www.imdb.com/title/{tconst}/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        poster_link = soup.find('a', class_='ipc-lockup-overlay ipc-focusable')
        if poster_link:
            poster_img = poster_link.find('img')
            if poster_img and 'src' in poster_img.attrs:
                return poster_img['src']

        # Return default image URL if no poster found
        return default_image_url
    except Exception as e:
        print(f"Erreur lors du scrapping de l'image: {e}")
        # Return default image URL in case of any exception
        return default_image_url
