import mysql.connector

# --- CLASSE EMPLOYE (CRUD) ---
class Employe:
    def __init__(self):
        # Connexion à la base de données
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Eucharia30*",
            database="entreprise"
        )
        self.cursor = self.db.cursor()

    # CREATE - ajoute un employé
    def ajouter(self, nom, prenom, salaire, id_service):
        sql = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(sql, (nom, prenom, salaire, id_service))
        self.db.commit()  # commit = sauvegarde la BDD
        print(f"Employé {prenom} {nom} ajouté")

    # READ - lire les employés
    def afficher_tous(self):
        self.cursor.execute("SELECT * FROM employe")
        resultats = self.cursor.fetchall()
        for emp in resultats:
            print(emp)
        return resultats

    # READ - employés avec salaire > 3000
    def salaire_superieur(self, montant):
        sql = "SELECT * FROM employe WHERE salaire > %s"
        self.cursor.execute(sql, (montant,))
        resultats = self.cursor.fetchall()
        for emp in resultats:
            print(emp)
        return resultats

    # UPDATE - modifier un employé
    def modifier(self, id_employe, nom, prenom, salaire, id_service):
        sql = "UPDATE employe SET nom=%s, prenom=%s, salaire=%s, id_service=%s WHERE id=%s"
        self.cursor.execute(sql, (nom, prenom, salaire, id_service, id_employe))
        self.db.commit()
        print(f"Employé {id_employe} modifié")

    # DELETE - supprimer un employé
    def supprimer(self, id_employe):
        sql = "DELETE FROM employe WHERE id = %s"
        self.cursor.execute(sql, (id_employe,))
        self.db.commit()
        print(f"Employé {id_employe} supprimé")

    # JOIN - récupérer employés et service
    def afficher_avec_service(self):
        sql = """SELECT employe.nom, employe.prenom, employe.salaire, service.nom 
                 FROM employe 
                 JOIN service ON employe.id_service = service.id"""
        self.cursor.execute(sql)
        resultats = self.cursor.fetchall()
        for emp in resultats:
            print(emp)
        return resultats

    # Fermer la connexion
    def fermer(self):
        self.cursor.close()
        self.db.close()


# --- TESTS ---
emp = Employe()

print("=== Tous les employés ===")
emp.afficher_tous()

print("\n=== Salaire > 3000 ===")
emp.salaire_superieur(3000)

print("\n=== Employés avec leur service ===")
emp.afficher_avec_service()

print("\n=== Ajout d'un employé ===")
emp.ajouter("Moreau", "Julie", 3300.00, 3)

print("\n=== Modification employé 1 ===")
emp.modifier(1, "Dupont", "Jean", 3700.00, 1)

print("\n=== Suppression employé 4 ===")
emp.supprimer(4)

print("\n=== Liste finale ===")
emp.afficher_tous()

emp.fermer()