
def suma(*numeros): #Parametros iterables 
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 6, 7)