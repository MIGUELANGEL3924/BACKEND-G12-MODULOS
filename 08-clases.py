# Una clase es una plantilla que puede ser utilizada n veces
class Persona:
    # las variables que creemos dentro de una clase se pasan a llamar ATRIBUTOS
    fechaNacimiento = '1984-10-28'
    nombre = 'MIGUEL ANGEL QUISPE TORRES'
    estatura = 1.60

    def saludar(self):
        # Funciones definidas dentro de la clase pasan a llamarse METODOS
        # todo METODO de una clase SIEMPRE llevara definido como primer parametro el 'self'
        # 'self': Sirve para hacer referencia a la funcionalidad de la clase como sus atributos y otros metodos
        # otros metodos,en otros lenguajes de programacion como C# o Java se utiliza el 'this'
        texto = 'Hola soy %s,mucho gusto' % self.nombre
        texto = 'Hola soy ' + self.nombre + ',mucho gusto '
        texto = 'Hola soy {},mucho gusto'.format(self.nombre)
        print(texto)

    def despedir(self):
        print('Adioooos')


 # crear una instancia de una clase , es sacar una copia de esa clase y almacenarla en esa variable
persona1 = Persona()
persona2 = Persona()

persona1.nombre = 'Rigoberto'
persona2.nombre = 'Derrick'

persona1.saludar()
persona2.saludar()
