"""
Dada una lista de números enteros y un entero k, escribe una función para cada uno de los siguientes ítems:
a.	Devuelva tres listas, una con los menores, otra con los mayores y otra con los iguales a k.
b.	Devuelva una lista con aquellos que son múltiplos de k.
"""

def separar_lista(lista, k):
    menores = list()
    iguales = list()
    mayores = list()

    for numero in lista:
        if numero < k:
            menores.append(numero)
        elif numero == k:
            iguales.append(numero)
        else:
            mayores.append(numero)

    return menores, iguales, mayores


def multiplos(lista, k):
    lista_multiplos = []

    for numero in lista:
        if numero % k == 0:
            lista_multiplos.append(numero)

    return lista_multiplos


def main():
    lista = [5, 10, 3, 10, 15, 20, 7, 10]
    k = 10

    menores, iguales, mayores = separar_lista(lista, k)
    lista_multiplos = multiplos(lista, k)

    print("Lista original:", lista)
    print("Menores que", k, ":", menores)
    print("Iguales a", k, ":", iguales)
    print("Mayores que", k, ":", mayores)
    print("Múltiplos de", k, ":", lista_multiplos)


main()

"""
Resultados esperados:

Lista original: [5, 10, 3, 10, 15, 20, 7, 10]
Menores que 10 : [5, 3, 7]
Iguales a 10 : [10, 10, 10]
Mayores que 10 : [15, 20]
Múltiplos de 10 : [10, 10, 20, 10]

"""