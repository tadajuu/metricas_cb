from math import *

# faça seu código aqui!
lado = int(input("digite o valor do lado:"))
import math
apotema = lado / (2*(math.tan(math.pi/8)))
area = 4*lado*apotema
print(round(area,2))