"""
- Función input(): recibe la entrada desde el teclado por parte del usuario, y devuelve como una cadena aquello que el usuario escribió.

- \n representa un salto de línea.

"""

# Definimos una variable con entrada de datos:
nombre = input("¿Cual es tu nombre?: ")
edad = input("¿Que edad tienes?:")
edad_convertida = int(edad)

print(f"Hola {nombre}, tienes {edad_convertida} años")
