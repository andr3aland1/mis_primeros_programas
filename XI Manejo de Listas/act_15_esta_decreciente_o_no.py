"""
Cree una función en python que determine si una lista de números está ordenada en orden decreciente.
Retorno True si es así, y False de otro modo.
"""
def orden(lista):
    i = 0
    while i < (len(lista) - 1) and lista[i] >= lista[i + 1] :
        i = i + 1
    return i == len(lista) - 1
numeros = [10, 9, 7, 6, 5, 5, 3,1]  

if(orden(numeros)):
    print("La lista esta ordenada ")
else: 
    print("La lista no está ordenada ")