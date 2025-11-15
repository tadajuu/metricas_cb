from math import *
da = float(input("distancia a: "))
db = float(input("distancia b: "))
a = float(input("angulo: "))
c = sqrt(da ** 2 + db ** 2 - 2 * da * db * cos(radians(a)))
print(round(c,2))