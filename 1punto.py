def calcular_inversion(monto_hipoteca, inversion_total):
    if monto_hipoteca < 1000000:
        inversion_propia = inversion_total * 0.5
        inversion_socio = inversion_total * 0.5
    else:
        inversion_propia = monto_hipoteca
        inversion_restante = inversion_total - monto_hipoteca
        inversion_propia += inversion_restante / 2
        inversion_socio = inversion_restante / 2

    return inversion_propia, inversion_socio

monto_hipoteca = float(input("Ingrese el monto de la hipoteca: "))
inversion_total = float(input("Ingrese el monto total de inversión requerido: "))

inversion_propia, inversion_socio = calcular_inversion(monto_hipoteca, inversion_total)

print("Inversión propia:", inversion_propia)
print("Inversión del socio:", inversion_socio)
