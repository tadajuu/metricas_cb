import math
a = float(input("Digite a distancia a?"))
b = float(input("Digite a distancia b?"))
y = math.radians(float(input()))
c = math.sqrt(a**2 + b**2 - 2*a*b * math.cos(y))
print(round(c, 2))