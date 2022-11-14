"""

Escriba un programa para solicitar al usuario las horas y la tarifa por hora utilizando la entrada para calcular el pago bruto. 
Utilice 35 horas y una tarifa de 2,75 por hora para probar el programa (la paga debería ser de 96,25). Debe usar input para leer 
una cadena y float() para convertir la cadena en un número. No se preocupe por la verificación de errores o datos de usuario incorrectos.

"""
horas_trabajadas = float(input("Introduce la cantidad de horas trabajadas: "))
tarifa_horas = float(input("Introduce la tarifa por hora: "))

salario_bruto = horas_trabajadas * tarifa_horas

print(salario_bruto)

