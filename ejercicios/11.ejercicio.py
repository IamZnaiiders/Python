"""Escribí un programa que le solicite al usuario ingresar una fecha formada por 8 números, 
donde los primeros dos representan el día, los siguientes dos el mes y los últimos cuatro 
el año (DDMMAAAA). Este dato debe guardarse en una variable con tipo int (número entero). 
Finalmente, mostrar al usuario la fecha con el formato DD / MM / AAAA."""

cadena=int(input("Ingresa el día => "))
cadena=str(cadena)
#De esta manera podemos accesar a un rango de carcateres
dia=cadena[0:2]
mes=cadena[2:4]
año=cadena[4:8]
print(f"{dia}/{mes}/{año}")
