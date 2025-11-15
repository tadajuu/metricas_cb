from math import *

# faça seu código aqui!
lado = float(input("valor do comprimento do lado do hexágono:"))
apotema = lado/2*(tan(pi/3))
area = 3*lado*apotema
print(round(area,2))