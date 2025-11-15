from math import *

# faça seu código aqui!
import math
lados = float(input('lados'))
apotema = lados/(2* math.tan(math.pi/5))
area = 5/2 * lados * apotema
print(round(area, 2))