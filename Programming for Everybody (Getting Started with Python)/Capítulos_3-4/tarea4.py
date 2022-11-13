"""

Reescribe el programa de calificaciones del capítulo anterior usando una 
función llamada calcula_calificacion, que reciba una puntuación como parámetro 
y devuelva una calificación como cadena.

"""

puntuacion = float(input("Introduce la puntuación: "))

# Definimos la función:

def calcula_calificacion(puntuacion):
    if puntuacion >= 1.0:
        print("Puntuación incorrecta")
    elif puntuacion >= 0.9:
        print("Sobresaliente")
    elif puntuacion >= 0.8:
        print("Notable")
    elif puntuacion >= 0.7:
        print("Bien")
    elif puntuacion >= 0.6:
        print("Suficiente")
    else:
        print("Insuficiente")

calcula_calificacion(puntuacion)