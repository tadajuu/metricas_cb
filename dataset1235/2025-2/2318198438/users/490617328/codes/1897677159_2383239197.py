from math import *

a = float(input())
b = float(input())
y = radians(float(input()))

t = sqrt(a**2 + b**2 - 2*a*b*cos(y))

print(round(t, 2))