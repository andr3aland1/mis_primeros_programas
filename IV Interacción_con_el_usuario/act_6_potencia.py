def potencia(base,exponente):
    return base**exponente
base = float(input("Ingrese la base de la potencia: "))
exponente = float(input("Ingrese el exponente: "))
resultado = potencia(base,exponente)
print("El resultado de la potencia es: ", round(resultado,2))