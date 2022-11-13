"""
Escribe un programa que le pida al usuario una temperatura en grados Celcius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.
"""

temp_celcius = float(input("Introduce la temperatura en celcius: "))

temp_fahrenheit = (temp_celcius * 1.8) + 32

print(temp_fahrenheit)

