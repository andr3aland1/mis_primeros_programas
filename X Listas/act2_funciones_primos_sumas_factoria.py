def es_primo(num):
    aux = num - 1
    while(num % aux > 0 and aux > 1):
        aux = aux - 1
    return aux == 1


def numeros_primos(lista):
    primos = list()
    for elemento in lista:
        if elemento > 2:
            if es_primo(elemento):
                primos.append(elemento)
        elif elemento > 1:
                primos.append(elemento)
    return primos

def suma_prom(lista):
    suma = 0
    prom = 0
    for e in lista:
        suma = suma + e
    prom = suma / len(lista)    
    return suma, prom
    
numeros = []
for i in range(0, 50):
    numeros.append(i)

res = numeros_primos(numeros)
print(res)
s, p = suma_prom(numeros)
print(f"La sumatoria es {s}, y el promedio es {p}")