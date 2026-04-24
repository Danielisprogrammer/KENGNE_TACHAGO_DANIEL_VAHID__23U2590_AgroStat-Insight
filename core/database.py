import sqlite3
import pandas as pd

class DatabaseManager:
    def __init__(self, db_name="data/agrostat.db"):
        self.db_name = db_name
        self._create_table()

    def _create_table(self):
        """Crée la table si elle n'existe pas encore."""
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
        """Sauvegarde un DataFrame dans la base SQLite."""
        conn = sqlite3.connect(self.db_name)
        df.to_sql("releves", conn, if_exists="append", index=False)
        conn.close()

    def load_data(self):
        """Charge toutes les données de la base vers un DataFrame."""
        conn = sqlite3.connect(self.db_name)
        query = "SELECT * FROM releves"
        df = pd.read_sql(query, conn)
        conn.close()
        return df