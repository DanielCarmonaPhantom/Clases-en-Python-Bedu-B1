sabores = []
nombre_helados = []

cantidad = int(input("¿Cuantos helados serían? "))

for i in range(cantidad): 
    sabor = input(f"¿De que sabor sería el helado {i+1}? ")
    nombre_helados.append(sabor)
    if sabor.lower() == 'oreo':
        sabores.append(19)
    elif sabor.lower() == 'm&m':
        sabores.append(19)
    elif sabor.lower() == 'fresas':
        sabores.append(19)
    elif sabor.lower() == 'brownie':
        sabores.append(19)
    else:
        print("No tenemos de ese sabor")
        nombre_helados.pop()
    
total = sum(sabores)     
    
print(f"El total de {cantidad} helados de {', '.join(nombre_helados)}es de $ {total}")
