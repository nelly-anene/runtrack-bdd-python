import mysql.connector

# Fonction de connexion à la base de données zoo
def connect():
    return mysql.connector.connect(
        host="localhost", user="root",
        password="***", database="zoo"
    )

# Fonction qui exécute requête SQL
# fetch=True = LIRE des données (SELECT)
# fetch=False = ÉCRIRE (INSERT, UPDATE, DELETE)
def run_query(sql, params=None, fetch=True):
    db = connect()
    cursor = db.cursor()
    cursor.execute(sql, params)  # params = valeurs %s à injecter
    if fetch:
        result = cursor.fetchall()  
        for row in result:
            print(row)
    else:
        db.commit()  # Sauvegarder les changements dans la BDD
        print("OK")
    cursor.close()
    db.close()

# Menu principal - directeur choisit quoi faire
def menu():
    while True:
        print("\n=== ZOO ===")
        print("1.Ajouter animal  2.Supprimer animal  3.Modifier animal")
        print("4.Afficher animaux  5.Animaux par cage")
        print("6.Ajouter cage  7.Supprimer cage  8.Modifier cage")
        print("9.Afficher cages  10.Superficie totale  0.Quitter")

        c = input("Choix : ")

        # --- CRUD ANIMAL ---
        if c == "1":  # CREATE animal
            run_query("INSERT INTO animal (nom,race,id_cage,date_naissance,pays_origine) VALUES(%s,%s,%s,%s,%s)",
                (input("Nom: "), input("Race: "), int(input("ID cage: ")),
                 input("Date (AAAA-MM-JJ): "), input("Pays: ")), fetch=False)

        elif c == "2":  # DELETE animal
            run_query("DELETE FROM animal WHERE id=%s", (int(input("ID animal: ")),), fetch=False)

        elif c == "3":  # UPDATE animal
            id_a = int(input("ID animal: "))
            run_query("UPDATE animal SET nom=%s,race=%s,id_cage=%s,date_naissance=%s,pays_origine=%s WHERE id=%s",
                (input("Nom: "), input("Race: "), int(input("ID cage: ")),
                 input("Date: "), input("Pays: "), id_a), fetch=False)

        elif c == "4":  # READ - tous les animaux
            run_query("SELECT * FROM animal")

        elif c == "5":  # READ - animaux avec leur cage (JOIN)
            run_query("SELECT cage.id, animal.nom, animal.race FROM animal JOIN cage ON animal.id_cage=cage.id ORDER BY cage.id")

        # --- CRUD CAGE ---
        elif c == "6":  # CREATE cage
            run_query("INSERT INTO cage (superficie,capacite_max) VALUES(%s,%s)",
                (int(input("Superficie: ")), int(input("Capacité: "))), fetch=False)

        elif c == "7":  # DELETE cage
            run_query("DELETE FROM cage WHERE id=%s", (int(input("ID cage: ")),), fetch=False)

        elif c == "8":  # UPDATE cage
            id_c = int(input("ID cage: "))
            run_query("UPDATE cage SET superficie=%s,capacite_max=%s WHERE id=%s",
                (int(input("Superficie: ")), int(input("Capacité: ")), id_c), fetch=False)

        elif c == "9":  # READ - toutes les cages
            run_query("SELECT * FROM cage")

        elif c == "10":  # Superficie totale avec SUM
            run_query("SELECT SUM(superficie) FROM cage")

        elif c == "0":  # Quitter le programme
            print("Au revoir!")
            break

# Lancer le menu
menu()