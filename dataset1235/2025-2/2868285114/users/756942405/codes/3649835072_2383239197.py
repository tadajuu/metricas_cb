import math

a = float(input("a: "))
b = float(input("b: "))
angulo = float(input("angulo: "))
soma = ((a**2) + (b**2))
cos = 2*a*b*math.cos(math.radians(angulo))
c = math.sqrt((soma-cos))
print(round(c, 2))