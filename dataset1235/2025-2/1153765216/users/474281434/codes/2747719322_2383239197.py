import math

a = float(input("Digite:"))
b = float(input("Digite:"))
grau = float(input("Digite:"))

angulos_radianos = math.radians (grau)
c = math.sqrt (a**2 + b**2 - 2 * a * b * math.cos(angulos_radianos))
print(round(c , 2))