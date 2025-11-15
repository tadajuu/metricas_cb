from math import *
Lado = int(input("Digite seu lado: "))
apotema = Lado / (2*tan(pi/8))
area = 4 * Lado * apotema
print(round(area, 2))