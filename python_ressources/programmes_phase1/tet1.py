import re

# # Définir le motif d'expression régulière sous forme de chaîne de caractères
# motif = r'\d+'

# # Compiler le motif en un objet d'expression régulière
# regex = re.compile(motif)
# print("regex=0",regex)


from urllib.parse import urlparse, urlunparse
import validators
# Votre URL
saisie_url = "http:/liNkdsEeDLin.Org/feed/?msgControlName=view_message_button&msgConversationId=2-OGU3Yjg4NDYtMThjYS00NjljLWJkODYtNmYwM2Y4MDI4Nzc4XzAxMg%3D%3D&msgOverlay=true&trk=false"

# Analyser l'URL
url = urlparse(saisie_url)

# Mettre en minuscule le domaine de l'URL
domaine_minuscule = url.netloc.lower()

# Créer une nouvelle URL avec le domaine en minuscule
nouvelle_url = urlunparse((url.scheme, domaine_minuscule, url.path, url.params, url.query, url.fragment))

# Vérifier si l'URL est valide
if validators.url(saisie_url):
    print("L'URL est valide.")
else:
    print("L'URL n'est pas valide.")

print("-"*50)
print(url)
print(domaine_minuscule)
print("nouvelle url ",nouvelle_url)
print("-"*50)

# print(saisie_url[:11])
# print(saisie_url[7:len(saisie_url)])
# print(saisie_url[11:len(saisie_url)])
# print(len(saisie_url))

# regex de reconnaissance d'une url
# regex_caracteres_speciaux:re.compile(r'^(?:http|ftp)s?://'  # http:// or https:// or ftp or ftps
#         r'(?:(?:A-Z0-9?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
#         r'localhost|'  # localhost...
#         r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
#         r'(?::\d+)?'  # optional port
#         r'(?:/?|[/?]\S+)$', re.IGNORECASE)
# regex_caracteres_speciaux: re.compile(
#     r'^(?:http|ftp)s?://(?:(?:A-Z0-9?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|localhost|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?::\d+)?(?:/?|[/?]\S+)$', re.IGNORECASE)
# regex_caracteres_speciaux: r"^(?:http|ftp)s?://|localhost|"

saisie_url="http://www.KJoogle.com"
saisie_url = "https://www.Go +- /:ogLe.com"
saisie_url=" -*656+google.com 56"
# saisie_url="https://www.google.fr/"
saisie_url="https://www.linkedin.com/feed/?msgControlName=view_message_button&msgConversationId=2-OGU3Yjg4NDYtMThjYS00NjljLWJkODYtNmYwM2Y4MDI4Nzc4XzAxMg%3D%3D&msgOverlay=true&trk=false"

# suppression des espaces 

saisie_url = saisie_url.strip()
saisie_url=re.sub(' ', '', saisie_url)

# définition du pattern regex à utiliser avec le flag re.X pour le MULTILINE
motif=r"""
# ^(?:http|ftp)s?://  # http:// or https:// or ftp or ftps
(?:(?:A-Z0-9?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|  # domain...
localhost|  # localhost...
\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})  # ...or ip
(?::\d+)?  # optional port
(?:/?|[/?]\S+)$'
"""
# print("motif=", motif)
match = re.match(motif, saisie_url)

# construction du regex
regex_caracteres_speciaux=re.compile(motif, re.X)

# pattern pour le test du début de l'url verifie si l'url comme par  http(s)://www.  ou ftp(s)://www.
regex_start_url=r'^(?:http|ftp)s?://www'
# test le début de l'url pour savoir elle commence par http ou https ou ftp ou ftps
# check_start_url = re.match(regex_start_url, saisie_url)
check_start_url = re.match(r'^(?:http|ftp)s?://www.', saisie_url)
# re.match(r'^(?:http|ftp)s?://', saisie_url)
if check_start_url:
    print("check start url= ",check_start_url)
    print("L'URL: "+saisie_url+" commence par http://, https://, ftp:// ou ftps://.")
else:
    print("check start url= ",check_start_url)
    print("L'URL: "+saisie_url+" ne commence pas par http://, https://, ftp:// ou ftps://.")

print("regex1= ",regex_start_url)
# print("check start url= ",check_start_url)

# regex_caracteres_speciaux.pattern
print("regex2= ", regex_caracteres_speciaux.pattern)
# verifie si le l'url saisie correspond à une url
# check_if_is_url = None
check_if_is_url = re.match(regex_start_url, saisie_url)
print("check=", check_if_is_url)

# epuration et mise en forme de l'url en fonction de sa saisie
# if re.match('^(?:http|ftp)s?://', saisie_url):
if re.match(regex_start_url, saisie_url):
    extract_saisie_url = saisie_url[7:len(saisie_url)]
    saisie_url = "https://www." + \
        re.sub(regex_caracteres_speciaux, '', extract_saisie_url)
# elif re.match('^(?:http|ftp)s?://www\.', saisie_url):
elif re.match(regex_start_url+r'www.', saisie_url):
    extract_saisie_url = saisie_url[11:len(saisie_url)]
    saisie_url = "https://www." + \
        re.sub(regex_caracteres_speciaux, '', extract_saisie_url)
else:
    saisie_url = "https://www." + \
        re.sub(regex_caracteres_speciaux, '', saisie_url)

print(saisie_url)

# print(1+2+3+4+12)
# import requests

# url = "https://www.gov.uk/search/news-and-communications"
# page = requests.get(url)

# # Voir le code html source
# print(page.content)
