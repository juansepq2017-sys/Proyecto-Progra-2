import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar el dataset (reemplaza 'datos.csv' por el nombre real de tu archivo

# Si es un archivo de Excel, usa esta línea en su lugar:
df = pd.read_excel('DATASET_proyecto_dic.xlsx')

# 2. Ver las primeras filas para confirmar que se cargó bien
print("Primeras filas del dataset:")
print(df.head(30))

# 3. Ver información general (tipos de datos, valores nulos, columnas)
print("Información general del dataset:")
print(df.info())

# Manejo de Datos Faltantes

#Boxplot de Outliers... En las variables Ages y Credit Amount.
# Box plot de Age
df.boxplot(column="Age", grid=False)
plt.title("Box plot de Age (Outliers)")
plt.ylabel("Edad")
plt.show()

# Box plot de Credit amount
df.boxplot(column="Credit amount", grid=False)
plt.title("Box plot de Credit amount (Outliers)")
plt.ylabel("Monto del crédito")
plt.show()