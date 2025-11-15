import math

cordeAx = float(input("Ax = "))
cordeAy = float(input("Ay = "))
cordeBx = float(input("Bx = "))
cordeBy = float(input("By = "))

dab = math.sqrt((cordeBx-cordeAx)**2 + (cordeBy - cordeAy)**2)

print(round(dab,3))