# 🌱 AgroStat Insight v1.0
> **Plateforme d'Intelligence Artificielle pour l'Optimisation des Rendements Agricoles.**

![GitHub language count](https://img.shields.io/github/languages/count/Danielisprogrammer/KENGNE_TACHAGO_DANIEL_VAHID__23U2590_AgroStat-Insight?style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/Danielisprogrammer/KENGNE_TACHAGO_DANIEL_VAHID__23U2590_AgroStat-Insight?style=for-the-badge)

---

## 🎯 Présentation du Projet
AgroStat Insight est une solution de **Data Science** permettant de transformer les données brutes de terrain en décisions stratégiques. Grâce à l'intégration de la **Régression Linéaire**, l'application prédit les récoltes futures en fonction des intrants.

### 🚀 Fonctionnalités Clés
- 📊 **Dashboard Interactif** : Visualisation en temps réel via [Plotly](https://plotly.com/python/).
- 🧠 **Moteur d'Analyse (IA)** : Calcul automatique des coefficients de corrélation.
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

Suivez ces étapes dans l'ordre pour configurer le projet sur votre machine locale (Linux/Ubuntu) :

### 1️⃣ Clonage du Dépôt
Commencez par récupérer le code source depuis GitHub :
```bash
git clone [https://github.com/Danielisprogrammer/KENGNE_TACHAGO_DANIEL_VAHID__23U2590_AgroStat-Insight.git](https://github.com/Danielisprogrammer/KENGNE_TACHAGO_DANIEL_VAHID__23U2590_AgroStat-Insight.git)
cd KENGNE_TACHAGO_DANIEL_VAHID__23U2590_AgroStat-Insight
2️⃣ Configuration de l'EnvironnementIl est recommandé d'utiliser un environnement virtuel pour isoler les dépendances :Bash# Création de l'environnement
python3 -m venv venv

# Activation (Linux/Ubuntu)
source venv/bin/activate
3️⃣ Installation des DépendancesInstallez toutes les bibliothèques nécessaires listées dans le fichier requirements.txt :Bashpip install --upgrade pip
pip install -r requirements.txt
4️⃣ Lancement de l'ApplicationUne fois l'installation terminée, lancez le serveur local Streamlit :Bashstreamlit run app.py
🧠 Méthodologie StatistiqueLe projet repose sur la Régression Linéaire Simple. L'équation de prédiction est modélisée sous la forme :$$y = ax + b$$Où :$y$ : Rendement prédit (Variable dépendante)$x$ : Quantité d'engrais (Variable indépendante)$a$ : Coefficient de pente (Impact de l'engrais)$b$ : Ordonnée à l'origineLe score $R^2$ est utilisé pour valider la fiabilité statistique du modèle.👨‍💻 DéveloppeurKENGNE TACHAGO DANIEL VAHID🆔 Matricule : 23U2590🏫 Niveau : Université - Informatique L2🔗 Profil : GitHubProjet réalisé dans le cadre du Travail Pratique de Programmation Python - 2026
---

### Comment le mettre à jour sur GitHub ?

1.  **Ouvre ton fichier `README.md`** dans VS Code.
2.  **Efface tout** et colle le code ci-dessus.
3.  **Enregistre.**
4.  **Envoie la mise à jour** avec ces commandes :

```bash
git add README.md
git commit -m "Docs: Structuration professionnelle du README en étapes"
git push