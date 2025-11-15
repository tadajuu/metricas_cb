from math import *

lado = float(input("Qual o comprimento do lado do Pentagono?: "))

apotema = lado / (2 * tan(pi/5))

area = (5/2) * lado * apotema

print(round(area, 2))