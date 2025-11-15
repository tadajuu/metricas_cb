from math import *
l = float(input("comprimento do lado: "))

apotema = l/(2*tan(pi/9))

a = (9/2)*l*apotema

print(round(a,2))