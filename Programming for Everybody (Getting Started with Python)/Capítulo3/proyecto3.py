score = input("Enter Score: ")

#Convertimos el dato de entrada de String a Float y lo guardamos en una variable:
nota = float(score)

#Nuestras condicionales:
#Primero para los valores fuera de rangos:
if nota < 0.0 or nota >1.0:
    print("Estas fuera del rango")
    
#Segundo, para valores dentro del rango:
elif nota < 0.6:
    print("F")
    
elif nota >= 0.6 and nota < 0.7:
    print("D")

elif nota >= 0.7 and nota < 0.8:
    print("C")
    
elif nota >= 0.8 and nota < 0.9:
    print("B")

else:
    print("A")
    