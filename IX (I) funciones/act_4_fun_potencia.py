def potencia(base,exponente):
    resultado = base**exponente
    return resultado

num1 = int(input("Ingrese un base de la potencia: "))
num2 = int(input("Ingrese el exponente de la potencia: "))
           
mostrar = potencia(num1,num2)

print(f"El resultado de elevar {num1} a {num2} es: {mostrar}")
