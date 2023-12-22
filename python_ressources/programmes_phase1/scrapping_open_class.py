""" scrapping du résumé de la page openclassroom module python"""
import asyncio
from pyppeteer import launch


async def main():
    """fonction de chargement de la page"""
    # Lancer le navigateur et ouvrir une nouvelle page
    browser = await launch()
    page = await browser.newPage()

    # Aller à la page Web
    # url = "https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python/7296776-extrayez-et-transformez-des-donnees-avec-l'extraction-web"
    url='https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python/7296681-importez-des-packages-python'
    await page.goto(url)

    # Récupérer tous les titres h3
    titres = await page.querySelectorAll('h3')
    print("titres :", titres)
    """
    # Trouver le titre "En résumé"
    titre = None
    for t in titres:
        if await t.querySelector('strong') is not None:
            if await page.evaluate('(element) => element.textContent', await t.querySelector('strong')) == "résumé":
                titre = t
                break

    # Si le titre est trouvé, trouver tout le texte suivant le titre
    if titre is not None:
        element = titre
        texte = ''
        while element:
            element = await page.evaluateHandle('(element) => element.nextElementSibling', element)
            if element:
                texte += '\n\n' + await page.evaluate('(element) => element.textContent', element)

        print(texte)
    else:
        print("Titre 'En résumé' non trouvé")

    """
    # Fermer le navigateur
    await browser.close()

# Exécuter la fonction principale
asyncio.run(main())
