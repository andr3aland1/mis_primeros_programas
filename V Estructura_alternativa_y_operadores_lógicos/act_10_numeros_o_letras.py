datos = input("Ingrese los datos: ")

if datos.isdigit ():
    print("Los datos ingresados son numéricos ")
elif datos.isalpha (): 
    print("Los datos ingresados son alfabéticos")
elif datos.isalnum ():
    print("Los datos ingresados son alfanuméricos")