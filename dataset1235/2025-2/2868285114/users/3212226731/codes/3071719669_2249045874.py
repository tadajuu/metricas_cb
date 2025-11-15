from math import *
lado = float(input())

apot = lado/(2*tan(pi/8))
area = 4*lado*apot
print (round(area,2))