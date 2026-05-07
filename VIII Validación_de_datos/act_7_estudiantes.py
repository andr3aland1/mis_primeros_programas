""" La Universidad ha lanzado una nueva plataforma virtual. Los estudiantes deben registrarse ingresando la siguiente información:
• Nombre de usuario (Debe tener más de 6 caracteres)
• Contraseña (Debe tener más de 8 caracteres, incluyendo números y letras)
• Repetir Contraseña (Debe coincidir con la anterior)
• Año de nacimiento (Debe abarcar un rango desde [Año actual-100; Año Actual]
Por último el programa debe mostrar un resumen de los datos ingresados. """

usuario = input("Ingrese el nombre se usuario: ")

while len(usuario) <= 6:
    usuario = input("El nommbre de usuario debe tener más de 6 caracteres.Vuelva a intentarlo:")

primer_contrasenia = input("Ingrese la contraseña: ")

while (len(primer_contrasenia) <= 8 ) and primer_contrasenia.isdigit() or primer_contrasenia.isalpha():
    primer_contrasenia = input("La contraseña debe tener más de 8 caracteres e incluir números y letras: ")

segunda_contrasenia = input("Vuelva a ingresar la constraseña: ")

while primer_contrasenia != segunda_contrasenia:
    segunda_contrasenia = input("Las contraseñas deben coincidir: ")

anio_nacimiento = input("Ingrese su año de nacimiento: ") 

while (not anio_nacimiento.isdigit()) or (int(anio_nacimiento) < 1926 or int(anio_nacimiento) > 2026):
    anio_nacimiento = input("Ingresee un año valido: ")

print("Guarde sus datos de usuario y no los comparta:")
print(f"Usuario: {usuario}\nContraseña{primer_contrasenia}\nAño nacimiento:{anio_nacimiento}")