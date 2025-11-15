import math
a = float(input())
b = float(input())
angYab = float(input())
gamma = math.radians (angYab)
c = math.sqrt( a**2 + b**2 - 2*a*b*math.cos(gamma))

print(round(c,2))