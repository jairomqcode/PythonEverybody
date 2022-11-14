""" 

Escriba un programa para solicitar al usuario las horas y la tarifa por hora utilizando la entrada para calcular el pago bruto. 
Pague la tarifa por hora por las horas hasta 40 y 1,5 veces la tarifa por hora por todas las horas trabajadas por encima de las 40 horas. 
Utilice 45 horas y una tarifa de 10,50 por hora para probar el programa (la paga debería ser de 498,75). Debe usar input para leer una 
cadena y float() para convertir la cadena en un número. No se preocupe por el error al verificar la entrada del usuario; suponga que el 
usuario escribe los números correctamente.

"""

# Datos de entrada por parte del usuario:
horas = input("Enter Hours:")
tarifa = input ("Enter rate: ")

# Convertir los datos de tipo string a float:
h = float(horas)
t = float(tarifa)

# Calculamos el valor del pago total para las 40 horas trabajadas:
# También tomamos en cuenta el valor de la tarifa por hora en 10.50
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

