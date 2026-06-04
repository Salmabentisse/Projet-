# Projet MNIST - Classification des Chiffres Manuscrits

**Auteur:** Salma Bentisse  
**Date:** Juin 2026

## Description

Ce projet porte sur la classification des chiffres manuscrits avec le dataset MNIST. J'ai comparé plusieurs approches : des modèles classiques (Ridge, Lasso, ElasticNet) et des réseaux de neurones (MLP, Transfer Learning avec MobileNetV2).

## Structure

```
tp2/
├── Untitled.ipynb       # Notebook principal
├── data_loader.py       # Chargement des données MNIST
├── preprocessing.py     # Normalisation et vérification des données
├── README.md
└── .gitignore
```

## Installation

```bash
python -m venv .venv
.venv\Scripts\activate
pip install tensorflow scikit-learn numpy matplotlib seaborn pandas
```

## Utilisation

```bash
jupyter notebook Untitled.ipynb
```

## Données

Le dataset MNIST est téléchargé automatiquement via TensorFlow (`mnist.load_data()`). Il n'est pas inclus dans le dépôt.

## Résultats

| Modèle | Accuracy |
|--------|----------|
| Ridge | 85.2% |
| Lasso | 91.5% |
| ElasticNet | 91.4% |
| MLP simple | 91.8% |
| MLP optimisé | 96.8% |
| MLP avancé | 97.5% |
