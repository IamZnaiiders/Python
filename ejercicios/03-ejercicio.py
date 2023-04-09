"""Escribí un programa que solicite al usuario dos números y los almacene en dos variables. 
En otra variable, almacená el resultado de la suma de esos dos números y luego mostrá ese resultado en pantalla.
A continuación, el programa debe solicitar al usuario que ingrese un tercer número, 
el cual se debe almacenar en una nueva variable. Por último, mostrá en pantalla el resultado
de la multiplicación de este nuevo número por el resultado de la suma anterior."""

num_1=float(input("Ingresa el primer numero => "))
num_2=float(input("Ingresa el segundo numero => "))

suma_num=num_1 + num_2

print(f"El resultado de la suma de los numeros => [{suma_num}]")

num_3=float(input ("Ingrese un tercer numero => "))

operacion=suma_num*num_3

print(f"El resultado de la multiplicacion es => [{operacion}]")