"""

1. Operadores: son símbolos especiales que representan cálculos.

2. Operandos: son los valores a los cuales se aplican los operadores.

3. Operadores Matemáticos:

* Suma (+)
* Resta (-)
* Multiplicación (*)
* División (/)
* División entera (//)
* Módulo (%)

4. Expresión: es una combinación de valores, variables y operadores.

5. Orden de las operaciones: el orden depende de las reglas de precedencia.

I. Los paréntesis tienen el nivel superior de precedencia.

II. La exponenciación (elevar un número a una potencia) tiene el siguiente
nivel más alto de precedencia.

III. La Multiplicación y la División tienen la misma precedencia, que es
superior a la de la Suma y la Resta.

IV. Los operadores con igual precedencia son evaluados de izquierda a derecha.

"""

# Creamos variables y les asignamos valores:
numero1 = 2
numero2 = 4

# Cálculos:
suma = numero1 + numero2
resta =numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
modulo = numero2 % numero1

# Resultados:
print(f"La suma es: {suma}")
print(f"La resta es: {resta}")
print(f"La multiplicación es: {multiplicacion}")
print(f"La división es: {division}")
print(f"La módulo es: {modulo}")