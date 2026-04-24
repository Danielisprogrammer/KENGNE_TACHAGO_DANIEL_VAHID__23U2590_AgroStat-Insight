import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import sqlite3
import os

class DatabaseManager:
    def __init__(self, db_name="data/agrostat.db"):
        self.db_name = db_name
        # Création du dossier data s'il n'existe pas
        os.makedirs(os.path.dirname(self.db_name), exist_ok=True)
        
        # Initialisation de la connexion Google Sheets
        try:
            self.cloud_conn = st.connection("gsheets", type=GSheetsConnection)
        except Exception as e:
            st.error("Erreur de connexion au Cloud Google Sheets.")
            self.cloud_conn = None
            
        self._create_local_table()

    def _create_local_table(self):
        """Initialise la table SQLite locale."""
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

    def load_data(self):
        """Récupère les données depuis le Cloud (ou SQLite si échec)."""
        if self.cloud_conn:
            try:
                # Lecture depuis Google Sheets (ttl=0 pour éviter le cache)
                df = self.cloud_conn.read(ttl=0)
                return df
            except Exception:
                st.warning("Cloud inaccessible, chargement des données locales...")
        
        # Secours : Lecture SQLite
        conn = sqlite3.connect(self.db_name)
        df = pd.read_sql("SELECT * FROM releves", conn)
        conn.close()
        return df

    def save_data(self, new_row_df):
        """Sauvegarde simultanée : Local (SQLite) + Cloud (Google Sheets)."""
        # 1. Sauvegarde locale (SQLite)
        conn = sqlite3.connect(self.db_name)
        new_row_df.to_sql("releves", conn, if_exists="append", index=False)
        conn.close()

        # 2. Sauvegarde Cloud (Google Sheets)
        if self.cloud_conn:
            try:
                # On récupère l'historique complet
                existing_df = self.load_data()
                # On fusionne avec la nouvelle ligne
                updated_df = pd.concat([existing_df, new_row_df], ignore_index=True)
                # On met à jour la feuille Google
                self.cloud_conn.update(data=updated_df)
                st.success("✅ Données synchronisées avec le Cloud !")
            except Exception as e:
                st.error(f"⚠️ Erreur de synchronisation Cloud : {e}")