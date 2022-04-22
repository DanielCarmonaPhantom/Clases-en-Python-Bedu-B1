numero1 = input("Dame el primer numero: ")
numero2 = input("Dame el segundo numero ")

operacion = input("Seleciona la operación (suma, resta, multiplicación o division")

if operacion == 'suma':
    operacion = '+'
elif operacion == 'resta':
    operacion = '-'
elif operacion == 'multiplicacion':
    operacion = '*'
elif operacion == 'division':
    operacion = '/'

print(f"El resultado de la operación de {numero1}{operacion}{numero2} es {eval(numero1+operacion+numero2)}")