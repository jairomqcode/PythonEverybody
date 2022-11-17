"""


CONDICIONALES ENCADENADOS:
Condicional IF, ELIF y ELSE.

if condición:
    instrucciones

elif condición:
    otras instrucciones

else:
    otro grupo de instrucciones


* No hay un límite para el número de sentencias elif.

* La sentencia else debe ir siempre al final.

* Cada condición es comprobada en orden.

"""

# Definimos dos variables:
x = 4 
y = 2

# Aplicamos las condicionales:
if x > y:
    print("X es mayor")
elif x < y:
    print("X es menor")
else:
    print("X e Y son iguales")