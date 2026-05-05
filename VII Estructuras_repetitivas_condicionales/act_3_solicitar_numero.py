""" Crea un script que le solicite al usuario leer un número entero entre 1 y 100. El programa debe ser capaz de solicitarle 
al usuario que ingrese el número cuantas veces sea necesario, hasta que el usuario provea un dato válido. 
Cada vez que detecte un error de validación, informele al usuario cuál fue el error, con los mensajes “El dato ingresado no 
es numérico.”, o “El número ingresado está fuera del rango permitido.”. Finalmente, cuando el usuario ingrese un dato válido, 
muestre el mensaje “[NÚMERO] es válido. Gracias!”. """

numero = input("Ingrese un número entre 1 y 100: ")

while not numero.isdigit() or int(numero) < 1 or int(numero) > 100:
    
    if  numero.isalpha():
        print("El dato ingresado no es numérico.")
    else:
        print("El número ingresado está fuera del rango permitido.")
    
    numero = input("Ingrese un número entre 1 y 100: ")

print(f"{numero} es válido. Gracias!")