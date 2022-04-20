def tablaMultiplicar(tabla):
    for i in range(1,11):
        print(f'{tabla} * {i} = {tabla*i}')
    
tabla = int(input("¿Cúal tabla te gustaria ver? "))
tablaMultiplicar(tabla)