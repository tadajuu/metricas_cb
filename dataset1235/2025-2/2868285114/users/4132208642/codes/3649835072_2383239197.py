from math import *

A = float(input(""))
B = float(input(""))
Y = float(input(""))

valor_CC = float(sqrt(A**2 + B**2 - (2 * A * B *cos(radians(Y)) )))
print(round(valor_CC,2))