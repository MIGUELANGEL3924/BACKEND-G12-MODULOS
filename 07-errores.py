try:
    raise Exception('Error!!!!')
    int('a')
    divicion = 10/0
    print(divicion)
except ValueError:
   # Ingresara a este bloque de codigo si algo en el try termino de manera abruprint ('Error al ejecutar el codigo')
    print('Error al ejecutar codigo')
except ZeroDivisionError:
    print('Error al dividir entre 0')


except:
    print('error desconocido')
else:
    # Se ejecutara si nunca ingreso a un except,si todo fue exitoso
    print('Yo me ejecuto de manera exitosa')
finally:
    # Si fue exitoso o no
    print('Yo me ejecuto si todo estuvo bien o no')

print('soy otro codigo importante en el proyecto')
