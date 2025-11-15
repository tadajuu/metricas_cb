import math
a = float(input(""))
b = float(input(""))
gama = float(input(""))
gama_rad = math.radians(gama)
c = math.sqrt (a**2 + b**2 - 2 * a * b * math.cos(gama_rad))
print(round(c,2))