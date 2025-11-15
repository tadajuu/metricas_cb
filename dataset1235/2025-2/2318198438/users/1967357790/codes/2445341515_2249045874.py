from math import *

lado = int(input())

apotema = lado / (2 * tan(pi / 8))

area = 4 * lado * apotema

print(round(area, 2))
