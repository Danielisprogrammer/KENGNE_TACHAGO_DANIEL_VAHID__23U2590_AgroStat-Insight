# 🌱 AgroStat Insight v1.0
> **Intelligence Artificielle et Analyse de Données pour l'Optimisation Agricole.**

AgroStat Insight est une application web de **Data Science** conçue pour aider les agriculteurs et ingénieurs agronomes à suivre la santé de leurs parcelles et à prédire les rendements grâce à la puissance de la régression linéaire.



## 🚀 Fonctionnalités Clés
* **Collecte de Données Intelligente** : Enregistrement structuré des cultures, apports en engrais, humidité et rendements.
* **Intelligence Décisionnelle (IA)** : Modélisation mathématique ($y = ax + b$) pour prédire la récolte en fonction des intrants.
* **Visualisation Interactive** : Graphiques dynamiques (Scatter plots, Histogrammes, Box plots) via Plotly.
* **Persistance SQLite** : Base de données locale sécurisée pour conserver l'historique sans serveur lourd.
* **Export Professionnel** : Téléchargement du registre au format CSV pour analyse externe.

## 🛠️ Stack Technique
* **Langage** : Python 3.12
* **Interface** : [Streamlit](https://streamlit.io/)
* **Analyse de données** : Pandas & Numpy
* **Machine Learning** : Scikit-Learn
* **Visualisation** : Plotly Express
* **Base de données** : SQLite3

## 📂 Structure du Projet
```text
AgroStat_Insight/
├── app.py                # Point d'entrée principal
├── components/           # Composants UI (Sidebar, Dashboard)
├── core/                 # Logique métier (IA, Base de données)
├── data/                 # Stockage des fichiers SQLite
└── requirements.txt      # Dépendances du projet
⚙️ Installation et Lancement
Cloner le projet :

```bash
git clone [https://github.com/Danielisprogrammer/KENGNE_TACHAGO_DANIEL_VAHID__23U2590_AgroStat-Insight.git]

```bash
cd AgroStat_Insight

Créer l'environnement virtuel :

```bash
python -m venv venv
source venv/bin/activate  # Sur Linux/Mac

Installer les dépendances :

```bash
pip install -r requirements.txt
Lancer l'application :

``bash
streamlit run app.py

🧠 Méthodologie Statistique
L'application utilise le coefficient de Corrélation de Pearson pour mesurer le lien entre l'engrais et le rendement, ainsi qu'une Régression Linéaire Simple pour fournir une équation de prévision fiable.

```bash
Développé avec passion par Daniel Kengne Étudiant en Informatique (L2) - Passionné par le développement Full-Stack et l'IA.