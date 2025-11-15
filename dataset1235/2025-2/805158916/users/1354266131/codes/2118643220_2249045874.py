
# faça seu código aqui!

lado = float(input())
from math import pi
from math import tan
apotema = lado/(2*tan(pi/8))
A = 4 * lado * apotema
print(round(A,2))