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

opcion = ""

while opcion != "4":

    print("********** MI PROGRAMA **********\n1. Saludar.\n2. Informar temperatura.\n3. Mostrar nombre de materia.\n4. Salir.")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        print("Hola, bienvenido a mi programa interactivo!")

    elif opcion == "2":
        print("Hay una sensación térmica de 20 grados Celsius.")

    elif opcion == "3":
        print("Estás en la materia Introducción a la Programación!")

    elif opcion == "4":
        print("Hasta la próxima!")

    else:
        print("Opción inválida.")