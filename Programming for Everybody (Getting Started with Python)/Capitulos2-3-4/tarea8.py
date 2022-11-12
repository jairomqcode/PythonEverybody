"""

Reescribe el programa del cálculo del salario para darle al empleado 1.5 veces
la tarifa horaria para todas las horas trabajadas que excedan de 40.

"""
# Introducimos los valores:
horas_trabajadas = float(input("Introduce la cantidad de horas trabajadas: "))
tarifa_horas = float(input("Introduce la tarifa por hora: "))
horas_extras = float(input("Introduce las horas extras trabajadas: "))

# Ecuaciones para los cálculos:
salario_bruto = horas_trabajadas * tarifa_horas
salario_extra = horas_extras * (tarifa_horas * 1.5)
salario_total = salario_bruto + salario_extra

# Resultado final:
print(salario_total)