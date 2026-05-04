"""Crea un script que le solicite al usuario ingresar notas de parciales por teclado, hasta que el usuario ingrese el valor -1, 
indicando que ya no hay más notas para cargar. Una vez ingresadas las notas, el programa debe informar la nota promedio 
(tenga cuidado de no incluir al -1 dentro del promedio). """

contador = 0
suma = 0

nota = float(input("Para salir escriba -1 sino ingrese la nota: "))

while nota != -1:
    suma = suma + nota
    contador = contador + 1
    nota = float(input("Para salir escriba -1 sino ingrese la siguiente nota: ")) 

if contador > 0:
    promedio = suma/contador
    print(f"El promedio es: {promedio}") 
else:
    print("No se ingresaron notas.")