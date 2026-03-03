import mysql.connector

# Connexion à la base de données
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password="***",S
    database="LaPlateforme"
)

cursor = db.cursor()

# Récupérer les étudiants
cursor.execute("SELECT * FROM etudiants")

# Récupérer et afficher les résultats
resultats = cursor.fetchall()
for etudiant in resultats:
    print(etudiant)

# Fin de connexion
cursor.close()
db.close()