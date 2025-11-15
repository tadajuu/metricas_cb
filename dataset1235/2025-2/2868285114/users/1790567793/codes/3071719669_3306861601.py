from math import *

# faça seu código aqui!
import math
lado = float(input("lados: "))
apot1 = (2*math.tan( math.pi/9))
apot2 = lado/apot1
area = 9/2 * lado * apot2
print(round(area,2))
