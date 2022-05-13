import click
import os
import csv

class Archivo():
    def __init__(self, ruta_nombre):
        self.ruta_nombre = ruta_nombre

    def __str__(self):
        """
        Representación en str de un objeto Archivo        
        """
        return self.ruta_nombre
    
    def list(self):
        """
        Representación en str de un objeto Archivo        
        """
        return [self.ruta_nombre,0,"2022-05-12"]

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
def guarda_csv( elementos,archivo):
    """
    Guarda la lista de elementos en archivo en formato csv
    """
    with open(archivo, 'w') as f:
        arch_write = csv.writer(f)
        for elemento in elementos:
            # fila =[str(elemento),0, "2022-08-12"]
            arch_write.writerow(elemento.list())

    print("Se ha creado el archivo salida.csv con los resultados")

@click.command()
@click.option("--txt", "archivo", type=str, help="Guarda el resultado en un archivo help")
@click.option("--csv", "archcsv", type=str, help="Guarda el resultado en un archivo csv")
@click.argument("carpeta", default=".", type=click.Path(exists=True))
def main(archivo,archcsv,carpeta):
    """"
    Imprime la lista de carpetas y archivos, indicada en la línea de comandos. Si no se especifica, se utiliza la carpeta actual
    """
    carpeta_base = Carpeta(carpeta)
    elementos = carpeta_base.lista()
    if archivo == None and archcsv == None:
        imprime_text_file(elementos)
    elif archivo != None:
        guarda_txt(elementos, archivo)
    elif archcsv != None:
        guarda_csv(elementos,archcsv)

if __name__ == '__main__':
    main()