from math import *
distA = float(input("primeira arvore"))
distB = float(input("segunda arvore"))
ang = float(input( "y entre a e b"))
ang2 = radians(ang)
c = sqrt(distA**2 + distB**2 - 2*distA*distB*cos(ang2))
print(round(c,2))