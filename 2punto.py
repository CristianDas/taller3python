def sembrar_arboles(superficie_bosque):
    if superficie_bosque > 1000000:
        pino = superficie_bosque * 0.7
        oyamel = superficie_bosque * 0.2
        cedro = superficie_bosque * 0.1
    else:
        pino = superficie_bosque * 0.5
        oyamel = superficie_bosque * 0.3
        cedro = superficie_bosque * 0.2

    return pino, oyamel, cedro


superficie_bosque = float(input("Ingrese la superficie del bosque en metros cuadrados: "))

pino, oyamel, cedro = sembrar_arboles(superficie_bosque)

print("Cantidad de árboles de pino:", pino)
print("Cantidad de árboles de oyamel:", oyamel)
print("Cantidad de árboles de cedro:", cedro)
