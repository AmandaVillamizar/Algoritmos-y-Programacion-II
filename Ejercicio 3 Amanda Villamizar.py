#Ejercicio 3
#Almacenar la contraseña en una variable
contraseña_guardada = "MangoyDora"

#Preguntar al usuario por la contraseña
contraseña_introducida = input("Ingrese la contraseña: ")

#Verificar si la contraseña introducida coincide con la guardada
if contraseña_guardada == contraseña_introducida:
    print("La contraseña es correcta")
else:
    print("La contraseña es incorrecta")
