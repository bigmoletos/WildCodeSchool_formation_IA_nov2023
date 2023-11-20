from PIL import Image

# Ouvrir les images
img1 = Image.open('quêtes\images\screenshot1.png')
img2 = Image.open('quêtes\images\screenshot2.png')
# ...
WIDTH=1280
HEIGHT=800
# Assurez-vous que toutes les images ont la même taille
img1 = img1.resize((WIDTH, HEIGHT))
img2 = img2.resize((WIDTH, HEIGHT))
# ...
nbre_image=2
# Fusionner les images
merged = Image.new('RGBA', (WIDTH, HEIGHT * nbre_image))  # Remplacer N par le nombre d'images
merged.paste(img1, (0, 0))
merged.paste(img2, (0, HEIGHT))
# ...

# Enregistrer l'image fusionnée
merged.save('quêtes\images\question1.png')