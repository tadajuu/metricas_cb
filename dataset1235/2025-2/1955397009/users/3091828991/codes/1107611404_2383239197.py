from math import *
da = float(input("Distancia da primeira arvore:"))
db = float(input("Distancia da segunda arvore: "))
y = float(input("Angulo entre da e db: "))
c = sqrt(da**2+db**2-2*da*db*cos(radians(y)))

print(round(c, 2))