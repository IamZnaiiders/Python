"""Escribí un programa que solicite al usuario ingresar la cantidad de kilómetros recorridos por una motocicleta 
y la cantidad de litros de combustible que consumió durante ese recorrido. Mostrar el consumo de combustible 
por kilómetro."""

cant_kilometros=float(input("Ingresa la cantidad recorridos => "))
cant_combustible=float(input("Ingresa la cantidad de litros de combustible => "))

div=cant_kilometros/cant_combustible

print(f"El consumo de combustible por KM => [{div}]")