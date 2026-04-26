"""Modifica el script del ejercicio anterior para que se muestren sólo los números pares. 
Para saber si un número es par, utilice el operador de módulo."""

for numeros in range(2,101,2):
    print(numeros)

par_impar = int(input("Ingrese un número: "))
if par_impar % 2 == 0:
    print("El número ingresado es par.")
else: 
    print("El número ingresado es impar.")