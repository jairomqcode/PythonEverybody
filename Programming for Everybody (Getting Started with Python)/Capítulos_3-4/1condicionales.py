"""
Ejecución Condicional.

Casi siempre vamos a necesitar la capacidad de comprobar condiciones y cambiar el comportamiento 
del programa de acuerdo a ellas. Las sentencias condicionales nos proporcionan esa capacidad. La
forma más sencilla es la sentencia "if":

if condición:
    Ejecución de sentencias...

Si la condición lógica es verdadera, la sentencia anidada será ejecutada. Si la condición es falsa,
la sentencia indentada será omitida.
"""

x = 7
if x > 0:
    print("x es positivo")


"""
Ejecución Alternativa.

La segunda forma de la sentencia "if" es la "ejecución alternativa", en la cual existen dos posibilidades
y la condición determina cual de ellas será ejecutada:

if condición:
    Ejecución de sentencias...

else:
    Ejecución de sentencias...


Las alternativas reciben el nombre de ramas, dado que se trata de ramificaciones en el flujo de la ejecución.

"""


y = 4

if y%2 == 0:
    print("y es par")
else:
    print("y es impar")


"""
Condicionales Encadenados.

Algunas veces hay más de dos posibilidades, de modo que necesitamos más de dos ramas. Una forma de expresar 
una operación como esá es usar un condicional encadenado:

if condición:
    Ejecución de sentencia...

elif condición:
    Ejecución de sentencia...

else:
    Ejecución de sentencia...

elif es una abreviatura para "else if". No hay un limite para el número de sentencias elif. Si hay una clausula,
else debe ir al final, pero tampoco es obligatorio que ésta exista.

Cada condición es comprobada en orden. Incluso si hay más de una condición que sea verdadera, sólo se ejecuta
la primera que se encuentra.

"""

x1 = 1
x2 = 3

if x1 < x2:
    print("x1 es menor que x2")
elif x1 > x2:
    print("x1 es mayor x2")
else:
    print("x1 y x2 son iguales")



"""

Condicionales anidados.

Un condicional puede también estar anidado dentro de otro.

"""

a = 2
b = 4

if a == b:
    print("a y b son iguales")
else:
    if a < b:
        print("a es menor que b")
    else:
        print("a es mayor que b")

"""

La condición exterior contiene dos ramas:
- Primera rama: ejecuta una sentencia simple.

- Segunda rama: contiene otra sentencia if, que tiene a su vez sus propias dos ramas.
Estas dos ramas son ambas sentencias simples, pero podrían haber sido sentencias 
condicionales también.

Es buena idea evitar las sentencias anidadas si se puede!!!

Los operadores lógicos a menudo proporcionan un modo de simplificar las sentencias
condicionales anidadas.

"""

if 0 < a:
    if a < 10:
        print("a es un número positivo de un sólo dígito")

"""

La sentencia print se ejecuta solamente si se cumple las dos condiciones anteriores, 
así que en realidad podemos conseguir el mismo efecto con el operador "and":

"""

if 0 < a and a < 10:
    print("a es un número positivo de un sólo dígito")
