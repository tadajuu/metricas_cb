from math import *

lado = float(input("Digite o comprimento do lado do comprimento"))

Apotema = lado/(2*tan (pi/7))
Area = (7/2)*lado*Apotema
print(round(Area,2))