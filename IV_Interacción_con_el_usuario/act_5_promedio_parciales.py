estudiante = input("Ingrese su apellido: ")
parcial1 = float(input("Ingrese la nota del primer parcial: "))
parcial2 = float(input("Ingrese la nota del segundo parcial. "))
promedio = round((parcial1 + parcial2)/2,2)
print(f"Alumno: {estudiante}\n- Primer Parcial: {parcial1}\n- Segundo Parcial:\
{parcial2}\n- Promedio: {promedio}\n")