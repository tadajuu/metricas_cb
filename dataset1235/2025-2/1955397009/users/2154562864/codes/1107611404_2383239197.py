import math

a = float(input())
b = float(input())
y = float(input())

c = round(math.sqrt((a**2 + b**2 - 2*a*b*math.cos(math.radians(y)))), 2)

print(c)