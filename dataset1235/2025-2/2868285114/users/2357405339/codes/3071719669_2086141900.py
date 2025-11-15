from math import *


lado = int(input())
apot = lado/ (2 * tan(pi/11))
area = 11/2 * lado * apot
print (round(area,2))