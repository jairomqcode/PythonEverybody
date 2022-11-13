"""

- Llamadas a funciones.
Una FUNCIÓN es una secuencia de sentencias que realizan una operación y que reciben un nombre.
Más adelante, se puede "llamar" a la función por ese nombre.

- Funciones internas.
Los creadores de Python han escrito un conjunto de funciones para resolver problemas comunes y 
las han incluido en Python para que las podamos utilizar.

"""

""" Las funciones 'max' y 'min' nos darán respectivamente el valor mayor y menor de una lista. """

print(max("Hola mundo"))
print(min("Hola mundo"))

""" 

En una cadena la función max nos dice cuál es el 'caracter más grande' y la función min nos dice 
cuál es el 'caracter más pequeño'. 

"""

""" 

La función 'len' nos dice cuantos elementos hay en su argumento. Si el argumento de 'len' es una cadena, 
nos devuelve el número de caracteres que hay en la cadena.

"""

print(len("Hola mundo"))

""" Se deben tratar los nombres de las funciones internas como si fueran palabras reservadas. """

"""

Funciones de conversión de tipos.
- Función int(): puede convertir valores en punto flotante a enteros, pero no los redondea; simplemente
 corta y descarta la parte decimal.

- Función float(): convierte enteros y cadenas en números de punto flotante.

- Función str(): convierte su argumentos en una cadena.

"""

print("\n##########")
print(int("7"))
print(int(3.14159))
print(int(-2.5))

print("\n##########")
print(float(32))
print(float("3.14159"))

print("\n##########")
print(str(32))
print(str(3.14159))
print("\n##########")

""" 
Funciones Matemáticas.
Python tiene un módulo matemático (math), que proporciona la mayoría de las funciones matemáticas habituales.

"""

import math
import random

""" 

Esta sentencia crea un objeto módulo llamado math.
El objeto módulo contiene las funciones y variables definidas en el módulo.
Para acceder a una de esas funciones, es necesario especificar el numbre del módulo y el nombre de la función, 
separados por un punto. Este formato recibe el nombre de "notación punto".

"""

grados = 45
radianes = grados / 360.0 * 2 * math.pi
print(math.sin(radianes))
print("\n##########")

"""
Números aleatorios.
- Números pseudoaleatorios: no son verdaderamente aleatorios, ya que son generados por una operación
determinista, pero si sólo nos fijamos en los números resulta casi imposible distinguirlos de los aleatorios de verdad.

- Módulo random: proporciona funciones que generan números pseudoaleatorios (a los que simplemente llamaremos 
"aleatorios" de ahora en adelante).

El módulo random devuelve un número flotante aleatorio entre 0.0 y 1.0 (incluyendo 0.0, pero no 1.0).

El módulo random también proporciona funciones para generar valores aleatorios de varias distibuciones 
continuas, incluyendo gaussiana, exponencial, gamma, y unas cuantas más.

"""

i = 0

for i in range(10):
    x = random.random()
    print(x)

print("\n##########")

""" 

La función 'randint' toma los parámetros inferior y superior, y devuelve un entero entre inferior y superior 
(incluyendo ambos extremos). 

"""
print(random.randint(5, 10))
print(random.randint(5, 10))
print("\n##########")

"""

Añadiendo funciones nuevas.

- Una "definición de función" especifica el nombre de una función nueva y la secuencia de sentencias que se ejecutan cuando
esa función es llamada. Una vez definida una función, se puede reutilizar una y otra vez a lo largo de todo el programa.

"""

def saludos():
    print("Hola Nicole")
    print("Hola Laurent")

saludos()
print(type(saludos))
print("\n##########")
"""
def es una palabra clave que indica que se trata de una definición de función. Las reglas para los nombres de las funciones
son los mismos que para las variables. Los parentesis vacíos después del nombre indican que esta función no toma ningún argumento.

La primera línea de la función es llamada la cabecera; el resto se llama el cuerpo. La cabecera debe terminar con dos puntos (:),
y el cuerpo debe ir identado. Por convención, el identado debe ser siempre de cuatro espacios. El cuerpo puede contener cualquier
número de sentencias.

Para finalizar la función, debes introducir una línea vacía. Al definir una función se crea una variable con el mismo nombre.
La sintaxis para llamar a nuestra nueva función es la misma que usamos para las funciones internas.

Una vez que se ha definido una función, puede usarse dentro de otra.
"""

def repetir_saludos():
    saludos()
    saludos()

repetir_saludos()
print("\n##########")

"""

Flujo de ejecución: es el orden en que las sentencias son ejecutadas.

La ejecución siempre comienza en la primera sentencia del programa. Las sentencias son ejecutadas una por una,
en orden de arriba hacia abajo.

Las sentencias dentro de una función no son ejecutadas hasta que se llama a esa función.

"""

"""

Parámetros y argumentos.
Dentro de las funciones, los argumentos son asignados a variables llamadas parámetros.

"""

def saludos_hijas(parametros):
    print(parametros)
    print(parametros)

saludos_hijas("Hola Nico y Lau")
print("\n##########")

def calculo(parametro):
    print(parametro)

calculo(math.pi)
print("\n##########")


"""

¿Por qué funciones?

* El crear una función nueva te da la oportunidad de dar nombre a un grupo de sentencias, lo cual hace tu 
programa más facil del leer, entender y depurar.

* Las funciones pueden hacer un programa más pequeño, al eliminar código repetido.

* Dividir un programa largo en funciones te permite depurar las partes de una en una y luego ensamblarlas 
juntas en una sola pieza.

* Las funciones bien diseñadas a menudo resultan útiles para otros muchos programas. Una vez que has escrito
y depurado una, puedes reutilizarla.

* Parte de la habilidad de crear y usar funciones consiste en llegar a tener una función que represente 
correctamente una idea.

"""
