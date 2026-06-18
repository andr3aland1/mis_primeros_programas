"""El precio final de un producto es la suma del costo, el porcentaje de beneficios del vendedor (8%) y el I.V.A. (21%). 
Diseña una función que calcule este precio usando el costo, el porcentaje de beneficios y el I.V.A. 
Retornar el resultado que debe ser impreso en el programa principal con dos decimales. """


from mis_funciones import precio_final

def main():
    costo = float(input("Ingrese el costo del producto: "))
    precio = precio_final(costo)
    print("El precio del producto es:", precio)
main()