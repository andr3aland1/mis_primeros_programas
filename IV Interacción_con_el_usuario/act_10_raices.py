import math

print("¡Bievenido! Este programa te permitirá resolver las raices de una función cuadrática")
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))
raiz1 = (-b + (b**2-4*a*c)**0.5) / (2 * a)
raiz2 = (-b - (b**2-4*a*c)**0.5) / (2 * a)
print(f"Las raices de la función son {raiz1} y {raiz2}")
# Valores para probar a=1 , b=-3, c= 2 raices x1=2 y x2=1 


print("¡Bievenido! Este programa te permitirá resolver las raices de una función cuadrática")
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))
raiz1 = (-b + math.sqrt(b**2-4*a*c)) / (2 * a)
raiz2 = (-b - math.sqrt(b**2-4*a*c)) / (2 * a)
print(f"Las raices de la función son {raiz1} y {raiz2}")