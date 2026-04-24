# 🌱 AgroStat Insight v1.0
> **Plateforme d'Intelligence Artificielle pour l'Optimisation des Rendements Agricoles.**

![GitHub language count](https://img.shields.io/github/languages/count/Danielisprogrammer/KENGNE_TACHAGO_DANIEL_VAHID__23U2590_AgroStat-Insight?style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/Danielisprogrammer/KENGNE_TACHAGO_DANIEL_VAHID__23U2590_AgroStat-Insight?style=for-the-badge)

---

## 🎯 Présentation du Projet
AgroStat Insight est une solution de **Data Science** permettant de transformer les données brutes de terrain en décisions stratégiques. Grâce à l'intégration de la **Régression Linéaire**, l'application prédit les récoltes futures en fonction des intrants.

### 🚀 Fonctionnalités Clés
- 📊 **Dashboard Interactif** : Visualisation en temps réel via [Plotly](https://plotly.com/python/).
- 🧠 **Moteur d'Analyse (IA)** : Calcul automatique des coefficients de corrélation de Pearson.
- 🗄️ **Base de Données SQLite** : Persistance des données locale et sécurisée.
- 📱 **Interface Responsive** : Développée avec [Streamlit](https://streamlit.io/).

---

## 🛠️ Stack Technique
| Technologie | Utilisation |
| :--- | :--- |
| **Python 3.12** | Langage Coeur |
| **Streamlit** | Interface Utilisateur (UI) |
| **Scikit-Learn** | Modélisation Prédictive (IA) |
| **Pandas** | Manipulation de données |
| **SQLAlchemy** | Gestion de la base de données |

---

## ⚙️ Installation et Lancement
Pour installer ce projet sur votre machine locale, suivez ces étapes :

### 1. Clonage du Dépôt
```bash
git clone [https://github.com/Danielisprogrammer/KENGNE_TACHAGO_DANIEL_VAHID__23U2590_AgroStat-Insight.git](https://github.com/Danielisprogrammer/KENGNE_TACHAGO_DANIEL_VAHID__23U2590_AgroStat-Insight.git)
cd AgroStat_Insight_v1.0
2. Configuration de l'EnvironnementBash# Créer l'environnement virtuel
python3 -m venv venv

# Activer l'environnement
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt
3. ExécutionBashstreamlit run app.py
🧠 Méthodologie StatistiqueLe projet repose sur la Régression Linéaire Simple. L'équation de prédiction est modélisée sous la forme :$$y = ax + b$$Où $y$ est le rendement et $x$ l'engrais. Le score $R^2$ permet de valider la précision du modèle.👨‍💻 DéveloppeurKENGNE TACHAGO DANIEL VAHIDMatricule : 23U2590Niveau : Informatique L2Profil : GitHub | [Portfolio en cours]Développé dans le cadre du TP de Programmation Python - 2026
### 2. Pourquoi cette version est "Professionnelle" ?
1.  **Les Badges (en haut)** : Ils affichent dynamiquement la taille du projet et les langages utilisés. Ça fait très "Open Source".
2.  **Le Tableau (Stack Technique)** : C'est beaucoup plus lisible qu'une simple liste.
3.  **Les Liens Cliquables** : Les mots comme "Streamlit" ou "Plotly" renvoient vers leurs sites officiels.
4.  **Le Rendu Mathématique** : L'équation $y = ax + b$ s'affichera proprement grâce au support LaTeX de GitHub.
5.  **Les Blockquotes** : Le petit `>` au début crée un encadré gris élégant.

### 3. Comment l'envoyer proprement maintenant ?
Comme tu viens de réussir ton `git push` léger, fais juste ceci pour mettre à jour le README :

```bash
git add README.md
git commit -m "Design : Amélioration visuelle du README"
git push