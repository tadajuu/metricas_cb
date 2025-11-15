from math import *

# faça seu código aqui!
import math
# 
lado = float(input("Informe o comprimento do lado do pentágono:"))
#calculo da apotema
apotema = lado / (2 * math.tan(math.pi / 5))
#calculo da area
area = (5 / 2) * lado * apotema
#saida
print(round(area,2))