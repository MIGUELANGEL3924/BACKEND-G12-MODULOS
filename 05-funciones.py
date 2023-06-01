def sumar(numero1, numero2):
    resultado = numero1 + numero2
    print(resultado)

    sumar(1, 5)


def saludar():

    print('Hola')

    sumatoria = sumar(1, 5)
    print(sumatoria)

    saludar()


def sumarIlimitado(*args, numero2):
    # Al utilizar el parametro que empieza con el * indicamos que podra ser ilimitado
    # args > arguments
    print(args)
    print(numero2)


sumarIlimitado(1, 3, 5, 7, 9, 11, numero2=10)

sumarIlimitado(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, numero2=20)


def valoresIlimitados(**kwargs):
    # En este caso recibiremos un numero ilimitado de valores pero definidos por sus nombres de parametros
    # Esta informacion se almacenara en un diccionario
    print(kwargs)

    valoresIlimitados(numero1=10, nombre='Eduardo',
                      nacionalidad='Peruano', muerto=False)

    valoresIlimitados(mes='Diciembre', dia='Sabado', biciesto=81)


def todoIlimitado(*args, **kwargs):

    print(args)
    print(kwargs)


todoIlimitado(10, 'Eduardo', False, 'Diciembre', marca='codigo', hora='15:15')
