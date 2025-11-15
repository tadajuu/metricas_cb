import math
a = float(input("digite a distancia a:"))
b = float(input("digite a distancia b:"))
y = math.radians(float(input("digite o angulo:")))
c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos (y))
print(round(c, 2))