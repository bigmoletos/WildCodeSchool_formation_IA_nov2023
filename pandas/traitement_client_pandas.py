import pandas as pd

# Charger le fichier CSV dans un dataframe
df = pd.read_csv('clients.csv')

# Calculer la somme de la colonne "price_paid"
total_price_paid = df['price_paid'].sum()

# Afficher le résultat
print(total_price_paid)

# -----------------
# Calculer la colonne "total_price"
df['total_price'] = df['total_paid'] * df['tax']

# Écrire le dataframe mis à jour dans un nouveau fichier CSV
df.to_csv('clients_updated.csv', index=False)

# Afficher le dataframe mis à jour
print(df)

# -----------------
print("\n\n end \n\n")
# -----------------
