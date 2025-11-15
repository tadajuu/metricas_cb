from math import *

lado = int(input("Comprimento do lado do hexagono"))
apotema = lado / (2*tan(pi/6))
Área = 3 * lado * apotema

print(round(Área, 2))
# faça seu código aqui!