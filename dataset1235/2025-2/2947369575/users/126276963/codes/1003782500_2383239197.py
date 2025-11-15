import math
a = float(input())
b = float(input())
graus = float(input())
rad = math.radians(graus)
cos_gamma = math.cos(rad)
c = math.sqrt(a**2+b**2-2*a*b*cos_gamma)
print(round(c,2))