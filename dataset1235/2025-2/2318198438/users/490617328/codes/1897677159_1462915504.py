from math import *

# faça seu código aqui!

side = int(input())

apotema = side/(2*tan(pi/5))

area = (5/2)*side*apotema

print(round(area, 2))