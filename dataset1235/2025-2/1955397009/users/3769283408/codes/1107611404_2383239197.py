import math
a = float(input())
b = float(input())
g = float(input())
graus = math.radians(g)
c = math.sqrt(a**2+b**2-2*a*b*math.cos(graus))
print(round(c,2))