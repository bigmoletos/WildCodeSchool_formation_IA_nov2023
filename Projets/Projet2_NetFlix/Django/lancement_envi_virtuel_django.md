# mettre python à jour
python.exe -m pip install --upgrade pip

# Installer virtualenv
pip install virtualenv

# Créer un environnement virtuel
virtualenv django_env

# Activer l'environnement virtuel
.\django_env\Scripts\activate

# Installer les packages
pip install django views pandas numpy plotly seaborn scikit-learn scipy bs4 fuzzywuzzy django-select2 requests joblib djangorestframework selenium  webdriver_manager

# Enregistrer les packages installés dans un fichier requirements.txt
pip freeze > requirements.txt

# Installer les packages à partir du fichier requirements.txt
pip install -r requirements.txt

# Créer un projet Django
django-admin startproject projet_recommandation_films

# lancer le fichier app.py
python manage.py  runserver

# Mise à jour des migrations de BDD
python manage.py migrate


# relancer le fichier app.py
python manage.py  runserver

# http://127.0.0.1:5000 sur le port 5000. Donc, l’URL serait http://localhost:5000 ou http://127.0.0.1:5000.

# pour arreter l'environnement virtuel
deactivate

# Pour relancer le projet
## se mettre dans le dossier ***Projet2_NetFlix\Django>***
cd Django
.\django_env\Scripts\activate
##  se mettre dans le dossier ***Projet2_NetFlix\Django\projet_recommandation_films>***
<!-- cd .\projet_recommandation_films\ -->
cd .\projet_recommandation_films\
python manage.py  runserver

# importer réguliérement les données statiques du site css, js ,image etc....
python manage.py collectstatic


# si besoin de désinstaller des prog
pip uninstall django pandas numpy plotly seaborn scikit-learn

#  les templates par défaut doivent se trouver dans le repertoire à la racine de app.py dans un dossier templates
créer un dossier ***my_application***
créer un dossier ***template*** comprenant tous les fichiers html
Django\projet_recommandation_films\my_application\template\
accueil.html
### les fichiers importants se trouvent dans:
Projets\Projet2_NetFlix\Django\projet_recommandation_films\
manage.py
Projets\Projet2_NetFlix\Django\projet_recommandation_films\my_application\
models.py
Django\projet_recommandation_films\my_application\
views.py
### Django\projet_recommandation_films\projet_recommandation_films\
Django\projet_recommandation_films\projet_recommandation_films\
urls.py
settings.py
### les fichiers python de l'application
Django\projet_recommandation_films\my_application\
stat_acteur.py
