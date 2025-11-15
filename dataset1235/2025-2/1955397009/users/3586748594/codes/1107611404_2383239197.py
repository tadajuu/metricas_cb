from math import *

a = float(input())
b = float(input())
g = float(input())

g_rad = radians(g)

c = sqrt(a**2 + b**2 -  2 *a * b * cos(g_rad))

print(round(c, 2))
