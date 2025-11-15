from math import *

A= float(input("Insira a quantidade A:"))
B= float(input("Insira a quantidade B:"))
G= float(input("Insira a quantidade do angulo:"))

J= radians(G)

C= sqrt((A**2) + (B**2) - 2*A*B*cos(J))

print(round(C,2))