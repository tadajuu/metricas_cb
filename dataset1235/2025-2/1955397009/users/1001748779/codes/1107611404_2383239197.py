from math import *

a = float(input())
b = float(input())
y = float(input())

c = sqrt(a ** 2 + b ** 2 - 2 * a * b * cos(radians(y)))

print(round(c, 2))