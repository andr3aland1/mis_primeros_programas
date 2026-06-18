"""Diseña una función que reciba una lista, vacía o no, e incorpore números hasta que el usuario ingrese el valor “salir”. 
Cuando termina de ingresar los datos, la función debe retornar la lista al programa principal."""

def ingresar_datos_lista(lista):
    dato = input("Ingrese un número o 'salir': ")

    while dato != "salir":
        lista.append(int(dato))
        dato = input("Ingrese un número o 'salir': ")

    return lista


def main():
    lista = []

    lista = ingresar_datos_lista(lista)

    print(lista)


main()