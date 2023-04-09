"""Escribí un programa que solicite al usuario el ingreso de una temperatura en escala 
Fahrenheit (debe permitir decimales) y le muestre el equivalente en grados Celsius. 
La fórmula de conversión que se usa para este cálculo es: _Celsius = (5/9) * (Fahrenheit-32)_"""

temperatura=float(input("Ingresa la temperatura => "))
celsius = (5/9) * (temperatura-32)
print(f"El resultado de celcius => [{celsius}]")