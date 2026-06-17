"""Modifica el script del ejercicio anterior para que la función retorne el resultado en vez de mostrarlo. 
El programa debe seguir mostrando el resultado en pantalla. 	
"""

def suma(a,b):
    """La función recibe dos números como parámetros y retorna la suma de ambos."""
    c = a + b
    return (c)

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese un número: "))

res = suma(num1, num2)

print(f"Resultado es {res}")