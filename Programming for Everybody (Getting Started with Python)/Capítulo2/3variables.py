"""

Definiciones:

1. Variables: es un nombre que se refiere a un valor. Una variables es un
contenedor de información, que dentro guardará un dato (o valor), se pueden
crear muchas variables y cada una tenga un dato distinto.

Los nombres de las variables pueden contener tanto letras como números, pero
no pueden comenzar con un número. Se pueden usar letras mayúsculas, pero es
buena idea comenzar los nombres de las variables con una letra minúsculas.

No se deben utilizar las palabras claves que reserva el interprete de Python,
como nombres de variables. Python reserva 33 palabras claves.

2. Valor: es una de las cosas más básicas que utiliza un programa, como
una letra o un número.

3. Sentencia de asignación '=': se utiliza para asignar un valor o dato
a una variable.

4. Concatenación '+': nos permite fusionar dos string.

"""

# Creamos algunas variables y asignarles un valor:
mensaje = "Hola mundo"
entero = 18
decimal = 3.14159
nombre = "Jairo"
apellido = "Mindiola Quintas"
web = "jairomqweb.es"

# Imprimimos el contenido de cada variable:
print(mensaje)
print(entero)
print(decimal)

# Concatenamos:
print(nombre + " " + apellido + " - " + web)
print(f"{nombre} {apellido} - {web}")
print("Mi nombre es {} {} y mi web es: {}".format(nombre, apellido, web))
print(nombre, apellido, web)
