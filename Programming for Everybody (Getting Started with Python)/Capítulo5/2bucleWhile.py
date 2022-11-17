"""

Bucle While.

Estructura de control que itera o repite la ejecución de una
serie de instrucciones tantas veces como sea necesario, hasta
que deje de cumplirse la condición.

while condición:
    bloque de instrucciones
    actualización del contador

Flujo de operación de la sentencia While:

* Se evalúa la condición, obteniendo Verdadero or Falso.

* Si la condición es falsa, se sale de la sentencia while y
se continúa la ejecución en la siguiente sentencia.

* Si la condición es verdadera, se ejecuta el cuerpo del while
y luego se vuelve al paso 1.

Este tipo de flujo recibe el nombre de bucle, ya que el tercer 
paso enlaza de nuevo con el primero. Cada vez que se ejecuta el
cuerpo del bucle se dice que realizamos una iteración.

A la sentencia while se la llama un bucle indefinido, porque
simplemente se repite hasta que cierta condición se hace Falsa.

"""

# Contar desde el 5 al 0.
n = 5

# Condición:
while n > 0:
    print(n)
    n = n - 1
    #print(n)

print("Terminado!")

""" Cuando no tenemos una variable de iteración iniciada, se ejecutará un bucle infinito. """


"""

La sentencia "break" nos permite alterar el comportamiento de los bucles while y for. Concretamente,
permite terminar con la ejecución del bucle. Esto significa que una vez se encuentra la palabra 
break, el bucle se habrá terminado.

El uso de "continue" al igual que el ya visto break, nos permite modificar el comportamiento de de los
bucles while y for. Concretamente, continue se salta todo el código restante en la iteración actual y
vuelve al principio en el caso de que aún queden iteraciones por completar.

"""