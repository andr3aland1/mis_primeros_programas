""" En un concurso, cada participante tiene que adivinar un número entre 1 y 10. 
El programa tiene un número secreto fijo (por ejemplo, 7). 
Se ingresan intentos hasta que se acierte. Se cuenta:
• Cuántos intentos fueron.
• Cuántos estuvieron por encima del número secreto.
• Cuántos estuvieron por debajo. """

numero_secreto = 7
intentos = 0
intentos_encima = 0
intentos_debajo = 0

numero = int(input("Ingrese un número entre el 1 - 10: "))

while numero != numero_secreto:

    intentos += 1

    if numero > numero_secreto:
        intentos_encima += 1

    elif numero < numero_secreto:
        intentos_debajo += 1
        
    numero = int(input("Ingrese un número entre el 1 - 10: "))

print(f"Usted a acertado el número secreto\nLa cantidad de intentos totales fueron: {intentos}")
print(f"La cantidad de intentos que estuvieron por encima del número fueron: {intentos_encima}")
print(f"La cantidad de intentos que estuvieron debajo: {intentos_debajo}")