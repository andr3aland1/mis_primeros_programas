segundos = int(input("Ingrese los segundos: "))
# Prueba 10000 es 02:46:40 
horas = segundos // 3600 
resto_segundos = segundos % 3600
minutos = resto_segundos // 60 
resto_segundos = resto_segundos % 60
segundos = resto_segundos

print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")