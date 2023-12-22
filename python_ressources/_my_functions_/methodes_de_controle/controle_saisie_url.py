"""controle de saisie d'une url"""
# import re
from urllib.parse import urlparse, urlunparse
import validators.url
from colorama import Fore, Style
# import validators


def controle_saisie_url() :
    """controle de la saisie d'une url':
    sans caractéres spéciaux
    espace au début ni à la fin
    remplacer les autres espaces par ds _
    et le nom doit commencer par une lettre"""
    print("saisie url")
    while True:
        try:
            menu="""
Veuillez entrer l'url ' :
-sans espace ni au début ni à la fin
-le nom  doit commencer par une lettre
-caractéres speciaux interdits
entrez le nom:  """
            saisie_url = input(menu)
            print(saisie_url)
            # controle de l'url
            if not saisie_url:
                 raise ValueError("l'URL ne peut pas être vide")
                        
            # Analyser l'URL, en parsant les differentes partie d'une url (domaine, path, requete, etc)
            url = urlparse(saisie_url)

            # Mettre en minuscule le domaine de l'URL
            domaine_minuscule = url.netloc.lower()

            # Créer une nouvelle URL avec le domaine en minuscule
            saisie_url = urlunparse((url.scheme, domaine_minuscule, url.path, url.params, url.query, url.fragment))

            # Vérifier si l'URL est valide
            if  not validators.url(saisie_url):
                raise ValueError(f"L'URL que vous avez saisie n'est pas valide. \n {saisie_url}")
            return saisie_url
            
        #  traitement des erreurs
        except (Exception , ValueError) as e:
                # affiche en rouge le message d'erreur
                print(f"{Fore.RED} Une erreur inattendue s'est produite. Veuillez réessayer: {e}{Style.RESET_ALL}")                # menu pour proposer au user de stopper son programme
                error_message="""
Voulez-vous quitter le programme
si oui tapez O (oui) ou Y (yes) 
ou toute autre touche pour continuer : """
                stop_program = input(error_message)
                if stop_program.lower() in ('o','y','x'):
                    break
       
        # dans tous les cas donner le nom de l'url
        finally:
                print(f"Vous avez saisie l'url \n {Fore.GREEN}{saisie_url}{Style.RESET_ALL}")



# saisie_url=input("saisir nom de fichier")
# controle_saisie_url()