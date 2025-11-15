from math import *

# faça seu código aqui!

comprimento = float(input())
apotema = (comprimento / (2 * tan(pi/5)))
area = (5/2) * comprimento * apotema

print(round(area, 2))