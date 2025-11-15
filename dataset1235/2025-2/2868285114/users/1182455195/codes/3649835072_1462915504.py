import math

# faça seu código aqui!
lado = float(input())
apotema = lado/(2*math.tan(math.pi/5))
a= (5/2)*lado*apotema
print(round(a,2))