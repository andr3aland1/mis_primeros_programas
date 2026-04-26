pesos = float(input("Ingrese la cantidad de pesos "))
dolar = 1450.0
reales = 260.3
euros = 1575.5
print(f"Usted tiene $ {pesos} pesos argentinos, los cuales se convierten en: \n \
- USD {pesos/dolar:.2f} \n - R$ {pesos/reales:.2f}\n - € {pesos/euros:.2f}")