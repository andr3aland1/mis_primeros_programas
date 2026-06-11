"""
Encuentra el elemento más frecuente, Cree una lista de 5000 elementos enteros cuyos valores estén entre 0 y 100, 
luego genere una función que informe cuál es el elemento que más se repite. 
Cargar la lista utilizando randint(), es necesario importar la biblioteca random, import random, para poder usar 
randint() Ejemplo: x=randint(-50, 50) almacena en x un número al azar entre -50 y 50. 
"""

from random import *

numeros = []

for i in range (5000):
    x = randint(0,100)
    numeros.append(x)

contadores = list()
for i in range (101):
    contadores.append(0)

for i in range(5000):
    contadores[numeros[i]]+=1


maximo=contadores[0]
mas_repetido = 0

for i in range(len(contadores)):
    if contadores[i] > maximo:
        maximo = contadores[numeros[i]
        mas_repetido = i
print(f"El número más repetido es el {mas_repetido} con {contadores[i]} apariciones ")



# NO SE PUEDE USAR 
# if 10 in contadores