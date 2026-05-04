""" Un cliente ha solicitado un programa que le permita ingresar cuántas cuadras caminó con su perro 
durante una cantidad de días determinada por él mismo.
El programa debe retornar al finalizar:
La cantidad total de cuadras caminadas.
El promedio de cuadras por día.
El número de día (empezando desde 1) en el que más caminó.
Además:
Si alguno de los días caminó más de 30 cuadras, mostrar el mensaje:
 "El perro necesita 24 horas de descanso"
Si el promedio es menor a 10 y ningún día caminó más de 20 cuadras, mostrar:
 "El perro necesita caminar más" """

total_cuadras = 0
dia_camino_mas = 0
maximo_cuadras = 0
posicion_max = 0

dias = int(input("Ingrese la cantidad de días que camino con su perro: "))

for i in range (1, dias+1):
    cuadras = int(input(f"Ingrese la cantidad de cuadras que caminó el día {i}: "))
    total_cuadras = total_cuadras + cuadras

    if maximo_cuadras < cuadras:
        maximo_cuadras = cuadras
        posicion_max = i 

promedio = total_cuadras / dias

print(f"El perro caminó {total_cuadras} cuadras con un promedio de {promedio:.2f} cuadras caminadas por día.")
print(f"El {posicion_max}º día fue el día que más camino.")

if promedio < 10 and maximo_cuadras < 20:
    print("El perro necesita caminar más")
elif maximo_cuadras > 30:
    print("El perro necesita 24 horas de descanso")
