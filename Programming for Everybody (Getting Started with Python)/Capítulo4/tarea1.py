"""

Reescribe el programa de cálculo del salario, con tarifa y media para las horas extras,
y crea una función llamada calculo_salario que reciba dos parámetros (horas y tarifa).

Introduzca Horas: 45
Introduzca Tarifa: 10
Salario: 475.0

"""

# Definimos la función parametrizada en función a las horas trabajadas y la tarifa por hora:
def calculo_salario(horas, tarifa):
    #Nuestra condicionales:
    if horas < 40 :

        return horas * tarifa

    else :
        return (40 * tarifa + (horas - 40) * (tarifa * 1.5))

# Datos de entradas:
horas_usuario = input("Introduce el número de horas:")
tarifa_usuario = input("Introduce la tarifa por hora trabajada: ")

#Convertimos los tipos de datos:
hrs = float(horas_usuario)
rate = float(tarifa_usuario)

#Resultados:
print("El pago es: ", calculo_salario(hrs,rate))