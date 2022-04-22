numero = int(input("¿Cúal tabla deseas ver? "))
print("".join([str(numero)+" * "+str(i)+" = "+str(i*numero)+'\n' for i in range(1,11)]))