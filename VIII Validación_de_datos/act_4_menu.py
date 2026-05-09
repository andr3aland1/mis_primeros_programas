""" La técnica de validación para un conjunto específico de valores se puede utilizar para construir menús de opciones. 
Construye un menú que le muestre al usuario lo siguiente: 
********* MI PROGRAMA ********* 
1. Saludar. 
2. Informar temperatura. 
3. Mostrar nombre de materia. 
4. Salir. 
Seleccionar una opción [1-4]: 
- Cuando el usuario ingrese la opción 1, se mostrará el mensaje “Hola, bienvenido a mi programa interactivo!”. 
- Cuando el usuario ingrese la opción 2, se mostrará el mensaje “Hay una sensación térmica de 20 grados Celsius.”. 
- Cuando el usuario ingrese la opción 3, se mostrará el mensaje “Estás en la materia Introducción a la Programación!”. 
- Cuando el usuario ingrese la opción 4, el programa debe terminar, mostrando el mensaje “Hasta la próxima!”. 
- Si el usuario ingresa una opción inválida, se muestra el mensaje “Opción inválida.”. """

import os

opcion = ""


while opcion != "4":
    
    print("********** MI PROGRAMA **********\n1. Saludar.\n2. Informar temperatura.\n3. Mostrar nombre de materia.\n4. Salir.\n")
   
    opcion = input("Ingrese una opción: ")
   
    if opcion == "1":
        print(f"\nHola, bienvenido a mi programa interactivo!\n")
    
    elif opcion == "2":
        print(f"\nHay una sensación térmica de 20 grados Celsius.\n")

    elif opcion == "3":
        print(f"\nEstás en la materia Introducción a la Programación!\n")

    elif opcion == "4":
        print("\nHasta la próxima!")

    else:
        print(f"\nOpción inválida.\n")
    
    if opcion != "4":
        input(f"Presione una tecla para volver al menu: ")
        os.system('cls')