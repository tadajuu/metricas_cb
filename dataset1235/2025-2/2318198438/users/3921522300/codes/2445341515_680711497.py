from math import *

lado = float(input())

apot = lado / (2 * tan(pi/12))

area = 6 * lado * apot

print(round(area,2))
