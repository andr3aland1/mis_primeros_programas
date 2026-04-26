""" Crea un script que le solicite al usuario ingresar 10 números enteros, y por cada uno, 
informarle si el mismo es positivo, negativo, o cero."""

for i in range (0,10):

    numero = int(input("Ingrese un número entero: "))

    if numero > 0:
        print("El número ingresado es positivo")
    elif numero < 0:
        print("El número es negativo")
    else:
        print("El número es cero") 