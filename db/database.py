import sqlite3
import hashlib

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



def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def creer_user(username, password):
    pwd_hash = hash_password(password)
    cursor.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        (username, pwd_hash)
    )
    conn.commit()
    print(f"Utilisateur {username} créé avec succès !")


def ajout_depense(user_id, montant, categorie, description, date):
    cursor.execute(
        """INSERT INTO depenses (montant, categorie, description, date, user_id)
           VALUES (?, ?, ?, ?, ?)""",
        (montant, categorie, description, date, user_id)
    )
    conn.commit()
    print(f"Dépense de {montant}€ ajoutée avec succès !")


creer_user("noir","manger778")


conn.close()