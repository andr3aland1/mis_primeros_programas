def cant_mayor_letras(nombre1, nombre2):
    """Retorna True si nombre1 tiene más letras que nombre2"""
    nom1 = len(nombre1)
    nom2 = len(nombre2)
    r = nom1 > nom2
    return r


def main():

    nombre1 = input("Ingrese un nombre: ")
    nombre2 = input("Ingrese otro nombre: ")

    r = cant_mayor_letras(nombre1,nombre2)

    print(f"El nombre uno tiene más letras: {r}")

main()