import numpy as np
import timeit
import pandas as pd
import matplotlib.pyplot as plt



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


medias_por_especie = df.groupby("Species").mean(numeric_only=True) # Calcular la media de las columnas numéricas agrupadas por "Species"
print("Medias por especie:\n", medias_por_especie.round(2)) # Mostrar las medias por especie


valor_maximo = df["PetalWidthCm"].max() # Encontrar el valor máximo en la columna "PetalWidthCm"
print("Valor máximo de PetalWidthCm:", valor_maximo) # Mostrar el valor máximo encontrado
fila_maxima = df[df["PetalWidthCm"] == valor_maximo] # Filtrar la fila que contiene el valor máximo
especie_maxima = fila_maxima["Species"].values[0] # Obtener la especie correspondiente al valor máximo
print("Especie con el valor máximo de PetalWidthCm:", especie_maxima) # Mostrar la especie correspondiente al valor máximo


#Matplotlib
plt.hist(df["SepalLengthCm"], bins=10, color='skyblue', edgecolor="black") # Crear un histograma de la columna "SepalLengthCm"
plt.title("Histograma de SepalLengthCm") # Título del histograma
plt.xlabel("SepalLengthCm (cm)") # Etiqueta del eje x
plt.ylabel("Frecuencia") # Etiqueta del eje y
plt.show() # Mostrar el histograma


medias = df.groupby("Species")["PetalLengthCm"].mean() # Calcular la media de "PetalLengthCm" agrupada por "Species"
print(medias) # Mostrar las medias calculadas

plt.bar(medias.index, medias.values, color=['lightcoral', 'lightgreen', 'lightblue']) # Crear un gráfico de barras con las medias
plt.title("Media de PetalLengthCm por Especie") # Título del gráfico
plt.xlabel("Especie") # Etiqueta del eje x
plt.ylabel("Media de PetalLengthCm (cm)") # Etiqueta del eje y
plt.show() # Mostrar el gráfico de barras


especies = df["Species"].unique() # Obtener las especies únicas
colores = ['lightcoral', 'lightgreen', 'lightblue'] # Definir colores para cada especie
for especie, color in zip(especies, colores): # Iterar sobre cada especie y su color correspondiente
    subset = df[df["Species"] == especie] # Filtrar el DataFrame por la especie actual
    plt.scatter(subset["SepalLengthCm"], subset["PetalLengthCm"], label=especie, color=color) # Crear un gráfico de dispersión para la especie actual
plt.title("SepalLengthCm vs PetalLengthCm") # Título del gráfico de dispersión
plt.xlabel("SepalLengthCm (cm)") # Etiqueta del eje x
plt.ylabel("PetalLengthCm (cm)") # Etiqueta del eje y
plt.legend(title="Especies") # Mostrar la leyenda del gráfico
plt.show() # Mostrar el gráfico de dispersión


#GUILLERMO FELIPE GARCÍA HERNÁNDEZ