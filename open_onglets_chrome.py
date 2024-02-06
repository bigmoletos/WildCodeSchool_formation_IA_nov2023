import webbrowser

# # Ce programme ouvre avec Chrome tous les onglets contenus dans le fichier clean_urls
# Spécifier le chemin de l'exécutable Chrome
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
browser = webbrowser.get(chrome_path)

# Ouvrir le fichier et lire les URLs
with open('datas/txt/clean_urls.txt', 'r') as f:
    urls = f.read().splitlines()

# Ouvrir chaque URL dans un nouvel onglet
for url in urls:
    browser.open_new_tab(url)
