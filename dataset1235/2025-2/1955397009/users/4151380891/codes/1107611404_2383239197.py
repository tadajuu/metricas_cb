from math import *
a = float(input(" distancia a:"))
b = float(input("distancia b:"))
y = float(input("angulo entre a e b:"))

c = sqrt(a**2 + b**2 -2*(a*b)*cos(radians(y)))
print(round(c, 2))
