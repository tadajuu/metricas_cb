from math import *

pa = float(input("distância observador e primeira árvore:"))


sa = float(input("distância observador e segunda árvore:"))
ang = float(input("ângulo:"))
angu = (radians(ang))
c = sqrt(pa**2+sa**2-2*pa*sa*cos(angu))
print(round(c,2))