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

temperatura = 15
opcion = 0 

while opcion != 4:

    print(f"********* MI PROGRAMA *********\n1. Saludar.\n2. Informar temperatura.\n3. Mostrar nombre de materia.\n4. Salir.")
   
    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        print("Hola!")

    elif opcion == 2:
        print (f"La temperatura es: {temperatura} ºC")

    elif opcion == 3:
        print (f"Introducción a la programación")

    elif opcion == 4:
        print("Adios!")

    else:
        print("Opción inválida.")