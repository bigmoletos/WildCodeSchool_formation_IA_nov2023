from PIL import Image

# Ouvrir les images
img1 = Image.open('quêtes\images\screenshot3.png')
img2 = Image.open('quêtes\images\screenshot4.png')
img3 = Image.open('quêtes\images\screenshot5.png')
img4 = Image.open('quêtes\images\screenshot6.png')
# ...
WIDTH = 1280
HEIGHT = 800
# Assurez-vous que toutes les images ont la même taille
img1 = img1.resize((WIDTH, HEIGHT))
img2 = img2.resize((WIDTH, HEIGHT))
img3 = img3.resize((WIDTH, HEIGHT))
img4 = img4.resize((WIDTH, HEIGHT))
# ...
nbre_image = 4
# Fusionner les images
# Remplacer N par le nombre d'images
merged = Image.new('RGBA', (WIDTH, HEIGHT * nbre_image))
merged.paste(img1, (0, 0))
merged.paste(img2, (0, HEIGHT))
merged.paste(img3, (0, HEIGHT*2))
merged.paste(img4, (0, HEIGHT*3))
# ...

# Enregistrer l'image fusionnée
merged.save('quêtes\images\Recuperer_des_informations.png')
