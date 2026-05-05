""" Si bien el while es útil cuando desconocemos la cantidad de veces que repetiremos un bloque de instrucciones,
también puede ser utilizado en los mismos casos que es utilizado el For (aunque la inversa no es verdadera). 
Rehaga todos los ejercicios del Trabajo Práctico VI utilizando un While en lugar de un For. """

""" Extiende el script de la actividad 8_6 para que también informe el número mínimo ingresado,
 y su posición. """ 

contador = 0

while contador != 10:
    
    contador += 1
    
    numero = int(input(f"Ingrese el {contador}º número: "))

    if contador == 1:
        numero_mayor = numero
        posicion_mayor = contador
        numero_menor = numero
        posicion_menor = numero
    
    elif numero > numero_mayor:
        numero_mayor = numero
        posicion_mayor = contador

    elif numero < numero_menor:
        numero_menor = numero
        posicion_menor = contador     

print(f"El número mayor ingresado es: {numero_mayor} y lo ingresaste en la posición: {posicion_mayor}")
print(f"El número menor ingresado es: {numero_menor} y lo ingresaste en la posición: {posicion_menor}")