from math import *

lado = float(input("digite o comprimento do lado: "))
tan_15 = 2 - (3**0.5)
apotema = lado/(2 * tan_15)
area = 6 * lado * apotema
print(round(area, 2))