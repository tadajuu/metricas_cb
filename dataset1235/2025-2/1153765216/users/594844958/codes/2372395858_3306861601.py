import math

lado = int(input())

apotema = lado / (2*math.tan(math.pi/9))

area = (9*lado*apotema) / 2

print(round(area, 2))

