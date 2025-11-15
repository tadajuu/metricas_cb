from math import *

# faça seu código aqui!
l = float(input("lado: "))
apotema = l / (2*tan(pi/11))
area = (11 * l * apotema)/2
print(round(area, 2))