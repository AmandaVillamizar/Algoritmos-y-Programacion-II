#Ejercicio 4
#Solicitar datos al usuario
nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo (M para mujer, H para hombre): ")

#Determinar el grupo según el nombre y el sexo
if (sexo == 'M' and nombre < 'm') or (sexo == 'H' and nombre > 'n'):
    grupo = 'A'
else:
    grupo = 'B'

#Mostrar el grupo correspondiente
print(f"El grupo que le corresponde es: {grupo}")
