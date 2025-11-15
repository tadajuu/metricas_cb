from math import tan
from math import pi
lado=float(input("escreva o valor do lado"))
apotema= lado/(2*tan(pi/8))
area=4*lado*apotema
print(round(area,2))
# faça seu código aqui!