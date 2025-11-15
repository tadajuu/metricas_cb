import math
l = float(input("lado do o: "))
a = l / (2 * (math.tan((math.pi)/8)))
A = 4 * l * a
print(round(A, 2))