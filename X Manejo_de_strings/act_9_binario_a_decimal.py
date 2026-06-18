"""Escribe una función que reciba una cadena de unos y ceros (es decir, un número en representación binaria) 
y devuelva el valor decimal correspondiente."""

def binario_decimal(binario):
    decimal = 0
    potencia = 0

    for i in range(len(binario)-1, -1, -1):
        decimal += int(binario[i]) * (2 ** potencia)
        potencia += 1

    return decimal

def main():
    b = input("Ingrese un número binario: ")
    print(binario_decimal(b))
main() 