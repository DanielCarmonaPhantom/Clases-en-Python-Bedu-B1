from email.policy import default
import click
import os

class Archivo():
    def __init__(self, ruta_nombre):
        self.ruta_nombre = ruta_nombre

    def __str__(self):
        """
        Representación en str de un objeto Archivo        
        """
        return self.ruta_nombre

class Carpeta(Archivo):
    def __init__(self, ruta_nombre):
        super().__init__(ruta_nombre)

    def __str__(self):
        """
        Representación en str de un objeto Carpeta       
        """
        return self.ruta_nombre + "/"
    
    def lista(self):
        """
        Regresa la lista de todos los elementos del objeto Carpeta
        """

        elementos =  os.listdir(self.ruta_nombre)
        elementos.sort()
        objetos = []
        for elemento in elementos:
            ruta_nombre = os.path.join(self.ruta_nombre, elemento)
            if os.path.isdir(ruta_nombre):
                carpeta = Carpeta(ruta_nombre)
                objetos.append(carpeta)
                lista_elementos = carpeta.lista()
                objetos += lista_elementos
            elif os.path.isfile(ruta_nombre):
                objetos.append(Archivo(ruta_nombre))
        return objetos



def imprime_text_file(elementos):
    """
    Imprime la lista de elementos en la salida estándar en formato string
    """
    for elemento in elementos:
        print(elemento)
def guarda_txt(elementos,archivo):
    """
    Guarda la lista de elementos en archivo en formato txt
    """
    with open(archivo, 'w') as f:
        for elemento in elementos:
            f.write(str(elemento) + "\n")

@click.command()
@click.option("--txt", "archivo", type=str, help="Guarda el resultado en un archivo help")
@click.argument("carpeta", default=".", type=click.Path(exists=True))
def main(archivo,carpeta):
    """"
    Imprime la lista de carpetas y archivos, indicada en la línea de comandos. Si no se especifica, se utiliza la carpeta actual
    """
    carpeta_base = Carpeta(carpeta)
    elementos = carpeta_base.lista()
    if archivo == None:
        imprime_text_file(elementos)
    else:
        guarda_txt(elementos, archivo)

if __name__ == '__main__':
    main()