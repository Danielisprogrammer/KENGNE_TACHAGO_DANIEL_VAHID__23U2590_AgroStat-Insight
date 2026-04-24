import pandas as pd

def clean_data(df):
    """Nettoyage des données pour l'analyse."""
    # Supprime les doublons
    df = df.drop_duplicates()
    # S'assure que les colonnes numériques sont au bon format
    df["Rendement"] = pd.to_numeric(df["Rendement"])
    df["Engrais"] = pd.to_numeric(df["Engrais"])
    return df