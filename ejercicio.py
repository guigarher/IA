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
print("Usuario evagd:", usuario_evagd)

#2.      Control de flujo (if/else)

def es_par(numero):
    """Función que determina si un número es par o impar."""
    if numero % 2 == 0:
        return True
    else:
        return False
numero = int(input("Introduce un número para verificar si es par o impar: "))
if es_par(numero):
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")
print("Usuario evagd:", usuario_evagd)

#3.      Bucles 
def tabla_multiplicar(n):
    """Función que imprime la tabla de multiplicar del número n."""
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
num = int(input("Introduce un número para ver su tabla de multiplicar: "))
tabla_multiplicar(num)
print("Usuario evagd:", usuario_evagd)