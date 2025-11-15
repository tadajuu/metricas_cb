from math import *

lado = int(input())
# faça seu código aqui!
apotema = lado /(2*tan(pi/12))
area = 6 * lado * apotema
print (round(area,2))
