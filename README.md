# Projet MNIST - Classification des Chiffres Manuscrits

**Auteurs:** Salma Bentisse   
**Date:** Juin 2026

## Objectif
Ce projet utilise TensorFlow et Keras pour charger et traiter le dataset MNIST, permettant la classification des chiffres manuscrits.

## Structure du Projet
```
tp2/
├── Untitled.ipynb          # Notebook principal
├── data_loader.py          # Module de chargement des données
├── preprocessing.py        # Module de prétraitement
├── README.md              # Ce fichier
└── .gitignore             # Fichiers à ignorer dans Git
```

## Installation

1. Créer un environnement virtuel:
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
```

2. Installer les dépendances:
```bash
pip install tensorflow numpy matplotlib seaborn
```

## Utilisation

Exécuter le notebook:
```bash
jupyter notebook Untitled.ipynb
```

## Données
Le dataset MNIST est téléchargé automatiquement par TensorFlow. Il ne sera **pas versionné** dans le dépôt Git.

## Critères de Validation

| Critère | Statut |
|---------|--------|
| Présence du fichier README.md | ✅ |
| Noms et Prénoms dans le README | ✅ |
| Dataset non versionné | ✅ |
| Code modulaire (.py importés) | ✅ |
