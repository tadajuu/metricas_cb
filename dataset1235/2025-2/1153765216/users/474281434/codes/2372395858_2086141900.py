from math import *

lado = float (input("digite o lado: "))

undecagano = lado / (2* math.tan(math.pi/11))

x = 4 * lado * undecagano

print(round(x, 2))