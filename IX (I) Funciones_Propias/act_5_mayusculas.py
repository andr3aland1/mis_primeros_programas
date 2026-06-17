"""Crea una función que reciba un string como parámetro, y retorna el mismo string, 
pero con todas las letras convertidas a mayúsculas."""

def mayusculas(a):
    """La función recibe un string como parámetro, y retorna el mismo string con tas sus letras en mayúscula"""
    m = a.upper()
    return m

def main():
    
    palabra = input("Ingrese una palabra en minúsculas: ")
    p = mayusculas(palabra)
    print(p)

main()