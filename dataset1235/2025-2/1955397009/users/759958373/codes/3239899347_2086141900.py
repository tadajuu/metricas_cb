import math

Lado = float(input())

Apotema = Lado/(2*math.tan(math.pi/11))
Area = 11*Lado*Apotema/2

print(round(Area, 2))