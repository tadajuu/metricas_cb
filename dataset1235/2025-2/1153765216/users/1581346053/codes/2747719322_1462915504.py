from math import *

# faça seu código aqui!
lado = float(input("qual o comprimento de um dos lados do pentagono?"))
apotema = lado / (2*tan(pi/5))
area = 5/2*lado*apotema
print(round(area, 2))
