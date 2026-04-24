import streamlit as st
import pandas as pd
from datetime import datetime

def render_sidebar():
    """Gère la saisie des données dans la barre latérale."""
    st.sidebar.header("📥 Saisie des Données")
    
    # Création du formulaire de saisie
    with st.sidebar.form("agri_form"):
        date = st.date_input("Date du relevé", datetime.now())
        culture = st.selectbox("Type de Culture", ["Maïs", "Soja", "Blé", "Riz", "Cacao"])
        engrais = st.number_input("Quantité d'Engrais (kg)", min_value=0.0, step=1.0)
        humidite = st.slider("Taux d'Humidité (%)", 0, 100, 50)
        rendement = st.number_input("Rendement Obtenu (T/ha)", min_value=0.0, step=0.1)
        
        submitted = st.form_submit_button("Enregistrer le relevé")
        
        if submitted:
            # On crée un DataFrame avec les noms en MINUSCULES pour SQLite
            new_data = pd.DataFrame([{
                "date": date.strftime("%Y-%m-%d"),
                "culture": culture,
                "engrais": engrais,
                "humidite": humidite,
                "rendement": rendement
            }])
            return new_data

    # --- SIGNATURE EXPERT (Hors du formulaire) ---
    st.sidebar.markdown("---")
    st.sidebar.info(
        "👤 **Développeur :** KENGNE TACHAGO DANIEL  VAHID\n\n"
        "🆔 **Matricule :** [23U2590]"
    )

    return None