import math
lado = float(input())
apotema = lado/(2*math.tan(math.pi/11))
area = round((11*lado*apotema)/2, 2)
print(area)