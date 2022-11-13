""" 
Reescribe el programa de cálculo del salario, con tarifa y media para las horas extras, 
y crea una función llamada calculo_salario que reciba dos parámetros (horas y tarifa). 

Introduzca Horas: 45
Introduzca Tarifa: 10
Salario: 475.0

"""

"""
# Introducción de valores:
horas_trabajadas = float(input("Introduce la cantidad de horas trabajadas: "))
tarifa_horas = float(input("Introduce la tarifa por hora: "))
horas_extras = float(input("Introduce las horas extras trabajadas: "))
"""

# Ecuaciones para los cálculos:
# Definimos las Función parametrizada:
def calculo_salario(horas_trabajadas, tarifa_horas, horas_extras):
    salario_bruto = horas_trabajadas * tarifa_horas
    salario_extra = horas_extras * (tarifa_horas * 1.5)
    salario_total = salario_bruto + salario_extra
    print(salario_total)

# Llamar a la función parametrizada:
calculo_salario(horas_trabajadas = 40, tarifa_horas = 10, horas_extras = 5)
