# visualizations.py
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis

# Función para mostrar histograma 
def plot_histograma(data, column):
    plt.figure()
    sns.histplot(data[column], kde=True)
    plt.title(f"Histograma de {column}")
    plt.xlabel(column)
    plt.ylabel("Frecuencia")
    plt.show()

# Función para mostrar boxplot 
def plot_boxplot(data, column):
    plt.figure()
    sns.boxplot(y=data[column])
    plt.title(f"Boxplot de {column}")
    plt.ylabel(column)
    plt.show()

# Función para mostrar dispersión 
def plot_dispersion(data, column1, column2):
    plt.figure()
    sns.scatterplot(data=data, x=column1, y=column2)
    plt.title(f"Gráfico de Dispersión entre {column1} y {column2}")
    plt.xlabel(column1)
    plt.ylabel(column2)
    plt.show()

# Función para mostrar matriz de correlación    
def plot_matriz_correlacion(data, numerical_columns):
    plt.figure(figsize=(10, 8))
    correlation_matrix = data[numerical_columns].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Matriz de Correlación entre Variables Numéricas")
    plt.show()

# Función para mostrar gráfico de barras 
def plot_barras(data, column):
    plt.figure(figsize=(12, 6))  # Ajuste de tamaño para dar más espacio a las barras
    ax = data[column].value_counts().plot(kind='bar')
    plt.title(f"Frecuencia de categorías en {column}")
    plt.xlabel(column)
    plt.ylabel("Frecuencia")
    
    # Rotar etiquetas y mostrar solo algunas para evitar amontonamiento
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', fontsize=8)
    
    # Mostrar solo cada n-ésima etiqueta si son demasiadas
    for index, label in enumerate(ax.get_xticklabels()):
        if index % 5 != 0:  # Ajusta '5' según la cantidad de datos para ver menos etiquetas
            label.set_visible(False)

    plt.tight_layout()  # Ajustar para que no se corten etiquetas
    plt.show()

# Función para mostrar gráfico de densidad 
def plot_densidad(data, column):
    plt.figure()
    sns.kdeplot(data[column], fill=True)
    plt.title(f"Densidad de {column}")
    plt.xlabel(column)
    plt.ylabel("Densidad")
    plt.show()

# Función para mostrar asimetría y curtosis 
def plot_asimetria_y_kurtosis(data, numerical_columns):
    for column in numerical_columns:
        skewness = skew(data[column].dropna())
        kurt = kurtosis(data[column].dropna())
        print(f"{column} - Asimetría: {skewness:.2f}, Kurtosis: {kurt:.2f}")
