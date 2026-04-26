""" Crea un script que le solicite al usuario ingresar 10 números, y una vez ingresados, 
le muestre en pantalla cuál es el máximo, y en qué posición lo ingresó. Por ejemplo, 
si el usuario ingresa los números 2, 63, -3, 20, 55, 89, 7, 32, 9, y 33, se le debería mostrar 
el mensaje “El mayor número ingresado es 89, y lo ingresaste en la posición 6”. 
NOTA: las posiciones posibles comienzan desde 1. """

maximo = 0

for i in range (1,11):
    numero = int(input("Ingrese un número: "))
    if numero > maximo:
        maximo = numero
        posicion = i
print(f"El número máximo es {maximo} y fue ingresado en la posición {posicion}")