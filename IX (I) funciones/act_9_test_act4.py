from act_4_fun_potencia import *

def test_potencia():
    print("Iniciando test...")
    assert potencia (2,3) == 8
    assert potencia (2,-2) == 0.25
    assert potencia (-3,2) == 9
    print("Paso el test")   
test_potencia()