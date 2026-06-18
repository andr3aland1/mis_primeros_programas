""" Dada una lista de números enteros, escribe una función para cada uno de los siguientes ítems:
a.	Devuelva una lista con todos los números  que sean primos.
b.	Devuelva la sumatoria y el promedio de los valores.
c.	Devuelva una lista con el factorial de cada uno de esos números."""


def es_primo(numero):
    """Devuelve True si el número es primo y False en caso contrario."""
    divisores = 0

    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores = divisores + 1

    return divisores == 2


def lista_primos(lista):
    """Devuelve una lista con los números primos de la lista recibida."""
    primos = []

    for numero in lista:
        if es_primo(numero):
            primos.append(numero)

    return primos


def suma_promedio(lista):
    """Devuelve la sumatoria y el promedio de los elementos de la lista."""
    suma = 0

    for numero in lista:
        suma = suma + numero

    promedio = suma / len(lista)

    return suma, promedio


def factorial(numero):
    """Calcula y devuelve el factorial de un número."""
    fact = 1

    for i in range(1, numero + 1):
        fact = fact * i

    return fact


def lista_factoriales(lista):
    """Devuelve una lista con el factorial de cada elemento de la lista recibida."""
    factoriales = []

    for numero in lista:
        factoriales.append(factorial(numero))

    return factoriales


def main():
    lista = [3, 4, 7, 8, 10, 11]

    print("Lista original:", lista)
    print("Primos:", lista_primos(lista))

    suma, promedio = suma_promedio(lista)
    print("Suma:", suma)
    print("Promedio:", round(promedio))

    print("Factoriales:", lista_factoriales(lista))


main()
