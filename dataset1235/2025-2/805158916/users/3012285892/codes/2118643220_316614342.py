import math

lado = float(input())

apotema = lado/(2*math.tan(math.pi/7))

area = (7/2)*lado*apotema

print(round(area,2))