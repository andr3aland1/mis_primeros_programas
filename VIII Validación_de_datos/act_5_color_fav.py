"""Crea un script que le solicite al usuario ingresar cuál es su color favorito, limitando las opciones a rojo, verde,
 y azul. 
 Aclaraciones: 
- Puedes asumir que el usuario ingresará los strings en minúsculas. Opcionalmente, puedes investigar el uso de las funciones 
upper() y lower() para transformar la entrada a mayúsculas o minúsculas y evitar así posibles errores de validación por este 
detalle. 
- Al validar entre un conjunto de opciones prefijadas (en lugar de hacerlo  un rango), es posible que no sea necesario validar 
el tipo del dato ingresado por teclado. 
- Al detectar un dato inválido, el programa debe darle las siguientes opciones al usuario:
 
** DATO INVÁLIDO ** 
1. Reintentar. 
2. Salir. 
- La opción 1. Reintentar le permite al usuario ingresar el dato de manera indefinida, siempre mostrando las opciones ante cada 
intento fallido.
- La opción 2. Salir finaliza el programa. """

opcion = "1"
color = ""

while opcion != "2":

    color = input("Ingrese su color favorito: ").lower()

    if color != "rojo" and color != "verde" and color != "azul":

        print("** DATO INVÁLIDO **\n1. Reintentar\n2. Salir")

        opcion = input("Elija una opción: ")


    elif color == "rojo" or color == "verde" or color == "azul":
        opcion = "2"
        print(f"Su color favorito es {color}")