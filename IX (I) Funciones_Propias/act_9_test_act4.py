def potencia(b,e):
    """La función retorna el resultado de elevar una base a un exponente."""
    P = b**e
    return P 

def test_potencia():
    """Test unitario para verificar potencia"""
    print("Iniciando test...")
    assert potencia (2,3) == 8
    assert potencia (2,-2) == 0.25
    assert potencia (-3,2) == 9
    print("Paso el test")   
test_potencia()