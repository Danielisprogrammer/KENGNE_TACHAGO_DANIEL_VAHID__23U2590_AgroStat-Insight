import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

class AnalystEngine:
    @staticmethod
    def calculate_correlation(df):
        """
        Calcule la corrélation de Pearson entre l'engrais et le rendement.
        """
        # On vérifie si les colonnes existent et s'il y a assez de données
        if 'engrais' in df.columns and 'rendement' in df.columns:
            if len(df) > 1:
                return df['engrais'].corr(df['rendement'])
        return 0.0

    @staticmethod
    def get_regression_formula(df):
        """
        Calcule la régression linéaire (y = ax + b).
        Retourne (pente, ordonnée, score_R2).
        """
        try:
            # Vérification de la présence des colonnes en minuscules
            if 'engrais' not in df.columns or 'rendement' not in df.columns:
                return None, None, None
            
            # On élimine les valeurs manquantes pour le calcul
            clean_df = df.dropna(subset=['engrais', 'rendement'])
            
            if len(clean_df) < 2:
                return None, None, None

            # Préparation des données pour Scikit-Learn
            X = clean_df[['engrais']].values
            y = clean_df['rendement'].values
            
            model = LinearRegression()
            model.fit(X, y)
            
            a = model.coef_[0]      # La pente (coefficient)
            b = model.intercept_    # L'ordonnée à l'origine
            r2 = model.score(X, y)  # Le coefficient de détermination
            
            return a, b, r2
            
        except Exception as e:
            # En cas d'erreur imprévue, on ne fait pas planter l'app
            print(f"Erreur StatsEngine: {e}")
            return None, None, None