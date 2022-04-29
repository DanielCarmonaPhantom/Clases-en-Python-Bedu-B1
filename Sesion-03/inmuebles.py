import csv

def lee_datos(nom_arch):
    """ 
    Lee todos los datos del archivo nom_arch y lo regresa como una lista
    """
    with open(nom_arch) as arch:
        csv_lector = csv.reader(arch)
        lista = list(csv_lector)

    return lista

def imprime_lista(inmuebles):
    """
    Imprime la lista de inmuebles en la salida estándar
    """
    columnas = zip(*inmuebles)
    tamanios = [len(max(col, key=len)) for col in columnas]
    formatos = ["{:"+str(t)+"}" for t in tamanios]
    linea = " ".join(formatos)
    for fila in inmuebles:
        print(linea.format(*fila))
        

def lee_palabras():
    """
    Lee las palabras que representan un Tipo de inmueble 
    """
    palabras = input("Escribe los tipos de inmubles separados por espacio ").split()
    return palabras

def filtra_por(inmuebles, tipos):
    """
    Filtra la lista de inmuebles con base a las palabras en *args que representan el Tipo de inmueble. Regresa la lista filtrada
    """
    filtrados = []
    for inmueble in inmuebles:        
        if inmueble[2] in tipos:
            filtrados.append(inmueble)
    return filtrados

def main():
    inmuebles= lee_datos("inmuebles.csv")
    palabras = lee_palabras()
    print(palabras)
    filtrados = filtra_por(inmuebles, palabras)

    imprime_lista(filtrados)

if __name__ == '__main__':
    main();