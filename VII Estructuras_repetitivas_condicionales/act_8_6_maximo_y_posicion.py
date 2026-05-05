""" Si bien el while es útil cuando desconocemos la cantidad de veces que repetiremos un bloque de instrucciones,
también puede ser utilizado en los mismos casos que es utilizado el For (aunque la inversa no es verdadera). 
Rehaga todos los ejercicios del Trabajo Práctico VI utilizando un While en lugar de un For. """

""" Crea un script que le solicite al usuario ingresar 10 números, y una vez ingresados, 
le muestre en pantalla cuál es el máximo, y en qué posición lo ingresó. Por ejemplo, 
si el usuario ingresa los números 2, 63, -3, 20, 55, 89, 7, 32, 9, y 33, se le debería mostrar 
el mensaje “El mayor número ingresado es 89, y lo ingresaste en la posición 6”. 
NOTA: las posiciones posibles comienzan desde 1. """

contador = 0

while contador != 10:
    
    contador += 1
    
    numero = int(input(f"Ingrese el {contador}º número: "))

    if contador == 1:
        numero_mayor = numero
        posicion_mayor = contador
    
    elif numero > numero_mayor:
        numero_mayor = numero
        posicion_mayor = contador    
    
   

print(f"El número mayor ingresado es: {numero_mayor} y lo ingresaste en la posición: {posicion_mayor}")