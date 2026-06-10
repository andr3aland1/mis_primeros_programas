def esta_nombre(lista_nombres, nombre):
    for i in lista_nombres:
        if i == nombre:
            return True 
    return False

lista = ["Maria", "Pepito", "Pancho", "Jaimito"] 

entrada = input("Ingrese un nombre: ")

res = esta_nombre(lista, entrada)

print(res)


