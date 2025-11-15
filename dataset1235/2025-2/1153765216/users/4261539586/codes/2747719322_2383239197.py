from math import *

a = float(input("informe a primeira distancia: "))
b = float(input("informe a segunda distancia: "))
ang = float(input("informe o valor de um angulo: "))

c = sqrt((a**2 + b**2) - 2*a*b*cos(radians(ang)))

print(round(c, 2))