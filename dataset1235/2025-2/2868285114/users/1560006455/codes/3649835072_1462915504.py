import math
comp = float(input("lado do pentagono: "))
apot = comp/(2 * ( math.tan(math.pi/5)))
a = (5/2) * comp * apot
print(round(a, 2))