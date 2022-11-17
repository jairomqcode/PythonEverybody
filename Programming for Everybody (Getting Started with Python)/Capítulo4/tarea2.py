"""

Reescribe el programa de calificaciones del capítulo anterior usando una función 
llamada calcula_calificacion, que reciba una puntuación como parámetro y devuelva
una calificación como cadena.

Puntuación Calificación:
> 0.9 Sobresaliente
> 0.8 Notable
> 0.7 Bien
> 0.6 Suficiente
<= 0.6 Insuficiente

Introduzca puntuación: 0.95
Sobresaliente

Introduzca puntuación: perfecto
Puntuación incorrecta

Introduzca puntuación: 10.0
Puntuación incorrecta

Introduzca puntuación: 0.75
Bien

Introduzca puntuación: 0.5
Insuficiente

"""

# Creamos la función:
def calcula_calificacion(nota):
    #Nuestras condicionales:
    #Primero para los valores fuera de rangos:
    if nota < 0.0 or nota >1.0:
        print("Estas fuera del rango")
        
    #Segundo, para valores dentro del rango:
    elif nota < 0.6:
        print("Insuficiente")
        
    elif nota >= 0.6 and nota < 0.7:
        print("Suficiente")

    elif nota >= 0.7 and nota < 0.8:
        print("Bien")
        
    elif nota >= 0.8 and nota < 0.9:
        print("Notable")

    else:
        print("Sobresaliente")

    #return

score = input("Introduce nota: ")
#Convertimos el dato de entrada de String a Float y lo guardamos en una variable:
nota = float(score)
#Resultado:
calcula_calificacion(nota)