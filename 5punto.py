def calcular_descuento(edad):
    if edad >= 5 and edad <= 14:
        return 0.35 
    elif edad >= 15 and edad <= 19:
        return 0.25 
    elif edad >= 20 and edad <= 45:
        return 0.10 
    elif edad >= 46 and edad <= 65:
        return 0.25  
    elif edad >= 66:
        return 0.35 
        return 0

precio_asiento = float(input("Ingrese el precio del asiento: "))
total_descuento = 0

while True:
    edad = int(input("Ingrese la edad del cliente (o ingrese -1 para salir): "))
    if edad == -1:
        break
    
    descuento = calcular_descuento(edad)
    descuento_dinero = descuento * precio_asiento
    total_descuento += descuento_dinero

    print("Descuento para la edad {}: ${:.2f}".format(edad, descuento_dinero))

print("Total de dinero que el teatro deja de percibir: ${:.2f}".format(total_descuento))
