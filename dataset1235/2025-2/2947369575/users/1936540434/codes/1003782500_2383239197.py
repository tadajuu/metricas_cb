from math import *

pa = float(input("Distancia observador e primeira árvore:" ))


sa = float(input("Distancia observador e segunda árvore:" ))
ang = float(input("Ângulo:" ))
angu = (radians(ang))
c = sqrt(pa**2+sa**2-2*pa*sa*cos(angu))
print (round(c,2))