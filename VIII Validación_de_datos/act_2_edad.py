
edad = int(input("Ingrese su edad: "))

while edad < 18 or edad > 60:
    edad = int(input("El dato no es válido.Ingrese su edad: "))

print(f"Usted tiene {edad} años el dato es válido")