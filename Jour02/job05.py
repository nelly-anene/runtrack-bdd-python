import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password***",
    database="LaPlateforme"
)

cursor = db.cursor()
# SUM(surfface) = additionne toutes les surfface des étages
cursor.execute("SELECT SUM(superficie) FROM etage")
result = cursor.fetchone()  # fetchone car on attend 1 seul résultat
print(f"La superficie de La Plateforme est de {result[0]} m2")

cursor.close()
db.close()