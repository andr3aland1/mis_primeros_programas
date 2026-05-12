"""Una heladería está haciendo una encuesta a sus clientes sobre la experiencia en su heladería, de cada cliente se solicita : 
• Edad (Entre 5 - 100) 
• Si le gustó el helado (si-no) 
• Sí recomendaría el helado (si-no)
La encuesta termina cuando en edad se ingresa 0.
El programa debe retornar el promedio de clientes que recomiendan la heladería y mostrar por pantalla : 
• Cantidad de clientes que recomendaron la heladeria
• Cantidad de clientes que no les gustó el helado
• Si a más de un menor de 15 años le disgustó el helado debe mostrar el mensaje “ Ojo! a más de un menor no le gustó el helado!” """

import os

respuesta_gusto = ""
contador_no_gusto = 0
respuesta_recomienda = ""
contador_recomienda = 0
contador_clientes = 0
contador_menores_no = 0
edad = 1

while edad != 0:

    edad = int(input("Ingrese su edad: "))

    while edad != 0 and (edad < 5 or edad > 100):
        print("El dato no es válido.")
        edad = int(input("Ingrese una edad entre 5 y 100: "))
        os.system('cls')

    if edad >= 5 and edad <= 100:

        contador_clientes += 1

        respuesta_gusto = input("¿Le gustó el helado? SI - NO: ").upper()

        if respuesta_gusto == "NO":
            contador_no_gusto += 1

            if edad < 15:
                contador_menores_no += 1

        respuesta_recomienda = input("¿Recomienda la heladería? SI - NO: ").upper()

        if respuesta_recomienda == "SI":
            contador_recomienda += 1

    input("Presione ENTER para continuar")
    os.system('cls')

if contador_clientes > 0:

    promedio = (contador_recomienda * 100) / contador_clientes

    print(f"Cantidad de clientes que recomendaron la heladería: {contador_recomienda}")

    print(f"Cantidad de clientes que no les gustó el helado: {contador_no_gusto}")

    print(f"Promedio de clientes que recomiendan la heladería: {promedio:.2f}")

    if contador_menores_no > 1:
        print("¡Ojo! A más de un menor no le gustó el helado")