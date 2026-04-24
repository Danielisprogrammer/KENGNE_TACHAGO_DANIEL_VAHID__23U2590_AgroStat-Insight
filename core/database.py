import sqlite3
import os
import pandas as pd  

class DatabaseManager:
    def __init__(self, db_name="data/agrostat.db"):
        # Définition du chemin de la base de données
        self.db_name = db_name
        
        # Création automatique du dossier 'data' s'il n'existe pas
        os.makedirs(os.path.dirname(self.db_name), exist_ok=True)
        
        self._create_table()

    def _create_table(self):
        """Crée la table 'releves' si elle n'existe pas encore."""
        conn = sqlite3.connect(self.db_name)
        query = """
        CREATE TABLE IF NOT EXISTS releves (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            culture TEXT,
            engrais REAL,
            humidite REAL,
            rendement REAL
        )
        """
        conn.execute(query)
        conn.commit()
        conn.close()

    def save_data(self, df):
        """Sauvegarde les nouvelles lignes du DataFrame dans la base SQLite."""
        conn = sqlite3.connect(self.db_name)
        # On utilise if_exists="append" pour ajouter les données sans écraser l'ancien
        df.to_sql("releves", conn, if_exists="append", index=False)
        conn.close()

    def load_data(self):
        """Charge toutes les données de la base vers un DataFrame Pandas."""
        conn = sqlite3.connect(self.db_name)
        query = "SELECT * FROM releves"
        # pd.read_sql a besoin que Pandas soit importé en tant que 'pd'
        df = pd.read_sql(query, conn)
        conn.close()
        return df