from math import *

Lado = int(input("Comprimento do lado do heptagono"))
apotema = Lado / (2*tan(pi/7))
Área = (7/2)*Lado*apotema

print(round(Área, 2))