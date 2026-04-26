primer_parcial = float(input("Ingrese la nota del primer parcial: "))
segundo_parcial = float(input("Ingrese la nota del segundo parcial: "))   
promedio = (primer_parcial + segundo_parcial)/2
if primer_parcial >= 7 and primer_parcial <= 10 and segundo_parcial >= 7 \
    and segundo_parcial <= 10:
    print(f"¡Felicitaciones! Promocionó Introducción a la programación. Su promedio es {promedio:.2f}")
elif primer_parcial >= 4 and primer_parcial <7 and segundo_parcial >= 4 and segundo_parcial < 7:
    print(f"¡Felicitaciones! Regularizó Introducción a la programación. Su promedio es {promedio:.2f} debe\
           rendir final")
else: 
    print(f"Esta libre. Debe rendir el recuperatorio de Introducción a la programación. Su promedio es: {promedio:.2f}")