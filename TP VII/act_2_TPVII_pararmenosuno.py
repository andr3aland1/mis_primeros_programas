contador = 0
nota = 0
suma = float(input("Para salir escriba -1 sino ingrese la nota: "))

while nota != -1:
    suma = suma + nota
    contador = contador + 1
    nota = float(input("Para salir escriba -1 sino ingrese la siguiente nota: ")) 

if contador > 0:
    promedio = suma/contador
    print(f"El promedio es: {promedio}") 
else:
    print("No se ingresaron notas.")