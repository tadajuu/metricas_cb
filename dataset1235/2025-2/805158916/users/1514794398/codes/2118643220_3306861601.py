from math import *

lado = int(input("comprimento do lado"))

apotema = lado / (2*tan(pi/9))

area = 9/2* lado * apotema 

print(round(area,2))