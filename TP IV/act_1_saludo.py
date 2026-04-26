def saludo(nombre):
    return "Hola " + nombre + " tu nombre tiene " + str(len(nombre)) + " letras."


nombre = input("Ingrese su nombre: ")

print(saludo(nombre))