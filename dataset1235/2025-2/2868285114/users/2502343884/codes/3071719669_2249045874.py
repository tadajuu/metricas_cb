from math import *

# faça seu código aqui!
import math
lado = float(input("lados:"))
apot1 = (2*math.tan (math.pi/8))
apot2 = lado/apot1
area = 4*lado*apot2
print(round(area,2))