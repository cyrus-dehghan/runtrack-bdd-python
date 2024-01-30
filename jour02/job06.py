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

def calculer_capacite_totale(conn):
    """Calculer la capacité totale des salles et afficher le résultat."""
    try:
        cursor = conn.cursor()

        query = "SELECT SUM(capacite) FROM salle"
        cursor.execute(query)

        capacite_totale = cursor.fetchone()[0]

        print(f"La capacité totale des salles est de {capacite_totale} personnes")

    finally:
        cursor.close()

def fermer_connexion(conn):
    """Fermer la connexion à la base de données."""
    conn.close()

try:
    connexion = se_connecter()

    calculer_capacite_totale(connexion)

finally:
    fermer_connexion(connexion)