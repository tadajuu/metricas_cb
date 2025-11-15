import math
a = float(input())
b = float(input())
gamma = float(input())
gamma_rad =math.radians (gamma)
c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(gamma_rad))
print(round(c,2))