import math

lado = float(input(""))

apotema = lado /(2 * math.tan(math.pi/5))

área = 5/2 * lado * apotema

print(round(área,2))