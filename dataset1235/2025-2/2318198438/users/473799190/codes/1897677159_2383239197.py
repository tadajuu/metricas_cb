import math
a = float(input())
b = float(input())
y = float(input())

d = math.radians(y)
c = math.cos(d)
n =((a**2) + (b**2)) - (2*((a*b)*c))
q = math.sqrt(n)

print (round(q, 2))