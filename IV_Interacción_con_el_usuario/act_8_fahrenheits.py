def fahrenheits_funcion (grados):
    """ Esta función convierte los grados Celcius en Fahrenheits. 
    La fórmula se debe a que las escalas Celsius y Fahrenheit 
    tienen tamaños de grado diferentes y puntos de inicio (congelación) distintos. 
    El factor ajusta la proporción entre los tamaños de los grados, 
    mientras que el compensa el desplazamiento del punto de congelación del agua. """
    return (grados * 1.8) + 32

grados = float(input("Ingrese cantidad de grados en Celcius: "))
fahrenheits = fahrenheits_funcion (grados)
print("La temperatura en Fahrenheits es de: ", round(fahrenheits,2))