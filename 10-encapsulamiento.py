class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        # Para que un atributo  o metodo sea privado se le coloca doble subguion antes del nombre
        self.__ganacia = self.precio * 0.3

    def mostrarGanacia(self):
        print('la ganancia es %s' % self.__ganacia)
        print('El IGV es {}'.format(self.__calcularIgv()))

    def __calcularIgv(self):
        return self.precio * 0.18


producto1 = Producto('Detergente', 7.50)
producto2 = Producto('Shampu', 18.40)
# podra ser "accedido" (no dara ningun error pero no hara caso alguno)
producto1.__ganacia = 1000000
producto1.mostrarGanacia()
producto2.mostrarGanacia()
# no se puede acceder a un metodo privado desde afuera de la clase
# producto1.__calcularIgv()
