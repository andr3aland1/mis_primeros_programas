""" Si bien el while es útil cuando desconocemos la cantidad de veces que repetiremos un bloque de instrucciones,
también puede ser utilizado en los mismos casos que es utilizado el For (aunque la inversa no es verdadera). 
Rehaga todos los ejercicios del Trabajo Práctico VI utilizando un While en lugar de un For. """

""" Crea un script que le solicite al usuario ingresar un número entero, y muestre en pantalla el factorial de dicho número.
NOTA: Puede obviar la validación en este ejercicio, pero recuerda que la función range no incluye al valor máximo enviado 
como parámetro. factorial de n = n! = 1 * 2 * 3 * … * (n - 1) * n """

tope = 0
factorial = 1

numero = int(input("Ingrese un número natural: "))

while tope != numero:
    tope += 1
    factorial *= tope
print(f"El factorial del número {numero} es: {factorial}")