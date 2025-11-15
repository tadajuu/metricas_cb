from math import *
a = float(input())
b = float(input())
y = float(input())
s = radians(y)
c = sqrt(a**2 + b**2 - 2*a*b*cos(s))
print(round(c,2))