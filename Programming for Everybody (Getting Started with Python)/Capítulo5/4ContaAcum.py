""" Contar el número de elementos de una lista. """
# Iniciamos una variable y será el contador:
contador = 0
# Aplicamos el bucle for:
"""

* Usamos un bucle for para movernos a través de la lista de número.

* Nuestra variable de iteración se llama valor, y dado que no usamos
la variable valor dentro del bucle, lo único que hace es controlar el
bucle y hacer que el cuerpo del mismo sea ejecutado una vez para cada
uno de los valores de la lista.

* En el cuerpo del bucle, añadimos 1 al valor actual de contador para
cada uno de los valores de la lista. Mientras el bucle se está ejecutando,
el valor de contador es la cantidad de valores que se hayan visto 
“hasta ese momento”.

* Una vez el bucle se completa, el valor de contador es el número total 
de elementos.

* Cuando no utilizamos la variable de iteración dentro del cuerpo del bucle,
esta variable recorrerá el conjunto de elementos, indicando la cantidad de
elementos dentro del conjunto.

"""
for valor in [3, 14, 12, 9, 74, 15]:
    #Obtendremos la cantidad de elementos en la lista:
    contador = contador + 1
print("Números de elementos: ", contador)



""" Utilizando la variable de iteración dentro del bucle. """
# Iniciamos la variable que será el acumulador:
acumulador = 0

""" 

* Cuando utilizamos la variable de iteración dentro del cuerpo del bucle,
esta variable recorrerá el conjunto de elementos, sumando entre sí cada
elemento del conjunto.

"""

# Aplicando el bucle for:
for valor1 in [3, 41, 12, 9, 74, 15]:
    #Sumaremos cada elemento de la lista:
    acumulador = acumulador + valor1
print('Total: ', acumulador)
