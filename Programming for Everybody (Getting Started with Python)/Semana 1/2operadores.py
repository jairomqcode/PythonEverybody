"""
- Sentencias: es una unidad de código que el interprete de python puede ejecutar.

- Script: contiene una secuencia de sentencias.

- Operadores: son símbolos especiales que representan cálculos. Los valores a los cuales se aplican esos operadores reciben el nombre de "operandos".

- Expresiones: es una combinación de valores, variables y operadores.

- Orden de las operaciones:
El orden de evaluación depende de las reglas de precedencia.

1. Los "Paréntesis" tienen el nivel superior de precedencia.
2. La "Exponenciación" tiene el siguiente nivel más alto de precedencia.
3. La "Multiplicación y la División" tienen la misma precedencia, que es superior a la de la "Suma y la Resta".
4. Los operadores con igual precedencia son evaluados de izquierda a derecha.

- Operador Módulo: trabaja con enteros y obtiene el resto de la operación consistente en dividir el primer operando por el segundo operando.

- Operaciones con cadenas: 
	El operador + funciona con las cadenas, realiza una "Concatenación", que quiere decir que une ambas cadenas, enlazando la parte final de la primera con el principio de la segunda.
	
	El operador * también trabaja con cadenas, multiplicando el contenido de una cadena por un entero.
	
"""

# Definimos las variables:
x = 5
y = 2

z = "nico"
p = "lau"
o = 3

# Operaciones:
suma = x + y
resta = x - y
multiplicacion = x * y
division = x / y
potencia = x ** y
division_entera = x // y
modulo = x % y
operacion = 2 + (3 * 4) - 5 / 2 + (2 ** 4) + (5 % 3)

# Resultados:
print(suma)
print(resta)
print(multiplicacion)
print(division)
print(potencia)
print(division_entera)
print(modulo)
print(operacion)
print(z + p)
print(z * o)
