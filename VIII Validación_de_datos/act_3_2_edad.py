"""Modifica todos los ejercicios anteriores para que en lugar de permitir reintentos de manera ilimitada, 
el programa permita sólo 10 reintentos. Si el usuario supera el límite de reintentos, el programa debe terminar 
con el mensaje “Usted está jugando conmigo, yo me retiro”. """

"""Crea un script que le solicite al usuario ingresar su edad. 
Verifica que el dato ingresado sea válido, teniendo en cuenta que la edad es un número entero, 
y el rango válido para este programa es de 18 a 60 años. 
El programa debe solicitar el reingreso de manera indefinida, hasta que el dato sea correcto """

edad = int(input("Ingrese su edad: "))
intentos = 0

while (edad < 18 or edad > 60) and intentos < 10:
    intentos += 1
    edad = int(input("El dato no es válido.Ingrese su edad: "))

if intentos == 10:

    print("Usted está jugando conmigo, yo me retiro")

else:

    print(f"Usted tiene {edad} años el dato es válido") 