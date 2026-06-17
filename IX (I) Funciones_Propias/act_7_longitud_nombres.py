"""Crea una función que reciba dos string como parámetro (nombre1 y nombre2), y retorne True si nombre1 tiene más letras 
que nombre2, o False en caso contrario.
"""

def comparar(nombre1, nombre2):
    """La función recibe dos string como parámetros y retorna verdadero si el primer nombre ingresado tiene más letras,
    de lo contrario retorna falso"""

    nom1 = len(nombre1)
    nom2 = len(nombre2)
    if nom1 > nom2:
        r = True
    else:
        r = False
    return r

def main():

    nombre1 = input("Ingrese un nombre: ")
    nombre2 = input("Ingrese otro nombre: ")

    r = comparar(nombre1,nombre2)

    print(f"El nombre uno tiene más letras: {r}")

main()