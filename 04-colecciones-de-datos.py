# listas(arrays)
# ordenada:puedo acceder a sus elementos mediante su posicion

meses = ['Enero', 'Febrero', 'Marzo']
mezclada = ['Eduardo', 10, 50.5, False]
print(mezclada)
print(meses[0])

# al usar valores negativos en la posicion de la lista estare indicando que lo hare de manera inversa
print(meses[-1])

# Desde la pos 1 <  2
print(meses[1:3])
print(meses[:2])
print(meses[1:])

meses.append('Abril')
print(meses)

# 1. Usando el metodo remove
meses.remove('Enero')
print(meses)

# 2. Usando el pop ademas de eliminarla tambien devuelve el valor quitado
mes_eliminando = meses.pop(1)

print(mes_eliminando)
print(meses)

# 3. del sirve para eliminar variables y contenidos de las listas
del meses[0]
print(meses)

# La longitud siempre sera la cantidad de elementos que hay en una coleccion de datos
print(len(meses))

# DICCIONARIOS
# pero el ordenamiento se hace mediante llaves y valores
persona = {
    'nombre': 'Eduardo',
    'edad': 80,
    'nacionalidad': 'Peruano',
    'soltero': True,
    'estatura': 1.92
}

print(persona['nombre'])
persona['fecha de nacimiento'] = 'agosto de 1970'
persona['nombre'] = 'Roberto'
print(persona)
print(persona.keys())
print(persona.values())

del persona['estatura']
print(persona)


# conjuntos
# es una coleccion de datos desordenada que una vez creada no se podra acceder a sus elementos por sus posiciones
alumnos = {'Eduardo', 'Maria', 'Luisa', 'Dante'}
alumnos.add('Roberto')
alumnos.remove('Eduardo')
print(alumnos)

print('Eduardo' in alumnos)

# Tuplas
# Es una coleccion de datos que una vez creada no se puede modificar
conocimientos = ('Matematica', 'Comunicacion', 'Backend')
