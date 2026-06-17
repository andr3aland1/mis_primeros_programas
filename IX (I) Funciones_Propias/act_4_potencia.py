"""Crea una función que reciba dos números como parámetro (base y exponente), y retorne el resultado de elevar base a la 
potencia exponente.      
"""

def potencia(base,exponente):
    
    """ Esta función recibe dos números como parámetros (base y exponente), 
    y retorna el resultado de elevar la base al exponente"""
    
    resultado = base**exponente
    return resultado

def main():

    num1 = int(input("Ingrese un base de la potencia: "))
    num2 = int(input("Ingrese el exponente de la potencia: "))
           
    mostrar = potencia(num1,num2)

    print(f"El resultado de elevar {num1} a {num2} es: {mostrar}")
    
main()