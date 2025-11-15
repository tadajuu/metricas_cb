from math import *
Xa = float(input("Xa: "))
Ya = float(input("Ya: "))
Xb = float(input("Xb: "))
Yb = float(input("Yb: "))
dAB = sqrt((Xb-Xa)**2 + (Yb-Ya)**2)

print(round(dAB, 3))