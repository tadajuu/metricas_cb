import math 

xa = float(input())
ya = float(input())
xb = float(input())
yb = float(input())

dab = math.sqrt((xb - xa)**2 + (yb - ya)**2)

print(round(dab, 3))
