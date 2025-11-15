from math import *

# faça seu código aqui!
lado_octo = float(input())

apotema = lado_octo / (2*tan(pi/8))

area = 4 * lado_octo * apotema

print(f"{round(area,2)}")