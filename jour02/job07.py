import mysql.connector

class Salarie:
    def __init__(self, user, password, host, database):
        self.conn = mysql.connector.connect(
            root=user,
            cyrus184419=password,
            localhost=host,
            equipe=database
        )
        self.cursor = self.conn.cursor()

    def ajouter_salarie(self, nom, prenom, salaire):
        query = "INSERT INTO employe (nom, prenom, salaire) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire)
        self.cursor.execute(query, values)
        self.conn.commit()

    def recuperer_salaries(self):
        query = "SELECT * FROM employe"
        self.cursor.execute(query)
        resultats = self.cursor.fetchall()
        return resultats

    def mettre_a_jour_salarie(self, salarie_id, nouveau_salaire):
        query = "UPDATE employe SET salaire = %s WHERE id = %s"
        values = (nouveau_salaire, salarie_id)
        self.cursor.execute(query, values)
        self.conn.commit()

    def supprimer_salarie(self, salarie_id):
        query = "DELETE FROM employe WHERE id = %s"
        values = (salarie_id,)
        self.cursor.execute(query, values)
        self.conn.commit()

    def fermer_connexion(self):
        self.cursor.close()
        self.conn.close()

try:
    salarie_manager = Salarie('votre_utilisateur', 'votre_mot_de_passe', 'votre_hôte', 'votre_base_de_donnees')

    salarie_manager.ajouter_salarie('Nouveau', 'Employe', 40000.00, 1)

    resultats_salaries = salarie_manager.recuperer_salaries()
    print("Salariés avant mise à jour :")
    for resultat in resultats_salaries:
        print(resultat)

    salarie_manager.mettre_a_jour_salarie(salarie_id=1, nouveau_salaire=45000.00)

    resultats_salaries_apres_maj = salarie_manager.recuperer_salaries()
    print("\nSalariés après mise à jour du salaire :")
    for resultat in resultats_salaries_apres_maj:
        print(resultat)

    salarie_manager.supprimer_salarie(salarie_id=1)

    resultats_salaries_apres_suppression = salarie_manager.recuperer_salaries()
    print("\nSalariés après suppression du premier salarié :")
    for resultat in resultats_salaries_apres_suppression:
        print(resultat)

finally:
    salarie_manager.fermer_connexion()
