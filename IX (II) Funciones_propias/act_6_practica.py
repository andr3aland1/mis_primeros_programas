"""Diseña una función que reciba cuántas personas participaron de un examen y cuántas aprobaron el mismo. 
Debe retornar el porcentaje de aprobación."""

from mis_funciones import porcentaje_aprobacion 

def main():
    alumnos = int(input("Ingrese la cantidad de estudiantes: "))
    aprobados = int(input("Ingrese la cantidad de aprobados: "))
    porcentaje = porcentaje_aprobacion(alumnos,aprobados) 
    print("El porcentaje de aprobados es de: ", porcentaje, "%")
main()
