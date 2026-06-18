"""Escribe una función que dada una cadena de caracteres devuelve solamente las letras consonantes. 
Por ejemplo, si recibe 'algoritmos' debe devolver 'lgrtms'."""


def sin_vocales(cadena):
    resultado = ""
    cadena = cadena.lower()

    for i in range(len(cadena)):
        if (cadena[i] != "a" and
            cadena[i] != "e" and
            cadena[i] != "i" and
            cadena[i] != "o" and
            cadena[i] != "u"):
            resultado += cadena[i]

    return resultado

def main():
    cadena = "murcielago"
    print(sin_vocales(cadena))

main()



#opción 2
"""
def consonantes(cadena):
    resultado = ""
    vocales = ["a", "e", "i", "o", "u",
               "A", "E", "I", "O", "U"]

    for i in range(len(cadena)):
        es_vocal = False

        for j in range(len(vocales)):
            if cadena[i] == vocales[j]:
                es_vocal = True

        if es_vocal == False:
            resultado += cadena[i]

"""