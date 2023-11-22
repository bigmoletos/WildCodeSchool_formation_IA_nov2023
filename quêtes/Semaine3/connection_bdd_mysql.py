import mysql.connector

# Se connecter à la base de données MySQL
connexion = mysql.connector.connect(
    host='localhost',
    user='mon_utilisateur',
    password='mon_mot_de_passe',
    database='ma_base_de_donnees'
)

# Créer un objet curseur
curseur = connexion.cursor()

# Exécuter une requête SQL
curseur.execute("SELECT * FROM ma_table")

# Récupérer tous les résultats
resultats = curseur.fetchall()

# Fermer la connexion
connexion.close()