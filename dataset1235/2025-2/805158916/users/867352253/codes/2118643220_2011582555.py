from math import pi
from math import tan
lado = float(input())
apotema = lado/(2 * tan(pi/6))  
area = 3 * lado * apotema
print(round(area, 2))