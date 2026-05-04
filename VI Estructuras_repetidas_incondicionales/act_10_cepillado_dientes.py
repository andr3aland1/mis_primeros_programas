""" Un odontólogo pide un programa donde el paciente ingrese cuantas veces se cepilló los dientes cada día 
durante una semana (7 días).
El programa debe :  
• Contar cuantos días se cepillo 3 o más veces.
• Si ningún día se cepilló más de una vez mostrar por pantalla “ Higiene insuficiente”. 
• Mostrar (si hubo) cuántos días no se cepillo los dientes. 
• Debe retornar la cantidad de días que se cepillo 3 veces o más y promedio de cepilladas diarias. """

mas_tres = 0
no_cepillo = 0
insuficiente = 0
cepilladas_total = 0

for i in range (1,8):
    cepillado = int(input(f"Ingrese cuantas veces se cepilló los dientes el {i}º día de la semana: "))
    cepilladas_total = cepilladas_total + cepillado
    if cepillado == 0:
        no_cepillo = no_cepillo + 1
        insuficiente = insuficiente + 1
    elif cepillado == 1:
        insuficiente = insuficiente + 1
    elif cepillado >= 3:
        mas_tres = mas_tres + 1
    
promedio = cepilladas_total / 7

print(f"Se cepillo tres o más veces {mas_tres} días ")

if insuficiente > 0:
    print("Higene insuficiente")

if no_cepillo > 0:
    print(f"Usted no se cepilló los dientes {no_cepillo} días")

print(f"Usted se cepilló 3 veces o más: {mas_tres} días.\n Se cepilló por día un promedio de {promedio:.2f} días")