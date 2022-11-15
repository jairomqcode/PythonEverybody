"""

Escriba un programa que solicite repetidamente al usuario números enteros hasta 
que el usuario ingrese 'hecho'. Una vez que haya ingresado 'hecho', imprima el 
mayor y el menor de los números. Si el usuario ingresa algo que no sea un número 
válido, atrápelo con un intento/excepto y emita un mensaje apropiado e ignore el 
número. Ingrese 7, 2, bob, 10 y 4 y haga coincidir el resultado a continuación.

"""

mas_grande = None
mas_pequeno = None

# Trabajamos con el bucle While:
while True:
    # El usuario introduce un dato:
    numero = input("Introduce un número: ")
    # Primera Condicional:
    if numero == "done":
        break #Detiene el programa
    # Try es el bloque con las sentencias que quieres ejecutar.
    # El bloque except se ejecutará cuando el bloque try falle debido a un error.
    try:
        #Convertimos el dato a valor entero:
        numero = int(numero)
    except:
        print ("Invalid input")
        continue
    
    # Segunda Condicional:
    if mas_grande is None:
        mas_grande = numero
    elif numero > mas_grande:
        mas_grande = numero
    if mas_pequeno is None:
        mas_pequeno = numero
    elif numero < mas_pequeno:
        mas_pequeno = numero
        break

#Salida de datos (solución):
print("El máximo es: ", mas_grande)
print("El minimo es: ", mas_pequeno)

