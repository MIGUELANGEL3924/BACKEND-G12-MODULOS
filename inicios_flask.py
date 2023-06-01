from flask import Flask

# indicar si nuestro archivo es el archivo principal , si el archivo es el principal su valor sera '__main__'
app = Flask(__name__)


@app.route('/')
def inicio():
    # modificar el comportamiento del metodo route de la clase flask para evitar modificar el metodo en la misma clase
    print('Hola ')
    return 'Bienvenido a mi aplicacion de flask'


if __name__ == '__main__':
    app.run(debug=True)
