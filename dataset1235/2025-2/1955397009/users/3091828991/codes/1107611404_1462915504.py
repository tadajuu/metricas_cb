from math import *

CompLP = int(input("Comprimento do lado do pentagono: "))
apotema = CompLP/(2*tan(pi/5))
A = (5/2*CompLP)*apotema

print(round(A, 2))