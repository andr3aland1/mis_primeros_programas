""" Extiende el script de la actividad 6 para que también informe el número mínimo ingresado,
 y su posición. """ 

for i in range(1, 11):
    numero = int(input("Ingrese un número: "))

    if i == 1:
        maximo = numero
        minimo = numero
        posicion_max = i
        posicion_min = i
    else:
        if numero > maximo:
            maximo = numero
            posicion_max = i
        elif numero < minimo:
            minimo = numero
            posicion_min = i

print(f"El número máximo es {maximo} y fue ingresado en la posición {posicion_max}")
print(f"El número mínimo es {minimo} y fue ingresado en la posición {posicion_min}")
