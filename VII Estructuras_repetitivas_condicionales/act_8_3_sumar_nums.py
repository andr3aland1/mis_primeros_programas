""" Si bien el While es útil cuando desconocemos la cantidad de veces que repetiremos un bloque de instrucciones, 
también puede ser utilizado en los mismos casos que es utilizado el For (aunque la inversa no es verdadera). 
Rehaga todos los ejercicios del Trabajo Práctico VI utilizando un While en lugar de un For. """

""" Crea un script para calcular el resultado de sumar los números desde el 75 al 150."""

numero = 75
tope = 75


while tope != 150:

    tope += 1
    
    numero += tope
    
print(f"El resultado de sumar los números desde el 75 al 150 es: {numero}") 
