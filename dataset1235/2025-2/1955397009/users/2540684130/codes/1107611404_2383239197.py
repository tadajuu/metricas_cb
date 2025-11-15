from math import *

a = float(input("distancia entre o observador e a arvore:"))
b = float(input("distancia entre o observador e a segunda arvore:"))
y = float(input("angulo entre a e b:"))

x = cos(radians(y))

c = (a ** 2 + b ** 2 - 2 * a * b * x ) ** (1/2)

print(round(c,2))