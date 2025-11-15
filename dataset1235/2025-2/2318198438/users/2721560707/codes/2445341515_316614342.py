from math import *

# faça seu código aqui!
lado = float(input())
apotema = lado / (2 * tan(pi/7))
area = (7/2) * lado * apotema
print(round(area, 2))