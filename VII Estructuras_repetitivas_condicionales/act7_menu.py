""" El programa deberá mostrar el menú y reaccionar a la opción seleccionada por el usuario, 
al ejecutar una opción, en vez de terminar el programa, se mostrará nuevamente el menú, 
hasta que el usuario seleccione la opción 4. Salir. 

********* MI PROGRAMA ********* 
1. Saludar. 
2. Informar temperatura. 
3. Mostrar nombre de materia. 
4. Salir. 
Seleccione una opción [1-4]:

Tip 1: puede utilizar la instrucción os.system('cls') para limpiar la pantalla antes de volver a mostrar el menú.
De esta manera su programa será más legible en la terminal. Para poder utilizar dicha instrucción deberá importar,
al principio del script, la librería os de la siguiente manera: 

import os 
# su código
Tip 2: antes de limpiar la pantalla y volver a mostrar el menú, puede esperar a que el usuario confirme que ha terminado 
de leer la información presentada, simplemente utilizando la función input(PRESIONE ENTER PARA CONTINUAR). """

import os

opcion = 0

while opcion != 4:

    print(f"********* MI PROGRAMA *********\n1. Saludar.\n2. Informar temperatura.\n3. Mostrar nombre de materia.\n4. Salir.")

    opcion = int(input("Seleccione una opción [1-4]: "))
    
    if opcion == 1:
        print("Hola! Bienvenido!")
        input("Presione enter para continuar: ")
    elif opcion == 2:
        print("Hoy hace una temperatura de 15 ºC")
        input("Presione enter para continuar: ")
    elif opcion == 3:
        print("La materia se llama: Introcucción a la programación")
        input("Presione enter para continuar: ")
    os.system('cls')

if opcion == 4:
    print("Adios!")
