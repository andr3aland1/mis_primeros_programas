lista = []
num = "salir"

num = input("Ingrese un número, sino escriba salir: ")

while num != "salir":
    lista.append(num)
    num = input("Ingrese un número, sino escriba salir: ")
    
print(lista)