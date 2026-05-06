""" Si bien el while es útil cuando desconocemos la cantidad de veces que repetiremos un bloque de instrucciones,
también puede ser utilizado en los mismos casos que es utilizado el For (aunque la inversa no es verdadera). 
Rehaga todos los ejercicios del Trabajo Práctico VI utilizando un While en lugar de un For. """

"""Crea un script para calcular el factorial de un número n y mostrarlo por pantalla. Permitir calcular más de uno."""

seguir = "SI"

while seguir != "NO":

    numero = input("Ingrese un número entero positivo: ")

    while not numero.isdigit():
        numero = input("Dato inválido. Ingrese un número entero positivo: ")

    numero = int(numero)

    factorial = 1
    contador = 0

    while contador != numero:
        contador += 1
        factorial *= contador

    print(f"El factorial de {numero} es {factorial}")

    seguir = input("¿Desea calcular otro factorial? Ingrese NO para salir: ").upper()