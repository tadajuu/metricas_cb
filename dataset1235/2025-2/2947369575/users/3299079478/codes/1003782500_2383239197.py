import math
a = float(input())
b = float(input())
gamma_graus = float(input())
gramma_rad = math.radians(gamma_graus)
cos_gamma = math.cos(gramma_rad)

c = math.sqrt(a**2+b**2-2*a*b*cos_gamma)
print(round(c, 2))