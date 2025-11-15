import math

a = float(input())

b = float(input())

ang = float(input())

c = round((a**2 + b**2 - 2*math.cos(math.pi * ang/180)*a*b)**0.5,2)

print(c)