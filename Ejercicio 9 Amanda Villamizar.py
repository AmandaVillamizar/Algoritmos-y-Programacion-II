#Ejercicio 9
#Solicitar datos al usuario
presupuesto = float(input("Ingrese el presupuesto del proyecto: "))
precio_proyecto = float(input("Ingrese el precio del proyecto: "))

#Calcular la diferencia porcentual
diferencia_porcentual = ((presupuesto - precio_proyecto) / presupuesto) * 100

#Determinar la factibilidad
if diferencia_porcentual >= 75:
    factible = True
else:
    factible = False

#Mostrar resultados
print(f"Diferencia porcentual: {diferencia_porcentual:}%")
if factible:
    print("El proyecto es factible")
else:
    print("El proyecto no es factible")
