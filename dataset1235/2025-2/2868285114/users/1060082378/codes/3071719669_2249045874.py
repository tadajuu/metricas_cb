from math import *
import math
# faça seu código aqui!
lado = float(input())
apotema = lado / (2 * math.tan(math.pi/8))
area = 4 * lado * apotema
print(round(area, 2))
