import math
a = float(input())
b = float(input())
g = float(input())
c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(g)))
print(round(c, 2))