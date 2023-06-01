from flask import Flask

# indicar si nuestro archivo es el archivo principal , si el archivo es el principal su valor sera '__main__'
app = Flask(__name__)

productos = [
    {
        'id': 1,
        'nombre': 'Platano',
        'precio': 3.50
    },
    {
        'id': 2,
        'nombre': 'Sandia',
        'precio': 2.80
    },
    {
        'id': 3,
        'nombre': 'Tomate',
        'precio': 2.30
    },
]


@app.route('/')
def inicio():
    # modificar el comportamiento del metodo route de la clase flask para evitar modificar el metodo en la misma clase
    print('Hola ')
    return 'Bienvenido a mi aplicacion de flask'


@app.route('/productos', methods=['GET', 'POST'])
def gestion_productos():
    return {
        'content': productos
    }


if __name__ == '__main__':
    app.run(debug=True)
