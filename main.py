# main.py
from tkinter import Tk, Label, Button, OptionMenu, StringVar, messagebox
import data_processing as dp
import visualizations as vz

# Cargar, preparar y normalizar datos
url = 'https://raw.githubusercontent.com/bolanosjosue/Laboratorio-4/main/datos.csv'
data, numerical_columns = dp.cargar_y_preparar_datos(url)

# Normalizar los datos al inicio
dp.normalizar_datos(data, numerical_columns)
print("Datos normalizados.")

# Función para mostrar el gráfico seleccionado
def mostrar_grafico():
    tipo_grafico = grafico_var.get()
    columna1 = columna1_var.get()
    columna2 = columna2_var.get()
    
    # Validación: verificar que se haya seleccionado la primera columna
    if columna1 == "Seleccione columna":
        messagebox.showerror("Error", "Debe seleccionar la primera columna antes de generar el gráfico.")
        return
    
    # Lógica para mostrar gráficos según la selección
    if tipo_grafico == "Histograma":
        vz.plot_histograma(data, columna1)
    elif tipo_grafico == "Boxplot":
        vz.plot_boxplot(data, columna1)
    elif tipo_grafico == "Dispersión":
        if columna2 == "Seleccione columna":
            messagebox.showerror("Error", "Seleccione ambas columnas para el gráfico de dispersión.")
        else:
            vz.plot_dispersion(data, columna1, columna2)
    elif tipo_grafico == "Matriz de Correlación":
        vz.plot_matriz_correlacion(data, numerical_columns)
    elif tipo_grafico == "Barras":
        vz.plot_barras(data, columna1)
    elif tipo_grafico == "Densidad":
        vz.plot_densidad(data, columna1)
    else:
        messagebox.showerror("Error", "Seleccione un tipo de gráfico.")

# Función para salir de la aplicación
def salir():
    root.quit()
    root.destroy()

# Configuración de la interfaz de Tkinter
root = Tk()
root.title("Visualización de Gráficos")
root.geometry("400x400")

# Variables de selección para Tkinter
grafico_var = StringVar(root)
grafico_var.set("Seleccione tipo de gráfico")

columna1_var = StringVar(root)
columna1_var.set("Seleccione columna")

columna2_var = StringVar(root)
columna2_var.set("Seleccione columna")

# Menú de opciones para el tipo de gráfico
Label(root, text="Seleccione el tipo de gráfico:").pack(pady=10)
opciones_graficos = ["Histograma", "Boxplot", "Dispersión", "Matriz de Correlación", "Barras", "Densidad"]
OptionMenu(root, grafico_var, *opciones_graficos).pack()

# Menú de opciones para columna 1
Label(root, text="Seleccione la primera columna:").pack(pady=10)
OptionMenu(root, columna1_var, *numerical_columns).pack()

# Menú de opciones para columna 2 (solo para gráficos de dispersión)
Label(root, text="Seleccione la segunda columna (solo para dispersión):").pack(pady=10)
OptionMenu(root, columna2_var, *numerical_columns).pack()

# Botón para mostrar el gráfico seleccionado
Button(root, text="Mostrar Gráfico", command=mostrar_grafico).pack(pady=10)

# Botón para salir de la aplicación
Button(root, text="Salir", command=salir).pack(pady=10)

# Ejecutar la interfaz
root.mainloop()
