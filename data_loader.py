"""
data_loader.py - Module de chargement du dataset MNIST
"""

from tensorflow.keras.datasets import mnist

def load_mnist_data():
    """
    Charge le dataset MNIST depuis TensorFlow.
    
    Returns:
        tuple: ((X_train, y_train), (X_test, y_test))
    """
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    
    print(f"✅ Dataset MNIST chargé:")
    print(f"   X_train shape: {X_train.shape}")
    print(f"   X_test shape:  {X_test.shape}")
    print(f"   y_train shape: {y_train.shape}")
    print(f"   y_test shape:  {y_test.shape}")
    
    return (X_train, y_train), (X_test, y_test)
