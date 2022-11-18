"""
Ejercicio. Escribir un script que nos muestre por pantalla
todos los números pares del 1 al 120.
"""

#Iniciamos el contador:
contador = 1
# Aplicamos el bucle for:
for contador in range(1, 121):
    if contador % 2 == 0:
        print(f"{contador} es par")
