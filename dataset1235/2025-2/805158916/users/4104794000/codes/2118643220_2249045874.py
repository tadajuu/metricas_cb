from math import pi 
from math import tan

lado = float(input("comprimento do lado"))

area = 4 * lado * (lado / (2 * tan (pi/8)))

print(round(area,2))