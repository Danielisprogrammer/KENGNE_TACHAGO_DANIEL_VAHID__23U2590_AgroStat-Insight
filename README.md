# 🌱 AgroStat Insight v1.0
> **Plateforme d'Intelligence Artificielle pour l'Optimisation des Rendements Agricoles.**

---
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://kengne-tachago-daniel-vahid-23u2590-agrostat-insight.streamlit.app/)


## 🖼️ Aperçu du Projet
*(Remplacez le lien ci-dessous par le chemin de votre capture d'écran une fois ajoutée au dépôt)*

![Capture d'écran de l'application]![alt text](<Capture d’écran du 2026-04-24 06-26-53.png>)

---

## 🎯 Présentation
AgroStat Insight est une solution de **Data Science** conçue pour aider les exploitants agricoles à transformer leurs données de terrain en décisions stratégiques. L'application permet d'analyser la corrélation entre les intrants (engrais) et les résultats (rendements) via des modèles prédictifs.

---

## 🛠️ Stack Technique

| Technologie | Rôle |
| :--- | :--- |
| **Python 3.12** | Langage de programmation principal |
| **Streamlit** | Framework pour l'interface utilisateur (UI) |
| **Scikit-Learn** | Moteur d'IA et de Régression Linéaire |
| **Pandas & NumPy** | Traitement et analyse de données |
| **Plotly** | Visualisations graphiques interactives |
| **SQLite** | Système de gestion de base de données local |

---

## ⚙️ Installation et Lancement

Suivez ces étapes de manière séquentielle pour configurer votre environnement de travail :

### 1️⃣ Étape 1 : Clonage du Dépôt

Récupérez le code source depuis GitHub :

```bash
git clone [https://github.com/Danielisprogrammer/KENGNE_TACHAGO_DANIEL_VAHID__23U2590_AgroStat-Insight.git](https://github.com/Danielisprogrammer/KENGNE_TACHAGO_DANIEL_VAHID__23U2590_AgroStat-Insight.git)
```

```bash
cd KENGNE_TACHAGO_DANIEL_VAHID__23U2590_AgroStat-Insight
```

---

### 2️⃣ Étape 2 : Configuration de l'Environnement

Créez et activez un environnement virtuel :

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
Bashsource venv/bin/activate
``` 

## 3️⃣ Étape 3 : Installation des Dépendances

Installez toutes les bibliothèques nécessaires à l'exécution du projet :

```bash 
Bashpip install --upgrade pip
```
```bash 
Bashpip install -r requirements.txt
```

## 4️⃣ Étape 4 : Lancement de l'ApplicationDémarrez le serveur local Streamlit pour visualiser l'application :Bashstreamlit run app.py

### 🧠 Méthodologie Statistique 

Le moteur d'analyse repose sur la Régression Linéaire Simple. 

L'équation de prédiction est modélisée sous la forme :
$$y = ax + b$$ 
Détails des variables :$y$ : Rendement prédit (Variable dépendante)$x$ : Quantité d'engrais utilisée (Variable indépendante)$a$ : Coefficient de pente (Impact marginal de l'engrais)$b$ : Ordonnée à l'origine (Rendement sans engrais) 
La fiabilité du modèle est validée par le calcul du coefficient de détermination $R^2$ et la corrélation de Pearson.👨‍💻 

```bash
Développeur: KENGNE TACHAGO DANIEL VAHID
🆔 Matricule : 23U2590
🏫 Niveau : Université - Informatique L2🔗 Profil : Mon GitHubProjet réalisé dans le cadre du Travail Pratique de Programmation Python - Avril 2026
```