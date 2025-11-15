from math import *
a = float(input())
b = float(input())
ang = float(input())
c = ((a**2) + (b**2) - 2*a*b* cos(radians(ang))) ** (1/2)
print(round(c,2))


