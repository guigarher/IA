# UD02A01 - Ejercicios básicos de Python

usuario_evagd = "Guillermo Felipe García Hernández"

#1.      Conversión de tipos y entrada de datos
def suma_enteros():
    """Función que pide dos números enteros y devuelve su suma."""
    try:
        num1 = int(input("Introduce el primer número entero: "))
        num2 = int(input("Introduce el segundo número entero: "))
        return num1 + num2
    except ValueError:
        print("Por favor, introduce números enteros válidos.")
        return None
print("La suma de los dos números es:", suma_enteros())
print(f"Usuario evagd: {usuario_evagd}")

#2.      Control de flujo (if/else)
def es_par(numero):
    """Función que determina si un número es par o impar."""
    if numero % 2 == 0: # Si el número es divisible por 2, es par
        return True
    else:
        return False
numero = int(input("Introduce un número para verificar si es par o impar: ")) 
if es_par(numero):
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")
print(f"Usuario evagd: {usuario_evagd}")

#3.      Bucles 
def tabla_multiplicar(n):
    """Función que imprime la tabla de multiplicar del número n."""
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}") 
num = int(input("Introduce un número para ver su tabla de multiplicar: "))
tabla_multiplicar(num)
print(f"Usuario evagd: {usuario_evagd}")

#4.      Estadísticas 
def estadisticas(lista):
    """Función que devuelve un diccionario con el mínimo, máximo y media de una lista numérica."""
    if not lista: 
        return {"mínimo": None, "máximo": None, "media": None} # Manejo de lista vacía
    
    minimo = min(lista) # Encontrar el valor mínimo
    maximo = max(lista) # Encontrar el valor máximo
    media = sum(lista) / len(lista) # Calcular la media
    
    return {"mínimo": minimo, "máximo": maximo, "media": media} # Devolver los resultados en un diccionario
numeros = [int(x) for x in input("Introduce una lista de números separados por espacios: ").split()] 
resultados = estadisticas(numeros) 
print("Estadísticas:", resultados)
print(f"Usuario evagd: {usuario_evagd}")

#5.      Diccionarios y conteo
def contar_palabras(texto):
    """Función que cuenta la frecuencia de cada palabra en un texto."""
    palabras = texto.split() # Dividir el texto en palabras
    frecuencia = {} # Diccionario para almacenar la frecuencia de las palabras
    
    for palabra in palabras: 
        palabra = palabra.lower().strip('.,!?;"()[]{}')  # Normalizar la palabra
        if palabra in frecuencia:
            frecuencia[palabra] += 1 # Incrementar el conteo si la palabra ya está en el diccionario
        else:
            frecuencia[palabra] = 1 # Inicializar el conteo si es la primera vez que aparece la palabra
            
    return frecuencia 
texto = input("Introduce un texto para contar la frecuencia de las palabras: ")
frecuencia_palabras = contar_palabras(texto) 
print("Frecuencia de palabras:", frecuencia_palabras) 
print(f"Usuario evagd: {usuario_evagd}")

#6.      Listas por comprensión
def cuadrados(lista):
    """Función que devuelve una lista con los cuadrados de los números de la lista original."""
    return [x**2 for x in lista] # Lista por comprensión para calcular los cuadrados
numeros = [int(x) for x in input("Introduce una lista de números separados por espacios: ").split()] 
cuadrados_numeros = cuadrados(numeros)
print("Cuadrados de los números:", cuadrados_numeros)
print(f"Usuario evagd: {usuario_evagd}")

#7.      Cadenas y slicing
def es_palindromo(cadena):
    """Función que verifica si una cadena es un palíndromo."""
    cadena = cadena.replace(" ", "").lower() # Normalizar la cadena
    return cadena == cadena[::-1] # Comparar la cadena con su reverso
texto = input("Introduce una cadena para verificar si es un palíndromo: ")
if es_palindromo(texto):
    print(f'La cadena "{texto}" es un palíndromo.')
else:
    print(f'La cadena "{texto}" no es un palíndromo.')
print(f"Usuario evagd: {usuario_evagd}")

#8.      Generación de listas
def pares_hasta(n):
    """Función que devuelve una lista con todos los números pares desde 0 hasta n."""
    return [x for x in range(n + 1) if x % 2 == 0]
n = int(input("Introduce un número para generar una lista de números pares hasta ese número: "))
lista_pares = pares_hasta(n)
print("Números pares hasta", n, ":", lista_pares)
print(f"Usuario evagd: {usuario_evagd}")

#9.      Excepciones
def division_segura(a, b):
    """Función que realiza una división segura."""
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: División por cero no permitida."
num1 = float(input("Introduce el dividendo (a): "))
num2 = float(input("Introduce el divisor (b): "))
resultado_division = division_segura(num1, num2)
print("Resultado de la división:", resultado_division)
print(f"Usuario evagd: {usuario_evagd}")

#10.  Tuplas y desempacado
def min_max(lista):
    """Función que devuelve el mínimo y máximo de una lista como una tupla."""
    if not lista:
        return (None, None)
    return (min(lista), max(lista)) # Devolver el mínimo y máximo como una tupla
numeros = [int(x) for x in input("Introduce una lista de números separados por espacios: ").split()]
minimo, maximo = min_max(numeros)
print(f"Mínimo: {minimo}, Máximo: {maximo}")
print(f"Usuario evagd: {usuario_evagd}")

#11.  Clases y objetos Crea una clase Rectangulo con atributos ancho y alto, y un método area() que devuelva el área.
class Rectangulo:
    def __init__(self, ancho, alto): # Constructor de la clase
        self.ancho = ancho # Atributo ancho
        self.alto = alto # Atributo alto
    
    def area(self): # Método para calcular el área
        return self.ancho * self.alto 
ancho = float(input("Introduce el ancho del rectángulo: "))
alto = float(input("Introduce el alto del rectángulo: "))
rectangulo = Rectangulo(ancho, alto) # Crear una instancia de Rectangulo
print("El área del rectángulo es:", rectangulo.area()) 
print(f"Usuario evagd: {usuario_evagd}")
