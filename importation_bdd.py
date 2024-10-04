import sqlite3
import csv

# Connecting to the database
con = sqlite3.connect("brief_cbdd.db")
# Creating the cursor
cur = con.cursor()

# Opening and reading the "clients" CSV file
with open("jeu-de-donnees-clients-66fed38c68779376654152.csv", "r") as csv_clients:
    csv_clients_reader = csv.reader(csv_clients)
    next(csv_clients_reader)

    # Inserting the "clients" CSV data into the database
    for row in csv_clients_reader:
        cur.execute("""
                    INSERT INTO Client (client_id, nom, prenom, email, telephone, date_naissance, adresse, consentement_marketing)
                    VALUES (?,?,?,?,?,?,?,?);
        """, row)
con.commit()

# Opening and reading the "commandes" CSV file
with open("jeu-de-donnees-commandes-66fe65226fdb5678959707.csv", "r") as csv_commandes:
    csv_commandes_reader = csv.reader(csv_commandes)
    next(csv_commandes_reader)

    # Inserting the "commandes" CSV data into the database
    for row in csv_commandes_reader:
        cur.execute("""
                    INSERT INTO Commande (commande_id, client_id, date_commande, montant_commande)
                    VALUES (?,?,?,?);
        """, row)
con.commit()

# Closing the connection
con.close()
