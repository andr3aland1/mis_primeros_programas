primer_lado = float(input("Ingrese un lado del triángulo: "))
segundo_lado = float(input("Ingrese otro lado del triángulo: "))
tercer_lado = float(input("Ingrese el último lado del triángulo: "))

if primer_lado != segundo_lado and primer_lado != tercer_lado:
    print("El triángulo es escaleno")
elif primer_lado == segundo_lado and primer_lado == tercer_lado:
    print("El triángulo es equilátero")
else:
    print("El triángulo es isósceles")