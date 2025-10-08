import numpy as np
import timeit
import pandas as pd


#Numpy
array = np.random.randint(0, 100, size=10) # Generar un array de 10 números aleatorios entre 0 y 100
print("Lista generada:", array) # Mostrar el array generado
print("Media:", np.mean(array)) # Calcular y mostrar la media
print("Desviación estándar:", np.std(array)) # Calcular y mostrar la desviación estándar
print("Máximo:", np.max(array)) # Calcular y mostrar el valor máximo
print("Mínimo:", np.min(array)) # Calcular y mostrar el valor mínimo



matriz = np.random.randint(0, 100, size=(3, 3)) # Generar una matriz 3x3 de números aleatorios entre 0 y 100
matriz_invertida = matriz[::-1, ::-1] # Invertir la matriz
print("Matriz original:\n", matriz) # Mostrar la matriz original
print("Matriz invertida:\n", matriz_invertida) # Mostrar la matriz invertida



array1 = np.random.randint(0, 100, size=5) # Generar el primer array de 5 números aleatorios entre 0 y 100
array2 = np.random.randint(0, 100, size=5) # Generar el segundo array de 5 números aleatorios entre 0 y 100
suma_arrays = array1 + array2 # Sumar los dos arrays elemento a elemento
resta_arrays = array1 - array2 # Restar los dos arrays elemento a elemento
producto_arrays = array1 * array2 # Multiplicar los dos arrays elemento a elemento
producto_punto = np.dot(array1, array2) # Calcular el producto punto de los dos arrays
print("Array 1:", array1) # Mostrar el primer array
print("Array 2:", array2) # Mostrar el segundo array
print("Suma:", suma_arrays) # Mostrar la suma de los arrays
print("Resta:", resta_arrays) # Mostrar la resta de los arrays
print("Producto:", producto_arrays) # Mostrar el producto de los arrays
print("Producto punto:", producto_punto) # Mostrar el producto punto de los arrays



codigo_listas = """
lista1= list(range(1_000_000))# Crear una lista de 1,000,000 elementos
lista2= list(range(1_000_000))# Crear otra lista de 1,000,000 elementos 
suma = [lista1[i] + lista2[i] for i in range(len(lista1))] # Sumar las dos listas elemento a elemento usando comprensión de listas
"""
tiempo_listas = timeit.timeit(stmt=codigo_listas, number=10) # Medir el tiempo de ejecución del código con listas
print("Tiempo con listas:", tiempo_listas, "segundos") # Mostrar el tiempo de ejecución con listas
codigo_numpy = """
array_1 = np.arange(1_000_000)# Crear un array de 1,000,000 elementos
array_2 = np.arange(1_000_000)# Crear otro array de 1,000,000 elementos
suma = array_1 + array_2 # Sumar los dos arrays elemento a elemento usando NumPy
"""
tiempo_numpy = timeit.timeit(stmt=codigo_numpy, setup="import numpy as np", number=10) # Medir el tiempo de ejecución del código con NumPy
print("Tiempo con NumPy:", tiempo_numpy, "segundos") # Mostrar el tiempo de ejecución con NumPy



#Pandas
df = pd.read_csv("Iris.csv") # Cargar el archivo CSV en un DataFrame



print("Primeras filas del DataFrame:\n", df.head()) # Mostrar las primeras filas del DataFrame
print("Información del DataFrame:\n", df.info()) # Mostrar información del DataFrame
print("Estadísticas descriptivas:\n", df.describe()) # Mostrar estadísticas descriptivas del DataFrame


print(df.columns) # Mostrar los nombres de las columnas del DataFrame
print(df["Species"].unique()) # Mostrar los valores únicos en la columna "Species"

cond_longitud = df["SepalLengthCm"] > 5 # Condición para longitud del sépalo mayor a 5 cm
cond_especie  = df["Species"] == "Iris-setosa" # Condición para especie "Iris-setosa"

filtro = df[cond_longitud & cond_especie] # Filtrar filas que cumplen ambas condiciones
print("Filas que cumplen ambas condiciones:\n", filtro) # Mostrar las filas que cumplen ambas condiciones


df["petal_area"] = df["PetalLengthCm"] * df["PetalWidthCm"] # Crear una nueva columna "petal_area" como el producto de "PetalLengthCm" y "PetalWidthCm"
print("DataFrame con la nueva columna 'petal_area':\n", df.head()) # Mostrar las primeras filas del DataFrame con la nueva columna

