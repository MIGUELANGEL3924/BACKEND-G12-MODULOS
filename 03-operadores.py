# operadores aritmeticos
edad1 = 10
edad2 = 30
# suma(+)
print(edad1 + edad2)

# Resta(-)
print(edad1 - edad2)

# Multiplicacion(*)
print(edad1 * edad2)

# Divicion(/)
print(edad1 / edad2)

# Modulo(%) > es el resultado entero de la division
print(edad1 % edad2)
# Cociente(//)
print(edad1 // edad2)

# Operadores de asignacion
# Asignacion(=)
persona = 'Ximena'

# Incremento
edad1 += 1  # incrementamos el valor de la variable edad1 en una unidad

# Decremento
edad1 -= 1

# Multiplicador
edad1 *= 2  # edad1= edad1 * 2

# Division
edad1 /= 2

# Potencia
edad1 **= 3  # edad1 = edad1 * edad1 * edad1

# Operadores de comparacion
persona1 = 'Eduardo'
persona2 = 'Juan'

# == > es igual que
# En python no existe el triple igual ===

print(persona1 == persona2)

# != > no es igual / es diferente de
print(persona1 != persona2)

# < , > menor que / mayor que
print(10 > 20)
print(50 < 80)

# <= , >= menor o igual que / mayor o igual que
print(10 >= 10)

# Operadores logicos
edad_juan = 10
edad_Jonathan = 15
edad_Roxana = 18
edad_Marthina = 19
# and (y) &&
#          v                               v                      > v
print((edad_Jonathan > edad_juan) and (edad_Marthina > edad_Roxana))
#          v                               f                      > f
print((edad_Jonathan > edad_juan) and (edad_Roxana > edad_Marthina))

# or (o)
#          v                               f                       > v
print((edad_Jonathan > edad_juan) or (edad_Roxana > edad_Marthina))
