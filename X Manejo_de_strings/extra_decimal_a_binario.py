def decimal_binario(numero):
    binario = ""

    while numero > 0:
        resto = numero % 2
        binario = str(resto) + binario
        numero = numero // 2

    return binario


numero = int(input("Ingrese un número decimal: "))
print("En binario es:", decimal_binario(numero))