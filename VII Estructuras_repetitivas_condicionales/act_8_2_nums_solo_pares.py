""" Si bien el While es útil cuando desconocemos la cantidad de veces que repetiremos un bloque de instrucciones, 
también puede ser utilizado en los mismos casos que es utilizado el For (aunque la inversa no es verdadera). 
Rehaga todos los ejercicios del Trabajo Práctico VI utilizando un While en lugar de un For. """

"""Modifica el script del ejercicio anterior para que se muestren sólo los números pares. 
Para saber si un número es par, utilice el operador de módulo."""

numero_par = 0
numero = 0

while numero_par != 100:
    numero += 1
    numero_par = numero * 2
    print(numero_par)