from math import *

#leitura do lado do pentagono
lado = float(input())

apotema = lado / (2 * tan(pi / 5)) 

area = (5/2) * lado * apotema 

print(f"{round(area, 2):.2f}")
