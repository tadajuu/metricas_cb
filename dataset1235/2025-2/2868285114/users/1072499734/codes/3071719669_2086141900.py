import math
lado = float(input())
apotema = lado / (2 * math.tan(math.pi /11))
area = (11 * lado * apotema) / 2
print(f"{area:.2f}")