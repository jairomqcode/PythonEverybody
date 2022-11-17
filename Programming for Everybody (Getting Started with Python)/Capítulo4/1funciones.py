"""

FUNCIONES.

En el contexto de la programación, una función es una secuencia de sentencias que
realizan una operación y que reciben un nombre. Cuando se define una función, se
especifica el nombre y la secuencia de sentencias. Más adelante, se puede “llamar”
a la función por ese nombre.

def nombre_función():
    Secuencia de sentencias

nombre_función()

"""

def saludos():
    print("Hola Nicole y Laurent, papi las ama!")

saludos()
print("########################################")

""" Una vez que se ha definido una función, puede usarse dentro de otra. """
def repetir_dosveces():
    print("Hola Nicole y Laurent, papi las ama!")
    print("Hola Nicole y Laurent, papi las ama!")

repetir_dosveces()
print("########################################")


""" 

FUNCIONES PARAMETRIZADAS.

Dentro de las funciones, los argumentos son asignados a variables llamadas parámetros.

def nombre_función(parámetro):
    Secuencia de sentencias(parámetro)

nombre_función(argumento)

"""

def muestra_tres_veces(nombre):
    print(f"Hola {nombre}")
    print(f"Hola {nombre}")
    print(f"Hola {nombre}")

muestra_tres_veces("NicLau")
print("########################################")



"""

Para devolver un resultado desde una función, usamos la sentencia "return" dentro
de ella. Por ejemplo, podemos crear una función muy simple llamada sumados, que 
suma dos números y devuelve el resultado.

"""



def sumados(a, b):
    suma = a + b
    return suma

x = sumados(3, 5)
print(x)
print("########################################")



"""

FUNCIONES MATEMÁTICAS.

Python tiene un módulo matemático "math", que proporciona la mayoría de las
funciones matemáticas habituales. Antes de que podamos utilizar el módulo,
deberemos importarlo.

import nombre_módulo

"""

# Cálculamos la raiz cuadrada de 25:
import math
#Definimos una variable:
x = 25
# Definimos la ecuación utilizando el módulo matemático:
raiz_cuadrada = math.sqrt(x)
# Resultado:
print(raiz_cuadrada)
print("########################################")


"""

NÚMEROS ALEATORIOS.

* Los números "pseudoaleatorios" no son verdaderamente aleatorios, ya que son generados
por una operación determinista, pero si sólo nos fijamos en los números resulta casi
imposible distinguirlos de los aleatorios de verdad.

* El módulo "random" proporciona funciones que generan números pseudoaleatorios
(a los que simplemente llamaremos “aleatorios” de ahora en adelante).

* La función "random" devuelve un número flotante aleatorio entre 0.0 y 1.0 (incluyendo
0.0, pero no 1.0). Cada vez que se llama a random, se obtiene el número siguiente de una
larga serie.

"""

import random

for i in range(10):
    x = random.random()
    print(x)
print("########################################")

"""

FUNCIONES INTERNAS.

Python proporciona un número importante de funciones internas, que pueden ser
usadas sin necesidad de tener que definirlas previamente. Los creadores de Python
han escrito un conjunto de funciones para resolver problemas comunes y las han
incluido en Python para que las podamos utilizar.

"""

print(max("Hola mundo"))        #La función max nos dice cuál es el “carácter más grande” de la cadena.
print(min("Hola mundo"))        #La función min nos dice cuál es el “carácter más pequeño” de la cadena.
print("########################################")

""" Otra función interna muy común es len(), que nos dice cuántos elementos hay en su argumento."""
print(len("Hola mundo"))
