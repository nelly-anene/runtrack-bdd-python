import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password***",
    database="LaPlateforme"
)

cursor = db.cursor()
# SELECT nom, capacite = 2 colonnes de la table salle
cursor.execute("SELECT nom, capacite FROM salle")
resultats = cursor.fetchall()
# Affiche la liste entière
print(resultats)

cursor.close()
db.close()