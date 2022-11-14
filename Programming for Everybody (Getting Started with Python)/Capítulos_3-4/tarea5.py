"""

Reescribe el programa de cálculo del salario, con tarifa y media para las horas extras (1.5), 
y crea una función llamada calculo_salario que reciba dos parámetros (horas y tarifa). 

Introduzca Horas: 45
Introduzca Tarifa: 10
Salario: 475.0

"""

# Definimos la función parametrizada en función a las horas trabajadas y la tarifa por hora:
def salario_total(horas, tarifas):
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
print("Pago", salario_total(horas2,tarifas2))