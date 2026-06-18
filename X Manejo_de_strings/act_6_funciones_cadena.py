"""
Escribe funciones que dada una cadena de caracteres:
Imprima los dos primeros caracteres.
Imprima los tres últimos caracteres.
Imprimir dicha cadena en sentido inverso.
"""

def primeros_dos(cadena):
    resultado = ""
    for i in range(2):
       resultado += cadena[i]
    print(resultado)

def tres_ultimos(cadena):
    resultado = ""
    for i in range(len(cadena)-3,len(cadena)):
        resultado += cadena[i]
    print(resultado)

def reves(cadena):
    resultado = ""
    for i in range (len(cadena)-1,-1,-1):
        resultado += cadena[i]
    print(resultado)

def main():

    cadena = "METAMORFOSIS"

    primeros_dos(cadena)
    tres_ultimos(cadena)
    reves(cadena)

main()