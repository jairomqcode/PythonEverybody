"""

Escriba un programa para solicitar al usuario las horas y la tarifa por hora utilizando la entrada para calcular el pago bruto. 
El pago debe ser la tarifa normal por horas hasta 40, y tiempo y medio por la tarifa por hora para todas las horas trabajadas por 
encima de las 40 horas. Ponga la lógica para realizar el cálculo del pago en una función llamada computepay() y use la función para 
realizar el cálculo. La función debe devolver un valor. Utilice 45 horas y una tarifa de 10,50 por hora para probar el programa 
(la paga debería ser de 498,75). Debe usar input para leer una cadena y float() para convertir la cadena en un número. No se preocupe
por el error al verificar la entrada del usuario a menos que lo desee; puede asumir que el usuario escribe los números correctamente. 
No nombre su variable sum ni use la función sum().

"""

# Definimos la función parametrizada en función a las horas trabajadas y la tarifa por hora:
def computepay(horas, tarifas):
    #Nuestra condicionales:
    if horas < 40 :

        return horas * tarifas

    else :
        return ((40 * tarifas) + ((horas - 40) * (tarifas * 1.5)))

# Datos de entradas
horas = input("Introduce el numero de horas:")
tarifas = input("Introduce la tarifa por hora trabajada: ")

#Convertimos los tipos de datos:
horas2 = float(horas)
tarifas2 = float(tarifas)

#Resultado:
print("Pago", computepay(horas2,tarifas2))
