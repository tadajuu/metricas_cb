from math import *

# faça seu código aqui!
lado = int(input())
apot = lado / (2 * tan(pi/9))
area = 9/2 * lado * apot
print (round(area,2))