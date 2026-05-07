"""Una heladería está haciendo una encuesta a sus clientes sobre la experiencia en su heladería, de cada cliente se solicita : 
• Edad (Entre 5 - 100) 
• Si le gustó el helado (si-no) 
• Sí recomendaría el helado (si-no)
La encuesta termina cuando en edad se ingresa 0.
El programa debe retornar el promedio de clientes que recomiendan la heladería y mostrar por pantalla : 
• Cantidad de clientes que recomendaron la heladeria
• Cantidad de clientes que no les gustó el helado
• Si a más de un menor de 15 años le disgustó el helado debe mostrar el mensaje “ Ojo! a un menor no le gustó el helado!” """

respuesta_gusto = ""
contador_gusto = 0
contador_no_gusto = 0
respuesta_recomienda = ""
contador_recomienda = 0
edad = 1
mensaje = ""

while edad != "0":
    edad = input("Ingrese su edad: ")

    while not edad.isdigit() and (int(edad) < 5 or int(edad) > 100):
        edad = input("El dato no es valido. Ingrese una edad entre 5 - 100: ")

    edad_num = int(edad)
    
    if edad_num >= 5 and edad_num <= 100:
        respuesta_gusto = input("¿Le gusto el helado? SI - NO ").upper()
    
        if respuesta_gusto == "SI":
            contador_gusto += 1
        
        elif respuesta_gusto == "NO":
            contador_no_gusto += 1
    
        if respuesta_gusto == "NO" and edad_num < 15:
            mensaje = "Ojo! a un menor no le gustó el helado"
            contador_no_gusto += 1

        respuesta_recomienda = input("¿Recomienda la heladería? SI + NO: ").upper()
    
        if respuesta_recomienda == "SI":
            contador_recomienda += 1

if edad == "0":
    print(f"Cantidad de clientes que recomiendan la heladería: {contador_gusto} personas")
    print(f"No les gusto el helado a {contador_no_gusto} personas")
    print(mensaje)





