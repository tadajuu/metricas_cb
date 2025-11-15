from math import *
a = float(input())
b = float(input())
gamma = float(input())
c_quadrado = a**2 + b**2 - 2*(a*b*cos(radians(gamma)))
c = sqrt(c_quadrado)
print(round(c,2))