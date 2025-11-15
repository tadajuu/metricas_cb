import math

xa = float(input())
ya = float(input())

xb = float(input())
yb = float(input())

dab = round( math.sqrt( (xb - xa)**2  + (yb - ya)**2 ) , 3)
print(dab)