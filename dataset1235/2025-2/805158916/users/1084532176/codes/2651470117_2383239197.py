from math import *
da = float(input("Distancia da primeira arvore: "))
db = float(input("Distancia da segunda arvore: "))
y = float(input("Angulo entre a primeira e segunda arvores: "))

c = sqrt(da**2+db**2-2*da*db*cos(radians(y)))

print(round(c, 2))

#ESSA FOI SOFRIDA!!!!!!!!