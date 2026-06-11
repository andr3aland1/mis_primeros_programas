"""
Realizar una función que reciba una Lista y dos elementos y busque el primer elemento especificado, en la lista, 
e inserte el segundo elemento como nuevo inmediatamente después. Ejemplo si el 1er elemento es 10, el segundo 20 
y la lista [7, 32, 44, 10, 15, 66] la lista debe quedar: [7, 32, 44, 10, 20, 15, 66]
""" 

def insertar(lista,num1,num2):
    resultado = []

    for i in lista:
        if i == num1:
            resultado.append(num1)
            resultado.append(num2)
        else: 
            resultado.append(i)
    return resultado

def main():
    numeros = [10,14,64,89,77,89,24]
    n1 = int(input("Ingrese un número: "))
    n2 = int(input("Ingrese otro número: "))
    numeros = insertar(numeros, n1, n2)
    print(numeros)
main()

