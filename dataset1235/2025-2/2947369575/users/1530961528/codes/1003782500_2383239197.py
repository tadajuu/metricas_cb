import math

a = float(input())
b = float(input())
y = float(input())

y = math.radians(y)
c = (a ** 2 + b ** 2 - 2  * a * b * math.cos(y)) ** 0.5

print(round(c, 2))