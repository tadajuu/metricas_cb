from math import *

lado = float(input())
apotema = lado /(2 * tan(pi/5))
area = (5/2) * lado* apotema
print(f"{area:.2f}")
