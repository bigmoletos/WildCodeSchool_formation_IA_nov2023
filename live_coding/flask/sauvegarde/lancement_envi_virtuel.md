# mettre python à jour
python.exe -m pip install --upgrade pip

# Installer virtualenv
pip install virtualenv

# Créer un environnement virtuel
virtualenv envFlask

# Activer l'environnement virtuel
.\envFlask\Scripts\activate

# Installer les packages
pip install flask pandas numpy plotly seaborn scikit-learn

# Enregistrer les packages installés dans un fichier requirements.txt
pip freeze > requirements.txt

# Installer les packages à partir du fichier requirements.txt
pip install -r requirements.txt

# http://127.0.0.1 sur le port 5000. Donc, l’URL serait http://localhost:5000 ou http://127.0.0.1:5000.

# pour arreter l'environnement virtuel
deactivate
