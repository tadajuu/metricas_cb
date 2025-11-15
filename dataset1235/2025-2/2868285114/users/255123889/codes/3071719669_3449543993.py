import math
pi = math.pi
tag = math.tan(pi/10)
lado = float(input(""))
apotema = lado / (2*tag)
área = 5*lado*apotema
print(round(área,2))