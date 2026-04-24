import streamlit as st
import pandas as pd
from components.sidebar import render_sidebar
from components.dashboard import render_metrics, render_charts
from core.database import DatabaseManager

# --- CONFIGURATION DE L'APPLICATION ---
st.set_page_config(
    page_title="AgroStat Insight Pro v1.0",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- INITIALISATION DU MOTEUR DE BASE DE DONNÉES ---
db = DatabaseManager()

# --- CHARGEMENT DES DONNÉES AU LANCEMENT ---
if 'data' not in st.session_state:
    st.session_state.data = db.load_data()

def main():
    # 1. RÉCUPÉRATION DES SAISIES (SIDEBAR)
    new_entry = render_sidebar()
    
    if new_entry is not None:
        # On force les colonnes en minuscules pour la base de données
        new_entry.columns = [c.lower() for c in new_entry.columns]
        
        # Sauvegarde physique (SQLite + Cloud Google Sheets)
        db.save_data(new_entry)
        
        # Mise à jour de la session pour l'affichage immédiat
        st.session_state.data = db.load_data()
        
        st.toast("Relevé enregistré et synchronisé !", icon="☁️")
        st.rerun()

    # --- EN-TÊTE DU DASHBOARD ---
    st.title("🌱 AgroStat Insight | Expert Mode")
    st.markdown(f"**Ingénieur :** Daniel Kengne | **Base de données :** Cloud Sync Active")

    # 2. TRAITEMENT ET NETTOYAGE DES DONNÉES
    if not st.session_state.data.empty:
        # On travaille sur une copie pour éviter les warnings
        df_clean = st.session_state.data.copy()
        
        # Harmonisation des colonnes
        df_clean.columns = [c.lower() for c in df_clean.columns]
        
        # Définition des colonnes numériques
        cols_numeriques = ["engrais", "humidite", "rendement"]
        
        for col in cols_numeriques:
            if col in df_clean.columns:
                df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')
        
        # On supprime les lignes qui n'ont pas pu être converties
        df_clean = df_clean.dropna(subset=cols_numeriques)

        # 3. AFFICHAGE DES COMPOSANTS (DASHBOARD)
        render_metrics(df_clean)
        render_charts(df_clean)
        
        # --- 4. OPTION D'EXPORTATION (NOUVEAU) ---
        st.divider()
        st.subheader("📄 Rapport et Exportation")
        col_exp1, col_exp2 = st.columns([1, 2])
        
        with col_exp1:
            @st.cache_data
            def convert_df(df_to_convert):
                # Conversion du DataFrame en CSV encodé en UTF-8
                return df_to_convert.to_csv(index=False).encode('utf-8')

            csv_file = convert_df(df_clean)

            st.download_button(
                label="📥 Télécharger les données (CSV)",
                data=csv_file,
                file_name='agrostat_insight_export.csv',
                mime='text/csv',
                help="Téléchargez l'intégralité du registre pour Excel ou un rapport externe."
            )
        
        with col_exp2:
            st.caption("💡 Le fichier CSV exporté contient toutes les lignes validées et synchronisées avec le Cloud Google Sheets.")

    else:
        # Message si la base est vide
        st.info("👋 Le registre est vide. Ajoutez des données via la barre latérale pour activer les analyses.")
        st.image("https://images.unsplash.com/photo-1523348837708-15d4a09cfac2?auto=format&fit=crop&q=80&w=1000", 
                 caption="Prêt pour l'analyse de vos parcelles.")

if __name__ == "__main__":
    main()
    # https://docs.google.com/spreadsheets/d/1g5Zs-fYLtldBzbXquk6Uq6QIAmYQtZQ_QE7olFbp61A/edit?usp=sharing    lien pour le googlesheets