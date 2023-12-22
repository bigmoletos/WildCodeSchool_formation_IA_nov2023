import csv

# Ouvrir le fichier CSV
with open('clients.csv', 'r') as file:
    # Créer un objet reader
    reader = csv.reader(file)

    # Ouvrir un nouveau fichier CSV pour écrire les données modifiées
    with open('clients_updated.csv', 'w', newline='') as new_file:
        # Créer un objet writer
        writer = csv.writer(new_file)

        # Parcourir chaque ligne du fichier
        for row in reader:
            # Remplacer le symbole "%" par une chaîne vide dans la colonne "tax"
            if row[0] == "tax":
                row = row.replace('%', '')

            # Écrire la ligne modifiée dans le nouveau fichier CSV
            writer.writerow(row)
       # Afficher les 10 premiers éléments de la colonne "tax"
        for i, row in enumerate(reader):
            if i == 0:
                tax_index = row.index('tax')
            else:
                if i > 10:
                    break
                print(row[tax_index])

# Afficher le résultat
# print(total_price_paid)


# -----------------
print("\n\n end \n\n")
# -----------------
