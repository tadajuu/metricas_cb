from math import *
pa = float(input("distancia:"))
sa = float(input("distancia2:"))
ang = float(input("angulo:"))
angul=(radians(ang))
c = sqrt(pa**2+sa**2-2*pa*sa*cos(angul))
print(round(c,2))