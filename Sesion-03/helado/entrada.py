"""
Nombre del módulo: entrada

Contiene los elementos de apoyo para la lectura de valores.

"""



def lee_respuesta():
    """ Leer las opción elegida por el usuario """
    opcion_str = input("Elige el topping: ")
    opcion = int(opcion_str)
    return opcion