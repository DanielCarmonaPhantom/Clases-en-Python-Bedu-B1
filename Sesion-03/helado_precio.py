import helado.varios
from helado import entrada
from helado.pantalla import imprime_toppings, imprime_precio



def main():
    """
    Función principal del programa
    # 1. Imprimir la lista de opciones en la pantalla.
    # 2. Leer la opción elegida por el usuario
    # 3. Con base a la opción del usuario, imrpimir el valor del 
    """
    imprime_toppings(helado.varios.menu)
    opcion = entrada.lee_respuesta()
    imprime_precio(opcion)

if __name__ == "__main__":
    main()