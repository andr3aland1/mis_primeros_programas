contador = 0
nombres = ""
primer_nombre= input("Para salir escriba fin sino ingrese un nombre: ")
while primer_nombre != "fin" and nombres != "fin":
    nombres = input("Para salir escriba fin sino ingrese el siguiente nombre: ")
    if primer_nombre == nombres:
        contador += 1
if primer_nombre != "fin": #En el caso que el usuario escriba fin al comienzo
    print(f"El primer nombre {primer_nombre} se repite {contador} veces") 