import math
a = float (input())
b = float (input())
angulo = float (input())

rad = math.radians(angulo)

c = math.sqrt(a**2+b**2-2*a*b*math.cos(rad))
print(round(c,2))