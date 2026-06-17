"""Modifica la función del ejercicio anterior para que retorne dos versiones del string recibido como parámetro: 
primero la versión en minúsculas, y luego la versión en mayúsculas.""" 

def min_mayus(a):
    """La función recibe un string como parámetro, y devuelve el mismo string prmero en minúsculas y luego en mayúsculas"""
    mi = a.lower()
    ma = a.upper()

    return mi,ma

def main():
    
    palabra = input("Ingrese una palabra: ")
    p1,p2 = min_mayus(palabra)
    print(f"Versión en minúsculas: {p1}\nVersión en mayúsculas: {p2}")

main()