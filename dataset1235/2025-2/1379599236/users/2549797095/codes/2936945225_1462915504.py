import math
lado = float(input())
apotema = lado / (2 * math.tan(math.pi/ 5))
area = (5*lado*apotema)/2
print(round(area, 2))
