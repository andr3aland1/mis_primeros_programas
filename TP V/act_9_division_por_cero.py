dividendo = float(input("Ingrese el número que desea dividir: "))
divisor = float(input("Ingrese el número por el cual lo quiere dividir: "))

if divisor != 0:
    division = dividendo/divisor
    print(f"La división da: {division:.2f}")
else: 
    print("No se puede dividir por cero.")