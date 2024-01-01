# mettre python à jour
python.exe -m pip install --upgrade pip

# Installer virtualenv
pip install virtualenv

# Créer un environnement virtuel
virtualenv django_env

# Activer l'environnement virtuel
.\django_env\Scripts\activate

# Installer les packages
pip install django views pandas numpy plotly seaborn scikit-learn

# Enregistrer les packages installés dans un fichier requirements.txt
pip freeze > requirements.txt

# Installer les packages à partir du fichier requirements.txt
pip install -r requirements.txt
# Créer un projet Django
django-admin startproject my_projet_django
# lancer le fichier app.py
python manage.py  runserver


# http://127.0.0.1:5000 sur le port 5000. Donc, l’URL serait http://localhost:5000 ou http://127.0.0.1:5000.

# pour arreter l'environnement virtuel
deactivate

# si besoin de désinstaller des prog
pip uninstall django pandas numpy plotly seaborn scikit-learn

#  les templates par défaut doivent se trouver dans le repertoire à la racine de app.py dans un dossier templates
templates
