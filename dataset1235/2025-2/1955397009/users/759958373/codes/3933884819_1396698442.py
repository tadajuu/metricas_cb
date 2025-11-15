import math

Xa = float(input())
Ya = float(input())

Xb = float(input())
Yb = float(input())

dAB = math.sqrt((Xb-Xa)**2 + (Yb-Ya)**2)

print(round(dAB, 3))