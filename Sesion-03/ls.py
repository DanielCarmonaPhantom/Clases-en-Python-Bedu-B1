from genericpath import exists
import click 
import os

import pandas as pd

@click.command()
@click.argument("path", default=".", type=click.Path(exists=True))
def main(path):
    """
    Programa que imprime la lista de los archivos de la carpeta actual o de agluna carpeta indicada en la línea de comandos
    """
    lista_archivos = os.listdir(path)

    names = []
    sizes = []
    dates = []

    diccionario = {}

    for item in lista_archivos:
        ruta = os.path.join(path, item)
        names.append(item)
        sizes.append(os.path.getsize(ruta))
        dates.append(os.path.getctime(ruta))

    diccionario['size'] = sizes
    diccionario['date'] = dates
    diccionario['names'] = names
    
        
    df = pd.DataFrame(diccionario)
    df['date'] = pd.to_datetime(df['date'], unit='s', errors='ignore')
    print(df)



if __name__ == '__main__':
    main();