""" Crea un script que le pida al usuario ingresar palabras, una a una, hasta que el usuario ingrese la palabra “parar”. 
A medida que se van ingresando las palabras, el programa simplemente debe mostrarlas en pantalla. 
Al detectar la palabra para detenerse, debe mostrar el mensaje “--- TERMINADO ---” """

parar = "parar"
palabra = ""

while palabra.lower() != parar:
    palabra = input("Ingrese una palabra: ")
    print(palabra)
print("--- TERMINADO ---")