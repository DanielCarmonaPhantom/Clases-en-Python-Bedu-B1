class Producto:
    def __init__(self, nombre, precio_unitario, cantidad):
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.cantidad = cantidad

    @property
    def subtotal(self):
        return self.precio_unitario * self.cantidad

    def __str__(self):
        return self.nombre


def main():
    producto_uno = Producto("Alcohol", 750,  3)
    producto_dos = Producto("Coca", 250 , 5)

    print(producto_uno, producto_uno.subtotal)
    print(producto_dos, producto_dos.subtotal)


if __name__ == "__main__":
    main()