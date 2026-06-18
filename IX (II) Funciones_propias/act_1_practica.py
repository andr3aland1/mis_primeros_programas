"""Diseña una función que calcule y retorne la suma de las cifras de un número entero positivo de 4 cifras."""

from mis_funciones import *

def main(): 

    print("Actividad 1")
    
    n = int(input("Ingrese un número: "))
    sumatoria = suma_cifras(n)
    print(sumatoria)
    
    
    print("Actividad 1_con_módulo")

    n = int(input("Ingrese un número: "))
    sumatoria = calculo_cifras(n)
    print(sumatoria)

main()