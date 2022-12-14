"""

Reescribe el programa del cálculo del salario para darle al empleado 1.5 veces la tarifa horaria para todas las horas trabajadas que excedan de 40.

Introduzca las Horas: 45
Introduzca la Tarifa por hora: 10
Salario: 475.0

"""

# Datos de entrada por parte del usuario:
horas = input("Enter Hours:")
tarifa = input ("Enter rate: ")

# Convertir los datos de tipo string a float:
h = float(horas)
t = float(tarifa)

# Calculamos el valor del pago total para las 40 horas trabajadas.
# También tomamos en cuenta el valor de la tarifa por hora en 10$.
sueldo_mensual = 40 * t

# Calculamos el número de horas extras trabajada:
h_extra = h - 40

# Calculamos la tarifa por hora extras:
tarifa_horas_extra = t * 1.5

# Aplicamos nuestras condicionales bien sea el caso:
if h > 40:
    sueldo_mensual_extra = sueldo_mensual + ((h_extra)*(tarifa_horas_extra))
    print(sueldo_mensual_extra)
else:
    print(sueldo_mensual)
