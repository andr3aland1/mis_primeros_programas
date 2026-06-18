"""Un millonario excéntrico tenía tres hijos: Carlos, José y Marta. Al morir dejó el siguiente legado: 
A José le dejó 4/3 de lo que le dejó a Carlos. A Carlos le dejó 1/3 de su fortuna. 
A Marta le dejó la mitad de lo que le dejó a José. Diseña una función que calcule y devuelva la suma a 
repartir y la herencia que recibió cada hijo.
"""
from mis_funciones import herencia

def main():
    cantidad = int(input("Ingrese la cantidad total: "))
    fortuna, carlos, jose, marta = herencia(cantidad)
    print (f"La herencia fue de: {fortuna:.2f}. Carlos recibió {carlos:.2f}, Jose recibió {jose:.2f} y Marta recibió {marta:.2f}.")
main()