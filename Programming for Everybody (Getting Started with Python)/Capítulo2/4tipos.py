"""

1. Función type(): nos permite conocer el tipo de dato o valor.

2. Algunos tipos de valores o datos:

* Dato tipo entero (integer): 1, 2, 77, etc..

* Dato tipo decimal (float): 3.14159 

* Dato tipo cadena (string): 'Hola mundo', 'Nicole', 'Laurent', etc..

* Dato tipo booleano: True, False.

* Dato tipo nada: None

3. Función int(): convierte un dato a tipo entero.

4. Función float(): convierte un dato a tipo punto flotante.

5. Función str(): convierte un dato a tipo cadena.

"""

# Creamos variables y les asignamos valores:
mensaje = "Hola mundo"
entero = 18
decimal = 3.14159
booleano = True
convertir_entero = int(3.14159)
convertir_flotante = float(18)
convertir_string = str(18)

# Imprimimos cada variable y conocemos el tipo de dato que contienen:
print(mensaje)
print(type(mensaje))
print("------------")
print(entero)
print(type(entero))
print("------------")
print(decimal)
print(type(decimal))
print("------------")
print(booleano)
print(type(booleano))
print("------------")

# Imprimimos las variables que convertiremos de un tipo de dato a otro:
print(convertir_entero)
print(type(convertir_entero))
print("----------------------")
print(convertir_flotante)
print(type(convertir_flotante))
print("----------------------")
print(convertir_string)
print(type(convertir_string))
print("----------------------")
