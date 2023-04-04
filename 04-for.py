"""Ciclos FOR"""

# Estructura de un for 
#range crea una secuencia o un listado que va a iniciar desde el 0
buscar=6
for numero in range(5):
    print(numero)
    if numero ==buscar:
        print('Encontrado => ',buscar)
        break
else:
    print("No encontre el numero buscado")

    print("*"*10)

    comando = ""

    while comando.lower() != "salir":
        comando = input("$ ")
        print(comando)

#loop infinito 
