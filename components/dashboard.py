import streamlit as st
import pandas as pd
import plotly.express as px
from core.stats_engine import AnalystEngine

def render_metrics(df):
    """Affiche les indicateurs clés de performance (KPI)."""
    st.markdown("### 📊 Vue d'ensemble")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Relevés", len(df))
    with col2:
        # CORRECTION : On utilise 'rendement' en minuscules
        avg_yield = df["rendement"].mean()
        st.metric("Rendement Moyen", f"{avg_yield:.2f} T/ha")
    with col3:
        # CORRECTION : On utilise 'humidite' en minuscules
        avg_moist = df["humidite"].mean()
        st.metric("Humidité Moyenne", f"{avg_moist:.1f} %")
    with col4:
        # CORRECTION : On utilise 'engrais' en minuscules
        total_fert = df["engrais"].sum()
        st.metric("Engrais Total", f"{total_fert:.0f} kg")

def render_charts(df):
    """Génère les graphiques et l'intelligence prédictive."""
    st.markdown("---")
    
    tab1, tab2, tab3 = st.tabs(["📊 Distributions", "🔗 Corrélations & IA", "📋 Registre Brut"])

    # --- ONGLET 1 : DISTRIBUTIONS ---
    with tab1:
        c1, c2 = st.columns(2)
        with c1:
            fig_hist = px.histogram(df, x="rendement", color="culture", 
                                   title="Distribution du Rendement",
                                   template="plotly_dark", barmode="group")
            st.plotly_chart(fig_hist, use_container_width=True)
        with c2:
            fig_box = px.box(df, x="culture", y="rendement", color="culture",
                            title="Variabilité par Culture",
                            points="all", template="plotly_dark")
            st.plotly_chart(fig_box, use_container_width=True)

    # --- ONGLET 2 : CORRÉLATIONS ET RÉGRESSION ---
    with tab2:
        st.markdown("#### Impact des intrants sur la productivité")
        
        # Graphique à bulles avec noms en minuscules
        fig_scatter = px.scatter(df, x="engrais", y="rendement", color="culture",
                                 size="humidite", trendline="ols",
                                 title="Régression Visuelle : Engrais vs Rendement",
                                 template="plotly_dark")
        st.plotly_chart(fig_scatter, use_container_width=True)

        # Calcul des statistiques
        a, b, r2 = AnalystEngine.get_regression_formula(df)
        corr = AnalystEngine.calculate_correlation(df)

        st.markdown("---")
        st.subheader("🧠 Intelligence Décisionnelle")

        if a is not None:
            c1, c2, c3 = st.columns(3)
            with c1:
                st.metric("Corrélation de Pearson", f"{corr:.2f}")
            with c2:
                st.write("**Modèle de Prédiction :**")
                st.latex(rf"y = {a:.3f}x + {b:.3f}")
            with c3:
                st.metric("Fiabilité (R²)", f"{r2*100:.1f} %")
        else:
            st.info("💡 Ajoutez plus de données pour activer l'analyse.")

    # --- ONGLET 3 : REGISTRE ---
    with tab3:
        st.markdown("#### Journal de bord")
        # On affiche le tableau (Pandas affiche les noms de colonnes tels qu'ils sont)
        st.dataframe(df.sort_values(by="date", ascending=False), use_container_width=True)