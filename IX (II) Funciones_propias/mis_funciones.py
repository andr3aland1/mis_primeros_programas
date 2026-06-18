"""Define las funciones que ejecuten las siguientes consignas, con los parámetros formales correspondientes como así 
también el programa principal que las invoque y les envíe los parámetros reales y reciba el/los retorno/s correspondiente/s 
para mostrar:
"""

# Actividad 1
# opción 1 utilizando strings

def suma_cifras(numero):
    """retorna y calcula la suma de las cifras de un número enntero positivo de 4 cifras"""
    suma = 0
    for cifra in str(numero):
        suma = suma + int(cifra)
    return suma

# opción 2 utilizando módulo

def calculo_cifras(numero):
    """retorna y calcula la suma de las cifras de un número enntero positivo de 4 cifras"""
    unidades = numero % 10
    decenas = (numero//10) % 10
    centenas = (numero //100) % 10
    miles = (numero//1000) % 10
    suma = unidades + decenas + centenas + miles 
    return suma

# Actividad 2

def sueldo(cantidad,valor):
    """retorna el sueldo de un empleado calculando el porcentaje de comision y sumando el sueldo básico"""
    sueldo_base = 5000
    comision = (cantidad * 200) + (valor * 0.08)
    sueldo_total = sueldo_base + comision
    return sueldo_total

# Actividad 3

"""Un millonario excéntrico tenía tres hijos: Carlos, José y Marta. Al morir dejó el siguiente legado: 
A José le dejó 4/3 de lo que le dejó a Carlos. A Carlos le dejó 1/3 de su fortuna. 
A Marta le dejó la mitad de lo que le dejó a José. Diseña una función que calcule y devuelva la suma a 
repartir y la herencia que recibió cada hijo.
"""
def herencia(cantidad):
    carlos = cantidad * 1/3
    jose = carlos * 4/3
    marta = jose/2
    fortuna = carlos + jose + marta
    return fortuna, carlos, jose, marta



    
    
