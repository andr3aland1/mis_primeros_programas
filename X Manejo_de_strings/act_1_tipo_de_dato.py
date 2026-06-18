"""Todas las variables y valores en Python tienen definido implícitamente un tipo. 
Mediante el uso de la función type(...), podemos averiguar el tipo de un dato en determinado momento del programa.
Utiliza la función type para mostrar en pantalla los tipos de los siguientes valores:

'Hola mundo'
"Hola mundo"
100
'100'

Luego de haber determinado los tipos de los valores listados, responde:
a. ¿De qué tipo son las cadenas de caracteres en Python?
b. ¿Cuáles son las dos formas de escribir strings en Python? Investigue cuál es la diferencia entre ambas.
c. ¿Es lo mismo que una variable tenga asignado el valor 100 a que tenga el valor '100'? ¿Cuál es la diferencia?
"""

def tipo_de_dato(valor):
    t = type(valor)
    return t


def main():
    
    dato = input("Ingrese un dato: ")
    
    while dato != "salir":

        t = tipo_de_dato(dato)
        print(t)
        dato = input("Ingrese un dato: ")

main()

"""
Respuestas:
a. Las cadenas de caracteres de python son str es decir string.
b. En Python podemos escribir los strings con comillas simples o dobles. Esto nos permite a su vez escribir comillas dentro del 
string sin escaparlas; siempre que usemos comillas de diferentes tipos ejemplo: "Hola 'mundo'!". Caso contrario, es decir, al
usar el mismo tipo de comillas deberiamos espacarlas, ejemplo: "Hola \"mundo\"" de esta manera no va a generar errores.
c. No es lo mismo, debido a que si escribimos 100 sin comillas lo va a tomar como número entero (int), mientras que si 
usamos comillas lo va a entender como un str, es decir una cadena de caracteres en este caso texto. 
"""
