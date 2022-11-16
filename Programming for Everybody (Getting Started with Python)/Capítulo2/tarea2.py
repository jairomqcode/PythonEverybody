"""

Ejercicio: Escribe un programa para pedirle al usuario el número de horas y la tarifa por hora
para calcular el salario bruto.

Introduzca Horas: 35
Introduzca Tarifa: 2.75
Salario: 96.25

"""

# Datos por parte del usuario:
hora_trabajo = float(input("Introduce las horas trabajadas: "))
tarifa = float(input("Introduce la tarifa por hora: "))

# Ecuaciones:
salario_promedio = hora_trabajo * tarifa

# Resultado:
print(f"El salario a ganar es: {salario_promedio}")
