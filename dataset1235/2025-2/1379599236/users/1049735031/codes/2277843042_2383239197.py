from math import*

a = float(input())
b = float(input())
y = float(input())

c = ((a**2) + (b**2) - 2*a*b*cos(radians(y)))**(1/2)
print(round(c, 2))