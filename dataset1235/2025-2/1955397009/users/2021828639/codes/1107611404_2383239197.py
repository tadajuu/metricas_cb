from math import *
a = float(input("Observador para primeira árvore:"))
b = float(input("Observador para primeira árvore:"))
y = float(input("Angulo entre a e b:"))

c = sqrt(a**2+b**2 - 2*a*b*cos(radians(y)))
print(round(c,2))