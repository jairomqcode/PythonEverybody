"""
Ejercicio: Ecribir un programa que muestre los cuadrados de los 
60 primeros números naturales. Resolverlo while y for.
"""

# BUCLE WHILE:
#Iniciamos el contador:
contador = 0
#Aplicamos el bucle while:
while contador <= 60:
    #Ecuación:
    cuadrado = contador * contador
    #Imprimir resultado:
    print(f"El cuadrado de {contador} es {cuadrado}")
    #Actualizamos:
    contador += 1

print("#########################")

# BUCLE FOR:
for numero in range(61):
    #Ecuación:
    cuadrado = numero * numero
    #Imprimir resultado:
    print(f"El cuadrado de {numero} es {cuadrado}")
