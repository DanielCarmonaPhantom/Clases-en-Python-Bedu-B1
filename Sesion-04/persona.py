class Persona():

    def __init__(self, nombre, apellido=None, email = None):
        self.nombre = nombre
        self.apellido = apellido

        self.__email = email

    def asignar_nombre(self, nombre):
        self.nombre = nombre

    def cambiar_email(self, email):
        self.__email = email

    def saluda(self):
        print("hola, soy {}".format(self.nombre))

    def get_nombre(self):
        return self.nombre

    def get_email(self):
        return self.__email

    def __str__(self):
        if self.apellido != None:
            return f'{self.nombre} {self.apellido}'
        else:
            return f'{self.nombre}'


class Empleado (Persona):
    pass



def main():
    """
    Función principal
    """
    empleado_1 = Empleado("Daniel")
    print(empleado_1.saluda())
    print(empleado_1.get_nombre())



if __name__ == "__main__":
    main()