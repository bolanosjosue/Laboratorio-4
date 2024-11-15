# data_processing.py
import pandas as pd
import numpy as np
from scipy.stats import zscore
from sklearn.preprocessing import StandardScaler

# Función para cargar y preparar el dataset
def cargar_y_preparar_datos(url):
    # Cargar el dataset desde GitHub
    data = pd.read_csv(url)

    # Tratar valores nulos
    data.fillna(data.mean(numeric_only=True), inplace=True)
    data.fillna("Desconocido", inplace=True)

    # Eliminar duplicados
    data.drop_duplicates(inplace=True)

    # Filtrar valores atípicos usando Z-score
    numerical_columns = data.select_dtypes(include=[np.number]).columns
    data = data[(np.abs(zscore(data[numerical_columns])) < 3).all(axis=1)]

    # Cambiar nombres de columnas
    data.columns = [col.strip().replace(" ", "_").lower() for col in data.columns]

    # One-Hot Encoding para variables categóricas
    data = pd.get_dummies(data, drop_first=True)
    
    return data, numerical_columns

# Función para normalizar los datos (Requisito 8)
def normalizar_datos(data, numerical_columns):
    scaler = StandardScaler()
    data[numerical_columns] = scaler.fit_transform(data[numerical_columns])
    print("\nDatos normalizados.")