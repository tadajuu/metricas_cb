import math
a = float(input())
b = float(input())
graus = float(input())
grau_radiano = math.radians(graus)
grau_cos = math.cos(grau_radiano)
c = math.sqrt(a**2 + b**2 - 2*a*b*grau_cos)
print(round(c, 2))