import sqlite3
import hashlib
from datetime import datetime
import os 

conn = sqlite3.connect("tables.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS depenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    montant REAL NOT NULL,
    categorie TEXT,
    description TEXT,
    date TEXT,
    user_id INTEGER,
    FOREIGN KEY(user_id) REFERENCES users(id)
)
""")

conn.commit()

categories = [
    "Alimentation",
    "Transport",
    "Logement",
    "Loisirs",
    "Santé",
    "Vêtements",
    "Éducation",
    "Autre"
]


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()



def creer_user(username, password):
    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
    if cursor.fetchone():
        print(f"L'utilisateur '{username}' existe déjà.")
        return
    
    pwd_hash = hash_password(password)
    cursor.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        (username, pwd_hash)
    )
    conn.commit()
    print(f"Utilisateur {username} créé avec succès !")


def ajout_depense(user_id, montant, categorie, description, date=None):
    if categorie not in categories:
        print(f"Catégorie invalide. Choisissez parmi : {', '.join(categories)}")
        return

    if date is None:
        date = datetime.now().strftime("%d/%m/%y")

    cursor.execute(
        """INSERT INTO depenses (montant, categorie, description, date, user_id)
           VALUES (?, ?, ?, ?, ?)""",
        (montant, categorie, description, date, user_id)
    )
    conn.commit()
    print(f"Dépense de {montant}€ ajoutée en '{categorie}' le {date} !")
    

def derniere_depense():
    if not os.path.exists("tables.db"):
        print("Base de données vide")
        return None

    cursor.execute("SELECT * FROM depenses ORDER BY id DESC LIMIT 1")
    colonne = cursor.fetchone()

    if colonne:
        print(colonne[1])
        return colonne[1]
    return None


def nombre_transaction():
    if not os.path.exists("tables.db"):
        # print("Base de données vide")
        return None

    cursor.execute(
        "SELECT COUNT(*) FROM depenses"
    )
    
    resultat = cursor.fetchone()

    if resultat:
        # print(f"nombre de depense : {resultat[0]}")
        return resultat[0]
    return None



def top_categorie(user_id):
    if not os.path.exists("tables.db"):
        print("Base de données vide")
        return None
    
    cursor.execute(
        """SELECT categorie, SUM(montant) AS total
           FROM depenses
           WHERE user_id = ?
           GROUP BY categorie
           ORDER BY total DESC
           LIMIT 1""",(user_id)
    )
    resultat = cursor.fetchone()

    if resultat:
        print(f"Catégorie qui a le plus dépenser : {resultat[0]} -> {resultat[1]}€")
        return resultat[0]
    return None


def depense_mois(user_id):
    if not os.path.exists("tables.db"):
        print("Base de données vide")
        return None

    mois_actuel = datetime.now().strftime("%m/%y")  # ex: "04/26"

    cursor.execute("""
        SELECT SUM(montant)
        FROM depenses
        WHERE user_id = ?
        AND substr(date, 4) = ?
    """, (user_id, mois_actuel))

    resultat = cursor.fetchone()
    if resultat and resultat[0]:
        total = resultat[0]
        print(f"Dépenses du mois : {total}€")
        return total
    return None


def selection_cat_camembert():
    cursor.execute("""
        SELECT categorie, SUM(montant) AS total
        FROM depenses
        GROUP BY categorie
        ORDER BY total DESC
""")
    resultats_cat = cursor.fetchall()

    return resultats_cat


def selection_date_barres():
    cursor.execute("""
        SELECT substr(date, 4, 2) AS mois, SUM(montant) AS total
        FROM depenses
        GROUP BY mois
        ORDER BY mois ASC
    """)
    resultats_mois = cursor.fetchall()

    return resultats_mois



if __name__ == "__main__":
    creer_user("Nadir", "Nadir772")
    ajout_depense(1, 65, "Alimentation", "description", "10/01/26")
    ajout_depense(1, 350, "Transport", "description", "10/03/26")
    ajout_depense(1, 150, "Alimentation", "description")
    conn.close()
