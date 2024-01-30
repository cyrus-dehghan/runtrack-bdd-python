import mysql.connector

class ZooManager:
    def __init__(self, user, password, host, database):
        self.conn = mysql.connector.connect(
            root=user,
            cyrus184419=password,
            localhost=host,
            zoo=database
        )
        self.cursor = self.conn.cursor()

    def ajouter_animal(self, nom, race, id_type_cage, date_naissance, pays_origine):
        query = "INSERT INTO animal (nom, race, id_type_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
        values = (nom, race, id_type_cage, date_naissance, pays_origine)
        self.cursor.execute(query, values)
        self.conn.commit()

    def ajouter_cage(self, superficie, capacite_max):
        query = "INSERT INTO cage (superficie, capacite_max) VALUES (%s, %s)"
        values = (superficie, capacite_max)
        self.cursor.execute(query, values)
        self.conn.commit()

    def afficher_animaux(self):
        query = "SELECT * FROM animal"
        self.cursor.execute(query)
        resultats = self.cursor.fetchall()
        return resultats

    def afficher_animaux_cages(self):
        query = "SELECT animal.nom, cage.id FROM animal LEFT JOIN cage ON animal.id_type_cage = cage.id"
        self.cursor.execute(query)
        resultats = self.cursor.fetchall()
        return resultats

    def calculer_superficie_totale(self):
        query = "SELECT SUM(superficie) FROM cage"
        self.cursor.execute(query)
        superficie_totale = self.cursor.fetchone()[0]
        return superficie_totale

    def fermer_connexion(self):
        self.cursor.close()
        self.conn.close()

try:
    zoo_manager = ZooManager('votre_utilisateur', 'votre_mot_de_passe', 'votre_hôte', 'zoo')

    zoo_manager.ajouter_animal('Lion', 'Sauvage', 1, '2022-01-01', 'Afrique')

    zoo_manager.ajouter_cage(100, 5)

    resultats_animaux = zoo_manager.afficher_animaux()
    print("Animaux dans le zoo :")
    for resultat in resultats_animaux:
        print(resultat)

    resultats_animaux_cages = zoo_manager.afficher_animaux_cages()
    print("\nAnimaux dans les cages :")
    for resultat in resultats_animaux_cages:
        print(resultat)

    superficie_totale = zoo_manager.calculer_superficie_totale()
    print("\nSuperficie totale des cages :", superficie_totale)

finally:
    zoo_manager.fermer_connexion()
