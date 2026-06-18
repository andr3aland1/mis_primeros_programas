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


def herencia(cantidad):
    """calcula y devuelve la suma a repartir y la herencia que recibió cada hijo."""
    carlos = cantidad * 1/3
    jose = carlos * 4/3
    marta = jose/2
    fortuna = carlos + jose + marta
    return fortuna, carlos, jose, marta

# Actividad 4


def corregir_tiempo(horas, minutos, segundos):
    """Transforma una medida arbitraria de tiempo en una expresión correcta y la devuelve"""
    minutos = minutos + segundos // 60
    segundos = segundos % 60

    horas = horas + minutos // 60
    minutos = minutos % 60

    return horas, minutos, segundos

# Actividad 5

def precio_final(costo):
    """calcula el precio final usando el costo, el porcentaje de beneficios (8%) y el I.V.A. 
    Retorna el resultado con dos decimales"""
    vendedor = costo*0.08
    iva = costo*0.21
    final = costo+vendedor+iva
    return round(final,2)


    
    
