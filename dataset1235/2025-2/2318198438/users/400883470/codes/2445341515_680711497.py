import math
lado = float(input())
apotema = lado / (2*math.tan(math.pi/12))
area = 6*lado*apotema
print(round(area,2))