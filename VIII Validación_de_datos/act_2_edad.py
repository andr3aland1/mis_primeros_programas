"""Crea un script que le solicite al usuario ingresar su edad. 
Verifica que el dato ingresado sea válido, teniendo en cuenta que la edad es un número entero, 
y el rango válido para este programa es de 18 a 60 años. 
El programa debe solicitar el reingreso de manera indefinida, hasta que el dato sea correcto """

edad = int(input("Ingrese su edad: "))

while edad < 18 or edad > 60:
    edad = int(input("El dato no es válido.Ingrese su edad: "))

print(f"Usted tiene {edad} años el dato es válido")