"""

La sentencia While.

El flujo de iteración de la sentencia while:
1. Se evalúa la condición, obteniendo verdadero o falso.

2. Si la condición es falsa, se sale de la sentencia "while" y se continúa 
la ejecución en la siguiente sentencia.

3. Si la condición es verdadera, se ejecuta el cuerpo del While y luego se
vuelve al paso 1.

variable inicializada.

while condición:
    secuencia de sentencia
    variable de iteración

Este tipo de flujo recibe el nombre de "bucle". Cada vez que se ejecuta el cuerpo
del bucle se dice que realizamos una "iteración".

El cuerpo del bucle debe cambiar el valor de una o más variable, de modo que la 
condición pueda en algún momento evaluarse como falsa y el bucle termine.

La variable que cambia cada vez que el bucle se ejecuta y controla cuando términa este,
recibe el nombre de "variable de iteración". Si no hay variable de iteración, el bucle
se repetira para siempre, resultando así un "bucle infinito".

Sentencia break: nos permite alterar el comportamiento de los bucles while y for. 
Concretamente, permite terminar con la ejecución del bucle. Esto significa que una
vez se encuentra la palabra break, el bucle se habrá terminado.

sentencia continue: el uso de continue al igual que el ya visto break, nos permite
modificar el comportamiento de los bucles while y for. Concretamente, continue se 
salta todo el código restante en la iteración actual y vuelve al principio en el 
caso de que aún queden iteraciones por completar.


"""

# Ejemplo: contemos del 5 al 0.

# Definimos la variable de iteración:
n = 5

# Bucle while:
while n > 0:
    print(n)
    n = n - 1

# Cuando se termine la iteración:
print("¡Terminado!")
