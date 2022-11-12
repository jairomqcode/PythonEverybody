"""

Operador lógicos: and (y, conjunción), or (o, disyunción) y not (no, negación).
El significado semántico de estas operaciones es similar a su significado en inglés.

- El operador "and" da como resultado el valor True (cierto) sí y sólo sí son ciertos sus
dos operandos.

- El operador "or" proporciona True (cierto) si cualquiera de sus operandos es True,
y False (falso) sólo cuando ambos operandos son falsos.

- El operador "not" es unario, y proporciona el valor True (cierto) si su operando es False 
(false) y viceversa.

"""

# Ejemplo del operador lógico "and":
x = 2
print(x > 0 and x < 10)

# Ejemplo del operador lógico "or":
n = 2
print(n%2 == 0 or n%3 == 0)

# Ejemplo del operador lógico "not":
x1 = 1 
x2 = 2
print(not(x1 < x2))
