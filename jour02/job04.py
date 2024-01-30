import mysql.connector

config = {
    'user': 'root',
    'password': 'cyrus184419',
    'host': 'localhost',
    'database': 'laplateforme'
}

def se_connecter():
    """Établir la connexion à la base de données."""
    return mysql.connector.connect(**config)

def recuperer_salles(conn):
    """Récupérer les noms et les capacités de la table 'salle' et les afficher en console."""
    try:
        cursor = conn.cursor()

        query = "SELECT nom, capacite FROM salle"
        cursor.execute(query)

        resultats = cursor.fetchall()

        for resultat in resultats:
            nom, capacite = resultat
            print(f"( {nom}, {capacite})")

    finally:
        cursor.close()

def fermer_connexion(conn):
    """Fermer la connexion à la base de données."""
    conn.close()

try:
    connexion = se_connecter()

    recuperer_salles(connexion)

finally:
    fermer_connexion(connexion)
