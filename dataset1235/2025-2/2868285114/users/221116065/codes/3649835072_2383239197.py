from math import *

A = float(input("Qual a distancia entre A e o observador?: "))
B = float(input("Qual a distancia entre A e o observador?: "))
Y = float(input("Qual o angulo entre A e B?: "))

C = sqrt((A**2 + B**2) - (2 * A * B) * (cos(radians(Y))))

print(round(C, 2))