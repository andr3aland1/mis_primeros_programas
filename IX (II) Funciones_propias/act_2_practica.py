"""Una empresa de ventas de Alemania paga a sus empleados un salario fijo de 5000 euros, 
más una comisión de 200 euros por cada venta realizada, más el 8 % del valor de esas ventas. 
Diseña una función que calcule y devuelva el sueldo correspondiente en un mes determinado, 
recibiendo la cantidad de ventas realizadas por un empleado y el valor total de las mismas."""

from mis_funciones import sueldo

def main():

    cantidad_ventas = int(input("Ingrese la cantidad de ventas: "))
    total_ventas = int(input("Ingrese valor total de las ventas: "))
    sueldo_empleado = sueldo(cantidad_ventas, total_ventas)
    print(f"El sueldo del empleado es: {sueldo_empleado:.2f}")

main ()