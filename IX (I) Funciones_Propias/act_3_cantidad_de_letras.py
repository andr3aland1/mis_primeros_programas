"""Crea una función que reciba un string como parámetro, y retorne la cantidad de letras que posee. 
Luego, utiliza la función para escribir un programa que solicite ingresar el nombre del usuario, y 
luego muestre en pantalla cuántas letras tiene ese nombre. 
"""

def letras (cadena):
    """La función recibe un string como parámetro y retorna la cantidad de letras que posee."""
    palabra = len(cadena)
    return palabra

def main():
    
    nombre = input("Ingrese su nombre: ")
    r = letras(nombre)
    print(f"Su nombre tiene {r} letras.")

main()