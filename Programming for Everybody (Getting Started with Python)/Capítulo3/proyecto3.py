"""

Escribe un programa que solicite una puntuación entre 0.0 y 1.0. Si la puntuación está fuera de ese rango, muestra un mensaje de error. 
Si la puntuación está entre 0.0 y 1.0, muestra la calificación usando la tabla siguiente:

Puntuación Calificación
>= 0.9 Sobresaliente
>= 0.8 Notable
>= 0.7 Bien
>= 0.6 Suficiente
< 0.6 Insuficiente


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

score = input("Enter Score: ")

#Convertimos el dato de entrada de String a Float y lo guardamos en una variable:
nota = float(score)

#Nuestras condicionales:
#Primero para los valores fuera de rangos:
if nota < 0.0 or nota >1.0:
    print("Estas fuera del rango")
    
#Segundo, para valores dentro del rango:
elif nota < 0.6:
    print("F")
    
elif nota >= 0.6 and nota < 0.7:
    print("D")

elif nota >= 0.7 and nota < 0.8:
    print("C")
    
elif nota >= 0.8 and nota < 0.9:
    print("B")

else:
    print("A")
    
