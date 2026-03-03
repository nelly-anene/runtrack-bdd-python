import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password***",
    database="LaPlateforme"
)

cursor = db.cursor()
# SUM(capacite) = additionne les capacités des salles
cursor.execute("SELECT SUM(capacite) FROM salle")
result = cursor.fetchone()
print(f"La capacité de toutes les salles est de : {result[0]}")

cursor.close()
db.close()