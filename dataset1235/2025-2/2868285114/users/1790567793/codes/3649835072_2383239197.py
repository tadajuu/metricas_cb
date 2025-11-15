import math
a = float(input(""))
b = float(input(""))
g = float(input(""))
gr = math.radians (g)
c = math.sqrt(a**2 + b**2 - 2*a*b* math.cos(gr))
print(f"{c:.2f}")