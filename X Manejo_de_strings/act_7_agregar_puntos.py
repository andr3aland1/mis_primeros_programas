"""Escribe una función que reciba una cadena que contiene un largo número entero y devuelva una cadena con el número y 
las separaciones de miles. Por ejemplo, si recibe '1234567890', debe devolver '1.234.567.890'."""

def puntos_miles(numero):
    resultado = ""
    contador = 0
    for i in range(len(numero)-1,-1,-1):
        resultado += numero[i]
        contador += 1

        if contador == 3 and i != 0:
            resultado += "."
            contador = 0
    return(resultado)

def main():
    numero_final = ""
    numero = input("Ingrese un número: ")
    numero = puntos_miles(numero)
    for i in range(len(numero)-1,-1,-1):
        numero_final+=numero[i]
    print(numero_final)

main()
