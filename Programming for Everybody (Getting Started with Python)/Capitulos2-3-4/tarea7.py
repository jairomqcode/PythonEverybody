"""
¿Qué resultara de evaluar las siguientes expresiones? Presta especial atención
al tipo de datos que resulta de cada operación individual.

a) 1 / 2 / 4.0
b) 1 / 2.0 / 4.0
c) 1 / 2.0 / 4
d) 1.0 / 2 / 4
e) 4 ** .5

f) 4.0 ** (1 / 2)
g) 4.0 ** (1 / 2) + 1 / 2
h) 4.0 ** (1.0 / 2) + 1 / 2.0
i) 3e3 / 10
j) 10 / 5e-3

"""
import math

a = 1/2/4.0
print(a)
print(type(a))
print("#######")
b = 1 / 2.0 / 4.0
print(b)
print(type(b))
print("#######")
c = 1 / 2.0 / 4
print(c)
print(type(c))
print("#######")
d = 1.0 / 2 / 4
print(d)
print(type(d))
print("#######")
e = 4 ** .5
print(e)
print(type(e))
print("#######")
f = 4.0 ** (1 / 2)
print(f)
print(type(f))
print("#######")
g = 4.0 ** (1 / 2) + 1 / 2
print(g)
print(type(g))
print("#######")
h = 4.0 ** (1.0 / 2) + 1 / 2.0
print(h)
print(type(h))
print("#######")
i =  3 * math.exp(3)/10
print(i) 
print(type(i))
print("#######")
j = 10 / 5 * math.exp(-3)
print(j)
print(type(j))
print("#######")