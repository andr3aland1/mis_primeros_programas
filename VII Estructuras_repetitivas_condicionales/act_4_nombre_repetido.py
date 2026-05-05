""" Realiza un programa que le permita al usuario ingresar nombres hasta que el ingreso sea “fin”, y luego retorne 
la cantidad de veces que se repite el primero de ellos."""

contador = 0
nombres = ""

primer_nombre = input("Para salir escriba fin sino ingrese un nombre: ").lower()

while primer_nombre != "fin" and nombres != "fin":
    nombres = input("Para salir escriba fin sino ingrese el siguiente nombre: ").lower()
    if primer_nombre == nombres:
        contador += 1