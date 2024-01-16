# pylint: disable=missing-module-docstring
import requests
from bs4 import BeautifulSoup
# https://www.imdb.com/title/tt0084555/mediaviewer/rm90479616/?ref_=tt_mi_sm
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



# def get_movie_poster2(tconst, default_image_url='url_of_default_image'):
#     url = f"https://www.imdb.com/title/{tconst}/"
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

#     try:
#         response = requests.get(url, headers=headers)
#         soup = BeautifulSoup(response.text, 'html.parser')

#         # On IMDb, the primary poster is within a div with class 'ipc-media--poster-l'
#         poster_div = soup.find('div', class_='ipc-media--poster-l')
#         if poster_div:

#         poster_img = poster_div.find('img', class_='ipc-image')
#         if poster_img and 'src' in poster_img.attrs:
#             return poster_img['src']
#             # Return default image URL if no poster found
#             return default_image_url
#         except Exception as e:
#             print(f"Erreur lors du scrapping de l'image: {e}")
#             # Return default image URL in case of any exception
#             return default_image_url

# print(get_movie_poster2('tt0084555'))
