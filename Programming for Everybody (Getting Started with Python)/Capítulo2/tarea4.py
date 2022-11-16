"""

Ejercicio: Escribe un programa que le pida al usuario una temperatura en grados Celsius,
la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.

Ecuación:

ºF = (ºC · 1,8) + 32

"""

# Temperatura por parte del usuario:
temperatura = float(input("Introduce la temperatura en grados celsius: "))

# Ecuación:
Fahrenheit = (temperatura * 1.8) + 32

# Resultado:
print(Fahrenheit)
