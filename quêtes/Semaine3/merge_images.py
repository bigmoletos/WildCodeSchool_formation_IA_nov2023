from PIL import Image

# nombre d'images à merger
nbre_image = 2
# taille des images souhaitées
WIDTH = 1280
HEIGHT = 800


# Ouvrir les images
img1 = Image.open('quêtes\images\quetes_wizard\screenshot_and_merge\screenshot7.png')
img2 = Image.open('quêtes\images\quetes_wizard\screenshot_and_merge\screenshot8.png')
# img3 = Image.open('quêtes\images\quetes_wizard\screenshot_and_merge\screenshot5.png')
# img4 = Image.open('quêtes\images\quetes_wizard\screenshot_and_merge\screenshot6.png')
# ...
# On met les images avec  la même taille
img1 = img1.resize((WIDTH, HEIGHT))
img2 = img2.resize((WIDTH, HEIGHT))
# img3 = img3.resize((WIDTH, HEIGHT))
# img4 = img4.resize((WIDTH, HEIGHT))
# ...

# Fusionner les images

merged = Image.new('RGBA', (WIDTH, HEIGHT * nbre_image))
merged.paste(img1, (0, 0))
merged.paste(img2, (0, HEIGHT))
# merged.paste(img3, (0, HEIGHT*2))
# merged.paste(img4, (0, HEIGHT*3))
# ...

# Enregistrer l'image fusionnée
merged.save('quêtes\images\quetes_wizard\screenshot_and_merge\manipulation_donnees.png')
