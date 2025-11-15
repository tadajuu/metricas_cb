from math import *

# faça seu código aqui!

lado = float(input("Digite o comprimento do lado: "))
apotema = (lado)/(2*tan(pi/12))
area = 6*lado*apotema

print(round(area,2))