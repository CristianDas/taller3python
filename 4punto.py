def calcular_salario_semanal(horas_trabajadas):
    salario_base = 20  
    horas_extra = max(horas_trabajadas - 40, 0) 
    salario_extra = 25 

    salario = (salario_base * min(horas_trabajadas, 40)) + (salario_extra * horas_extra)

    return salario


num_obreros = int(input("Ingrese el número de obreros: "))

for i in range(num_obreros):
    horas_trabajadas = float(input("Ingrese las horas trabajadas del obrero {}: ".format(i + 1)))
    salario_semanal = calcular_salario_semanal(horas_trabajadas)
    print("Salario semanal del obrero {}: ${:.2f}".format(i + 1, salario_semanal))
