"""Las operaciones aritméticas tradicionales tienen un comportamiento especial cuando las aplicamos a strings. 
Utiliza un script de Python para responder:

a. ¿Qué función cumple el operador + entre strings?
b. ¿Qué función cumple el operador * entre strings?
c. Ejecuta el siguiente código y describe con tus palabras cuál es el problema:

mi_valor = 'Hola' + 7
print(mi_valor) 

Respuestas:

a. El operador + concatena, es decir une cadenas de caracteres. Ejemplo: "hola" + "mundo" produce "holamundo"
b. El operador de * correspondiente a multiplicación, repite la cadena de caracteres tantas veces como lo indique el número 
elegido. Ejemplo: "mundo" * 3 produce mundomundomundo, a su vez podemos dejar un espacio al final de la palabra para que no se nos peguen 
las palabras ejemplo: "mundo " * 3 produce mundo mundo mundo.
c. El problema es que estamos tratando de concatenar un str con un int y eso no se puede hacer. 
"""

print("'hola' + 'mundo' = ", ("hola" + "mundo"))

print("'hola ' + 'mundo' = ", ("hola " + "mundo"))

print("'mundo' * 3 =", ("hola" *3))

print("'mundo ' * 3 =", ("hola " *3))
