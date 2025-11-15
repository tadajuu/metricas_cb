from math import *
x=float(input("insira a primeira distancia: "))
y=float(input("insira a segunda distancia: "))
z=float(input("insira o angulo:"))
c=sqrt(x**2+y**2-2*x*y*cos(radians(z)))
print(round(c,2))
