from math import *

Lado = int(input("Comprimento do lado do octógono: "))
apotema = Lado / (2*tan(pi/8))
Área = 4 * Lado * apotema

print(round(Área, 2))