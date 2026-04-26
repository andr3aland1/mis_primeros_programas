base = float(input("Ingrese el valor de la base del rectángulo: "))
altura = float(input("Ingrese el valor de la altura del rectángulo: "))
def perimetro_rectangulo(base, altura):
        return round(2*(base + altura),2)
perimetro = perimetro_rectangulo(base,altura)
print("El perímetro del rectángulo es: ", perimetro)
