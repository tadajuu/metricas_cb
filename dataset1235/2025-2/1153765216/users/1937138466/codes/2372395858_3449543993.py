from math import *
lado = int(input("Informe um lado: "))
apotema = lado / (2*tan(pi/10))
area = 5 * lado * apotema
print(round(area, 2))
