""" Usa las funciones para strings que ya conoces e implementa un script que haga lo siguiente:
I. Le solicite al usuario ingresar una palabra por teclado. Se debe validar que la palabra tenga al menos una ‘ñ’.
En caso de no ser válida, se le debe pedir al usuario que la reingrese.
II. Informe en pantalla la cantidad de letras de la palabra ingresada.
III. Transforme la palabra a mayúsculas, reemplace todas las ‘Ñ’ por 'N', y luego muestre el resultado en pantalla."""

def validacion(palabra):
    """valida si la palabra tiene ñ sino la vuelve a solicitar, sale cuando se ingresa una palabra con ñ"""

    enie = False

    while enie == False:
        palabra = palabra.lower()

        for letra in palabra:
            if letra == "ñ":
                enie = True

        if enie == False:
            palabra = input("Ingrese una palabra con ñ: ")

    return palabra


def cambiar_enie(palabra):
    """crea una una palabra a partir de la original y cambia las ñ por las n"""
    palabra = palabra.upper()
    palabra_transformada = ""

    for letra in palabra:
        if letra == "Ñ":
            palabra_transformada += "N"
        else:
            palabra_transformada += letra

    return palabra_transformada


def main():
    palabra = input("Ingrese una palabra con ñ: ")
    palabra = validacion(palabra)

    cantidad_letras = len(palabra)
    print(f"La palabra tiene {cantidad_letras} letras")

    palabra_transformada = cambiar_enie(palabra)
    print(f"La palabra transformada es {palabra_transformada}")


main()