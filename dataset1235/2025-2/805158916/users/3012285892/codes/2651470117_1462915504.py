import math

compri = float(input())
apotema = (compri/(2*math.tan(math.pi/5)))
area = (5/2)*compri*apotema

print(round(area,2))