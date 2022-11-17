"""

CONDICIONALES ANIDADOS:
Condicional IF y ELSE.

if condición:
    Primera instrucción

else:
    if condición:
        Segunda instrucción
    else:
        Tercera instrucción

* Es importante saber que los operadores lógicos a menudo proporcionan un modo de simplificar
las sentencias condicionales anidadas.

"""

# Definimos las variables:
x = 4
y = 8

# Aplicando las condicionales:
if x == y:
    print("X e Y son iguales")
else:
    if x < y:
        print("X es menor que Y")
    else:
        print("X es mayor que Y")