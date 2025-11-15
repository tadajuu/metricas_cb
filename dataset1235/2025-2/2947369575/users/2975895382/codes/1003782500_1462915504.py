from math import *

# faça seu código aqui!

lado = float(input("Valor do lado: "))

apotema = lado/(2 * tan(pi/5))
area = (5 * lado * apotema)/2

print(round(area,2))