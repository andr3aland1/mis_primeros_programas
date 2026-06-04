def agregar(lista):
    num = input("Ingrese un numero: ")
    while(num.lower()!="salir"):
        lista.append(int(num))
        num = input("Ingrese un numero: ")
    return lista
    
numeros = [3, 86, 954]
numeros = agregar(numeros)
print(numeros)