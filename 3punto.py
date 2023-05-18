def obtener_categoría_edad(edad):
    if edad <= 12:
        return "Niños"
    elif edad <= 29:
        return "Jóvenes"
    elif edad <= 59:
        return "Adultos"
    else:
        return "Viejos"

cantidad_muestreo = 50
pesos_por_categoría = {"Niños": [], "Jóvenes": [], "Adultos": [], "Viejos": []}

for i in range(cantidad_muestreo):
    edad = int(input("Ingrese la edad de la persona {}: ".format(i + 1)))
    peso = float(input("Ingrese el peso de la persona {}: ".format(i + 1)))
    categoría = obtener_categoría_edad(edad)
    pesos_por_categoría[categoría].append(peso)

promedios_por_categoría = {}

for categoría, pesos in pesos_por_categoría.items():
    if len(pesos) > 0:
        promedio = sum(pesos) / len(pesos)
    else:
        promedio = 0
    promedios_por_categoría[categoría] = promedio

print("Promedio de peso por categoría de edad:")
for categoría, promedio in promedios_por_categoría.items():
    print("{}: {:.2f}".format(categoría, promedio))
