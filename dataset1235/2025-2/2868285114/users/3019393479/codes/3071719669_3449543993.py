from math import *

lado = float(input())

apotema = float(lado / (2 * tan(pi/10)))

area = float(5 * lado * apotema) 

print(round(area,2))