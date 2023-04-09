"""Escribí un programa que solicite al usuario el ingreso de un texto y almacene 
ese texto en una variable. A continuación, mostrar en pantalla la primera letra 
del texto ingresado. Luego, solicitar al usuario que ingrese un número positivo 
menor a la cantidad de caracteres que tiene el texto que ingresó (por ejemplo, 
si escribió la palabra “HOLA”, tendrá que ser un número entre 0 y 4) y almacenar 
este número en una variable llamada indice.
Mostrar en pantalla el carácter del texto ubicado en la posición dada por indice."""

cadena=str(input("Ingresa un texto => "))
caracter=cadena[0]
print(caracter)

indice =int(input("Ingresa un numero positivo menor a la cantidad de caracteres del texto => "))
caracter=cadena[indice]

print(f"El caracter acorde al indice ingresado es => [{caracter}]")