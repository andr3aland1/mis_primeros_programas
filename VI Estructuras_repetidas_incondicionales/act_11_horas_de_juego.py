""" Una madre preocupada por las horas de juego de su hijo nos solicita un programa que permita registrar 
cuantas horas juega su hijo durante diez (10) días. 
El programa debe: 
Mostrar el primer día que jugó 0 horas. 
Mostrar en cuantos días jugó más de 5 horas.
Si el promedio supera las 3 horas diarias debe mostrar : “Demasiadas horas frente a la pantalla” 
Si el promedio no supera las 3 horas o hubo más de 1 día en los que jugó 0 horas debe retornar False 
(Haciendo referencia a que el niño no se excede en horas de juego). 
Si no, debe retornar True y mostrar el mensaje “Su hijo no excede las horas de juego”. """

acumulador_horas = 0
mas_cinco = 0
jugo_cero = 0
dia_cero = 0
demasiadas_horas = True

for i in range(10):
    horas_juego = int(input(f"Ingrese la cantidad de horas que jugo el dia Nº {i + 1}: "))
    acumulador_horas = acumulador_horas + horas_juego

    if horas_juego > 5:
        mas_cinco += 1
    if horas_juego == 0:
        jugo_cero += 1
        if jugo_cero == 1:
            dia_cero = i + 1 

promedio = acumulador_horas / 10

if promedio <= 3 or jugo_cero > 1:
    demasiadas_horas = False
    mensaje = "El niño no excede las horas de juego"
else:
    demasiadas_horas = True
    mensaje = "Demasiadas horas frente a la pantalla. Su hijo excede las horas de juego"

print(f"El primer día que jugó cero horas fue el día {dia_cero}")
print(f"Los días que jugó más de cinco horas fueron: {mas_cinco}")
# control promedio   print(f"Promedio de horas: {promedio}")
print(f"Supera las horas de juego: {demasiadas_horas}\n{mensaje}")
