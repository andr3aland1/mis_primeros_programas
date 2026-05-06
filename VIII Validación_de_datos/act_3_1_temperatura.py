"""Modifica todos los ejercicios anteriores para que en lugar de permitir reintentos de manera ilimitada, 
el programa permita sólo 10 reintentos. Si el usuario supera el límite de reintentos, el programa debe terminar 
con el mensaje “Usted está jugando conmigo, yo me retiro”. """

""" Crea un script que le solicite al usuario ingresar una temperatura en grados Celsius, 
y valide que la entrada es correcta, teniendo en cuenta que la temperatura debe ser un valor numérico, 
y el rango válido está entre -18 y 50. El programa debe permitir ingresar el dato cuantas veces sea necesario, 
hasta que el usuario provea un dato válido. Procure informar al usuario cuando su dato es inválido, 
y cuáles son los valores aceptados. """ 

intentos = 0

temperatura = int(input("Ingrese la temperatura en grados Celsius: "))

while (temperatura < -18 or temperatura > 50) and intentos < 10:

    intentos += 1

    temperatura = int(input("Dato inválido. Ingrese una temperatura entre -18 y 50 ºC: "))

if intentos == 10:

    print("Usted está jugando conmigo, yo me retiro")

else:

    print("La temperatura", temperatura, "es un dato válido")