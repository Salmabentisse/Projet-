"""
preprocessing.py - Module de prétraitement des données
"""

import numpy as np

def check_missing_values(X_train, X_test):
    """
    Vérifie la présence de valeurs manquantes (NaN).
    
    Args:
        X_train: Données d'entraînement
        X_test: Données de test
    """
    nan_train = np.isnan(X_train.astype(float)).sum()
    nan_test = np.isnan(X_test.astype(float)).sum()
    
    print(f"✅ Vérification des valeurs manquantes:")
    print(f"   NaN train: {nan_train}")
    print(f"   NaN test:  {nan_test}")
    
    return nan_train, nan_test


def normalize_data(X_train, X_test, scale=255.0):
    """
    Normalise les données en les divisant par une valeur d'échelle.
    
    Args:
        X_train: Données d'entraînement
        X_test: Données de test
        scale: Facteur de normalisation (par défaut 255.0)
    
    Returns:
        tuple: (X_train_normalized, X_test_normalized)
    """
    X_train = X_train / scale
    X_test = X_test / scale
    
    print(f"✅ Normalisation (division par {scale}):")
    print(f"   X_train range: [{X_train.min():.3f}, {X_train.max():.3f}]")
    print(f"   X_test range:  [{X_test.min():.3f}, {X_test.max():.3f}]")
    
    return X_train, X_test
