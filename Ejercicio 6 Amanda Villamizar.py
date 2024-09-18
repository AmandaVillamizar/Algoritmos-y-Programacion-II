#EJERCICIO Nª6
#Programa para calcular descuento de zapatos
#Determinamos precio de cada zapato
precio_por_zapato = 80

#Solicitamos la cantidad de zapatos al usuario
cantidad = int(input("Ingrese la cantidad de zapatos que desea comprar: "))

#Calculamos el total antes de descuento
total_compra = cantidad * precio_por_zapato

#Determinamos el porcentaje de descuento y usamoa los auxiliares if-elif-else
if cantidad > 30:
 descuento = 0.40  # 40% de descuento
elif cantidad >= 20:
 descuento = 0.20  # 20% de descuento
elif cantidad > 10:
 descuento = 0.10  # 10% de descuento
else:
 descuento = 0.00  # Sin descuento

#Calculamos el total después del descuento
total_descuento = total_compra * (1 - descuento)

#Mostrar resultados
print(f"\nTotal original: ${total_compra: }")
print(f"Descuento aplicado: {descuento * 100: }%")
print(f"Total después del descuento: ${total_descuento: }")
