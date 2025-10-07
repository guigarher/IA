import numpy as np

lista = np.random.randint(0, 100, size=10) # Generar un array de 10 números aleatorios entre 0 y 100

print("Lista generada:", lista) # Mostrar el array generado

print("Media:", np.mean(lista)) # Calcular y mostrar la media
print("Desviación estándar:", np.std(lista)) # Calcular y mostrar la desviación estándar
print("Máximo:", np.max(lista)) # Calcular y mostrar el valor máximo
print("Mínimo:", np.min(lista)) # Calcular y mostrar el valor mínimo

matriz = np.random.randint(0, 100, size=(3, 3)) # Generar una matriz 3x3 de números aleatorios entre 0 y 100