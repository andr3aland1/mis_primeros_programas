seguir = "SI"

while seguir != "NO":

    numero = input("Ingrese un número entero positivo: ")

    while not numero.isdigit():
        numero = input("Dato inválido. Ingrese un número entero positivo: ")

    numero = int(numero)

    factorial = 1

    for i in range(1, numero + 1):
        factorial *= i

    print(f"El factorial de {numero} es {factorial}")

    seguir = input("¿Desea calcular otro factorial? Ingrese NO para salir: ").upper()