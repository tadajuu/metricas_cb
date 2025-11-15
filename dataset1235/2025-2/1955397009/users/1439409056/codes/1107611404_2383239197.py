from math import *
a = float(input("distancia: "))
b = float(input("distancia: "))
y = float(input("distancia: "))

r = radians(y)
c = sqrt((a**2+b**2)-2*a*b*cos(r))

print(round(c,2))