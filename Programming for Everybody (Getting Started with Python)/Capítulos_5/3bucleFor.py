"""

A veces se desea repetir un bucle a través de un conjunto de elementos,
como una lista de palabras, las líneas de un archivo, o una lista de
números. Cuando se tiene una lista de cosas para recorrer, se puede
construir un bucle "definido" usando una sentencia "for".

A la sentencia "while" se le llama un bucle "indefinido" porque simplemente
se repite hasta que cierta condición se hace falta, mientras que el bucle
"for" se repite a través de un conjunto conocido de elementos, de modo 
que ejecuta tantas iteraciones como elementos hay en el conjunto.

variable = conjunto de elementos

for variable_de_iteración in variable:
    secuencia de sentencia
    variable que se actualiza



"""

# Ejemplo: Recorriendo una lista.
# Definimos la lista:
familia = ['Nicole', 'Laurent', 'Nancy']

# Aplicamos el bucle for:
for persona in familia:
    print('Feliz año: ', persona)

#Final del programa:
print('¡Terminado!')
