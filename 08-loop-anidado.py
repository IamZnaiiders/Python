# Ejecuta el codigo de arriba hacia abajo
for j in range(3):
    for k in range(2):
        print(f"{j}, {k}")


comando = ""

print("*"*10)
print("Bienvenidos a la calculadora")
print("Para salir escribe salir")
print("Las operaciones son: suma, resta, multiplicacion y division")
print("*" * 20)
resultado=""

while(True):
    #if not  Prueba si una condición es falsa y luego ejecuta algunas declaraciones.
    #Como es falso va a ejecutar lo siguiente
    if not resultado:
        resultado = input("Ingresa un numero => ")
        if resultado.lower() == "salir":
            break
        resultado=int(resultado)
    op=input("Ingresa operacion => ")    
    if op.lower()=="salir":   
        break

    siguienteNum = input("Ingresa el siguiente numero => ")
    if siguienteNum.lower()=="salir": 
        break  
    siguienteNum= int(siguienteNum)
    if op.lower() == "suma":
        resultado+=siguienteNum
        print(f"suma => {resultado}" )
    #Resta
    elif op.lower() == "resta":
        resultado-=siguienteNum
        print(f"resta => {resultado}" )
    else:
        print("Operacion no valida")
        break
