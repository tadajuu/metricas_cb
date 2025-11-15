from math import *
import math
# faça seu código aqui!
lado = float(input("Lado: "))
apotema = lado / (2 * (math.tan(math.pi / 11)))
area = (11 * lado * apotema) / 2
print(round(area,2))