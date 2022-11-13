"""

Escribe un programa que solicite una puntuación entre 0.0 y 1.0. Si la
puntuación está fuera de ese rango, muestra un mensaje de error. Si la puntuación
está entre 0.0 y 1.0, muestra la calificación usando la tabla siguiente:


Puntuación Calificación
>= 0.9 Sobresaliente
>= 0.8 Notable
>= 0.7 Bien
>= 0.6 Suficiente
< 0.6 Insuficiente


* Introduzca puntuación: 0.95
Sobresaliente

* Introduzca puntuación: perfecto
Puntuación incorrecta

* Introduzca puntuación: 10.0
Puntuación incorrecta

* Introduzca puntuación: 0.75
Bien

* Introduzca puntuación: 0.5
Insuficiente

Ejecuta el programa repetidamente, como se muestra arriba, para probar con varios
valores de entrada diferentes.

"""

puntuacion = float(input("Introduce la puntuación: "))

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
    
