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

def calculer_superficie_totale(conn):
    """Calculer la superficie totale de l'ensemble des étages et afficher le résultat."""
    try:
        cursor = conn.cursor()

        query = "SELECT SUM(superficie) FROM etage"
        cursor.execute(query)

        superficie_totale = cursor.fetchone()[0]

        print(f"La superficie de La Plateforme est de {superficie_totale} m2")

    finally:
        cursor.close()

def fermer_connexion(conn):
    """Fermer la connexion à la base de données."""
    conn.close()

try:
    connexion = se_connecter()

    calculer_superficie_totale(connexion)

finally:
    fermer_connexion(connexion)