from math import *

# faça seu código aqui!

lado = float(input("Insira o comprimento do lado de seu pentágono:"))
apotema = lado/ (2*tan(pi/5))
area = (5/2)*lado*apotema
print(float(round(area,2)))
             