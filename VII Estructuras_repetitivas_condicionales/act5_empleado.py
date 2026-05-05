""" En una empresa, cada operario informa cuántos productos fabrica por día.
El sistema registra esta producción hasta que el operario cargue un día con 0 productos 
(lo que indica que no trabajó) el programa debe mostrar : 
• Cuántos días trabajó
• Promedio de producción por día
• Día con máxima producción """

dias = 0
dia_max = 0
max_produccion = 0
produccion_total = 0

produccion = int(input("Ingrese la producción del día de hoy: "))

while produccion != 0:
    dias+=1 
    produccion_total += produccion

    if produccion > max_produccion:
        max_produccion = produccion
        dia_max = dias
    
    produccion = int(input("ingrese la cantidad producida de hoy: "))

promedio = produccion_total / dias

print(f"Se trabajaron {dias} dias.\n El promedio de producción fue {promedio} unidades.\n\
El dÍa de mayor producción fue {dia_max}")