import math

L = float(input("comprimento do lado do pentagono:"))
apotema = (L / (2 * math.tan(math.pi / 5)))
A = ((5/2) * L * apotema)
print(round(A, 2))