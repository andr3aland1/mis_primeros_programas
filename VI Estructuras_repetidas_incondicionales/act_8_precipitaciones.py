""" Un cliente ha solicitado un programa que le permita ingresar los mililitros de lluvia caídos diariamente en una semana, 
para que el programa le informe en pantalla el promedio de precipitación de esa semana. El cliente también desea saber 
cuál fue el día en que más llovió en la semana. 
A modo ilustrativo, un reporte generado por el programa debería verse, luego de haber leído las precipitaciones de los 
7 días de la semana, así: 
            El promedio de precipitaciones fue de XX ml diarios. 
            El día de más precipitaciones fue el xxxxxx (nombre del día). 
Ten en cuenta que la numeración de los días de la semana comienza con el 1 para el día domingo. 
Codifica el programa para dar solución a lo solicitado por el cliente. """

acumulador = 0
for i in range (1,8):
    precipitaciones = int(input("Ingrese la cantidad en mililitros de precipitaciones: "))
    acumulador = acumulador + precipitaciones
    if i == 1:
        maximo = precipitaciones
        posicion = i
    elif maximo < precipitaciones:
        maximo = precipitaciones
        posicion = i
promedio = acumulador / 7
print (f"El promedio de precipitaciones fue de {promedio:.2f} ml diarios")
if posicion == 1:
    print("El día con más precipitaciones fue el día domingo")
elif posicion == 2:
    print("El día con más precipitaciones fue el día lunes")
elif posicion == 3:
    print("El día con más precipitaciones fue el día martes")
elif posicion == 4:
    print("El día con más precipitaciones fue el día miércoles")
elif posicion == 5:
    print("El día con más precipitaciones fue el día jueves")
elif posicion == 6:
    print("El día con más precipitaciones fue el día viernes")
else:
    print("El día con más precipitaciones fue el día sábado")