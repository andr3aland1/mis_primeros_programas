""" Si bien el while es útil cuando desconocemos la cantidad de veces que repetiremos un bloque de instrucciones,
también puede ser utilizado en los mismos casos que es utilizado el For (aunque la inversa no es verdadera). 
Rehaga todos los ejercicios del Trabajo Práctico VI utilizando un While en lugar de un For. """

""" Crea un script que le solicite al usuario ingresar 10 números enteros, y por cada uno, 
informarle si el mismo es positivo, negativo, o cero."""

contador = 0

while contador != 10:
    contador += 1
    numero = int(input("Ingrese un número entero: "))
    if numero > 0:
        print(f"El número {numero} es positivo")
    elif numero < 0:
        print(f"El número {numero} es negativo")
    else: 
        print("El número es cero")