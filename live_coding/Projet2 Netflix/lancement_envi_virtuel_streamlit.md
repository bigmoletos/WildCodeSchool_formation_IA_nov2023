# mettre python à jour
python.exe -m pip install --upgrade pip

# Installer virtualenv
pip install virtualenv

# Créer un environnement virtuel
python -m venv streamlit_env


# Activer l'environnement virtuel
.\streamlit_env\Scripts\activate


# Installer les packages
pip install streamlit pandas numpy plotly seaborn scikit-learn pandas

# Enregistrer les packages installés dans un fichier requirements.txt
pip freeze > requirements.txt

# Installer les packages à partir du fichier requirements.txt
pip install -r requirements.txt


# lancer le fichier app.py depuis le terminal !
streamlit run app.py
# pour arreter l'environnement virtuel
deactivate

# si besoin de désinstaller des prog
pip uninstall streamlit pandas numpy plotly seaborn scikit-learn

#  les templates par défaut doivent se trouver dans le repertoire à la racine de app.py dans un dossier templates
/my_streamlit_app
|-- /templates
|-- /static
|   |-- /images
|   |-- /css
|-- app.py

# sur le navigateur ou http://localhost:8501/

