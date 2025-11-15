from math import *

# faça seu código aqui!

lado=int(input())

apotema=lado/(2*tan(pi/6))
area=3*lado*apotema

print(round(area,2))